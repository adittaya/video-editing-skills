# THE GENERATIVE ENVIRONMENT — mandatory

> **MANDATORY. Load this before you plan, and use it for every heavy task.**
>
> **Repository:** https://github.com/adittaya/local-generative-colab-skill
> (raw: `https://raw.githubusercontent.com/adittaya/local-generative-colab-skill/main/SKILL.md`)
>
> This is the pack's **execution environment**. It turns your machine into the
> controller for a heavy generative-media pipeline that runs on a **remote Google
> Colab GPU (NVIDIA T4, ~16 GB)** — or Kaggle (2× T4, ~32 GB) — through the Colab
> CLI. It builds, runs, monitors, debugs, resumes, packages and returns the whole
> job. You do not explain it — you **use** it.

---

## Why it is mandatory

The skill pack tells you **what** to make. This environment is **how you make the
heavy parts fast**: it does the model inference the pack's asset pipeline needs —
image reconstruction, editable-asset extraction, 3D, audio, **voice**, and video
generation — on a real GPU, without you building models locally.

Load it at the same time as the pack's `LOAD FIRST` files. Then, at every stage
below, route the heavy work to it.

## What it gives the pack

| The pack needs | The environment provides |
|---|---|
| **Images** for `ASSETS-PROMPT.md` (backgrounds, plates, illustrations) | Visual reconstruction / image generation — a top-tier generative model conditioned on your source, not a plain upscaler. |
| **Transparent assets + matting** (the A-roll prep, cut-outs, alpha) | **Editable asset extraction** — **SAM 2.1 Large** for segmentation + **BiRefNet** for refinement → maximally editable transparent 2D assets. This is the strong path for `a-roll-matting`. |
| **3D elements** the concept calls for | **Hunyuan3D 2.1** — editable 3D asset generation. |
| **Music + SFX** for `ASSETS-PROMPT.md` (sound) | Audio reconstruction / generation — **ACE-Step 1.5**, **Stable Audio Open 1.5** (music, SFX, ambience). |
| **Voice** (the A-roll voiceover) | **Qwen3-TTS** — speech synthesis **and voice cloning**. |
| **Word-level timings** (drives the Sentence Law + captions) | **Qwen3-ASR + Qwen3-ForcedAligner** — word-level transcription and alignment. |
| **Motion / B-roll** when needed | **LTX-2.5** video generation & regeneration (T2V/I2V/A2V, retake, extend, inpaint/outpaint, upscale/restore, SDR→HDR). |

## How to load it

Point your agent at the repo and follow its `SKILL.md` + `INSTALL.md` (the
install prompt is a copy-paste block). The core instruction:

```
Install and run the "local-generative-colab-skill".
Repository: https://github.com/adittaya/local-generative-colab-skill
Read SKILL.md at the repository root, load the references/ files as each stage
needs them, and operate as the controller: ALL work runs on a remote Colab or
Kaggle GPU. Actually build / execute / monitor / debug / resume / package / return
the project. Do not explain — execute.
```

## The rules it carries (obey them)

- **Discover before you lock.** Never default to one all-rounder — research the
  best specialist model per task; keep one fallback.
- **Remote is scratch; local is the source of truth.** Pull outputs back to local
  immediately.
- **Pick the backend per task** — Kaggle for heavier/longer, Colab for iteration.
- **Never waste the GPU.** One task at a time; unload and stop when idle.
- **Controller only** — the local machine never runs the heavy work.
- **No manual steps for the user.**
- **Quality > Fidelity > Editability > Speed.**

## How it changes the pack's limits

- **Voice is no longer user-only.** The pack previously said "no TTS — the A-roll
  is user-supplied." With the environment, the A-roll **voice can be synthesised
  or cloned** (Qwen3-TTS). Still offer the user the choice; never clone a voice
  without consent.
- **Matting gets a strong path.** Prefer SAM 2.1 + BiRefNet here over the local
  `rembg` fallback in `tools/matte.py` when the environment is available.
- **Word-level sync is now measurable.** Qwen3-ASR + ForcedAligner gives the
  word timings the Sentence Law and the caption engine need.
- **Video/motion can be generated** where the concept calls for it — but the
  pack's rule stands: **video clips never go in `ASSETS-PROMPT.md`**; they are
  requested separately.

## Honesty

Disclose what was generated. Never synthesise a real person's voice or likeness
without consent. Label every reconstruction, generation and composite. The
environment's outputs are assets like any other — they pass the same QA gate.
