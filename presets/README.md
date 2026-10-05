# presets/ — captured editing styles

A **preset** is a named, portable style recipe captured from a reference video:
palette, type behaviour, motion grammar, transitions, pacing and structure —
written as its own skill file so it can be reproduced on demand.

## Why presets live here
There is **no mandatory style** in this pack — the look is chosen per job in the
Style Pass. A preset is simply a **captured style**: a reference video measured
and locked into a reusable recipe, so a client can ask for that exact look on
demand. Nothing here is an "override"; it is one of the available styles.

## What's in here
| File | What it is |
|---|---|
| `preset-authoring/SKILL.md` | The skill that turns a reference (contact-sheet PDF, video file, or link) into a preset. Read this first. |
| `preset-001-zayyan-blue-glass/SKILL.md` | The first captured preset — from the "Turning ideas into visuals" reel. |
| `preset-002-realtor-word-caption/SKILL.md` | A bright, high-key vertical talking-head reel with word-by-word bold captions and a two-colour keyword accent system (blue/cyan + orange/amber). |
| `preset-003-saaswave-tactile-purple/SKILL.md` | A bright, high-key 3D "digital workspace" product reel — photoreal objects in a purple/magenta wash, floating UI cards, a purple cursor, a morph-to-logo. |
| `preset-004-cloudy-esport-neon/SKILL.md` | A high-energy vertical eSports montage — blue-neon architecture, silhouettes, glow/bloom, glitch/whip transitions, 3D milestone numerals, a gold trophy. |
| `preset-005-higgsfield-dark-ui/SKILL.md` | A high-contrast dark-mode product demo — white UI floating in a black void, 2D→3D spatial UI transforms, a neon lime-green accent, a neon-blue command line. |

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
- It states its palette as **measured hex**, and keeps the pack's type,
  motion, readability and word-sync laws unless the reference genuinely differs.
- It is honest about what was measurable: sampled colour is measured; motion
  and audio are inferred from frames unless a video file is supplied.
