# The Video Editing Skills Pack

30 narrow, client-ready skills — one per editing style / client vertical — plus
the master list of every style in the landscape.

**Why narrow:** one generalist skill carries the *average* of every style
(pacing tuned for nothing, graphics tuned for nothing). A podcast and an Apple
product film are different crafts. Each skill here has exactly one voice.

## THE LOOK — APPLE STANDARD ONLY (mandatory)

**Every skill in this pack uses one look: the Apple Standard.** There is no
style menu and no alternative palette. The verified tokens (canvas
`#ffffff`/`#f5f5f7`, text `#1d1d1f`/`#6e6e73`, the one blue `#0071e3`/`#0066cc`/
`#2997ff`, the type ramp down to the 17px body, the 980px pill buttons, the
one-shadow philosophy, the spring motion) are mandatory in all 30 skills.

Verticals differ **only** in what the graphics depict and which single accent
carries meaning — never in the underlying system. Each skill's look section
carries the full token set plus its vertical application; any other palette
named anywhere in a skill is deprecated.

## ▶ Copy-paste prompt (give this to your AI agent)

```text
You are a motion designer and video editor with full skill access. Load your
skill set from this public repository:

https://github.com/adittaya/video-editing-skills

Fetch and read (raw URLs under
https://raw.githubusercontent.com/adittaya/video-editing-skills/main/):

1. README.md
2. ASSET-REQUEST-GUIDE.md
3. ADVANCED-FEATURE-USE-CASES.md
4. modern-editing-features-reference.md
5. video-editing-styles-master-list.md     (the router: vertical -> skill)
6. DOCUMENTARY-STYLE-GUIDE.md              (the documentary router: 14 styles)
7. EXAMPLE-ASSETS-PROMPT.md
8. presets/README.md
9. The ONE skill under skills/<name>/SKILL.md that matches my task.

Everything is connected — work strictly in this order and keep the record linked:

- STEP 0 — SOURCE. Ask me for the source first (clip, voiceover/audio, or
  transcript). Analyse it and save SOURCE-ANALYSIS.json.
- STEP 1 — CONCEPT. Write CONCEPT.md: premise, segment plan, SENTENCE TABLE
  (sentence -> visual -> lane -> stressed word -> camera), CAMERA-TRACK PLAN,
  CONTACT-SHEET PLAN (V1/V2/V3), the CAPTION STYLE SHEET, sync map, asset
  manifest. It is the single source of truth.
- STEP 2 — ASSETS-PROMPT. Write it from the manifest: images, transparent images
  (incl. transparent caption PNGs / alpha clips), logos, music, sound effects,
  code components (incl. the advanced-feature kits and the caption engine).
  Return ONE master zip containing MULTIPLE zips inside.

Hard rules:
- CAPTIONS: declare ONE styled-caption style and hold it; use styled captions,
  transparent-background (alpha) captions and chroma-key text/subject as the
  concept needs. A plain SRT is an optional sidecar, never the on-screen text.
  Chroma key: flat green #00B140/blue, despill, 1-2px choke, light wrap, garbage
  matte.
- RENDER GATE: build contact-sheet VARIANTS from 1 FPS frames — V1 Classic Grid,
  V2 Storyboard Filmstrip, V3 Pro QC Sheet — present them, and ASK ME: "Did you
  like any of these, or shall I generate more variants so you can choose?" The
  variant I pick is written BACK INTO CONCEPT.md. Render only after I finalise.
- A new contact sheet means a new CONCEPT revision.
- The ADVANCED FEATURE USE-CASES are mandatory where the concept needs them.
- Obey the CAMERA LAW and the SENTENCE LAW.
- If the task is a documentary, pick the style from DOCUMENTARY-STYLE-GUIDE.md.
- The look is APPLE STANDARD, mandatory and the only option, unless a preset or
  a named documentary style is explicitly requested.
- NEVER include voiceover or video clips in ASSETS-PROMPT.md. I supply the
  A-roll up front; ask for B-roll SEPARATELY. You generate images, audio, code.
- A-roll = whatever carries the meaning. Never invent facts; label every
  recreation, animation and composite.

Start by telling me which skill you will use and what source you need from me.
```

---

## How to use
1. Read `video-editing-styles-master-list.md` to find the right style/vertical.
2. Open that skill's `skills/<name>/SKILL.md` and follow it — it is complete on
   its own: intake questions, asset request, look, edit, audio, delivery, QA,
   limits.
3. **Every skill begins by asking for assets.** Tier 2 skills STOP until the
   client's real assets arrive.

## The asset tiers (the rule that matters most)
| Tier | Meaning | Behaviour |
|---|---|---|
| **0** | Synthetic-ready — nothing needed | build immediately |
| **1** | Asset-enhanced — works without, better with | offer the synthetic path, request assets to upgrade |
| **2** | **Asset-mandatory** — cannot exist without real inputs | **STOP, emit ASSET-REQUEST.md, wait** |

Every skill declares its tier up front. AI-generated images can satisfy *some*
Tier-2 needs (backgrounds, textures, stylised shots) but **never**
authenticity-critical ones (a real listing, a real person, a real event, a real
testimonial). Voice is always a Tier-2 asset — no voice generation exists.

## The 31 skills

### Tier 1 — highest demand
| Skill | Makes | Asset tier |
|---|---|---|
| `apple-product-motion` | product launches, feature reveals, app films | 0–1 |
| `saas-demo-explainer` | product demos, onboarding, software explainers | 1–2 |
| `short-form-retention` | Reels / Shorts / TikTok | 0–2 |
| `podcast-talking-head` | podcast episodes, clips, interviews | **2** |
| `corporate-brand-film` | brand films, culture, investor, thought leadership | 1–2 |
| `ecommerce-dtc-ads` | product ads, UGC ads, offer videos | **2** |
| `documentary-film` | documentaries, mini-docs, observational, archival | **2** |

### Tier 2 — client verticals
| Skill | Makes | Asset tier |
|---|---|---|
| `real-estate-video` | listing tours, agent brand, neighbourhood, CGI tours | **2** |
| `esports-gaming-hype` | roster reveals, recruitment, highlight montages | 1–2 |
| `education-course-video` | lessons, modules, course promos, training | 1–2 |
| `healthcare-medical-video` | practitioner intros, myth-vs-fact, testimonials | **2** |
| `finance-insurance-video` | explainers, market updates, trust films | 1–2 |
| `fitness-wellness-video` | transformations, workouts, coaching | **2** |
| `restaurant-hospitality-video` | menu reels, chef stories, hotel/travel films | **2** |
| `music-artist-visuals` | music videos, lyric videos, tour visuals | **2** (audio) |
| `event-wedding-film` | highlights, teasers, event recaps | **2** |
| `personal-brand-creator` | vlogs, tutorials, opinion, day-in-the-life | **2** |
| `fashion-beauty-video` | lookbooks, collection films, routines, demos | **2** |

### Added in v2
| Skill | Makes | Asset tier |
|---|---|---|
| `youtube-long-form-essay` | 6–25 min essays, explainers, documentary-style | 0–2 |
| `automotive-reveal-film` | model reveals, feature demos, dealer reels | **2** |
| `sports-athletics-highlight` | highlights, recruiting reels, athlete profiles | **2** |
| `legal-professional-services` | attorney/advisor intros, FAQ, trust films | **2** |
| `crypto-web3-launch` | protocol explainers, launches, community reels | 1–2 |

| `retail-grocery-promo` | offer videos, weekly deals, in-store loops | 1–2 |
| `beverage-alcohol-brand` | brand films, serve/ritual shorts, event recaps | **2** |
| `pharma-medical-device` | mechanism explainers, trial data, device IFU | **2** |
| `hr-recruitment-employer-brand` | culture films, role explainers, onboarding | **2** |
| `agency-showreel` | showreels, capability films, case studies | **2** |

### Tier 3 — specialised
| Skill | Makes | Asset tier |
|---|---|---|
| `cgi-3d-architectural` | off-plan walkthroughs, product renders | **2** (geometry) |
| `government-nonprofit-psa` | PSAs, civic explainers, impact films, appeals | 1–2 |
| `immersive-360-vr` | 360 tours, VR, interactive/branching | **2** |

## The build order — SOURCE, CONCEPT, then PROMPTS (mandatory)

1. **STEP 0 — Source.** Get at least one of: the **video clip**, the
   **voiceover/audio**, or the **transcript/script**. Then analyse it
   comprehensively and save `SOURCE-ANALYSIS.json` — video analytics (ffprobe,
   scene detection, loudness, palette, BPM), a **word-level transcription JSON**
   (faster-whisper `word_timestamps=True`), or the sentence list.
2. **STEP 1 — Concept.** Write **CONCEPT.md**: premise, style, segment plan,
   scene table, visual-narration plan, sync map, asset manifest.
3. **STEP 2 — Prompts.** Only now write **`ASSETS-PROMPT.md`**, from the
   concept's asset manifest.

## ASSETS-PROMPT.md is itself a prompt (returns a zip)

The file is not a spec sheet — **it is a prompt you hand straight to your AI
agent.** It opens with the role and the task, gives the deliverable tree, numbers
every asset with its own brief and output path, and closes with acceptance
checks. The agent executes it and returns **ONE master zip containing MULTIPLE zips
inside** — `MANIFEST.md` plus a zip per category (`images.zip`,
`transparent.zip`, `logos.zip`, `music.zip`, `sfx.zip`) and `components.zip`,
which itself holds one zip per component kit. No loose asset files. A complete
real example ships in **`EXAMPLE-ASSETS-PROMPT.md`**.

## The prompts are addressed to an AI agent with image, audio AND coding

Every brief in `ASSETS-PROMPT.md` is written to an AI agent that can **generate
images, generate audio, and write code**. Six categories: **images ·
transparent images (PNG/alpha) · logos · music · sound effects · code
components**. The code briefs ask for the graphics code does best (glass cards,
animated type, diagrams, count-ups, UI mockups, shaders, 3D) and specify the
**kit deliverable**: a folder with `index.html`, `styles.css`, `README.md` and
`assets/`, zipped, palette exposed as CSS variables.

**Voiceover and ALL video clips are excluded.** You supply the A-roll (voice /
footage / transcription JSON) at the start; any **B-roll clip** the build needs
is requested **separately**, never in this file. The agent generates images,
audio and code only — it cannot generate video.

## The mandatory prompt list — ASSETS-PROMPT.md

**Strict rule:** before building, every skill produces ONE file listing every
generatable asset with **one paste-ready prompt per item** — images, transparent
images (PNG/alpha), logos, music, and sound effects. You generate them with your
own tools. **Voiceover and video clips are excluded** — you supply those
separately. Format, prompt rules and a worked example: `ASSET-REQUEST-GUIDE.md`.

## The asset-request file (how you get asked for assets)

Whenever a skill needs something it cannot make, it hands you ONE markdown file —
an **ASSET-REQUEST.md** — never scattered chat questions. Every image entry
carries a **ready-to-paste generation prompt**, so you can generate the assets
yourself. The format, the prompt-writing rules, a prompt library, and a full
worked example are in **`ASSET-REQUEST-GUIDE.md`**.

## Every SKILL.md is standalone
Each skill file is complete and production-ready on its own — hand ONE file to an agent and it has everything: intake, asset request, look, edit, audio, industry benchmarks, worked example, common mistakes, the full visual-narration spec, the platform & delivery standards, QA and hard limits. No other file is required.

## What every skill contains
Intake → asset request → look → edit → audio → **industry benchmarks** → **worked example (timecoded beat sheet)** → **common mistakes** → **visual-narration spec** → **signature techniques for the style** → **modern editing toolkit (technique catalogue, terminal toolchain, 21 tested FFmpeg recipes, production loop, premium rules)** → **hybrid premium style & advanced feature pack (NLE feature→terminal map, asset request, recipes 22–36, cut-list and tracking scripts, hybrid dial)** → **platform & delivery standards** → QA → hard limits.

Also included: `tools/cutlist.py` (ripple/slip/slide cut-list renderer) and `tools/track_text.py` (text that follows an object) — both also embedded in every SKILL.md; `modern-editing-features-reference.md` — a plain-language list of the editing techniques and terminal tools (optional reading; no skill depends on it).

## The laws every skill obeys
- **Text Law** — on-screen text maps the visual; never generic subtitles.
- **No-Metadata Law** — nothing burned that is metadata (labels, watermarks).
- **Palette & Gradient Law** — clean premium palette + background gradient.
- **Asset & Clearance Protocol** — always free to ask the client for assets.
- **No-Clank Law** — aligned, consistent, smooth, restrained, clean sound.
- **Caption & text system** — styled text captions · transparent-background (alpha) captions · chroma-key text & subject, with the style sheet, word-level timing, alpha/despill/choke/light-wrap specs, and a text-motion surprise pack (kinetic typography, word-pop, text-behind-subject).
- **Pipeline connectivity law** — everything is connected: SOURCE → CONCEPT (sentence table + camera track + contact-sheet plan) → ASSETS-PROMPT → BUILD → RENDER GATE → SIGN-OFF → RENDER; the chosen contact-sheet variant is written back into CONCEPT.md, and a new contact sheet means a new CONCEPT revision.
- **Contact-sheet variants (render gate)** — before the full render the agent offers **V1 Classic Grid · V2 Storyboard Filmstrip · V3 Pro QC Sheet**, presents them, and asks "did you like any of these, or shall I generate more variants?" Render only after sign-off.
- **Advanced feature use-cases** — the full professional toolset is mandatory in every skill (multi-track timeline, multicam, proxy editing, keyframing, motion tracking, masking/rotoscoping, speed ramping, stabilisation, optical flow, colour correction + grading + scopes + HDR, chroma key, compositing/VFX, 3D camera tracking, advanced transitions, noise reduction/EQ/sync/mixing, auto subtitles, AI background removal, auto reframing, scene detection, AI colour, plus the stills/design craft) — with the **Camera Law** and the **Sentence Law**. Full guide: `ADVANCED-FEATURE-USE-CASES.md`.
- **Documentary family** — 14 documentary-style skills (Vox explainer, map-led geo, streaming docuseries, true crime, investigative, immersive field, archival essay, Ken Burns, animated, essay film, nature, docudrama, Op-Docs short, bodycam) plus `DOCUMENTARY-STYLE-GUIDE.md`, the router.
- **Mandatory feature use-cases** — every skill carries the modern-standard set
  (anchor zoom in/out, motion tracing, keyframing, bezier easing, word-pop,
  count-ups, readability zoom, micro-interactions, screen transitions, cursor
  physics, cut-on-beat, a sound per cut, correct-then-grade, speed ramps, motion
  blur, parallax, mask reveals, freeze frames, callouts, PiP, loops). They are
  required, not optional — without them the edit reads as amateur.
- **Render Gate** — before the full render, always produce a **1 FPS contact
  sheet** (`ffmpeg -i build.mp4 -vf fps=1`) and wait for the user's sign-off.
- **The lane is defined by function** — A-roll is whatever carries the meaning.
  In a graphics-led piece the motion graphics ARE the A-roll and the footage
  becomes B-roll.
- **No voice generation · no logins/credentials · no invented facts · disclose
  recreations.**
