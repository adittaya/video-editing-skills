# Modern Editing Features & Terminal Toolchain — Reference

A human-readable summary of the techniques and tools built into every SKILL.md in this pack.
Each skill also carries its own **Signature techniques** list and **tested FFmpeg recipes** (verified on FFmpeg 6.1.1),
so a single SKILL.md is enough for an agent.

## Part 1 — The technique catalogue: what top editors actually reach for
**Cutting & structure** — jump cut · J-cut / L-cut · match cut (shape, motion, colour) · smash cut · cutaway/insert · split edit · cut-on-beat montage · invisible cut hidden by a whip, zoom or object wipe · freeze frame · reverse · seamless loop · transcript-based rough cut · silence/filler removal · multicam switching.
**Motion & camera** — eased punch-in/push-in · slow digital push · pan/tilt on stills (Ken Burns) · 2.5D parallax from separated layers · camera shake on impacts · speed ramp / time remap · optical-flow slow-motion · stabilisation · whip pan · simulated dolly-zoom · motion blur on fast moves.
**Transitions** — hard cut is the default; then push/slide, whip, zoom-through, shape/mask reveal, luma wipe, light-leak/flash, glitch/RGB split, crossfade. Every transition has a matching sound. Never repeat the same transition twice in a row.
**Text & captions** — kinetic typography · word-by-word karaoke captions · one-accent-word highlight · animated lower-thirds · text tracked to a moving object · **text behind the subject** (matte) · typewriter/mask reveals · drawn-on callouts and arrows · count-up numbers.
**Compositing & depth** — subject cut-out/matting · background blur/replace · split-screen · picture-in-picture · chroma/luma key · screen replacement (UI on a device) · shadow + reflection under cut-outs · glow/bloom · overlays (grain, dust, light leaks) · blend modes (screen, add, multiply).
**Colour & look** — correct first (exposure, white balance), then log→Rec.709, LUT, contrast curve, secondary tweaks (skin, sky), split-tone/film emulation, halation/bloom, grain, vignette, letterbox (2.39:1), shot matching. Protect skin tones.
**Audio design** — dialogue chain (high-pass → denoise → de-ess → compress → loudnorm) · side-chain ducking · SFX layer (whoosh, impact, riser, tick, sub-drop) · ambience/room tone · music edited to phrases · a 0.2–0.4 s silence before the drop · stem separation for cleanup.
**Graphics & data** — animated charts with a single highlight colour · count-ups · map/route draws · diagrams that draw on the narration · UI demo with eased cursor + click ripple · stat "bento" grids · progress bars · timeline graphics.
**AI-assisted (2026)** — word-level transcription · filler/silence removal · scene detection · auto-chapters · face-tracked auto-reframe · matting/rotoscope · upscaling · frame interpolation · stem separation · beat detection · generative B-roll/imagery (disclose when real footage is implied).

## Part 2 — Terminal toolchain (pick the lightest tool that does the job)
| Tool | Use it for | Notes |
|---|---|---|
| **FFmpeg / ffprobe** | cuts, concat, scale/crop, zoom, xfade transitions, speed ramps, LUT/grade, grain/glow, overlays, captions (ASS), audio chain, loudness, export | The backbone. Chain edits in ONE `filter_complex` pass to avoid generation loss. |
| **auto-editor** | rough cut by removing silence/dead air via loudness/motion analysis | Signal analysis, not generative. |
| **faster-whisper / WhisperX** | transcription with word-level timestamps (captions, beat plans, filler cuts) | Needed for ±100 ms word sync. |
| **PySceneDetect / ffmpeg `select='gt(scene,0.3)'`** | find shot boundaries in source footage | |
| **librosa** (Python) | BPM + beat timestamps for cut-on-beat | |
| **HyperFrames (HeyGen, Apache-2.0)** | motion graphics as HTML/CSS/GSAP/Lottie/Three.js → deterministic MP4; CLI `init`, `preview`, `lint`, `render` | Agent-friendly: `npx hyperframes init my-video` → edit `index.html` → `npx hyperframes render`. |
| **Remotion** (React) | code-defined video compositions, data-driven templates | Check its licence terms for company/commercial use. |
| **MoviePy** (Python) | scripted clip assembly where FFmpeg graphs get unwieldy | Slower than raw FFmpeg. |
| **rembg / Robust Video Matting / SAM-family** | subject cut-out (alpha) for text-behind-subject and layered looks | Check each model's licence (some are non-commercial). Review edges/hair; rembg is per-frame (flicker risk), RVM is temporally consistent. |
| **MediaPipe** | face tracking for auto-reframe to 9:16 | |
| **Demucs** | separate vocals/music for cleanup | |
| **Blender (headless `blender -b -P script.py`)** | 3D titles, product/architecture renders, camera moves | Heavy; use only when 3D is the point. |
| **MLT/melt, GStreamer, OpenTimelineIO** | timeline-style assembly and interchange | Optional; not needed for most jobs. |
| **ImageMagick / Pillow** | stills, masks, cards, contact sheets | |
*Always check what is installed first and fall back to FFmpeg-only:* `for t in ffmpeg ffprobe python3 node npx auto-editor scenedetect melt blender; do command -v $t >/dev/null && echo "have $t" || echo "missing $t"; done`. If the network is off, do not plan on installing anything.


## Part 3 — What makes it feel premium (rules, not effects)
- **One system:** one palette, one type pair, one motion grammar, one transition vocabulary per video. Consistency reads as expensive.
- **Ease everything:** entrances `cubic-bezier(0.16,1,0.3,1)`, transforms `cubic-bezier(0.65,0,0.35,1)`, playful overshoot `cubic-bezier(0.34,1.56,0.64,1)`. Never linear.
- **Depth:** separate foreground / mid / background; add soft shadows, subtle parallax (≤ 3–6% travel), grain 5–12% and a gentle vignette.
- **Hierarchy:** one focal point per frame, ≥ 30% negative space, max ~6 elements.
- **Rhythm:** vary shot length; land graphics and cuts on beats/words; let important moments breathe.
- **Sound sells picture:** a sound for every cut and graphic land; the quiet before the hit.
- **Restraint:** effects serve the idea. If it doesn't clarify or emphasise, delete it.
- **Polish:** no audio pops, no jitter, no black edges, no text outside safe zones, no single-frame flashes.


## Part 4 — Hybrid premium style & advanced feature pack (from six reference videos)

### H1. What "hybrid" means (observed in six premium reference videos)
Text and graphics are treated as **objects inside the scene**, not captions laid on top. Footage, 3D/AI renders, UI cards and kinetic type share one visual system. Devices seen across the references:
1. **Hierarchy inside one line** — a small lead-in word and one huge keyword (e.g. "here's the branding secret" small → "no one tells you" large).
2. **Single accent colour** (red, gold, orange or brand blue) against a controlled base (white, black or one graded footage look) with soft shadows and glow for depth.
3. **Words appear on the spoken beat** with blur-in/rise-in; the key word gets the accent colour and the largest size.
4. **Text integrated with the subject** — text arcs/wraps around the speaker, sits behind them (matte), or tracks an object; neon face-glow or flash on impact words.
5. **UI-as-graphics** — stat cards (64%, $50k), badges, toggles, a search bar that types "Comment ___", cursor/hand pointer, app-icon orbit, mind-map nodes.
6. **Hero objects** — 3D or AI-generated renders (statue, badge, product, device mock) on clean backgrounds, slow push + soft shadow.
7. **Hidden cuts** — a whip, flash, starburst/ribbon sweep, zoom-through or object wipe covers the edit; the hard cut is invisible.
8. **Before/After or phone-frame framing** — split-screen labelled panels, or a phone-shaped inset over a blurred, enlarged copy of the same footage.
9. **Matched cinematic B-roll** graded to the same look as the talking head; the speaker may be cloned/multiplied for emphasis.
10. **Comment-keyword CTA** ("Comment 'folder'") and a brand end card with a soft focus-pull.
**Pace:** a new visual event every 1–2.5 s (measured cut ASL 2.3–3.2 s, but most changes were in-scene motion, not cuts). **Audio:** speech forward, bass-heavy bed, impact/whoosh hits on the key-word slams; delivered around −14 LUFS.

### H2. How much of it to use ("hybrid dial") — decide per job
**0** = none (clean, regulated, calm) · **1** = light (accent colour, hierarchy lines, subtle push) · **2** = medium (+ UI cards, stat count-ups, hidden-cut transitions) · **3** = full (+ behind-subject text, 3D/AI hero objects, glow/flash, phone-frame, tracked text). Ask the client which dial; default is given in "Hybrid dial for this skill" below. Higher dial = more assets required (see H4) and more render time.

### H3. Editor feature → terminal equivalent (NLE checklist)
| Editor feature | In the terminal |
|---|---|
| Cut / split / trim | `trim` + `setpts`, or `cutlist.py` clips (in/out) |
| **Ripple edit** (close the gap) | delete the clip from the cut list — concat closes the gap |
| **Slip** (change content, keep position/length) | shift `in` and `out` by the same amount |
| **Slide** (move a clip, neighbours keep length) | reorder/shift entries in the cut list |
| **Copy/paste attributes** | reuse the same `vf` string/preset for many clips (store presets in one file) |
| Speed / ramp / slow-mo | `setpts`, split+concat ramp (recipe 3), `minterpolate` |
| Colour correct / LUT / contrast / saturation | `eq`, `curves`, `colorbalance`, `lut3d` (recipe 5) |
| **Sharpen / blur** | `unsharp` (recipe 23), `gblur`, `boxblur` |
| Film grain / vignette / glow | recipe 4 |
| **Light leaks / lens flares** | generated gradient overlay + `blend=screen` (recipes 24–25) |
| Transitions (fade, whip, zoom, glitch, match) | `xfade`, recipes 2, 7, 21, 31 |
| Keyframes: zoom, pan, **opacity, position** | expressions in `scale`/`crop`/`overlay` with `t` (recipes 1, 26) |
| **Object tracking (text follows subject)** | `track_text.py` (OpenCV CSRT → ASS positions) |
| Subtitles / kinetic type | ASS from word timestamps (recipe 13), HTML/GSAP via HyperFrames |
| Lower thirds / callouts | drawtext / PNG overlay with eased entrance (recipes 12, 26) |
| **Emoji / sticker pop** | transparent PNG overlay with scale-pop timing (recipe 26); never rely on system emoji fonts in drawtext |
| Audio: music sync, SFX, denoise, EQ, ducking | recipes 17, 18, librosa beats |
| Jump cuts / silence removal | auto-editor or `silencedetect` (recipe 19) |
| Pattern interrupts / B-roll / loop ending | recipes 1, 3, 15, 27 |
| **Green screen (chroma key)** | `chromakey` + `despill` (recipe 22) |
| **Masking & reveal** | animated `alphamerge` mask (recipe 28) |
| **Depth blur / fake bokeh** | radial-mask blur (recipe 29) |
| Letterbox | recipe 8 |
| **Proxy editing** | recipe 36 |
| Multicam | cut list across several sources + audio-energy/transcript switching |
| Presets/templates | keep a presets folder (LUTs, ASS styles, `vf` strings, HTML templates) |
| Auto subtitles (AI) | faster-whisper / WhisperX → SRT + ASS |

### H4. Hybrid-style asset request (ASK THE CLIENT — never fabricate)
At dial 2–3, add these to ASSET-REQUEST.md and wait for them (or confirm the AI may generate/synthesize each):
- **Brand kit:** the accent colour, base colours, 1–2 fonts, logo (SVG/PNG with transparency), end-card wording and the comment-keyword CTA.
- **Script/transcript with the key word of each line** marked (the one word that gets the accent).
- **Subject files:** the speaker/product footage; for behind-subject or cut-out looks either a **green-screen shot**, a **clean background plate**, or permission to run a matting model (check its licence).
- **Hero objects:** 3D renders, AI images or product packshots **with transparent background** (PNG/WebM-alpha), or approval to use generated placeholders (disclosed).
- **UI assets:** real screenshots/screen recordings, logo/icon set, names and figures to show on cards (each with source/date).
- **Sound pack:** whoosh, impact, riser, click, pop, sub-drop (licensed) and the music bed.
- **References:** 1–3 videos whose look is wanted (we match the system, never copy the content).
If an asset is missing and cannot be generated honestly, **lower the dial**, say so, and list what unlocks the next level.

### H5. Tested recipes 22–36 (FFmpeg 6.1.1; all executed on synthetic sources)
```bash
# 22 Green screen: key + remove green spill, composite over a background
-i bg.mp4 -i green.mp4 -filter_complex "[1:v]chromakey=0x00ff00:0.12:0.08,despill=type=green[fg];[0:v][fg]overlay=(W-w)/2:(H-h)/2:shortest=1"
# 23 Sharpen (apply last, small amount; avoid on noisy footage)
-vf "unsharp=5:5:0.8:5:5:0.0"
# 24 Moving warm light leak (screen-blend a generated gradient that sweeps across)
-i in.mp4 -f lavfi -i "color=c=black:s=1920x1080:r=30:d=4,geq=r='255*exp(-pow((X-1920*(0.2+0.2*T))/500,2))':g='140*exp(-pow((X-1920*(0.2+0.2*T))/400,2))':b='40*exp(-pow((X-1920*(0.2+0.2*T))/300,2))'" -filter_complex "[0:v][1:v]blend=all_mode=screen:all_opacity=0.7"
# 25 Lens-flare hotspot (static or animate the centre with T)
-f lavfi -i "color=c=black:s=1920x1080:r=30:d=4,geq=r='255*exp(-hypot(X-1400,Y-300)/90)':g='220*exp(-hypot(X-1400,Y-300)/90)':b='160*exp(-hypot(X-1400,Y-300)/90)'"  (then blend=all_mode=screen:all_opacity=0.8 as in 24)
# 26 Pop-in card / sticker / emoji PNG: fade in + rise with ease-out (cubic) between t=0.3 and 0.8 s
-i video.mp4 -loop 1 -i card.png -filter_complex "[1:v]format=rgba,fade=t=in:st=0.3:d=0.4:alpha=1[c];[0:v][c]overlay=x=(W-w)/2:y='H-h-120+80*pow(1-min(max((t-0.3)/0.5,0),1),3)':shortest=1"
# 27 Loop ending: last 0.5 s cross-dissolves into the first 0.5 s (output = duration − 0.5)
-filter_complex "[0:v]split[m][h];[h]trim=0:0.5,setpts=PTS-STARTPTS[head];[m]trim=0.5:DUR,setpts=PTS-STARTPTS[body];[body][head]xfade=transition=fade:duration=0.5:offset=DUR-1.0[v]" -map "[v]"
# 28 Mask reveal (left→right wipe of clip B over A over 1.5 s; swap the geq for circles/shapes)
-i a.mp4 -i b.mp4 -filter_complex "color=c=white:s=1920x1080:r=30:d=4[w];[w]geq=lum='if(lt(X,1920*T/1.5),255,0)',format=gray[m];[1:v][m]alphamerge[fg];[0:v][fg]overlay=shortest=1"
# 29 Fake depth blur: sharp centre, blurred edges (radial mask made once with geq → radial.png)
ffmpeg -f lavfi -i "color=c=black:s=1920x1080,format=gray,geq=lum='clip((hypot(X-960,Y-540)-300)*0.6,0,255)'" -frames:v 1 radial.png
-i in.mp4 -loop 1 -i radial.png -filter_complex "[0:v]split[s][b];[b]gblur=sigma=18[bl];[bl][1:v]alphamerge[blm];[s][blm]overlay=shortest=1"
# 30 Neon / glow text (draw text, blur a copy, screen-blend it back)
-vf "drawtext=text='WORD':fontsize=200:fontcolor=0xff2040:x=(w-text_w)/2:y=(h-text_h)/2:fontfile=FONT.ttf,split[a][b];[b]gblur=sigma=25[g];[a][g]blend=all_mode=screen:all_opacity=1"
# 31 Impact flash (brightness pulse at t=2.0) + barrel-distortion punch
-vf "eq=brightness='0.6*exp(-12*abs(t-2))':eval=frame"        |        -vf "lenscorrection=k1=-0.25:k2=-0.1"
# 32 Count-up that lands on the spoken number (here 0→64 % in 1 s)
-vf "drawtext=text='%{eif\:trunc(min(t/1.0\,1)*64)\:d}%':fontsize=300:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:fontfile=FONT.ttf"
# 33 Phone-frame inset over a blurred, darkened, enlarged copy of the same footage (rounded-corner mask)
-filter_complex "[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=40,eq=brightness=-0.15[bg];[b]scale=-2:1500,crop=800:1500,format=yuva420p,geq=lum='lum(X,Y)':cb='cb(X,Y)':cr='cr(X,Y)':a='if(lt(hypot(max(abs(X-400)-340,0),max(abs(Y-750)-690,0)),60),255,0)'[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2"
# 34 Before/After labelled vertical split
-i after.mp4 -i before.mp4 -filter_complex "[0:v]scale=1080:-2,pad=1080:960:0:(960-ih)/2[t];[1:v]scale=1080:-2,pad=1080:960:0:(960-ih)/2[u];[t][u]vstack,drawtext=text='After':fontsize=44:fontcolor=white:box=1:boxcolor=0xff3366@0.9:boxborderw=14:x=30:y=30:fontfile=FONT.ttf,drawtext=text='Before':fontsize=44:fontcolor=white:box=1:boxcolor=0x333333@0.9:boxborderw=14:x=30:y=990:fontfile=FONT.ttf"
# 35 Cut list (ripple/slip/slide/speed/copy-attributes) → see cutlist.py below
# 36 Proxy workflow: edit on 360p proxies, then re-render the SAME cut list against the originals
ffmpeg -i original.mp4 -vf scale=-2:360 -c:v libx264 -preset ultrafast -crf 28 -an proxy.mp4
```
**Not testable with FFmpeg alone — build these in HTML/CSS/GSAP/Three.js (HyperFrames or Remotion) or request assets:** text arcing/wrapping around a subject in 3D, particle-dissolve text, 3D camera moves on hero objects, app-icon orbit, mind-map/UI motion, speaker cloning/"many arms", AI-generated hero renders. Render those layers with transparency, then composite with FFmpeg (overlay) and grade the whole. These approaches are documented but were not executed in this pack's test run — render a 2-second test and inspect frames before building the full video.

### H6. Scripts (tested)
**`cutlist.py` — NLE-style edits in one FFmpeg pass.**
```python
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
```
Example `edit.json`: three clips with one shared `vf` (copy-attributes), clip 2 at 0.5× and clip 3 at 2×. Ripple delete = remove an entry; slip = move `in`/`out` together; slide = reorder entries. Re-render in seconds.
**`track_text.py` — make text follow a moving object (OpenCV CSRT).** Requires `opencv-contrib-python`. Tracker can drift on fast motion/occlusion: review, re-seed the box, split into shots.
```python
#!/usr/bin/env python3
"""Make text follow a moving object. Usage: python3 track_text.py in.mp4 x y w h "LABEL" out.ass [dx dy]
(x,y,w,h = bounding box of the object on the FIRST frame, in pixels.) Then burn with: ffmpeg -i in.mp4 -vf subtitles=out.ass ...
Uses OpenCV CSRT tracker (opencv-contrib). Review the result; re-seed the box if the tracker drifts."""
import cv2,sys
src,x,y,w,h,label,out=sys.argv[1],*map(int,sys.argv[2:6]),sys.argv[6],sys.argv[7]
dx,dy=(int(sys.argv[8]),int(sys.argv[9])) if len(sys.argv)>9 else (0,-50)
cap=cv2.VideoCapture(src); fps=cap.get(cv2.CAP_PROP_FPS); W=int(cap.get(3)); H=int(cap.get(4))
ok,f=cap.read(); tr=cv2.TrackerCSRT_create(); tr.init(f,(x,y,w,h))
def ts(t): return f"{int(t//3600)}:{int(t%3600//60):02d}:{t%60:05.2f}"
ev=[]; i=0
while ok:
    ok2,b=tr.update(f)
    if ok2:
        cx=int(b[0]+b[2]/2)+dx; cy=int(b[1])+dy
        ev.append(f"Dialogue: 0,{ts(i/fps)},{ts((i+1)/fps)},T,,0,0,0,,{{\\an5\\pos({cx},{cy})}}{label}")
    ok,f=cap.read(); i+=1
hdr=f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: T,DejaVu Sans,{max(24,H//14)},&H00FFFFFF,&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,3,0,5,10,10,10,1
[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""
open(out,'w').write(hdr+"\n".join(ev)); print(len(ev),"tracked frames ->",out)
```

### H7. Motion rules for the hybrid look
- Entrance: blur 10–18 px → 0, rise 20–40 px, scale 0.9 → 1, over 0.25–0.45 s with ease-out (`cubic-bezier(0.16,1,0.3,1)`); exit faster (0.2–0.3 s).
- Key word: accent colour, 1.6–2.5× the lead-in size; land within ±100 ms of the spoken word (eye leads the ear by up to 80 ms).
- Impact words: 2-frame flash or glow pulse + low hit; never flash faster than 3 per second.
- Hidden cut recipe: start the whip/flash/sweep 3–5 frames before the cut and finish 3–5 frames after; put the whoosh on the first frame of motion.
- Depth: soft shadow under every card/object, background slightly desaturated or blurred, ≤ 6% parallax.
- Keep ≥ 30% negative space, ≤ 6 elements per frame, and keep text inside the platform text-safe zone.
- Do not copy a creator's specific artwork, brand or wording. Match the *system* (hierarchy, rhythm, motion), never the content.

## Part 5 — Colour management, HDR & delivery (the gap this pack flagged)

**Working space**
- Grade in ONE working space. For SDR delivery that is **Rec.709 / sRGB**.
  Convert every source into it FIRST (log/HLG/LUT → 709), then grade. Never
  grade mixed spaces.
- Tag the output explicitly so players do not guess:
  `-colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv`
- Range: deliver **limited/TV (16–235)**; keep it consistent end to end — a
  double full↔limited conversion crushes blacks.

**HDR**
- Two transfer functions: **HLG** (`arib-std-b67`) for broadcast/live, **PQ**
  (`smpte2084`) for streaming masters. Both need **BT.2020** primaries and
  **10-bit** (`-pix_fmt yuv420p10le`).
- Master HDR only when the client needs it. **Most social platforms do not
  accept HDR** — deliver SDR, or tone-map down.
- HDR → SDR tone map:
  `zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p`
  (use `libplacebo` where available). Judge it on a phone, not in the editor.
- **Graphics for HDR:** reference white is ~203 nits, not 1000 — pure-white
  1000-nit graphics glare. Build graphics in SDR and place them, or set graphic
  white ≈ 203 nits.

**Banding & gradients (the Palette Law's weak point)**
- Gradients band in 8-bit. Prevent it: add 1–2% grain/dither
  (`noise=alls=2:allf=t`) or deliver 10-bit for gradient-heavy pieces.
- Never upscale a gradient from a small source — generate at delivery
  resolution.

**Verify (never ship unseen)**
- `ffprobe -v error -select_streams v:0 -show_entries stream=color_space,color_primaries,color_transfer,color_range,pix_fmt -of default=nw=1`
  — confirm the tags are what you intended.
- View on a phone AND a second display; check skin tones and black level.

## Part 6 — Reference cards (teardowns of real videos)

### Card 005 — "Turning ideas into visuals" editor portfolio reel (31 s, 16:9)

Read from a 1-second contact sheet. One-hue blue monochrome with purple
accents, soft-blurred gradients, floating UI objects, glassmorphism/3D, and the
speaker composited INTO the scene.

| Time | Beat | What is on screen |
|---|---|---|
| 0–4 s | Hook aimed at the scroll | "Scrolling past" → "Scrolling past boring" → cursor → "Need an editor who understands your vision?" |
| 5–9 s | Identity before credentials | "Meet your editor." → the person → "Mohammed zayan" + dotted line → "video editor" → bio card |
| 10–14 s | Tools as trust | Ae icon expands to After Effects / Premiere Pro / DaVinci Resolve under "Where the mag…" |
| 15–19 s | The client's own questions | phone chat "Reels?" / "Cinematic?" / "What about motion graphics" → "works?" → 4-clip collage → floating 3D discs |
| 20–24 s | Positioning + proof | "Your idea." → "Your idea. My craft." → Client Reviews card expanding to 5 starred reviews → cursor clicking one |
| 25–29 s | Brand + close | "zayyaanedits" badge → "Let's make something great." → "Open for projects." |
| 30–31 s | The ask | "Open for projects. DM me." → fade |

**Devices:** name-the-behaviour hook · identity before credentials · tool-stack
as trust · question-bubble (the buyer's own words as UI) · role-assigning
positioning line · testimonial wall · soft CTA. Placements used: **front
overlay** (bio card, software list over the speaker) and **behind/around the
subject** (speaker composited over the gradient with elements beside him).

**THE LESSON — decorative vs explanatory.** This reel's graphics are beautiful
but they do not TEACH. The discs, the collage, the cards carry mood, not
meaning; nothing shows *how* the editing works. Copy the LOOK, then add what it
lacks: the **E-visual explain moments** from the Visual Narration Layer — a
before/after, a technique breakdown, a diagram of the process. A portfolio reel
can survive on vibe; a client-facing explainer cannot.

**Do-not-copy line:** methods only — never the name, handle, bio claims,
testimonials, or the exact palette.

## Part 7 — The look is Apple Standard (mandatory, pack-wide)

Every skill uses one system. There is no style menu. The tokens (canvas
`#ffffff`/`#f5f5f7` bands, text `#1d1d1f`/`#6e6e73`/`#86868b`, the one blue
`#0071e3`/`#0066cc`/`#2997ff`, the Inter-for-SF-Pro type ramp down to
17px/400/-0.374px, 980px pill buttons, one-CTA-per-scene, the single-source
shadow, the spring motion grammar) are mandatory in all 30 skills. Vertical
difference = what the graphics depict + which one accent carries meaning. Where
Part 1's technique catalogue names a stylised palette (neon, glitch, teal-orange,
halftone), treat it as a **technique to use sparingly inside the Apple system**,
never as an alternative look.

## Part 8 — The mandatory feature use-cases (modern standard)

A build is not finished until it uses these where the concept needs them:

**Camera & motion** — anchor zoom in · zoom out (reveal) · motion tracing /
follow camera · slow push · camera shake on impact · speed ramp · motion blur
(velocity; zero at rest).

**Keyframing & animation** — keyframe everything (position, scale, opacity,
rotation, blur) · bezier easing (curve the path, never linear) · mask / wipe
reveal · parallax / 2.5D depth · freeze frame / hold.

**Text & data** — kinetic text / word-pop · count-up numbers · text tracked to an
object · text behind the subject · callouts & arrows.

**UI & product (any demo)** — readability zoom (>=4% of frame height) ·
micro-interactions (hover, press, ripple, toggle, focus) · screen transitions
(push/pull, modal + scrim, sheet) · cursor physics (bezier, minimum-jerk,
overshoot, click anatomy) · comparison split / PiP · screen replacement.

**Edit & finish** — cut-on-beat / cut-on-action · a sound for every cut ·
correct then grade · seamless loop.

Every SKILL.md lists these with a per-style emphasis line; the style governs HOW
they look, never WHETHER they are used.


## Part 9 — The documentary style family

Fourteen documentary styles, each a skill, mapped by `DOCUMENTARY-STYLE-GUIDE.md`:

**Explainer family** — vox-explainer (narration-driven flat-design motion
graphics: 12fps stutter, camera-blur transitions, animated maps, highlighter,
narration-synced motion) · geo-explainer-maps (map-led geo storytelling) ·
archival-essay-doc (argumentative montage, statistic typography, photo
zoom-and-pan) · ken-burns-archival (stills-in-motion, sepia, letter narration).

**Journalistic family** — investigative-doc (evidence-led reconstruction,
documents/data, multicam sync) · true-crime-doc (thriller structure, hook
episode, ticking clock, low-res surveillance) · bodycam-evidence-doc (raw
institutional footage, no VO) · immersive-field-doc (embedded first-person
reportage).

**Cinematic family** — netflix-docuseries (streaming house style, Slow Media,
episodic cliffhangers) · nature-wildlife-doc (blue-chip natural history) ·
op-docs-short (short prestige documentary, form-forward) · documentary-film (the
general craft).

**Form-forward family** — animated-documentary (rotoscope / illustrated) ·
docudrama-reenactment (dramatized reconstruction, labelled) · essay-film
(first-person inquiry, lateral montage).

Underneath sits **Bill Nichols' six modes** (poetic, expository, observational,
participatory, reflexive, performative) and the craft approaches (evidentiary,
verité, montage, radio-cut, additive, subtractive). Ethics that hold everywhere:
no fabricated quotes/stats, label every recreation/animation/composite, never
manufacture a confession, never distort meaning, and never trick the audience.


## Part 10 — The advanced professional toolset (mandatory in every skill)

Every skill now carries an **ADVANCED FEATURE USE-CASES** section (mandatory) and
a pointer to `ADVANCED-FEATURE-USE-CASES.md`. The toolset:

**Timeline** multi-track layering · multi-camera editing · proxy editing · batch
export · collaboration. **Motion** keyframing · motion tracking · masking/
rotoscoping · speed ramping / time remapping · stabilisation · frame blending /
optical flow. **Colour** colour correction -> grading · scopes (waveform,
vectorscope, histogram, parade) · HDR grading. **Compositing** chroma key ·
compositing/VFX · 3D camera tracking · advanced transitions & effects.
**Audio** noise reduction · EQ · audio syncing · multi-track mixing ·
surround/spatial. **AI** auto subtitles · AI background removal · auto reframing ·
scene detection & auto cutting · AI colour/exposure. **Stills & design** layers,
masks, blending modes · frequency separation · dodge & burn · content-aware fill ·
perspective correction · RAW/tone curves/HDR merge/panorama · AI selection ·
non-destructive · vector/bezier · gradient mesh · kerning/tracking/leading ·
symbols · artboards · grids · multi-format export.

**The Camera Law** (mandatory where there is a camera): one camera wrapper only ·
one move at a time · every zoom has a reason (READ/EMPHASIZE/REVEAL/FOLLOW/
BREATHE) · never cut while zoomed · motion blur only during fast motion
(`blur = clamp(v*k, 0, max)`; k~0.012, max~24px). Anchor zoom sets the origin on
the target; follow keeps the subject in a safe zone with a damped spring.

**The Sentence Law** (mandatory): every narration sentence gets its own visual
event, bound to the sentence's stressed word (+/-100 ms); no visual-less
sentences, no sentence-less visuals; the camera move is itself a sentence-level
event.


## Part 11 — Contact-sheet variants (the render gate)

The render gate now offers the reviewer a choice of contact-sheet designs, built
from 1 FPS frames (`ffmpeg -i build.mp4 -vf fps=1`), at least two of:

- **V1 — Classic Grid**: uniform grid in time order, each frame timestamped.
- **V2 — Storyboard Filmstrip**: larger frames over a time ruler with scene-cut
  ticks and a one-line caption per frame (reads like a storyboard; best for
  pacing/flow).
- **V3 — Pro QC Sheet**: timecode + scene-cut flag + motion indicator + safe-zone
  overlay per thumbnail, plus a colour-swatch strip and a summary header
  (duration, shots, ASL, loudness, palette).

The agent must present the variants and ask: "Did you like any of these, or shall
I generate more variants so you can choose?" Render the full video only after the
variant and the cut are finalised.


## Part 12 — Pipeline connectivity (everything is connected)

CONCEPT.md is the single source of truth, and each stage feeds the next and
writes its result back:

SOURCE -> `SOURCE-ANALYSIS.json` -> CONCEPT (premise, sentence table, camera-track
plan, **contact-sheet plan**, sync map, asset manifest) -> ASSETS-PROMPT (from the
manifest) -> BUILD (follows the sentence table + camera track) -> RENDER GATE
(contact-sheet variants V1/V2/V3 visualise the beat map) -> SIGN-OFF -> RENDER.

**A new contact sheet means a new CONCEPT revision** — if the sheet reveals a
change, the concept is updated first, then the build follows. Nothing is decided
in isolation and no stage is skipped.


## Part 13 — The caption & text system

Every skill now carries a mandatory **CAPTION & TEXT SYSTEM** section:

**Three modes** — styled text captions (designed, on-brand, animated, timed to
the word) · transparent-background captions (alpha PNG or alpha clip: outline
text, sticker/karaoke text, cut-out words, text-behind-subject) · chroma-key text
& subject (flat green #00B140 / blue, despill, 1-2 px choke, light wrap, garbage
matte).

**Styled-caption spec** — style sheet (font, weight, size, tracking, leading,
case, fill, stroke/box, accent, entrance/exit); word-level timing (+/-100 ms);
<=2 lines; <=17 chars/s; minimum cue ~0.84 s; inside the text-safe zone.

**Transparent-caption spec** — PNG with alpha, no background (or WebM VP9 alpha /
ProRes 4444); 1-2 px feather, no halo, premultiplied; text-behind-subject uses a
clean matte.

**Surprise pack** — kinetic typography (word-by-word, anchor repositioning) ·
word-pop / karaoke captions · animated underline / highlight / hand-drawn circle ·
text-behind-subject / rotoscoped text · alpha overlays (lower-thirds, sticker
captions, floating labels).


## Part 14 — The QA validator (audit -> re-think -> revalidate)

Every build ends at the QA gate. The `edit-qa-validator` skill runs three passes:

1. **AUDIT** — the MASTER CHECKLIST (pipeline connectivity, advanced toolset,
   modern-standard features, Camera Law, Sentence Law, Caption & Text System,
   visual narration layer, render gate, ethics, platform) marked OK / WEAK /
   MISSING / N/A, with timecode evidence.
2. **AI RE-THINK** — for each WEAK/MISSING item, the concrete fix: what to add,
   where (scene/timecode/sentence), how (the exact move or kit), why it improves
   the video, and the expected gain.
3. **REVALIDATE** — re-audit after the fixes and produce the diff; PASS only when
   no star-mandatory item is MISSING and the caption system / Camera Law /
   Sentence Law are clean. Report: `EDIT-QA.md`.

**Caption style library (`CAPTION-STYLES.md`):** Apple-Clean, Vox-Highlighter,
Sticker-Pop, Outline-Alpha, Karaoke-Word — each with a full style sheet, motion,
timing, alpha notes and when to use it.


## Part 15 — Runnable tools

`tools/qa_check.py` — the machine half of the QA validator: audits a project
folder (pipeline artifacts + every mandatory feature keyword + video analytics:
resolution, duration, scene cuts, ASL, loudness LUFS/true-peak), scores each item
OK/MISSING/N/A, lists a fix for each MISSING item, and writes `EDIT-QA.md`
(PASS 1 audit, PASS 2 AI re-think, PASS 3 revalidate, verdict).

`tools/contact_sheet.py` — renders the three render-gate variants from a video:
V1 Classic Grid, V2 Storyboard Filmstrip (time ruler + scene-cut ticks), V3 Pro QC
Sheet (timecode + cut flag + safe-zone overlay + palette strip + summary header).

`tools/cutlist.py`, `tools/track_text.py` — cut-list application and text-to-object
tracking. Typical flow: contact_sheet -> pick variant -> qa_check -> fix -> re-run.


## Part 16 — The complete advanced-feature catalogue (11 groups)

`ADVANCED-FEATURE-USE-CASES.md` is now a full catalogue, and CONCEPT.md runs a
mandatory **Feature Pass** over it.

1. **Camera & framing** — zoom in/out · character/face zoom · push in/pull out ·
   pan/tilt · truck/pedestal/crane/boom · orbit/arc · whip pan · snap/crash zoom ·
   dolly zoom (Vertigo) · rack focus/focus pull · follow focus · parallax move ·
   Dutch angle · handheld vs stabilised · drone/aerial · slow reveal · reframe.
2. **Motion & animation** — keyframing · easing/bezier · anchor point · motion
   tracking · masking/rotoscoping · shape morph · puppet/rig · expressions ·
   text animators · spring/follow.
3. **Speed & time** — speed ramp · time remap · reverse · freeze · slow motion
   (optical flow) · timelapse/hyperlapse · strobe/posterize · frame blending ·
   jump cut.
4. **Transitions & cutting** — hard/J/L/match/cut-on-action/cut-on-beat · cross
   dissolve · dip to black · whip/zoom/blur · mask/wipe/iris · light leak/film
   burn · glitch/RGB split · morph cut · slide/push/3D flip · invisible cut.
5. **Text & titling** — kinetic type · word-pop · karaoke · lower thirds · text
   behind subject · type-on/draw-on · highlight/underline/circle · sticker/alpha
   captions · count-ups · SRT/VTT.
6. **Colour** — correction · grading (LUT/film/split-tone) · scopes · colour
   match · skin-tone protection · LOG/HDR conversion · vignette/grain/halation.
7. **Compositing & VFX** — chroma key · rotoscoping · tracking · 3D camera
   tracking/matchmove · set extension · screen replacement · particles/shaders ·
   light wrap/glow/flare · object removal/clean plate · 2.5D parallax · nesting.
8. **Audio** — noise reduction · EQ/compression/limiting · sync · multi-track
   mixing · sound design/SFX/foley · music beat mapping · dialogue/VO · spatial ·
   loudness.
9. **AI & smart** — auto subtitles · AI background removal · auto reframing ·
   scene detection · AI colour · generative fill · AI upscale/denoise · face/
   object detection.
10. **Stills & design** — layers/masks/blending · frequency separation · dodge &
    burn · content-aware fill · perspective correction · RAW/curves/HDR merge/
    panorama · AI selection · vector/bezier · gradient mesh · typography ·
    symbols · artboards · grids · multi-format export.
11. **Workflow & delivery** — multi-track · multicam · proxy · nesting · batch
    export · colour management · collaboration.

**The Feature Pass:** walk all 11 groups, record every feature in the FEATURE MAP
(applies? -> where -> how -> why). No group skipped; every applicable feature has
a row; the map feeds the asset manifest and the QA gate.


## Part 17 — The Thinking System & the Style library

`THINKING-SYSTEM.md` — the decision-making: the **planning stack** (goal →
audience → angle → concept → script → beats → shots, top-down); the **EZRA**
lenses (Emotion, Story, Rhythm, Action); **Murch's Rule of Six** (emotion 51%,
story 23%, rhythm 10%, eye-trace 7%, 2D plane 5%, 3D space 4%); the two mental
states (audience + architect); and the **only-a-script path** — script audit →
thesis test → beat map → two-column (said | shown) → shot cards → visual plan
(beat → viewer question → evidence → risk → asset) → style/feature pass →
animatic. Plus the motion-design pre-production chain (brief → script → boards →
styleframes → animatic → animation → sound → delivery), where each stage locks a
layer and changes are cheapest earliest.

`MOTION-UI-STYLE-LIBRARY.md` — the motion-style catalogue (types, ~25 styles,
techniques) and the UI/UX style families (depth/surface, flat/structured,
raw/experimental, retro, layout-led, nature, spatial, motion-first, vendor
languages) plus the 2026 UI/UX patterns. The **Style Pass** picks a motion style,
a UI style and a caption style deliberately, with one primary + one garnish, the
failure mode named, and a style frame proved before the build.

Both are wired into **STEP 1** of every skill: CONCEPT.md now carries a mandatory
**THINKING PASS** and **STYLE PASS** alongside the feature map and contact-sheet
plan.


## Part 18 — The agent prompt & the creative director

`AGENT-PROMPT.md` is the paste-ready brief. The agent runs five phases: **INTAKE**
(asks for goal, audience, platform, duration, message, tone, brand, source,
deliverables, deadline, must-haves, no-gos — one list, then waits) -> **OPTIONS**
(2-3 distinct directions: concept, motion style, UI style, caption style, feature
emphasis, why it works) -> **RECOMMENDATION** (its own pick, reasoning,
trade-offs, failure mode, confidence) -> **PLAN** (CONCEPT.md) -> **BUILD & GATES**
(contact-sheet gate + QA gate).

The **`creative-director`** skill is that brain: intake checklist, the option
template, a 5-point scoring rubric (fit, impact, feasibility, distinctiveness,
risk), and a handoff to the build skill. It is the front door to the pack.

`tools/think_check.py` scaffolds a CONCEPT.md from a raw script (sentences ->
beats -> the two-column -> visual plan -> style pass -> feature map), so the
only-a-script thinking pass is ready to complete.


## Part 19 — Style freedom (the barrier removed)

There is **no mandatory style**. The Apple Standard is the pack's **house
default** — a strong starting point for product, UI and corporate work — and a
**recommendation, not a rule**. Every build chooses its look in the **Style Pass**
(a motion style + a UI style from `MOTION-UI-STYLE-LIBRARY.md`, and a caption
style from `CAPTION-STYLES.md`), the agent recommends the best fit with its
reasoning, and **no style is deprecated**. Each skill still names the style
natural to its vertical as a reference; the agent may recommend another when it
fits the brief better. The remedy (`AGENT-PROMPT.md`) and every skill's look
notice carry this framing.
