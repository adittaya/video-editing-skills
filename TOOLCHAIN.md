# THE TOOLCHAIN — Blender first, everything else by use case

> **Main focus: BLENDER (+ Remotion).** Blender is the pack's primary engine —
> 3D, motion graphics, VFX, camera tracking, Geometry Nodes, compositing, render
> and encode. **Remotion** is the 2D motion-graphics engine (React/CLI).
> Everything below **supports** them. For each row: **research the latest version,
> pick per need** (the `model-discovery` habit, applied to software).

---

## The rule

**Don't fix a version. Detect, research, choose.** For every tool: find the
current best for the job, verify it fits the hardware and the licence, keep one
fallback. Use the full power the environment has.

## The stack

### Core engines

**Blender** — the **3D engine**. Headless, scripted via `bpy`. 3D modelling,
materials/textures/lighting, cameras + animation, camera tracking / matchmoving,
VFX / particles / simulations, rigging, Geometry Nodes, compositing, render, and
video encode. → `BLENDER-ENGINE.md`, `skills/blender-engine`.

**Remotion** — the **2D motion-graphics engine**. React/CLI, headless. Kinetic
typography, captions, lower thirds, charts, maps, diagrams, UI animation, data
visualization, 2D motion graphics, titles, labels, transitions, overlays,
procedural graphics. → `skills/headless-documentary-motion-studio`.

Together they drive the **headless studio** — `skills/headless-documentary-motion-studio`
(a deterministic, shot-specified, render → inspect → revise loop).

### By use case

| Use case | Primary | Supporting packages | Notes |
|---|---|---|---|
| **3D / motion graphics / VFX / tracking / Geometry Nodes / compositing / render** | **Blender** | GPU drivers — OptiX / CUDA (NVIDIA), HIP (AMD), Metal (Apple) | the pack's main engine |
| **2D motion graphics · kinetic type · captions · charts · maps · overlays** | **Remotion** | Node + React | the 2D engine; headless CLI render |
| **Orchestration · shot generation · validation · render orchestration** | **Python** | — | the glue of the headless studio |
| **QC of rendered frames** | **vision analysis** | — | inspect before you accept |
| **Edit · assemble · trim · encode · mux** | — | **FFmpeg** | Blender bundles one; the workspace has one |
| **Colour management / grading** | **Blender** (OpenColorIO built in) | — | ACES / LUTs |
| **Stills, plates, backgrounds** | **Blender** render | or the workspace's image models | reference-conditioned |
| **Matting / segmentation / alpha** | the workspace — **SAM 2.1 + BiRefNet** | `rembg` (local fallback) | `a-roll-matting` |
| **3D asset generation** | **Blender** (model it) | the workspace — **Hunyuan3D 2.1** | |
| **Audio · music · SFX** | the workspace — **ACE-Step 1.5 / Stable Audio Open** | FFmpeg | |
| **Voice / TTS / cloning** | the workspace — **Qwen3-TTS** | — | never clone without consent |
| **Word-level timing** | the workspace — **Qwen3-ASR + ForcedAligner** | — | drives Sentence Law + captions |
| **Video generation / regeneration** | the workspace — **LTX-2.5** | — | never in ASSETS-PROMPT.md |
| **Python data / vision** | — | **numpy**, **Pillow**, **OpenCV** | glue and QC |

### Where each runs

- **Remote workspace** (`REMOTE-WORKSPACE.md`) — the execution environment; heavy
  work runs there (GPU). Blender installs there too.
- **Local machine** — the controller and the source of truth; light scripts only.
- **Blender** — the engine, wherever it runs.

## Choosing Blender's build (per environment)

| Route | When |
|---|---|
| Portable build (bundles Python) | any box, or the workspace — most robust |
| `bpy` module | Python pipelines (Python-pinned: 4.x → 3.11, 5.1+ → 3.13) |
| Distro / container package | a machine that ships it |
| Archived wheels | old versions (`download.blender.org/pypi/bpy/`) |

Prefer the **latest stable** unless the environment requires otherwise.

## Adding a tool

Ask three questions before you add anything:
1. **Does Blender already do it?** If yes, use Blender — fewer moving parts.
2. **What is the current best tool** for this exact job (not the most popular)?
3. **Does it fit** the hardware, the licence, and the workspace?

Then lock it in, keep one fallback, and record it.
