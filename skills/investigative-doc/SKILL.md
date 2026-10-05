---
name: investigative-doc
description: "Investigative documentary: evidence-led reconstruction, document and data on screen, bodycam and audio multicam, sober authoritative tone. Use for investigative journalism films, accountability pieces and evidence-driven reconstructions."
---

# Investigative Documentary (Frontline / ProPublica style)

**Scope.** Investigative journalism documentaries and evidence-driven reconstructions — accountability, public-interest and current-affairs films.

**Asset tier: 2 — MANDATORY: primary evidence (records, documents, footage, audio), interviews. Every fact verified.**

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

With the source analysed, write **CONCEPT.md** — the plan the whole build follows:
- **Premise** — the video in one sentence + its emotional arc.
- **Style** — the named style (this skill) and how it applies here.
- **Segment plan** — the beat map with timings, taken from the analysis.
- **Scene table** — sentence -> visual concept -> lane (A speaker / B visual) ->
  timing -> element bindings -> camera.
- **Visual narration plan** — every spoken concept and the visual that shows it.
- **Sync map** — the word-level timings that drive text and visuals.
- **Asset manifest** — what the build needs; this feeds STEP 2.

Then STEP 2 writes `ASSETS-PROMPT.md` from this plan.

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


## THE STYLE — investigative grammar

### The look
Sober, authoritative, **evidence-led**. Restrained motion. The tone is
"questions, explains and changes the world" — journalism, not entertainment.

### The grammar
Reconstruct what happened **from the evidence**, in order, and ask questions about
it. Build from primary materials — public records, FOIA documents, bodycam, 911
audio, interviews, data. Where a claim is contested, show the evidence for both
sides.

### Signature techniques
- **Evidence multicam sync** — line up the multiple sources (two or more bodycams
  on every scene, dashcams, ring cams, radio traffic) and intercut to condense
  time while staying true to what happened simultaneously.
- **Documents on screen** — the document is shown, then the key line is
  highlighted and read; draw the eye to one thing at a time.
- **Timeline reconstruction** — the sequence of events laid out with a scrolling
  timeline; the ticking clock made literal.
- **Data journalism graphics** — charts, maps and stat cards that visualise the
  investigation's findings; a simplified version when a scene is too complex.
- **Narrator spine** — a measured narrator holds the through-line; expert
  interviews give context.
- **"How it slipped" beats** — explain the mechanism (a chart of the burden of
  proof, a policy) so the audience sees how the failure happened.

### The accordion process
Most investigative films go through an **accordion**: add detail and context when
audiences are confused, then cut exposition when the film bloats; go back and
forth until the sweet spot. Trust the logical and emotional flow before leaning
on voiceover.

### Ethics
Verify every fact and attribution; hold the same rigour as print journalism.
Transparency about what is real and what is reconstructed is mandatory.

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

- **The evidence is the A-roll** — documents, footage, data and recordings carry the meaning; the narrator and experts are the connective tissue.

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


**For this skill:** **For this skill:** restrained and legible — documents on screen, timelines, count-ups for figures, callouts on charts, cut-on-action. Calm motion; the rigour is the drama.

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


## RENDER GATE — the 1 FPS contact sheet (mandatory before the full render)

**Never render the full video without sign-off.** Before the final render:

1. Extract one frame per second from the finished timeline:
   `ffmpeg -i build.mp4 -vf fps=1 sheet/f%04d.jpg`
2. Tile them into a **contact sheet** — a grid in time order, each frame
   labelled with its timestamp — so the whole edit reads at a glance.
3. **Show the user the contact sheet and wait for approval.** Render the full
   video only after they finalise.

The contact sheet is the cheapest place to catch pacing, composition, safe-zone
and continuity problems.

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
