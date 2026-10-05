# presets/ — captured editing styles

A **preset** is a named, portable style recipe captured from a reference video:
palette, type behaviour, motion grammar, transitions, pacing and structure —
written as its own skill file so it can be reproduced on demand.

## Why presets live here
The pack's rule is **Apple Standard only** — with ONE exception: a preset the
user explicitly asks for. This folder is that sanctioned override channel.
Everything else stays Apple.

## What's in here
| File | What it is |
|---|---|
| `preset-authoring/SKILL.md` | The skill that turns a reference (contact-sheet PDF, video file, or link) into a preset. Read this first. |
| `preset-001-zayyan-blue-glass/SKILL.md` | The first captured preset — from the "Turning ideas into visuals" reel. |
| `preset-002-.../` | Add one folder per captured style. |

## A preset is a full skill

A preset is **not** a thinner, separate document. It is the same skill as every
other in this pack — same sections, same depth, same laws — with the look,
motion and pacing pre-decided from the captured reference. If a preset is only a
few kilobytes, it is incomplete.

## The workflow
1. Send the reference — a **frame-level contact-sheet PDF**, a video file, or a link.
2. The authoring skill extracts the palette (sampled as hex), type system,
   motion grammar, transitions, pacing and beat map.
3. It writes `presets/preset-NNN-<name>/SKILL.md`.
4. To build: open that preset and follow its build recipe.

## The rule every preset obeys
- It records **methods, never content** — never the source's name, logo,
  copy, or exact marks.
- It states its palette as an **explicit override** of the Apple Standard
  (user-requested), and keeps Apple's type ramp and motion laws unless the
  reference genuinely differs.
- It is honest about what was measurable: sampled colour is measured; motion
  and audio are inferred from frames unless a video file is supplied.
