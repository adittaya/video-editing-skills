# Advanced Feature Use-Cases — the mandatory professional toolset

This is the checklist every build reads. **"Mandatory" means: if the concept
needs it, you use it.** These are the features that separate a professional edit
from an amateur one. Use each where it earns its place; each skill carries a
per-skill emphasis line naming the ones that are non-negotiable for that
vertical.

Reading this file is meant to make the agent *reach for the feature* — and every
time a needed feature is used, the video improves toward an industry standard.

---

## 1 · Timeline & structure
- **Multi-track timeline** — layer video, audio and effects; never a flat single
  track. Plan V1/V2/V3 + A1/A2 and keep the structure legible.
- **Multi-camera editing** — sync angles by waveform or timecode, then cut on
  speaker or on action.
- **Proxy editing** — cut on low-res proxies, then re-render the SAME cut list
  against the originals.
- **Batch export & render** — deliver every ratio/resolution from one master.
- **Project collaboration** — shared bins, markers and a naming convention so a
  second editor can pick up the timeline.

## 2 · Motion & animation
- **Keyframing** — animate position, scale, opacity, rotation, blur on an eased
  curve. Nothing moves without keys.
- **Motion tracking** — attach text/effects to a moving object (point or planar
  track). Smooth the track with a short lowpass before binding, or the graphic
  will jitter.
- **Masking & rotoscoping** — isolate a person or object frame-by-frame for a
  cut-out, a reveal or a replacement.
- **Speed ramping / time remapping** — speed curves across a beat; ramp into and
  out of the key moment.
- **Stabilisation** — 2-pass warp stabilise; crop a few percent to hide the warp.
- **Frame blending / optical flow** — smooth slow motion without stutter.

## 3 · Colour
- **Colour correction** — exposure, white balance and contrast FIRST.
- **Colour grading** — the look (LUT, film emulation, split-tone) SECOND.
- **Scopes** — waveform, vectorscope, histogram and RGB parade: grade by the
  numbers, not by eye. Legalise with the scope, not the monitor.
- **HDR grading** — only on explicit request; tone-map to SDR for delivery.

## 4 · Compositing & effects
- **Chroma key** — green/blue-screen removal with spill suppression and a clean
  edge; refine with a matte choke and a light wrap.
- **Compositing / VFX** — combine multiple layers into one scene (screen
  replacement, set extension, particle passes, light wraps).
- **3D camera tracking** — solve the camera move and add 3D elements that sit in
  real footage.
- **Advanced transitions & effects** — blur, glow, glitch, light leaks, film
  grain, chromatic aberration — each timed to a cut or a beat.

## 5 · Audio
- **Noise reduction** — remove hiss, hum and room tone before anything else.
- **EQ** — high-pass dialogue, de-mud the low-mids, carve space for the music.
- **Audio syncing** — match audio to picture by waveform or timecode.
- **Multi-track mixing** — dialogue, music and SFX balanced; duck music 12–18 dB
  under voice.
- **Surround / spatial** — only where the delivery needs it (cinema, 360/VR).

## 6 · AI & smart features
- **Auto subtitles (speech-to-text)** — word-level timing drives the captions AND
  the narration plan.
- **AI background removal** — matte a subject without a green screen.
- **Auto reframing** — re-frame the master for 9:16 / 1:1 / 4:5 keeping the
  subject in the safe zone.
- **Scene detection & auto cutting** — build a cut list from detected scene
  changes.
- **AI colour / exposure correction** — a first-pass normalisation, then grade by
  hand.

## 7 · Assets & stills (for every generated image and graphic)
The photo- and design-craft features apply to every asset the build makes:
- Layer-based editing · layer masks · blending modes.
- Frequency separation (skin retouch) · dodge & burn.
- Content-aware fill / object removal · perspective correction.
- RAW processing · tone curves · HDR merge · panorama stitch.
- AI-assisted selection · non-destructive workflow.
- Vector editing (bezier) · gradient mesh · typography controls (kerning,
  tracking, leading) · symbol/asset libraries · artboards · grid systems ·
  export for multiple formats/resolutions.

## 8 · The Camera Law (mandatory wherever there is a camera)

A camera move is a feature, not a decoration. Five rules:

1. **One camera wrapper only.** All zooms and pans come from a single master
   camera. Never apply local ad-hoc transforms to multiple nested elements.
2. **One camera move at a time.** Never stack camera transforms. If two moves
   overlap, resolve priority or queue them.
3. **Every zoom has a reason** — READ · EMPHASIZE · REVEAL · FOLLOW · BREATHE.
   If you cannot justify it, remove it. **Constant zoom = no zoom.**
4. **Do not cut while zoomed.** Either return to rest or hold the scene; cuts
   while scaled break spatial continuity.
5. **Motion blur only during fast motion.** Compute blur from the instantaneous
   camera velocity and apply it only while velocity is high: `blur = clamp(v*k,
   0, max)` (start k ≈ 0.012, max ≈ 24 px). Blur at rest = soft focus.

**Anchor zoom** — set the transform origin on the target (its centre) before you
animate scale, so the zoom grows *out of* the thing being read. **Follow
(motion trace)** — keep the tracked subject inside a safe rectangle with a
critically-damped spring; trigger a gentle auto-zoom when subject activity
exceeds a threshold.

## 9 · Sentence-level narration — the Sentence Law (mandatory)

Every **sentence** of narration gets its own visual event, bound to that
sentence's stressed word. See the Visual Narration Layer in each skill.

- One sentence → one visual beat (a cutaway, a reveal, a label, a count, a camera
  move).
- Land the visual on the sentence's **stressed word** (±100 ms), not the sentence
  start.
- If a sentence has no visual, either give it one or cut the sentence.
- If a visual has no sentence, it belongs to a different beat.
- The camera move (READ / EMPHASIZE / REVEAL) is itself a sentence-level event,
  bound to a word or phrase.

## 10 · The test

Walk the timeline. For each feature the concept needed, ask: **"is it there, and
is it doing a job?"** A missing needed feature — a flat single track, an ungraded
image, a jittery tracked label, a static sentence — means the edit is not
finished. Reading "mandatory" is the prompt to use the feature; using the feature
is what makes the video hold up.
