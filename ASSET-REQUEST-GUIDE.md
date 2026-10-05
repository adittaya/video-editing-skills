# The build order — SOURCE, CONCEPT, then PROMPTS

Three mandatory steps, in this order. Never jump to prompts before the first two.

---

## STEP 0 — SOURCE (get it, then analyse it)

Obtain at least ONE of: **the video clip** · **the voiceover / audio** · **the
transcript / script**. If the build is genuinely from-scratch graphics, say so
and record it.

Then analyse comprehensively and save **`SOURCE-ANALYSIS.json`**:
- **clip -> video analytics:** `ffprobe` (codec, size, fps, duration, channels);
  scene detection for cut times and ASL; loudness (LUFS + true peak); palette
  sampled from frames (hex); BPM if music.
- **audio -> word-level transcription:** faster-whisper `word_timestamps=True`
  -> `{word, start, end}` per word + segments. Drives the visual-narration plan,
  captions and word sync.
- **text ->** the sentence list mapped to the Sentence Law table.

## STEP 1 — CONCEPT.md (write the plan before any prompt)

With the source analysed, write **CONCEPT.md** — the single plan the whole build
follows. **Everything is connected: every line here drives a later stage, and
every later stage writes its result back here.** Follow `THINKING-SYSTEM.md` — the
planning stack, the four lenses (EZRA), and (when you have only a script) the
only-a-script path.

- **Premise** — the video in one sentence + its emotional arc.
- **THINKING PASS (mandatory).** Work the stack **top-down** — goal -> audience ->
  angle -> concept -> script -> beats -> shots — and record:
  - the target **emotion** per section (EZRA: Emotion, Story, Rhythm, Action);
  - the **beat map** with the **two-column (said | shown)** filled for every row;
  - the **visual plan** table: beat -> viewer question -> visual evidence ->
    risk to review -> final asset;
  - the **retention check** — where the video is most likely to lose people, and
    the fix.
- **Style** — the named build style (this skill) and how it applies here.
- **STYLE PASS (mandatory).** Pick deliberately and record: the **motion style**
  and the **UI style** from `MOTION-UI-STYLE-LIBRARY.md`, and the **caption
  style** from `CAPTION-STYLES.md`. One primary + at most one garnish; name the
  chosen style's failure mode.
- **Segment plan** — the beat map with timings, taken from the analysis.
- **Sentence table** — one row per narration sentence: sentence -> visual concept
  -> lane (A speaker / B visual) -> the **stressed word** to land on -> timing ->
  element bindings -> **camera** (reason + target + zoom). (The Sentence Law.)
- **Camera-track plan** — the ordered camera entries
  (READ / EMPHASIZE / REVEAL / FOLLOW / BREATHE) with their word bindings.
  (The Camera Law.)
- **FEATURE MAP — the Feature Pass (mandatory).** Walk the **full catalogue** in
  `ADVANCED-FEATURE-USE-CASES.md` — camera & framing, motion & animation, speed &
  time, transitions, text, colour, compositing & VFX, audio, AI, stills & design,
  workflow — and record for **every** feature whether it applies and how:
  `feature -> applies? -> where (scene/timecode/sentence) -> how (implementation)
  -> why (the job it does)`. **Every group is visited; no group is skipped.** The
  concept is not finished until every applicable advanced feature has a row (a
  "yes" with no *how* is not a plan; every "no" is a deliberate choice).
- **Contact-sheet plan** — which sign-off variants will be built (V1 Classic Grid
  / V2 Storyboard Filmstrip / V3 Pro QC Sheet) and why. **The variant the user
  picks is written back here.**
- **Sync map** — the word-level timings that drive text and visuals.
- **Asset manifest** — what the build needs (fed by the feature map); this feeds
  STEP 2.

Then STEP 2 writes `ASSETS-PROMPT.md` from this plan.

### PIPELINE CONNECTIVITY LAW (mandatory)
Everything is connected — no stage is decided in isolation, and no stage is
skipped:

- **SOURCE** -> analysed into `SOURCE-ANALYSIS.json`, which feeds the concept.
- **CONCEPT** -> drives the thinking pass, the style pass, the asset manifest, the
  camera track, the sentence table and the feature map; it is the single source of
  truth for the build.
- **ASSETS-PROMPT** -> written from the concept's manifest; nothing unplanned
  appears in the build.
- **BUILD** -> follows the concept's sentence table, camera track and feature map
  exactly.
- **RENDER GATE** -> the contact-sheet variants visualise the concept's beat map;
  the variant the user picks is written **back into CONCEPT.md**.
- **QA GATE** -> `edit-qa-validator` / `tools/qa_check.py` re-check that every
  feature the map marked "yes" actually made it into the edit.
- **SIGN-OFF -> RENDER** -> the full render happens only after the variant AND
  the cut are finalised.
- **A new contact sheet means a new CONCEPT revision.** If the sheet reveals a
  change, the concept is updated FIRST, then the build follows. The record stays
  connected end to end: source -> concept -> assets -> build -> sheet -> sign-off
  -> render.

## STEP 2 — ASSETS-PROMPT.md (the prompts, written from the concept)

Only now produce **`ASSETS-PROMPT.md`** — the prompt list, derived from the
concept's asset manifest.

---

# THE CAPTION & TEXT SYSTEM (mandatory)

The Text Law: on-screen text maps the visual; a plain SRT is an optional sidecar,
never the on-screen text. Every build declares one caption style and holds it,
and uses up to three caption modes:

1. **Styled text captions** — designed, on-brand, animated (style sheet: font,
   weight, size, tracking, leading, case, fill, stroke/box, accent, entrance/
   exit; timed to the word; <=2 lines; <=17 chars/s).
2. **Transparent-background captions (alpha)** — no background: transparent PNGs
   or an alpha clip (WebM VP9 alpha / ProRes 4444) for outline text, sticker/
   karaoke text, cut-out words and text-behind-subject. Clean premultiplied edge.
3. **Chroma key** — text or a subject shot on flat green (#00B140)/blue, keyed
   with despill, a 1-2 px matte choke, a light wrap and a garbage matte.

**Where to ask for them in ASSETS-PROMPT.md:** transparent caption PNGs / alpha
clips under **transparent images (category 2)**; the caption font/style and any
animated caption engine under **code components (category 6)**.

**Surprise pack:** kinetic typography · word-pop/karaoke captions · animated
underline/highlight/circle · text-behind-subject · alpha overlays.

# THE MANDATORY FEATURE USE-CASES (modern standard + advanced toolset)
See `ADVANCED-FEATURE-USE-CASES.md` for the full professional toolset (multi-track,
colour/scopes/HDR, chroma key, motion tracking, rotoscoping, multicam, speed
ramping, stabilisation, 3D tracking, audio mixing, AI features, stills craft) and
the Camera Law.

Before the render gate, confirm the build used the required techniques where the
concept needs them: anchor zoom in/out, motion tracing, keyframing, bezier
easing, word-pop, count-ups, readability zoom, micro-interactions, screen
transitions, cursor physics, cut-on-beat, a sound for every cut, correct-then-
grade — plus speed ramps, motion blur, parallax, mask reveals, freeze frames,
callouts, PiP and loops. Each skill lists the set with its per-style emphasis.

# BEFORE THE RENDER - the contact-sheet variants (mandatory)

## RENDER GATE — the contact sheet (mandatory before the full render)

**Never render the full video without sign-off.** Before the final render,
extract one frame per second and build a **contact sheet** for approval:

`ffmpeg -i build.mp4 -vf fps=1 sheet/f%04d.jpg`

Then **offer the user a choice of contact-sheet variants** — build 2-3 and let
them pick. The sheet is the cheapest place to catch pacing, composition,
safe-zone and continuity problems; a variant lets the reviewer read the edit the
way that suits them.

### The contact-sheet variants (build at least TWO; label them V1 / V2 / V3)
- **V1 — Classic Grid.** A uniform grid of 1 FPS frames in time order (left to
  right, top to bottom), each frame labelled with its **timestamp**. The baseline
  read of the whole edit at a glance.
- **V2 — Storyboard Filmstrip.** Larger frames laid in horizontal rows over a
  **time ruler**, with **scene-cut ticks** marked on the ruler and a one-line
  **caption** under each frame (what happens in that second). Reads like a
  storyboard; best for reviewing pacing, flow and the beat map.
- **V3 — Pro QC Sheet.** A dense technical sheet: each thumbnail carries its
  **timecode**, a **scene-cut flag**, a **motion/velocity indicator**, and a
  **safe-zone overlay**; a **colour-swatch strip** (the sampled palette) and a
  **summary header** run across the top (duration, shot count, ASL, loudness
  LUFS + true-peak, palette). Best for technical sign-off and continuity.

Build them at whatever aspect suits the cut (grid for a horizontal piece, a
vertical column for 9:16). Keep the Apple Standard chrome and the brand accent.

### The ask (mandatory)
Present the variants and ask the user directly:

> "Here are the contact-sheet variants — V1, V2, V3. **Did you like any of
> these, or shall I generate more variants so you can choose?**"

Then wait. If they want more, generate additional variants. **Render the full
video only after they finalise** — both the variant they prefer and the cut.

# WHICH LANE IS THE A-ROLL? (function, not source)

A-roll = whatever carries the meaning; B-roll = whatever supports it. In a
talking-head piece the speaker is the A-roll. In a graphics-led piece the motion
graphics ARE the A-roll and the footage becomes B-roll — the hybrid inversion.

---

# ASSETS-PROMPT.md IS ITSELF A PROMPT

The file is not a spec sheet for a human to read — **it is a prompt you hand
directly to an AI agent.** The agent has image generation, audio generation and
coding; it executes every item and **returns ONE zip file**.

So write it as a self-contained instruction:
1. **Open with the role and the task** — "You are an AI agent with image
   generation, audio generation and coding. Produce every asset below and return
   ONE zip file." State that voiceover and video clips are excluded.
2. **Give the deliverable tree — ONE master zip containing MULTIPLE zips
   inside.** The outer zip holds `MANIFEST.md` plus **a zip per category**
   (`images.zip`, `transparent.zip`, `logos.zip`, `music.zip`, `sfx.zip`) and
   **`components.zip`**, which itself contains **one zip per component kit**.
   No loose asset files — the manifest is the only loose file.
3. **Number every asset with its own brief** and its output path.
4. **Close with acceptance checks** — everything present, every value used
   exactly, no text in images, every component a kit folder, no voice/clips.

A real, complete example of the file is `EXAMPLE-ASSETS-PROMPT.md`.

---

# Who the prompts are addressed to

**Write every prompt as an instruction to an AI agent that has THREE
capabilities: image generation, audio generation, and coding.** Address it
directly, as a brief that agent can execute and return as files. Do not write
"vague asset descriptions" — write executable briefs.

That means six categories:

### 1. Images — an image-generation brief each
Backgrounds, plates, hero objects, textures, backdrops, charts. Give: subject ·
composition · style · palette (hex) · lighting · aspect + background · negatives.
One prompt per asset.

### 2. Transparent images (PNG / alpha) — an image-generation brief each
Cut-outs, icons, overlays, badges. The brief MUST end with
"transparent background, PNG with alpha, no background".

### 3. Logos — a brief or a note
Every mark needed (client logo, partner, badge). If the client supplies it, say
so; otherwise give a description/brief.

### 4. Music — an audio-generation brief each
Mood · genre · BPM · length · instrumentation · energy arc. Written as a brief a
music model can execute (e.g. "calm modern electronic bed, 95 BPM, 31 s, soft
synth pad + light piano, steady with a gentle lift at 20 s").

### 5. Sound effects — an audio-generation brief each
Type (whoosh / impact / tick / riser / pop) · character · duration. One per cut
or graphic land.

### 6. Code components — a CODING brief each  ← the one people forget
The agent can **write code**. Ask it to build the graphics that code does better
than an image model: glass cards, animated type, diagrams, count-ups, UI mockups,
particles, shaders, 3D scenes. A coding brief gives: the component, its
structure, the exact values, the motion, and the deliverable format.

**The kit deliverable (this is the shape to ask for).** One coding brief should
produce a **self-contained kit folder**, exactly like this:
```
<component-name>/
  index.html        <- the component, semantic, commented
  styles.css        <- all values as CSS custom properties (easy to recolor)
  README.md         <- what each file is + how to customize
  assets/
    <generated>.png <- the image assets the code references
```
Ask for it zipped, with a README, and with the palette exposed as variables so it
can be recolored without editing the code.

**Advanced-feature kits to request (pick what the concept needs).** Beyond the
graphics, ask the coding agent for the *tooling* the build uses, each as its own
kit:
- **camera-track** — one master camera wrapper with a per-frame resolver
  (anchor zoom, follow/safe-zone spring, velocity->motion-blur), driven by a
  keyframe array (READ / EMPHASIZE / REVEAL / FOLLOW / BREATHE).
- **motion-track** — a point/planar tracker that binds a DOM element to a moving
  target, with a lowpass on the track.
- **chroma-key** — a canvas/WebGL green-screen keyer with spill suppression and a
  matte choke control.
- **mask-rotoscope** — an SVG/canvas mask tool for frame-by-frame isolation and
  reveals.
- **grade-stack** — a CSS/WebGL colour pipeline (exposure, white balance,
  contrast, LUT, split-tone) with a scope readout (waveform/vectorscope).
- **speed-ramp** — a time-remap curve editor (keyframed speed with easing).
- **audio-mix** — a multi-track mixer stub (dialogue/music/SFX buses, ducking,
  EQ, noise-reduction placeholder).
- **subtitle-sync** — a word-level caption engine fed by the transcription JSON.
- **reframe** — an auto-reframe helper that keeps a subject inside 9:16/1:1/4:5
  safe zones.
Each kit uses the same folder shape (`index.html`, `styles.css`, `README.md`,
`assets/`) and exposes its values as CSS/JS variables.


---

## The file format (copy this)

```markdown
# ASSETS-PROMPT.md — <project>

**Addressed to:** an AI agent with image generation, audio generation and coding.
**Voiceover & video clips:** supplied separately by the user — NOT listed here. The agent generates **images, audio and code only** — it cannot generate video. The user provides the A-roll (voice / primary footage / transcription JSON) at the start; any **B-roll clip** the build needs is requested **separately**, never in this file.

## 1. Images (N)
| # | Used for | Size / aspect | BRIEF |
|---|---|---|---|

## 2. Transparent images (PNG/alpha) (N)
| # | Used for | Size | BRIEF (must say transparent/alpha) |
|---|---|---|---|

## 3. Logos (N)
| # | Mark | Supplied? | Brief / description |
|---|---|---|---|

## 4. Music (N)
| # | Used for | Mood / genre | BPM | Length | Instrumentation | BRIEF |
|---|---|---|---|---|---|---|

## 5. Sound effects (N)
| # | Used for (which cut/land) | Type | Character | Length | BRIEF |
|---|---|---|---|---|---|

## 6. Code components (N)  <- ask for a kit folder + README each
| # | Component | Built from | Deliverable | BRIEF |
|---|---|---|---|---|
| 1 | <e.g. glass hero card> | HTML/CSS | kit zip: index.html, styles.css, README.md, assets/ | "Build a ... with ... values ... motion ... expose palette as CSS variables ..." |

## Not needed
- <what you decided you don't need, and why>
```

---

## Prompt rules
- **Executable, one per item.** Every asset gets its own complete brief.
- **Address the agent directly** — "Generate…", "Build…", "Produce…".
- **Never write text inside an image brief** — generated type is garbled; type is
  rendered in the edit.
- **Code briefs must specify exact values** (colours in hex, radii in px, blur in
  px, easing curves, durations) and **expose the palette as variables**.
- **Ask for the kit shape** — folder + README + assets, zipped.
- **Transparent means transparent.**
- **Nothing that the user supplies** appears in this file — no voiceover, no
  A-roll footage, no B-roll clips. **B-roll is always requested separately.**
- **The look is Apple Standard** unless a preset overrides it — so briefs
  describe Apple-clean plates (soft gradients, `#f5f5f7`/`#ffffff`, one accent)
  unless a preset says otherwise.

---

## Worked example — a 30 s Apple-style product launch

```markdown
# ASSETS-PROMPT.md — <Product> launch

## 1. Images (2)
| # | Used for | Size | BRIEF |
|---|---|---|---|
| 1 | hero background | 1920x1080 | "Generate an ultra-soft gradient, near-white #F5F5F7 into pale blue, blurred organic shapes, minimal, no text, 16:9" |
| 2 | finale glow | 1920x1080 | "Generate a radial blue glow on near-black #0D0D0F, soft bloom, subtle grain, no text, 16:9" |

## 2. Transparent images (2)
| # | Used for | Size | BRIEF |
|---|---|---|---|
| 1 | feature icon | 512x512 | "Generate a rounded-square icon, blue gradient #41A6FF to #0A64E8, matte, soft light, transparent background, PNG with alpha, no text" |
| 2 | device cut-out | 1200x900 | "Generate a smartphone, three-quarter view, clean edges, transparent background, PNG with alpha, no text, no logo" |

## 3. Logos (1)
| # | Mark | Supplied? | Brief |
|---|---|---|---|
| 1 | product wordmark | client supplies SVG | — |

## 4. Music (1)
| # | Used for | Mood / genre | BPM | Length | Instrumentation | BRIEF |
|---|---|---|---|---|---|---|
| 1 | full film | calm premium electronic | 100 | 35 s | synth pad, light piano, subtle pulse | "Generate a calm premium tech bed, 100 BPM, 35 s, soft pads + light piano, steady with a gentle lift at 25 s" |

## 5. Sound effects (3)
| # | Used for | Type | Character | Length | BRIEF |
|---|---|---|---|---|---|
| 1 | scene land | whoosh | airy, smooth | 0.6 s | "Generate an airy whoosh, smooth, 0.6 s" |
| 2 | stat count-up | tick | soft, precise | 0.1 s | "Generate a soft UI tick, single, 0.1 s" |
| 3 | finale | impact | low, cinematic | 1.4 s | "Generate a low cinematic impact, deep, 1.4 s" |

## 6. Code components (2)
| # | Component | Built from | Deliverable | BRIEF |
|---|---|---|---|---|
| 1 | glass stat card | HTML/CSS | kit zip: index.html, styles.css, README.md, assets/ | "Build a frosted-glass stat card: radius 28px, fill rgba(255,255,255,.15), 1px stroke rgba(255,255,255,.62), backdrop-filter blur(22px) saturate(125%), one accent #0071e3 on the number. Expose --glass-fill, --glass-stroke, --glass-radius as CSS variables. Entrance: rise 24px + fade over 0.5s, cubic-bezier(0.16,1,0.3,1). Deliver a kit folder (index.html, styles.css, README.md, assets/) as a zip." |
| 2 | count-up number | JS | kit zip | "Build a count-up that animates 0 -> <value> over 1.2s, eased, triggered by a data attribute; return index.html + styles.css + README.md." |

## Not needed
- No live-action plates — this build is graphics-only.
```
