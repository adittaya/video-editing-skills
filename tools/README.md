# tools/ — runnable helpers

Self-contained scripts. Each runs on a plain Python 3 with `ffmpeg` on PATH (or
`pip install imageio-ffmpeg`) and Pillow where noted. No network, no side effects
beyond the output you name.

## qa_check.py — the runnable QA validator
Audits a project folder against the pack's mandatory lists and writes
`EDIT-QA.md` (PASS 1 audit, PASS 2 AI re-think, PASS 3 revalidate, verdict).
```bash
python tools/qa_check.py PROJECT_DIR [--video build.mp4] [--out EDIT-QA.md]
```
It checks the pipeline artifacts (SOURCE-ANALYSIS.json, CONCEPT.md,
ASSETS-PROMPT.md), scans the concept/notes for every mandatory feature, and runs
video analytics (resolution, duration, scene cuts, ASL, loudness LUFS + true
peak). Items are scored **OK / MISSING / N/A**; anything MISSING is listed with a
concrete fix. This is the machine half of `skills/edit-qa-validator`.

## contact_sheet.py — the render-gate contact sheets
Renders the three RENDER GATE variants from a video so the reviewer can pick one.
```bash
python tools/contact_sheet.py VIDEO [--out DIR] [--variant all|v1|v2|v3] [--fps 1]
```
- **V1 — Classic Grid**: 1 FPS frames in a uniform grid, each timestamped.
- **V2 — Storyboard Filmstrip**: larger frames over a time ruler, with scene-cut
  ticks and a per-frame caption.
- **V3 — Pro QC Sheet**: timecode + scene-cut flag + safe-zone overlay per
  thumbnail, plus a colour-swatch strip and a summary header (duration, shots,
  ASL, palette).

Needs Pillow. Uses `ffmpeg -vf fps=1` for frames and ffmpeg scene detection for
the cut ticks.

## think_check.py — scaffold a CONCEPT.md from a raw script
```bash
python tools/think_check.py SCRIPT [--out CONCEPT.md] [--title "My Video"]
```
Splits the script into sentences and beats and emits a CONCEPT.md skeleton
pre-filled with the beat map, the two-column (said | shown), the visual plan, the
style pass, the sentence table and the feature map (all 11 groups) — the
only-a-script path, ready to complete. Standard library only.

## matte.py — A-roll matting (get the character off the background)
```bash
python tools/matte.py VIDEO [--out DIR] [--model u2netp|u2net|isnet-general-use] [--scale 0.6]
```
Mates a video frame-by-frame with rembg and writes `alpha.webm` (VP9 alpha),
`green.mp4`, plus `alpha/`, `green/`, `matte/` and `stills/`. Downscales the
matte input and caps threads for low-memory boxes. **The first job on any
talking-head / voiceover / podcast.**

## cutlist.py — apply a cut list
Applies a ripple/slip/slide/speed cut list to a source (see the pack's FFmpeg
cookbook). 

## track_text.py — track text to an object
Produces an ASS subtitle file that follows a tracked point (needs
`opencv-contrib-python` for tracking).

---

**Typical flow:** `contact_sheet.py` -> pick a variant -> `qa_check.py` -> fix the
MISSING items -> re-run `qa_check.py` until the verdict is PASS.
