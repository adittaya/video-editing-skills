# THE BLENDER ENGINE — the pack's central 3D / graphics engine

> **Your AI does not need to *see* Blender. Your AI *programs* Blender.**
>
> Blender is the pack's **primary engine** — the most powerful single tool an AI
> can drive for editing and motion graphics. It runs **headless** (no desktop, no
> GUI, no account/login) and is commanded entirely by **Python** through `bpy`.
> This is where the pack's 3D work lives: 3D text and objects, motion graphics,
> camera tracking / matchmoving, geometry nodes, simulations, particles, rigging,
> compositing, and rendering to images, animation and video.

---

## 0 · THE ENVIRONMENT-ADAPTIVE LAW (read this first)

**Do not assume limits. Detect the machine, research the latest, then choose.**
The engine, the version and the supporting packages are **selected per
environment** — never hard-coded.

1. **Detect the environment** — CPU cores, RAM, GPU (and which: CUDA / OptiX /
   HIP / Metal / none), the OS, and the Python version.
2. **Research the latest** — the current stable Blender, the current best render
   engine for the hardware, and the current best supporting package for each job.
   Never default to an old build or a single all-rounder.
3. **Choose** the version + engine + packages that fit **this** machine — then use
   the full power it has. On a strong GPU box, render on the GPU; on a plain CPU
   box, render on CPU. Both are Blender; only the settings differ.

> A weak or headless box is **not** a limit of the skill — it is one environment
> the skill adapts to. A powerful GPU environment gets the full pipeline.

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

Or as a Python module — `import bpy` inside a normal Python process (same
behaviour as `--background`).

## Getting it (research the latest; pick the route that fits)

Blender is **free, no account/login**. Choose the install route per environment:

| Route | When | Note |
|---|---|---|
| **Portable build** | any Linux/Windows/macOS box, or the remote workspace | bundles its own Python — most robust, version-independent |
| **`bpy` Python module** | Python pipelines | `pip install bpy` — **pinned to one Python**: Blender 4.x → **3.11**, 5.1+ → **3.13**; match your Python (e.g. `uv python install 3.11`) |
| **Distro / container package** | a machine that ships it | fastest to install |
| **Archived wheels** | old versions | `download.blender.org/pypi/bpy/` |

**Always prefer the latest stable** unless the environment requires otherwise.

## Choosing the render engine (per environment)

Detect the GPU, then pick — this is an adaptation, not a limitation:

| Environment | Engine |
|---|---|
| GPU (NVIDIA / AMD / Apple) | **Cycles GPU** (OptiX / CUDA / HIP / Metal) — or **EEVEE Next** for speed |
| No GPU / headless server | **Cycles CPU** (EEVEE needs a GPU/GL context, so it is not available there) |

Detect first — query the available devices and print them before you commit:

```python
import bpy
prefs = bpy.context.preferences.addons['cycles'].preferences
prefs.get_devices()
for d in prefs.devices:
    print(d.type, d.name, "usable:", d.use)
```

## Performance & robustness (tune to the box, don't assume)

- **Use the power you have** — on a strong GPU box, enable GPU + high samples +
  denoising. On a modest box, lower samples and disable the denoiser.
- **Tune samples / tiles / resolution** to RAM and VRAM.
- **Watch memory** — the OpenImageDenoise pass can be heavy; if it OOMs, lower
  samples or disable denoising, then re-enable on a bigger box.
- **Render one test frame and view it** before rendering a sequence.

## The toolchain by use case (Blender first)

| Job | Primary | Supporting |
|---|---|---|
| **3D · motion graphics · VFX · tracking · geometry nodes · compositing · render** | **Blender** | GPU drivers (OptiX/CUDA/HIP/Metal) |
| Edit · assemble · encode · mux | — | **FFmpeg** (Blender bundles one) |
| Colour management | **Blender** (OpenColorIO built in) | — |
| Images / stills / plates | **Blender** render, or the workspace's image models | — |
| Matting / segmentation | the workspace (SAM 2.1 + BiRefNet) | `rembg` |
| Audio · music · SFX | the workspace's audio models | FFmpeg |
| Voice | the workspace (Qwen3-TTS) | — |
| Video generation | the workspace (LTX-2.5) | — |
| Python data / vision | — | numpy, Pillow, OpenCV |

Full detail: `TOOLCHAIN.md`. Rule for every row: **research the latest, pick per need.**

## Where Blender fits in the pack

- **3D & motion graphics** — 3D text, product objects, procedural geometry, camera moves.
- **Camera tracking / matchmoving** — for the advanced feature catalogue's "3D camera tracking".
- **The advanced-feature code kits** — a Blender script is the heavy sibling of a web kit.
- **VFX / compositing** — simulations, particles, render passes.
- **Render + encode** — Blender renders; FFmpeg (bundled or the workspace's) encodes.

**Blender is the engine. The remote workspace (`REMOTE-WORKSPACE.md`) is the
execution environment. `bpy` is how the AI commands both.**
