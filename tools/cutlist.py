#!/usr/bin/env python3
"""Cut-list renderer: NLE-style edits (ripple, slip, slide, speed, per-clip filters) -> one FFmpeg run.
Usage: python3 cutlist.py edit.json out.mp4
edit.json = {"fps":30,"size":[1080,1920],"clips":[{"src":"a.mp4","in":0.0,"out":3.0,"speed":1.0,"vf":""}, ...]}
Ripple delete = remove a clip from the list (gap closes automatically).  Slip = change in/out by the same amount (length unchanged).
Slide = reorder/shift clips; neighbours' lengths are untouched. Copy attributes = reuse the same "vf" string."""
import json,subprocess,sys
e=json.load(open(sys.argv[1])); W,H=e["size"]; fps=e.get("fps",30)
inputs=[];parts=[];labels=[]
for i,c in enumerate(e["clips"]):
    if c["src"] not in inputs: inputs.append(c["src"])
    k=inputs.index(c["src"]); sp=c.get("speed",1.0); vf=c.get("vf","")
    chain=f"[{k}:v]trim={c['in']}:{c['out']},setpts=(PTS-STARTPTS)/{sp},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={fps},setsar=1,format=yuv420p"+(","+vf if vf else "")+f"[v{i}]"
    parts.append(chain); labels.append(f"[v{i}]")
fc=";".join(parts)+";"+"".join(labels)+f"concat=n={len(labels)}:v=1:a=0[v]"
cmd=["ffmpeg","-y","-loglevel","error"]
for s in inputs: cmd+=["-i",s]
cmd+=["-filter_complex",fc,"-map","[v]","-c:v","libx264","-pix_fmt","yuv420p",sys.argv[2]]
subprocess.run(cmd,check=True); print("rendered",sys.argv[2])
