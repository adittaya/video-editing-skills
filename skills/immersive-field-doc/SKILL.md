---
name: immersive-field-doc
description: "Immersive first-person field documentary: embedded reporting, handheld/gimbal on-the-move, reporter as protagonist, hidden camera, subtitled foreign dialogue. Use for field reporting, conflict/access documentaries and immersive reportage."
---

# Immersive Field Documentary (Vice style)

**Scope.** Immersive, first-person field documentaries and reportage: embedded journalism, access-led stories, conflict and subculture films.

**Asset tier: 2 — MANDATORY: field footage with the reporter present; access and consent.**

> **THE LOOK.** The graphic chrome (cards, captions, lower-thirds, colour tags)
> defaults to the **Apple Standard** in the look section. This skill's named
> style governs the **footage treatment, structure and signature techniques**;
> where the style's own palette or typography is essential, that named style is
> the sanctioned override — chosen by the user picking this skill.


## STEP 0 — SOURCE GATE (mandatory, BEFORE the assets prompt)

**You cannot plan assets without the material.** Before writing
`ASSETS-PROMPT.md`, obtain at least ONE of:

1. **the video clip** — the footage to edit, or
2. **the voiceover / audio** — the narration track, or
3. **the transcript / script** — the words.

Ask for it up front. If the build is genuinely from-scratch graphics (no source
exists), say so and record it — the concept you write becomes the script.

**Then analyse the source and save the evidence** as `SOURCE-ANALYSIS.json`:

- **If a clip -> video analytics:** `ffprobe` (codec, size, fps, duration, audio
  channels); scene detection for cut times and ASL
  (`ffmpeg -i in.mp4 -filter:v "select='gt(scene,0.3)',showinfo" -f null -`);
  loudness (integrated LUFS + true peak); palette sample (quantise frames ->
  hex); beat/BPM if there is music.
- **If audio -> word-level transcription:** faster-whisper with
  `word_timestamps=True` -> a JSON of `{word, start, end}` per word, plus
  segments. This drives the Visual Narration Plan, the captions and the word
  sync. Recipe: decode to 16 kHz mono WAV with ffmpeg, pass a numpy array, run
  with `MKL_THREADING_LAYER=GNU OMP_NUM_THREADS=1` and `cpu_threads=1`, model
  `tiny` (base/small for accuracy).
- **If text only ->** the sentence list, mapped to the Sentence Law table.

**Only once the source is in hand and analysed** do you write
`ASSETS-PROMPT.md` — so every prompt reflects what the build actually needs.

## STEP 1 — CONCEPT.md (write the plan before any prompt)

With the source analysed, write **CONCEPT.md** — the single plan the whole build
follows. **Everything is connected: every line here drives a later stage, and
every later stage writes its result back here.**

- **Premise** — the video in one sentence + its emotional arc.
- **Style** — the named style (this skill) and how it applies here.
- **Segment plan** — the beat map with timings, taken from the analysis.
- **Sentence table** — one row per narration sentence: sentence -> visual concept
  -> lane (A speaker / B visual) -> the **stressed word** to land on -> timing ->
  element bindings -> **camera** (reason + target + zoom). (The Sentence Law.)
- **Camera-track plan** — the ordered camera entries
  (READ / EMPHASIZE / REVEAL / FOLLOW / BREATHE) with their word bindings.
  (The Camera Law.)
- **Contact-sheet plan** — which sign-off variants will be built (V1 Classic Grid
  / V2 Storyboard Filmstrip / V3 Pro QC Sheet) and why. **The variant the user
  picks is written back here.**
- **Sync map** — the word-level timings that drive text and visuals.
- **Asset manifest** — what the build needs; this feeds STEP 2.

Then STEP 2 writes `ASSETS-PROMPT.md` from this plan.

### PIPELINE CONNECTIVITY LAW (mandatory)
Everything is connected — no stage is decided in isolation, and no stage is
skipped:

- **SOURCE** -> analysed into `SOURCE-ANALYSIS.json`, which feeds the concept.
- **CONCEPT** -> drives the asset manifest, the camera track and the sentence
  table; it is the single source of truth for the build.
- **ASSETS-PROMPT** -> written from the concept's manifest; nothing unplanned
  appears in the build.
- **BUILD** -> follows the concept's sentence table and camera track exactly.
- **RENDER GATE** -> the contact-sheet variants visualise the concept's beat map;
  the variant the user picks is written **back into CONCEPT.md**.
- **SIGN-OFF -> RENDER** -> the full render happens only after the variant AND
  the cut are finalised.
- **A new contact sheet means a new CONCEPT revision.** If the sheet reveals a
  change, the concept is updated FIRST, then the build follows. The record stays
  connected end to end: source -> concept -> assets -> build -> sheet -> sign-off
  -> render.

## ASSETS-PROMPT.md — MANDATORY (strict rule)

After the concept, produce ONE file — **`ASSETS-PROMPT.md`** — listing every
asset the build needs, **one executable brief per item**, addressed to **an AI
agent that has image generation, audio generation AND coding**. No prompt list,
no build.

1. **Images** — image briefs: subject · composition · style · palette (hex) ·
   lighting · aspect + background · negatives.
2. **Transparent images (PNG/alpha)** — briefs ending "transparent background,
   PNG with alpha, no background".
3. **Logos** — a brief, or "client supplies".
4. **Music** — audio briefs: mood · genre · BPM · length · instrumentation.
5. **Sound effects** — audio briefs: type · character · duration.
6. **Code components** — CODING briefs for what code does best (cards, animated
   type, diagrams, maps, count-ups, timelines): exact values (hex, px, easing,
   durations), the motion, and the **nested-zip deliverable**: ONE master zip
   containing a zip per category and a zip per component kit (each kit unzips to
   `index.html`, `styles.css`, `README.md`, `assets/`, palette exposed as CSS
   variables).

**This file IS the prompt** — write it as a self-contained instruction you hand
straight to the agent, ending with the deliverable tree (one zip) and acceptance
checks. A full worked example: `EXAMPLE-ASSETS-PROMPT.md`.

**EXCLUDED — never in this file:** **voiceover** and **ALL video clips**
(A-roll and B-roll). The user supplies the A-roll — voice, primary footage, or a
transcription JSON — at the start. If the build needs any **B-roll clip**, ask
the user for it **separately**; clips are never listed in this prompt file.

Full format and a worked example: `ASSET-REQUEST-GUIDE.md`.


## THE STYLE — immersive field grammar

### The look
Handheld, subjective, **embedded**. The image is raw and immediate; polish is
suspicious. The reporter is on camera, in the frame, in the story.

### The grammar
**Access is the story.** The reporter is the protagonist; "we're here" is the
mode. Immediacy, danger and being-there are the value. The camera moves with the
reporter, so the audience travels with them.

### Signature techniques
- **On-the-move handheld / gimbal follow** — the camera walks and rides with the
  reporter; safe-zone follow keeps the subject readable.
- **To-camera pieces** — the reporter addresses the lens in the field; the
  low-light and imperfect framing are kept.
- **Hidden camera / covert** — used only where lawful and justified; label the
  technique in the edit.
- **Subtitled foreign dialogue** — subjects speak in their own language; the
  reporter's questions are kept.
- **J-cuts and ambient sound** — audio leads picture; the place is heard before
  it is seen.
- **Travel montage** — music under movement between locations to mark the
  journey.
- **Surveillance texture** — where the state is watching, let it show (following
  cars, checkpoints) — the surveillance becomes part of the story.

### Ethics
Informed consent where possible; protect sources (disguise voices/faces when
needed); never stage the "danger" — the access is real or it is not shown.

## WHICH LANE IS THE A-ROLL? (function, not source)

**A-roll = whatever carries the meaning. B-roll = whatever supports it.** The
lane is defined by FUNCTION, never by whether it came off a camera.

- In a **talking-head** piece the speaker is the A-roll; graphics and footage
  are B-roll.
- In a **graphics-led** piece — the motion graphics carrying the argument, the
  footage used as cutaways — **the motion graphics ARE the A-roll and the
  footage becomes B-roll.** This inversion is normal and correct.
- So when the visual narration carries the meaning, treat the graphics as the
  spine: plan them first, bind them to the words, and let the footage serve them.

- **The reporter's journey is the A-roll** — presence, movement and access carry the meaning; B-roll is the world around them.

## ADVANCED FEATURE USE-CASES (mandatory — the professional toolset)

**"Mandatory" means: if the concept needs it, you use it.** These are the
features that separate a professional edit from an amateur one. Reading
"mandatory" is the prompt to reach for the feature; using the feature is what
makes the video hold up. Full guide + terminal recipes:
`ADVANCED-FEATURE-USE-CASES.md`.

**Timeline & structure** — **multi-track timeline** (layer video/audio/effects,
never a flat single track) · **multi-camera editing** (sync angles, cut on
speaker/action) · **proxy editing** (cut proxies, re-render the same cut list on
the originals) · **batch export** (every ratio from one master) · project
collaboration.

**Motion & animation** — **keyframing** (position, scale, opacity, rotation,
blur on an eased curve) · **motion tracking** (bind text/effects to a moving
object; lowpass the track first) · **masking & rotoscoping** (frame-by-frame
isolation) · **speed ramping / time remapping** (speed curves across a beat) ·
**stabilisation** (2-pass warp) · **frame blending / optical flow** (smooth slow
motion).

**Colour** — **colour correction** (exposure, white balance, contrast FIRST) ·
**colour grading** (the look: LUT, film emulation, split-tone, SECOND) ·
**scopes** (waveform, vectorscope, histogram, RGB parade — grade by the numbers)
· **HDR grading** (only on request; tone-map to SDR for delivery).

**Compositing & effects** — **chroma key** (green/blue removal with spill
suppression and a clean edge) · **compositing / VFX** (combine layers into one
scene) · **3D camera tracking** (solve the move, place 3D in real footage) ·
**advanced transitions & effects** (blur, glow, glitch, light leaks, grain,
chromatic aberration — each timed to a cut or beat).

**Audio** — **noise reduction** (hiss, hum, room tone) · **EQ** (high-pass
dialogue, de-mud, carve space for music) · **audio syncing** (by waveform or
timecode) · **multi-track mixing** (dialogue/music/SFX; duck music 12–18 dB under
voice) · surround/spatial only where the delivery needs it.

**AI & smart** — **auto subtitles** (word-level timing drives captions AND the
narration plan) · **AI background removal** (matte without a green screen) ·
**auto reframing** (re-frame for 9:16 / 1:1 / 4:5 keeping the subject safe) ·
**scene detection & auto cutting** (cut list from scene changes) · **AI
colour/exposure correction** (first pass, then grade by hand).

**Assets & stills** (for every generated image/graphic) — layer-based editing,
layer masks, blending modes · frequency separation (skin retouch) · dodge & burn ·
content-aware fill / object removal · perspective correction · RAW processing ·
tone curves · HDR merge · panorama stitch · AI-assisted selection ·
non-destructive workflow · vector editing (bezier) · gradient mesh · typography
controls (kerning, tracking, leading) · symbol/asset libraries · artboards · grid
systems · multi-format export.

### The Camera Law (mandatory wherever there is a camera)
1. **One camera wrapper only** — all zooms/pans from a single master camera;
   never local ad-hoc transforms on nested elements.
2. **One camera move at a time** — never stack camera transforms.
3. **Every zoom has a reason** — READ / EMPHASIZE / REVEAL / FOLLOW / BREATHE.
   Constant zoom = no zoom.
4. **Do not cut while zoomed** — return to rest or hold the scene.
5. **Motion blur only during fast motion** — `blur = clamp(v*k, 0, max)`, zero at
   rest (start k ≈ 0.012, max ≈ 24 px). **Anchor zoom** sets the origin on the
   target; **follow** keeps the subject in a safe zone with a damped spring.

**The test:** walk the timeline. For each feature the concept needed, ask "is it
there, and is it doing a job?" A missing needed feature — a flat single track, an
ungraded image, a jittery tracked label — means the edit is not finished.

**For this skill:** stabilisation, colour grade, audio noise reduction, auto subtitling and motion tracking.

## MANDATORY FEATURE USE-CASES (the modern standard)

These are not optional extras. Each has a job; if the job is missing, the edit
reads as amateur. Apply what the concept needs — the items marked **★** apply to
almost every build.

**Camera & motion**
- **★ Zoom in (anchor zoom)** — bring a detail to readable size; origin on the
  target; return to rest before the next cut.
- **★ Zoom out (reveal)** — pull back for context after a detail; wide <-> detail
  rhythm is the pacing engine.
- **★ Motion tracing / follow camera** — the camera follows the cursor or the
  action (safe-zone follow, spring-damped); never leave motion under a static
  frame.
- **Slow push** — <=8% over 3-5s for tension.
- **Camera shake on impact** — a brief 2-4 frame shake on a hit.
- **Speed ramp** — slow->fast or fast->slow across a key beat.
- **Motion blur (velocity)** — blur only while fast; exactly 0 at rest.

**Keyframing & animation**
- **★ Keyframe everything** — position, scale, opacity, rotation, blur; nothing
  moves without keyframes and a curve.
- **★ Easing curves (bezier)** — every move eased, never linear; curve the PATH
  (bezier), not just the timing.
- **Mask / wipe reveal** — draw-on reveals, mask transitions, trim-path draws.
- **Parallax / 2.5D depth** — layers move at different rates (<=3-6% travel).
- **Freeze frame / hold** — stop on the moment that matters.

**Text & data**
- **★ Kinetic text / word-pop** — words appear on the beat; one accent keyword
  per line.
- **★ Count-up numbers** — every stat animates to its value on the spoken word.
- **Text tracked to an object** / **text behind the subject** — for hybrid pieces.
- **Callouts & arrows** — draw-on annotations pointing at the thing.

**UI & product (mandatory for ANY demo)**
- **★ Readability zoom** — any UI text the viewer must read renders >=4% of frame
  height (>=44px at 1080p).
- **★ Micro-interactions** — hover, press, ripple, toggle, focus; the UI answers
  the cursor.
- **★ Screen transitions** — push/pull navigation, modal rise + scrim, sheet slide.
- **★ Cursor physics** — bezier path, minimum-jerk timing, overshoot, click anatomy.
- **Comparison split / PiP** — two states side by side.
- **Screen replacement** — UI on a device.

**Edit & finish**
- **★ Cut-on-beat / cut-on-action** — cuts land on the beat or mid-movement.
- **★ A sound for every cut** — whoosh/impact/tick; silence before the biggest hit.
- **★ Correct then grade** — exposure and white balance first, then the look.
- **Seamless loop** — for social/web loops (end state = start state).

**The test:** open the finished timeline and ask, for each ★, "did this build use
it where the concept needed it?" If a needed ★ is missing, the edit is not
finished.


**For this skill:** **For this skill:** the camera is a participant — motion tracing (handheld/gimbal follow), J-cuts, cut-on-action, speed ramps on travel, ambient sound. No polish that would break the immediacy.

## Visual narration layer — full spec (mandatory wherever a person speaks)
The market-dominant format: the speaker carries the voice, the **visuals carry
the meaning**. Whoever is speaking — on camera, walking, or voiceover — the
video must SHOW what is being said.

### Three placements (choose per beat, alternate them)
1. **Full-screen cutaway** — visual takes the frame (icon, diagram, stat
   count-up, keyword card, B-roll). Voice continues (L-cut in, J-cut out).
2. **Front overlay** — motion graphics over the speaker; face stays visible.
3. **Behind / around the subject** — speaker keyed/cut-out over a graphic
   background; elements animate behind and beside.

### Rules
- Every spoken concept gets a visual landing on the exact word (±100 ms).
- One visual event every 6-10 s; no talking frame static > ~8 s.
- Alternate placements; avoid 3 of the same in a row.
- **Captions are additive, never the layer** — remove them and the ideas must
  still show.
- Motion: fade + rise + settle, eased, never linear (180-450 ms in, 250-350 ms out).

### The Visual Narration Plan (write BEFORE cutting)
| Timecode | Spoken phrase (word to land on) | Concept | Placement | Visual | Duration | Sound |


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

## Platform & delivery standards (self-contained reference)
Working standards (2026); re-verify before a paid campaign.

### 1. Vertical safe zones (1080×1920)
| Zone | Rule |
|---|---|
| **Universal action-safe** | keep faces/products/key action inside the centre ≈ **900×1330** |
| **Universal text-safe** | keep captions, prices, CTAs, legal text inside the centre ≈ **860×1100**, biased slightly above centre |
| **Shorts (measured)** | top ≈ 240px · bottom ≈ 380px · right ≈ 200px · left ≈ 60px |
| **TikTok / Reels** | bottom caption tray is deep; right button column ≈ 120–200px; Reels preview can crop top/bottom ≈ 285px |
Design for the most restrictive app (Instagram bottom UI); then it works everywhere.

### 2. Audio loudness (ITU-R BS.1770 integrated)
| Destination | Integrated | True peak ceiling |
|---|---|---|
| YouTube long-form, web | **−14 LUFS** | **−1 dBTP** |
| Social vertical, mobile | **−16 to −14 LUFS** | −1 dBTP |
| Broadcast TV | −23 LUFS (EBU R128) / −24 LKFS (ATSC A/85) | −1 to −2 dBTP |
| Streaming/VOD drama spec | −24 to −27 | −2 dBTP |
Use a true-peak-aware limiter. Dialogue ~6–10 dB above music; duck music 12–18 dB under voice.

### 3. Picture
- **Frame rate:** keep source rate (24 cinematic · 25 PAL · 30 web/social · 50/60 gaming/sports/screen). Never mix rates without conforming. 180° shutter.
- **Colour:** Rec.709 / sRGB delivery; tag colour metadata (`-colorspace bt709 -color_primaries bt709 -color_trc bt709`). HDR only on request.
- **Export (H.264):** `-c:v libx264 -preset slow -crf 16-18 -pix_fmt yuv420p -profile:v high -movflags +faststart`, AAC 48 kHz 192–320 kbps, CFR.

### 4. Captions & accessibility
- Always deliver a sidecar **SRT/VTT**. Burned captions: ≤2 lines, ≤ ~42 chars/line, high contrast, inside text-safe zone.
- Never rely on colour alone; contrast ≥ 4.5:1. No more than 3 flashes per second.

### 5. Delivery checklist (every skill)
Hook/first frame verified · loudness + true peak measured · safe zones checked · captions delivered · colour tags set · CFR confirmed · plays on a phone sound-off AND sound-on.

## QA
Every claim has a picture · interviews matched and clean · no filler · grade
consistent · music licensed · **no invented facts** (verify every number, quote
and attribution). Director's review: does it move someone who does not know the
subject?

## Hard limits
No fabricated quotes or statistics — verify against source. No voice generation.
No unlicensed music or footage. **Disclose every recreation, animation and
composite.** Where a style's ethics require a label (re-enactment, composite
animal, actors used), the label is mandatory.
