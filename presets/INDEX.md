# Preset Index — the captured-style library

Five ready, measured styles. Each is a **full skill** locked to a reference,
so a client can ask for that exact look by name. Pick one when it fits; each
row says **what it is** and **ask for this when…**.

| # | Preset | What it is | Ask for this when… |
|---|---|---|---|
| 001 | **Blue Glass** (`preset-001-zayyan-blue-glass`) | Soft royal-blue glassmorphism portfolio reel: floating glass UI cards, dotted connectors, the speaker composited into the scene, kinetic mapped text. 16:9. | A premium personal-brand / portfolio reel with a soft-blue glass look. |
| 002 | **Realtor Word-Caption** (`preset-002-realtor-word-caption`) | Bright, high-key vertical talking-head reel: **word-by-word bold captions**, a two-colour keyword accent system (blue/cyan + orange/amber), hard cuts + a whip transition, a frosted-glass pill end card. 9:16. | A realtor / creator / coach talking-head reel that must hold sound-off attention. |
| 003 | **SaaSWave Tactile Purple** (`preset-003-saaswave-tactile-purple`) | Bright 3D "digital workspace" product reel: photoreal objects in a purple/magenta wash, floating UI cards, a purple cursor, 3D buttons, a morph-to-logo. 16:9. | A SaaS / product / course launch that should feel tactile and playful. |
| 004 | **Cloudy eSport Neon** (`preset-004-cloudy-esport-neon`) | High-energy vertical eSports montage: blue-neon architecture, silhouettes, glow/bloom, glitch + whip transitions, 3D milestone numerals, chat-bubble UI, a gold trophy. 9:16. | An esports team milestone, roster reveal or recruitment hype reel. |
| 005 | **Higgsfield Dark-UI** (`preset-005-higgsfield-dark-ui`) | High-contrast dark-mode product demo: white UI floating in a black void, 2D→3D spatial UI transforms, a neon lime-green accent, a neon-blue command line, a light-mode end card. 16:9. | An AI / software / tool launch with a sleek dark-UI demo. |

## How to use a preset
1. Open `presets/<name>/SKILL.md` — it is a complete skill (same depth as every
   other), with the measured palette, type, motion, beat map and signature
   techniques.
2. Run it like any build skill: STEP 0 source → CONCEPT → ASSETS → BUILD →
   RENDER GATE → QA GATE.
3. If the client wants this look **plus** a variation, treat the preset as the
   base and adjust only what changes.

## Add your own
Send a reference (video file, contact-sheet PDF, or link) and follow
`presets/preset-authoring/SKILL.md` — it measures the palette (sampled hex), type,
motion and pacing and writes a new `preset-NNN-<name>/SKILL.md`. A preset is
never a few KB; if it is, it is incomplete.

## Provenance rule
A preset records **methods, never content** — never the source's name, logo or
copy. Palette is **measured**; motion/audio are measured where possible and
inferred otherwise (stated in each preset's Provenance).
