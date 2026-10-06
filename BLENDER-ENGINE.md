# THE BLENDER ENGINE — the pack's central 3D / graphics engine

> **Your AI does not need to *see* Blender. Your AI *programs* Blender.**
>
> Blender is the pack's **central 3D and graphics engine**. It runs **headless**
> — no desktop, no GUI, no account/login — and is driven entirely by **Python**
> through the `bpy` API. This is where the pack's 3D work lives: 3D text and
> objects, camera tracking / matchmoving, geometry nodes, simulations, particles,
> rigging, compositing, and rendering to images, animation and video.
>
> Verified in-sandbox: **Blender 5.0.1 headless, Cycles CPU, rendered a frame**
> (cube + 3D extruded text + 35 mm camera + sun) → see `blender-headless-proof.png`.

---

## The idea

Instead of an agent clicking buttons (*"open this panel → drag this slider"*), it
**writes Blender Python** and executes it:

```
"Create a 35 mm camera, track this footage, reconstruct the camera motion, create
 a 3D text object, animate it from frame 1-120, add motion blur, composite it, and
 render frames 1-120."
```

That becomes a `bpy` script, run headless. The AI programs the whole 3D pipeline.

## What it does (all via `bpy`)

- **Model / edit 3D** — meshes, booleans, modifiers, sculpt.
- **Materials, textures, lighting** — Principled BSDF, procedural + image textures, HDRI, sun/area lights.
- **Cameras & animation** — camera rigs, keyframes, f-curves, motion blur, easing.
- **Camera tracking / matchmoving** — track footage, solve camera, reconstruct motion (`bpy.ops.clip.*`).
- **VFX, particles, simulations** — fluids, smoke, cloth, rigid body, particle systems.
- **Rigging & character animation** — armatures, weights, constraints.
- **Geometry Nodes / procedural generation** — node graphs for procedural geometry.
- **Compositing** — the compositor node tree, render passes.
- **Render** — stills and animation, multiple engines and passes.
- **Video via FFmpeg** — Blender bundles FFmpeg; encode image sequences to MP4/WebM.
- **Edit `.blend` files** — open, modify and save `.blend` scenes.
- **The whole Blender API** — anything the UI can do, Python can do.

## How to run it

```bash
blender --background --python script.py          # headless, run a script
blender -b file.blend --python script.py         # open a .blend, then run
blender -b --python-expr "import bpy; print(bpy.app.version_string)"
blender -b --render-output /out/ --render-frame 1   # render a frame
```

Or, as a Python module, `import bpy` inside a normal Python process (same
behaviour as `--background`, with a few caveats — no command-line args, default
startup scene).

## Installing it (verified recipes)

Blender is **free, no account/login**. Two routes:

**Route A — the portable build (most robust).** Download the official Linux
tarball (it **bundles its own Python**, so the system Python never matters),
extract, and run `./blender`. This works on any Linux box and on the remote
Colab/Kaggle workspace. *(If the host blocks blender.org, use Route B.)*

**Route B — the `bpy` Python module (verified in-sandbox).** `pip install bpy`,
but **each wheel is pinned to one exact Python version**:

| Blender / bpy | Python |
|---|---|
| 4.x (LTS) | **3.11** |
| 5.1 + | **3.13** |
| *(none)* | 3.12 |

So if your Python does not match, get one that does — e.g. with `uv`:

```bash
pip install uv
uv python install 3.11
uv venv --python 3.11 bpyenv
uv pip install --python bpyenv/bin/python bpy
bpyenv/bin/python my_blender_script.py
```

(Archived bpy wheels live at `download.blender.org/pypi/bpy/`.)

## Headless gotchas (learned the hard way — obey these)

1. **EEVEE needs a GPU / EGL context and FAILS headless** on a box with no
   display or GPU (`EGL_NOT_INITIALIZED`). **Use Cycles.**
2. **Cycles on CPU renders headless with no GPU** — set `cycles.device='CPU'`.
3. **The denoiser (OpenImageDenoise) can OOM** on a constrained box — set
   `cycles.use_denoising = False`.
4. **Where to run it:** on the **remote workspace** (Colab / Kaggle GPU) for heavy
   work — there you get Cycles **GPU** and EEVEE. Locally, use Cycles CPU for
   light scripts. Route every heavy Blender job to the workspace
   (`REMOTE-WORKSPACE.md`).

Minimal headless recipe that works:

```python
import bpy
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = 'CYCLES'
sc.cycles.device = 'CPU'
sc.cycles.samples = 16
sc.cycles.use_denoising = False          # avoids the OOM above
sc.render.resolution_x, sc.render.resolution_y = 1920, 1080
sc.render.filepath = "/out/frame.png"
bpy.ops.render.render(write_still=True)
```

## Where Blender fits in the pack

- **3D & motion graphics** — 3D text, product objects, procedural geometry, camera moves.
- **Camera tracking / matchmoving** — for the advanced feature catalogue's "3D camera tracking".
- **The advanced-feature code kits** — a Blender script is the heavy sibling of a web kit.
- **VFX / compositing** — simulations, particles, render passes.
- **Render + encode** — Blender renders; FFmpeg (bundled or the workspace's) encodes.

It is the pack's **graphics engine**; the remote workspace is its **execution
environment**; `bpy` is how the AI commands both.
