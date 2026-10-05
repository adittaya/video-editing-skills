# ASSET KIT PROMPT — "Blue Glass" portfolio reel

You are an AI agent with **image generation, audio generation, and coding**.
Produce every asset specified below and return **ONE zip file** containing all
outputs, organised exactly as the deliverable tree shows. Use every value given
exactly as written. Do not ask questions. Do not include voiceover or video clips — the user
supplies the A-roll (voice / footage / transcription JSON) at the start, and any
B-roll clip is requested separately, never here. You generate images, audio and
code only — you cannot generate video.

---

## Deliverable — return ONE master zip, containing MULTIPLE zips inside

Return a single outer zip. Inside it: a manifest, plus **one zip per category and
one zip per component kit** — never loose files.

```
blue-glass-assets.zip                 ← the ONE master zip you return
├── MANIFEST.md                       ← the only loose file
├── images.zip                        ← section 1 outputs
├── transparent.zip                   ← section 2 outputs (PNG with alpha)
├── logos.zip                         ← section 3 (or a NOTE.md inside)
├── music.zip                         ← section 4
├── sfx.zip                           ← section 5
└── components.zip                    ← contains ONE ZIP PER COMPONENT
    ├── glass-bio-card.zip            ← each kit is itself a zip
    │     └── index.html, styles.css, README.md, assets/
    ├── phone-chat.zip
    ├── review-wall.zip
    └── kinetic-text.zip
```

Every component zip must unzip to its own folder with `index.html`,
`styles.css`, `README.md` and `assets/`.

---

## 1. Images — generate (3)

1. **Background plate** — 2560×1440 (16:9) → `images/background_plate.png`
   Generate a soft, blurred abstract gradient background: deep navy `#182B74`
   at the bottom blending up through royal blue `#144EDF` and periwinkle
   `#5876E9` into a pale `#C7CFDF` highlight at the top. Smooth organic blobs,
   very soft focus, subtle film grain. No text, no objects, no people. High
   resolution, wallpaper quality.

2. **Workspace plate** — 1920×1080 → `images/workspace_plate.png`
   Generate a top-down soft-3D desk scene: matte rounded objects (a pencil cup,
   folded paper, a small cube) on a flat surface, lit in cool purple-blue light,
   shallow depth of field, gentle shadows. Muted and minimal. No text, no logos.

3. **Grain overlay** — 1920×1080 → `images/grain_overlay.png`
   Generate a very light film-grain texture, neutral grey, even, seamless and
   tileable. No objects, no text.

## 2. Transparent images — generate (3) → `transparent/`

Each must be a PNG with a transparent background (alpha). No text.

1. **App tiles** — 512×512 each → `transparent/app_tiles.png` (three tiles in
   one file or three files). Three rounded-square tiles in one consistent style:
   glossy soft-3D, subtle inner highlight, soft shadow, one accent hue each.
2. **Glass disc** — 800×800 → `transparent/glass_disc.png`. A glossy translucent
   blue disc, refractive glass material, soft specular rim, subtle blue glow,
   centred.
3. **Hand cursor** — 256×256 → `transparent/hand_cursor.png`. A clean white
   hand-pointer cursor icon, minimal, slight soft shadow, crisp edges.

## 3. Logos — `logos/`

The editor's wordmark and handle badge are **supplied by the user as an SVG**.
Do not generate or reproduce a logo. If nothing is supplied, write
`logos/NOTE.md` saying the wordmark is set in the reel's typeface as plain text
— no generated mark.

## 4. Music — generate (1) → `audio/music/`

1. **Reel bed** — 31 s, 95 BPM, WAV + MP3 → `audio/music/reel_bed.*`
   Generate a calm, premium electronic bed. Soft sustained synth pad under a
   light piano motif and a very subtle pulse. Steady and unhurried, with a
   gentle lift at 20 s that settles by 27 s. No vocals, no drums, no big drops.

## 5. Sound effects — generate (5) → `audio/sfx/`

Short WAV files, clean, no reverb unless stated.

1. `tick_text_land.wav` — 0.1 s. A single soft UI tick: clean, quiet,
   high-frequency.
2. `whoosh_card_expand.wav` — 0.4 s. A smooth airy whoosh, soft and low-energy,
   no pitch sweep up.
3. `pop_badge.wav` — 0.15 s. A clean bright UI pop, rounded, short.
4. `swipe_message.wav` — 0.2 s. A soft tactile swipe/blip, quiet, as a message
   bubble arrives.
5. `impact_finale.wav` — 1.2 s. A low soft cinematic impact with a gentle tail —
   warm, not aggressive.

## 6. Components — build (4) → `components/<name>/`

Build each as a **kit folder**: `index.html`, `styles.css`, `README.md`,
`assets/`. All styling values must be exposed as CSS custom properties so the
palette can be changed without editing the code. Use the given values exactly.

### 6.1 `glass-bio-card` — a frosted-glass card
- border-radius 30px; background `rgba(255,255,255,0.15)`; 1px solid stroke
  `rgba(255,255,255,0.62)`; `backdrop-filter: blur(22px) saturate(125%)` with a
  `-webkit-` fallback; shadow `0 24px 60px rgba(18,43,116,.28)`.
- Text white; DM Sans / Manrope with system fallback; headline 40px/600; body
  17px/400; letter-spacing -0.02em.
- Expose `--glass-fill`, `--glass-stroke`, `--glass-radius`, `--accent`
  (`#7C5CFF`) as CSS variables.
- Entrance animation: rise 24px + fade 0→1 over 0.5s with
  `cubic-bezier(0.16,1,0.3,1)`.
- README explains each file and how to recolor.

### 6.2 `phone-chat` — a dark-mode phone chat (HTML/CSS/JS)
- Rounded phone frame, radius 44px, thin bezel; status bar reading **9:41**.
- Messages arrive in sequence with a soft rise+fade (0.3s each, 0.9s apart),
  driven by a small JS driver reading a `data-schedule` JSON:
  `[{t:0,side:"right",text:"Reels?"},{t:1,side:"right",text:"Cinematic?"},{t:2,side:"right",text:"What about motion graphics"},{t:3,side:"left",text:"works?"}]`
- Bubble fill `rgba(255,255,255,0.12)`, white text, radius 18px. Colours as
  variables. README included.

### 6.3 `review-wall` — an expanding testimonial card (HTML/CSS/JS)
- A "Client Reviews" card that starts collapsed showing one review and expands to
  five, animated (height + opacity, 0.5s, `cubic-bezier(0.16,1,0.3,1)`).
- Each review: avatar circle with an initial, five stars in the accent
  `#7C5CFF`, one short line of white text. Glass styling as in 6.1.
- Data from a `reviews` JSON array. README included.

### 6.4 `kinetic-text` — word-level text (HTML/CSS/JS)
- Given a sentence and per-word timings, each word rises 18px + fades in on its
  cue; ONE keyword per line is set in the accent colour at 1.15× size.
- `data-words` JSON, e.g. `[{w:"Scrolling",t:0},{w:"past",t:0.4}]`. Easing
  `cubic-bezier(0.16,1,0.3,1)`, 0.35s per word. Font-size, colour and accent
  exposed as variables. README included.

---

## Acceptance checks before you return the zip

- All of sections 1, 2, 4, 5, 6 are present; section 3 is a note if nothing is
  supplied.
- Every value given was used exactly (hex, px, durations, easings, BPM, lengths).
- No text appears inside any generated image.
- Every component folder contains `index.html`, `styles.css`, `README.md` and
  `assets/`, and exposes its palette as CSS variables.
- The master zip contains **multiple zips** (one per category, one per component) — no loose asset files except `MANIFEST.md`.
- `MANIFEST.md` lists every zip, and inside them every file, with its size/duration and the beat it serves.
- The zip contains **no** voiceover and **no** video clips.
