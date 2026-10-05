#!/usr/bin/env python3
"""
matte.py — A-roll matting: get a talking character off their background.

Mates a video frame-by-frame with rembg (u2net / u2netp / isnet) and writes:
  alpha/<n>.png   RGBA cut-out per frame
  green/<n>.png   the same on a green screen (#00B140)
  matte/<n>.png   the grayscale alpha (for manual cleanup)
  alpha.webm      WebM VP9 with alpha (yuva420p)
  green.mp4       H.264 green-screen version
  stills/         a few transparent PNGs for the asset kit

Usage:
  python matte.py VIDEO [--out DIR] [--model u2netp|u2net|isnet-general-use]
                        [--scale 0.6] [--max-frames N] [--stills 3]

Deps: rembg, onnxruntime, Pillow, numpy, ffmpeg (system or imageio-ffmpeg).
Runs one model per process; caps threads for low-memory boxes.
"""
import argparse, os, shutil, subprocess, sys, time

def ffmpeg_exe():
    e = shutil.which("ffmpeg")
    if e: return e
    try:
        import imageio_ffmpeg; return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        sys.exit("ffmpeg not found. pip install imageio-ffmpeg")

def run(c): return subprocess.run(c, capture_output=True, text=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--out", default="matte_out")
    ap.add_argument("--model", default="u2netp")
    ap.add_argument("--scale", type=float, default=0.6)
    ap.add_argument("--max-frames", type=int, default=0)
    ap.add_argument("--stills", type=int, default=3)
    ap.add_argument("--fps", type=float, default=0)
    a = ap.parse_args()

    # thread caps BEFORE importing onnxruntime
    for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ.setdefault(k, "1")
    from rembg import remove, new_session
    from PIL import Image
    import numpy as np

    FF = ffmpeg_exe()
    os.makedirs(a.out, exist_ok=True)
    fr_dir = os.path.join(a.out, "_frames"); os.makedirs(fr_dir, exist_ok=True)
    for sub in ("alpha", "green", "matte", "stills"):
        os.makedirs(os.path.join(a.out, sub), exist_ok=True)

    vf = f"fps={a.fps}" if a.fps else "null"
    print("extracting frames...")
    run([FF, "-y", "-v", "error", "-i", a.video, "-vf", vf,
         os.path.join(fr_dir, "f%05d.png")])
    frames = sorted(f for f in os.listdir(fr_dir) if f.endswith(".png"))
    if a.max_frames: frames = frames[:a.max_frames]
    if not frames: sys.exit("no frames extracted")
    print(f"frames: {len(frames)} | model: {a.model} | scale: {a.scale}")

    print("loading model (downloads on first use)...")
    sess = new_session(a.model)
    GREEN = (0, 177, 64)
    t0 = time.time(); done = 0
    for i, fn in enumerate(frames):
        src = os.path.join(fr_dir, fn)
        im = Image.open(src).convert("RGB"); W, H = im.size
        small = im.resize((max(1,int(W*a.scale)), max(1,int(H*a.scale))))
        cut = remove(small, session=sess)                     # RGBA
        alpha = cut.split()[-1].resize((W, H), Image.LANCZOS)
        rgba = im.convert("RGBA"); rgba.putalpha(alpha)
        rgba.save(os.path.join(a.out, "alpha", fn))
        alpha.convert("L").save(os.path.join(a.out, "matte", fn))
        g = Image.new("RGB", (W, H), GREEN); g.paste(rgba, (0, 0), rgba)
        g.save(os.path.join(a.out, "green", fn))
        done += 1
        if i % 10 == 0: print(f"  {done}/{len(frames)}  ({time.time()-t0:.0f}s)")
    print(f"matted {done} frames in {time.time()-t0:.0f}s")

    # stills for the asset kit
    step = max(1, len(frames)//max(1, a.stills))
    for j, fn in enumerate(frames[::step][:a.stills]):
        Image.open(os.path.join(a.out, "alpha", fn)).save(
            os.path.join(a.out, "stills", f"cutout_{j+1}.png"))

    # rebuild: alpha WebM + green MP4
    fps = a.fps or 25
    run([FF, "-y", "-v", "error", "-framerate", str(fps), "-i",
         os.path.join(a.out, "alpha", "f%05d.png"),
         "-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-b:v", "0", "-crf", "30",
         os.path.join(a.out, "alpha.webm")])
    run([FF, "-y", "-v", "error", "-framerate", str(fps), "-i",
         os.path.join(a.out, "green", "f%05d.png"),
         "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p",
         os.path.join(a.out, "green.mp4")])
    print("wrote", a.out+"/alpha.webm, green.mp4, alpha/, green/, matte/, stills/")
    print("CHECK: no holes · no baked-caption artifacts · stable alpha · clean hair.")

if __name__ == "__main__":
    main()
