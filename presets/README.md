# presets/ — captured editing styles, organised by category

A **preset** is a named, portable style recipe captured from a reference video:
palette, type behaviour, motion grammar, transitions, pacing and structure —
written as its own full skill so it can be reproduced on demand.

## How this folder is organised

Presets live in **category subfolders** (so the folder stays readable as the
library grows). Each preset is a full skill; `preset-authoring/` is the tool that
makes them.

```
presets/
  README.md            <- this file
  INDEX.md             <- the flat list of every preset ("ask for this when…")
  preset-authoring/    <- the skill that captures a reference into a preset
  portfolio/           <- portfolio / personal reels
  short-form/          <- vertical short-form talking-head reels
  product/             <- product, SaaS and UI demos
  esport/              <- esports / gaming hype
  podcast/             <- podcast-framing talking-head explainers
  creator/             <- creator / coach "infotainment" talking-head
```

| Category folder | Presets | Parent skill |
|---|---|---|
| `portfolio/` | 001 Blue Glass | `agency-showreel` |
| `short-form/` | 002 Realtor Word-Caption | `short-form-retention` |
| `product/` | 003 SaaSWave Tactile Purple · 005 Higgsfield Dark-UI | `saas-demo-explainer` |
| `esport/` | 004 Cloudy eSport Neon | `esports-gaming-hype` |
| `podcast/` | 006 Podcast-Overlay Explainer | `podcast-talking-head` |
| `creator/` | 007 Creator Kinetic-Text | `personal-brand-creator` |

## A preset is a full skill

A preset is **not** a thinner, separate document. It is the same skill as every
other in this pack — same sections, same depth, same laws — with the look, motion
and pacing pre-decided from the captured reference. If a preset is only a few
kilobytes, it is incomplete.

## The workflow

1. Send the reference — a **video file**, a **frame-level contact-sheet PDF**, or a
   link.
2. Follow `preset-authoring/SKILL.md` — it captures the palette (sampled hex),
   type system, motion grammar, transitions, pacing and beat map at 2 FPS.
3. It writes `presets/<category>/preset-NNN-<name>/SKILL.md`.
4. To build: open that preset and follow its build recipe.

## The rules every preset obeys

- It records **methods, never content** — never the source's name, logo, copy, or
  exact marks.
- It states its palette as **measured hex**, and keeps the pack's type, motion,
  readability and word-sync laws unless the reference genuinely differs.
- It is honest about what was measurable: sampled colour is measured; motion and
  audio are measured where possible and inferred otherwise.

## PRESET -> SKILL LINKAGE LAW (mandatory)

A preset is not a dead end. Capturing a reference also **patches the parent
skill** it belongs to, so the AI that triggers the *skill* by name inherits the
real-world learnings. Every preset names its parent skill; every parent skill
carries a **"Reference-learned patterns"** section drawn from its preset(s). See
`preset-authoring/SKILL.md`.
