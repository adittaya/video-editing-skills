# Preset Index — the captured-style library

Seven ready, measured styles, organised in **category subfolders**. Each is a
**full skill** locked to a reference, so a client can ask for that exact look by
name. Each row says **what it is** and **ask for this when…**.

| # | Preset (path) | Category | What it is | Ask for this when… |
|---|---|---|---|---|
| 001 | `portfolio/preset-001-zayyan-blue-glass` | portfolio | Soft royal-blue glassmorphism reel: floating glass UI cards, dotted connectors, the speaker composited into the scene, kinetic mapped text. 16:9. | A premium personal-brand / portfolio reel with a soft-blue glass look. |
| 002 | `short-form/preset-002-realtor-word-caption` | short-form | Bright high-key vertical talking-head: word-by-word bold captions, a two-colour keyword accent (blue/cyan + orange/amber), hard cuts + a whip transition, a frosted-glass pill end card. 9:16. | A realtor / creator talking-head reel that must hold sound-off attention. |
| 003 | `product/preset-003-saaswave-tactile-purple` | product | Bright 3D "digital workspace" product reel: photoreal objects in a purple/magenta wash, floating UI cards, a purple cursor, 3D buttons, a morph-to-logo. 16:9. | A SaaS / product / course launch that should feel tactile and playful. |
| 004 | `esport/preset-004-cloudy-esport-neon` | esport | High-energy vertical eSports montage: blue-neon architecture, silhouettes, glow/bloom, glitch + whip transitions, 3D milestone numerals, chat-bubble UI, a gold trophy. 9:16. | An esports team milestone, roster reveal or recruitment hype reel. |
| 005 | `product/preset-005-higgsfield-dark-ui` | product | High-contrast dark-mode product demo: white UI floating in a black void, 2D→3D spatial UI transforms, a neon lime-green accent, a neon-blue command line, a light-mode end card. 16:9. | An AI / software / tool launch with a sleek dark-UI demo. |
| 006 | `podcast/preset-006-podcast-overlay-explainer` | podcast | Single static talking-head in a dark, desaturated studio carrying a bright graphics layer — UI-mimicking overlays, full-screen cutaway diagrams, one yellow keyword, white drop-shadow captions, a brand end-card. 16:9. | A talking-head explainer where the graphics carry the proof. |
| 007 | `creator/preset-007-creator-kinetic-text` | creator | Stark white studio, presenter in a black tee, kinetic word-by-word text on the chest, an orange script + pill badges, outlined grey section numerals, screenshot/UI proof cutaways, a colour-inverted emphasis frame, a brand end-card. 16:9. | A high-energy creator / coach / business talking-head. |

## Parent skills (PRESET -> SKILL LINKAGE)
| Preset | Parent skill |
|---|---|
| 001 Blue Glass | `agency-showreel` |
| 002 Realtor Word-Caption | `short-form-retention` |
| 003 SaaSWave Tactile Purple | `saas-demo-explainer` |
| 004 Cloudy eSport Neon | `esports-gaming-hype` |
| 005 Higgsfield Dark-UI | `saas-demo-explainer` |
| 006 Podcast-Overlay Explainer | `podcast-talking-head` |
| 007 Creator Kinetic-Text | `personal-brand-creator` |

Each parent skill carries a **"Reference-learned patterns"** section drawn from
its preset(s), so triggering the *skill* (not the preset) already applies the
real-world learnings.

## How to use a preset
1. Open `presets/<category>/<preset>/SKILL.md` — a complete skill (same depth as
   every other), with the measured palette, type, motion, beat map and signature
   techniques.
2. Run it like any build skill: STEP 0 source → CONCEPT → ASSETS → BUILD →
   RENDER GATE → QA GATE.
3. If the client wants this look **plus** a variation, treat the preset as the
   base and adjust only what changes.

## Add your own
Send a reference (video, contact-sheet PDF, or link) and follow
`presets/preset-authoring/SKILL.md` — it measures the reference at 2 FPS and
writes a new `presets/<category>/preset-NNN-<name>/SKILL.md`, then patches the
parent skill (the linkage law).

## Provenance rule
A preset records **methods, never content** — never the source's name, logo or
copy. Palette is **measured**; motion/audio are measured where possible and
inferred otherwise (stated in each preset's Provenance).
