---
name: preset-authoring
description: "Turns a reference video (supplied as a frame-level contact-sheet PDF, a video file, or a link) into a reusable PRESET: a named, portable style recipe covering palette, type behaviour, motion grammar, transitions, pacing and structure, saved as a skill file under presets/. Use when the user supplies reference frames or a video and wants that exact editing style captured and reproduced."
---

# Preset Authoring — capture a reference's editing style

**Scope.** Given a reference (contact-sheet PDF, video file, or link), produce a
**preset**: a portable skill file that reproduces that style. One reference →
one `presets/preset-NNN-<name>/SKILL.md`.

**This is the one sanctioned override of the Apple Standard** — a preset is
explicitly requested by the user. Everywhere else, Apple Standard governs.

## STEP 0 — SOURCE GATE (mandatory)

Before anything, obtain at least one of: the **video clip**, the
**voiceover/audio**, or the **transcript/script** — then analyse it and save
`SOURCE-ANALYSIS.json` (video analytics, a word-level transcription JSON, or the
sentence list). Only then write `ASSETS-PROMPT.md` and the preset. A preset
cannot be authored from nothing.

## STEP 1 — CONCEPT.md

Write the concept before any prompt: premise, the captured style applied here,
the segment/beat plan, the scene table, the visual-narration plan, the sync map
and the asset manifest. STEP 2 (the prompt list) is written from it.

## STEP 2 — ASSETS-PROMPT.md (mandatory, from the concept)

The preset build produces the same mandatory prompt file as every skill:
**`ASSETS-PROMPT.md`**, one executable brief per asset, addressed to an AI agent
with **image generation, audio generation and coding**. Six categories:
**images · transparent images (PNG/alpha) · logos · music · sound effects ·
Code components** (glass cards, animated type, diagrams, UI mockups, shaders —
delivered as a kit folder: `index.html`, `styles.css`, `README.md`, `assets/`,
zipped). **This file IS the prompt** — write it as a self-contained instruction handed straight to the agent, ending with the deliverable tree (ONE master zip containing MULTIPLE zips inside) and acceptance checks. A worked example: `EXAMPLE-ASSETS-PROMPT.md`. **Voiceover and ALL video clips are excluded** — the user supplies A-roll (voice/footage/transcription) at the start, and any B-roll is requested **separately**, never listed in this prompt file. (The agent generates images, audio and code only — not video.)
Full format: `ASSET-REQUEST-GUIDE.md`.

## 1. Accept the input
| Input | What you can measure |
|---|---|
| **Contact-sheet PDF** (frames + timestamps) | palette (sampled), type, composition, beat map, pacing (approximate) |
| **Video file** | everything above + true cut times, ASL, motion, audio |
| **Link only** | script/structure from the transcript; no pixels — say so |

State plainly which of the three you got.

## 2. Extraction procedure (frame-level)
1. **Render** the PDF pages to images (one page = a grid of frames, in time
   order). Read each frame: what is on screen, any text verbatim, the layout.
2. **Build the beat map** — a table of `timecode -> beat -> what is on screen`.
   The timestamps on the sheet give the order; the frames give the content.
3. **Sample the palette programmatically** — quantise the frames and take the
   dominant colours as hex. Never eyeball a palette you can measure:
   `Image.open(p).quantize(colors=6).convert('RGB')` → most-common → hex.
   Record 5–6 colours: base, mid, light, ink, accent.
4. **Read the type system** — family (sans/serif/script), weight, the size
   hierarchy (which line is largest), tracking, case, and where text sits.
5. **Read the motion grammar** — how elements enter (rise/fade/scale/blur), the
   transition vocabulary (hard cut / dissolve / wipe / whip), and whether the
   camera moves. From frames only, mark these as *inferred*.
6. **Read the pacing** — how many beats per second, where it speeds up, where it
   breathes. From a video file, compute ASL; from frames, approximate.
7. **Name the signature devices** — the 3–6 moves that make it feel like itself.

## RENDER GATE — the 1 FPS contact sheet (mandatory before the full render)

Never render the full video without sign-off: `ffmpeg -i build.mp4 -vf fps=1
sheet/f%04d.jpg`, tile the frames into a contact sheet in time order (each
labelled with its timestamp), show it to the user, and wait. Render only after
they finalise.

## WHICH LANE IS THE A-ROLL? (function, not source)

A-roll = whatever carries the meaning; B-roll = whatever supports it. In a
graphics-led piece the motion graphics ARE the A-roll and the footage becomes
B-roll — the hybrid inversion.

## 2b. A preset is a FULL skill — same depth, locked to one style

A preset is **not a separate, thinner document**. It is the same skill as every
other in this pack — the same sections, the same depth, the same laws — with the
look, motion grammar and pacing **pre-decided from the captured reference**.

A complete preset carries ALL of these, at the same depth as the pack skills:
- frontmatter + scope + provenance (source, date, measured vs inferred)
- the mandatory **ASSETS-PROMPT.md** block with its five categories and prompts
- intake · structure & pacing (the captured beat map) · the captured palette
  (as an explicit override) · the edit · audio
- industry benchmarks · a worked example · common mistakes
- the **full Visual Narration Layer spec** · signature techniques
- the **modern editing toolkit** (technique catalogue, terminal toolchain,
  tested FFmpeg recipes, production loop, premium rules)
- the **platform & delivery standards** · QA · hard limits

If a preset is a few kilobytes, it is incomplete — rebuild it from a pack skill
as the base, replacing only the style-specific sections.

## 3. The preset file format (copy this)
```markdown
---
name: preset-<slug>
description: "<one line: what this style is and when to use it>"
---
# Preset <NNN> — <name>

**Source:** <what it was captured from, and how (PDF / video / link)>
**Captured:** <date>  ·  **Confidence:** <measured / inferred>

## The look (explicit override of the Apple Standard)
- Palette (sampled): base `<hex>` · mid `<hex>` · light `<hex>` · ink `<hex>` ·
  accent `<hex>`
- Type: <family, weights, hierarchy, tracking, case>
- Composition: <framing, placements, whitespace>

## Motion grammar
<entrances, transitions, camera, easing — marked measured/inferred>

## Pacing & structure
| Time | Beat | On screen |

## Signature devices
1. …

## Build recipe (how to reproduce it)
1. …

## Do-not-copy line
Methods only — never the source's name, logo, copy, or exact marks.
```

## 4. Apply a preset
Open the preset, read the build recipe, and build with it. Where the preset and
the Apple Standard disagree, **the preset wins for this job** (it was requested)
— but keep Apple's type ramp, motion laws, readability, sync and QA unless the
preset explicitly records a different value.

## 5. QA — does it match?
- Palette matches the sampled hexes (compare a probe frame to the reference).
- The beat map timings are reproduced (±10%).
- The signature devices are all present.
- The type hierarchy reads the same at phone size.
- Nothing clanky; every craft law still holds.

## 6. Limits

- **Assets still need prompts.** A preset build also produces the mandatory
  `ASSETS-PROMPT.md` (images, transparent images, logos, music, SFX — one prompt
  each; voice and footage excluded). See `ASSET-REQUEST-GUIDE.md`.
- **Methods, never content.** Never copy the source's name, logo, copy, or marks.
- **Honest confidence.** Sampled colour is measured; motion and audio are
  inferred from frames unless a video file was supplied — say which.
- **Assets still apply.** A preset changes the LOOK, not the asset tier — if the
  style needs footage or a cut-out subject, request it.
- Never reproduce a living person's likeness or a protected mark.
