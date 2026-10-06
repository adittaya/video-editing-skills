---
name: blender-engine
description: "The pack's central 3D / graphics engine. Drives Blender HEADLESS via Python (bpy) - no GUI, no desktop, no account. Covers 3D modelling, materials/textures/lighting, cameras and animation, camera tracking / matchmoving, VFX / particles / simulations, rigging, Geometry Nodes, compositing, rendering stills and animation, and video encoding via FFmpeg. Use whenever a build needs real 3D, motion graphics, 3D text, camera tracking, or procedural geometry."
---

# Blender Engine — the central 3D / graphics engine

**Scope.** The pack's 3D and graphics engine. It runs **headless** and is driven
**entirely by Python** through `bpy`. Nothing needs a desktop, a GUI, or a login.

**When to use.** Whenever the build needs real 3D — 3D text/objects, motion
graphics, camera tracking / matchmoving, geometry nodes, simulations, particles,
rigging, compositing, or a 3D render. Also when a web code-kit is not enough and
the element is genuinely volumetric.

> **THE PROGRAM-IT LAW (mandatory).** Your AI does not need to *see* Blender.
> Your AI **programs** Blender. Never describe UI clicks — write `bpy` code and
> execute it headless. If you can do it in Blender's UI, you can do it in Python.

---

## STEP 0 — THE ENGINE GATE (before you script)

1. **Choose where it runs.** Heavy jobs → the **remote workspace**
   (`REMOTE-WORKSPACE.md`): Cycles **GPU** / EEVEE there. Light scripts → local,
   **Cycles CPU**.
2. **Get Blender.** Portable build (bundles its own Python — most robust), or the
   `bpy` module (Python-version-pinned: 4.x → 3.11, 5.1+ → 3.13). See
   `BLENDER-ENGINE.md`.
3. **Verify it runs** before the real job: `blender -b --python-expr "import bpy; print(bpy.app.version_string)"`.

## STEP 0.5 — A-ROLL PREP (if a person speaks)

If a person speaks to camera, prep the A-roll first (see `a-roll-matting`).
Blender's motion tracker can then **matchmove** the shot (STEP 3.4).

---

## 1 · Run it headless

```bash
blender --background --python script.py          # run a script
blender -b scene.blend --python script.py        # open a .blend, then run
blender -b --render-frame 1                      # render a frame
```

## 2 · The verified headless recipe (obey these gotchas)

- **EEVEE fails headless** with no GPU/display (`EGL_NOT_INITIALIZED`). **Use Cycles.**
- **Cycles CPU renders headless with no GPU** — `sc.cycles.device='CPU'`.
- **Disable the denoiser** on constrained boxes — `sc.cycles.use_denoising=False`
  (OpenImageDenoise can OOM).

```python
import bpy
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = 'CYCLES'; sc.cycles.device = 'CPU'
sc.cycles.samples = 16; sc.cycles.use_denoising = False
sc.render.filepath = "/out/frame.png"
bpy.ops.render.render(write_still=True)
```

## 3 · What to script (the pipeline)

1. **Model / edit** — meshes, booleans, modifiers (`bpy.ops.mesh.*`, `bpy.data.meshes`).
2. **Materials, textures, lighting** — Principled BSDF, procedural + image textures, HDRI, sun/area lights.
3. **Cameras & animation** — camera rigs, keyframes, f-curves, motion blur, easing.
4. **Camera tracking / matchmoving** — track footage, solve the camera, reconstruct motion (`bpy.ops.clip.*`); place 3D on the moving shot.
5. **VFX, particles, simulations** — fluids, smoke, cloth, rigid body, particles.
6. **Rigging & character animation** — armatures, weights, constraints.
7. **Geometry Nodes / procedural generation** — node graphs for procedural geometry.
8. **Compositing** — compositor node tree, render passes.
9. **Render** — stills and animation; choose engine, samples, resolution, passes.
10. **Encode video** — Blender bundles **FFmpeg**; encode image sequences to MP4/WebM (or hand frames to the workspace's FFmpeg).

## 4 · Quality checks (before you trust a render)

- **Look at the frame.** Render one frame and *view* it before rendering the
  sequence — never render 120 frames blind.
- **Check the camera** — framing, lens, the move; is the subject in frame the whole time?
- **Check the matte/track** — no drift, no sliding, no holes.
- **Check the render settings** — engine, samples, resolution, colour management.
- **Check the encode** — codec, fps, colour range, audio.

## 5 · Where it sits

- **Remote workspace** (`REMOTE-WORKSPACE.md`) — the execution environment (GPU).
- **`bpy`** — how the AI commands Blender.
- **FFmpeg** — the encoder (bundled, or the workspace's).
- **`a-roll-matting`** — the prep step when a person speaks.
- **`ADVANCED-FEATURE-USE-CASES.md`** — 3D camera tracking, motion graphics, compositing.

---

## QA GATE
Run `skills/edit-qa-validator` and `tools/qa_check.py` before delivery — audit the
render (framing, matte/track, colour, encode), AI-re-think anything weak,
revalidate, and write `EDIT-QA.md`.

## HARD LIMITS
- **Program it, never click it.** Headless, scripted, no GUI.
- **Cycles for headless** — EEVEE needs a GPU/display.
- **Never invent** geometry, brands, faces or claims; label every reconstruction.
- **Route heavy jobs to the workspace**; run one job at a time, release the GPU.
- No account or login is ever required for the core software.
