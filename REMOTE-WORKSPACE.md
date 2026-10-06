# THE REMOTE WORKSPACE — mandatory (your execution environment)

> **MANDATORY. Load this before you plan, and do ALL work here.**
>
> **Repository:** https://github.com/adittaya/local-generative-colab-skill
> (raw: `https://raw.githubusercontent.com/adittaya/local-generative-colab-skill/main/SKILL.md`)
>
> This is the pack's **workspace and execution environment**. It is **not only a
> generative environment** — it is a **full, powerful remote workspace** where you
> **analyse, edit, assemble, generate and run commands**, all on a **remote GPU**
> (Google Colab 1×T4 ~16 GB, or Kaggle 2×T4 ~32 GB) through the Colab / Kaggle
> CLI. It is fast because the machine is powerful. Your local machine is the
> **controller** and the **source of truth**; the workspace does the work.

---

## The three rules (memorise them)

1. **ALL WORK RUNS ON THE REMOTE MACHINE — mandatory.** Not just the heavy model
   inference. *Everything*, heavy and light: analysis, editing, assembling,
   downloading, packaging, file operations, running commands. The remote machine
   is faster at all of it. The local machine **never** runs the work itself.
2. **The local machine is the controller + the source of truth.** It only saves
   files, runs the controller scripts, and collects outputs. Your originals stay
   unchanged on local.
3. **Outputs are saved back to your machine.** Both remote filesystems are
   **ephemeral scratch** — pull every output and checkpoint back to the local
   home directory immediately. **Never leave the only copy of a result on a
   remote session.**

---

## Why it is mandatory

The skill pack tells you **what** to make. This workspace is **how you make it,
fast**: it gives you a powerful GPU machine and a full toolchain, remotely, so
you can **edit, assemble, analyse and command** at speed instead of grinding on a
weak local box — and it saves the results precisely on your own machine.

Load it at the same time as the pack's `LOAD FIRST` files. Then route **every**
task to it.

## What it gives the pack

| The pack needs | The workspace provides |
|---|---|
| **Images** for `ASSETS-PROMPT.md` (backgrounds, plates, illustrations) | Visual reconstruction / image generation — a top-tier model conditioned on your source, not a plain upscaler. |
| **Transparent assets + matting** (A-roll prep, cut-outs, alpha) | **Editable asset extraction** — **SAM 2.1 Large** + **BiRefNet** → maximally editable transparent 2D assets. The strong path for `a-roll-matting`. |
| **3D elements** | **Hunyuan3D 2.1** — editable 3D asset generation. |
| **Music + SFX** for the sound prompt | **ACE-Step 1.5**, **Stable Audio Open 1.5** (music, SFX, ambience). |
| **Voice** (the A-roll voiceover) | **Qwen3-TTS** — speech synthesis **and voice cloning**. |
| **Word-level timings** (Sentence Law + captions) | **Qwen3-ASR + Qwen3-ForcedAligner**. |
| **Motion / B-roll** | **LTX-2.5** video generation & regeneration. |
| **The edit itself** — analyse, cut, assemble, package | The full remote toolchain: everything runs there, heavy and light. |

## How to load it

Point your agent at the repo and follow its `SKILL.md` + `INSTALL.md` (a
copy-paste install prompt). The core instruction:

```
Install and run the "local-generative-colab-skill".
Repository: https://github.com/adittaya/local-generative-colab-skill
Read SKILL.md at the repository root, load the references/ files as each stage
needs them, and operate as the CONTROLLER: ALL work runs on a remote Colab or
Kaggle GPU — heavy AND light (inference, downloads, packaging, editing,
assembling, file operations). The local machine only saves files, runs the
controller scripts and collects outputs. Treat both remote filesystems as
ephemeral scratch; pull outputs and checkpoints back to local. Actually build /
execute / monitor / debug / resume / package / return the project. Do not
explain — execute.
```

## The rules it carries (obey them)

- **Discover before you lock** — research the best specialist model per task;
  keep one fallback. Never default to one all-rounder.
- **Remote is scratch; local is the source of truth.**
- **Pick the backend per task** — Kaggle for heavier/longer, Colab for iteration.
- **Never waste the GPU** — one task at a time; unload the model, free the GPU,
  stop the session when idle. No working time limit, but never trade quality for
  speed.
- **Controller only** — no local inference, packaging, editing or downloads.
- **No manual steps for the user** — never ask them to open a notebook,
  authenticate, upload, or paste code.
- **Verify the remote GPU** — `nvidia-smi`, CUDA, VRAM; if there is no GPU,
  report it and stop heavy inference (never silently fall back to local).
- **Quality > Fidelity > Editability > Speed.**

## How it changes the pack's limits

- **Voice is no longer user-only.** The A-roll **voice can be synthesised or
  cloned** (Qwen3-TTS). Still offer the user the choice; **never clone a voice
  without consent.**
- **Matting gets a strong path** — prefer SAM 2.1 + BiRefNet over the local
  `rembg` fallback in `tools/matte.py`.
- **Word-level sync is measurable** — Qwen3-ASR + ForcedAligner gives the word
  timings the Sentence Law and the caption engine need.
- **Video/motion can be generated** where the concept calls for it — but the
  pack's rule stands: **video clips never go in `ASSETS-PROMPT.md`**; they are
  requested separately.

## Honesty

Disclose what was generated. Never synthesise a real person's voice or likeness
without consent. Label every reconstruction, generation and composite. The
workspace's outputs are assets like any other — they pass the same QA gate.
