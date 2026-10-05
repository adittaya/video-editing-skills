# Video Editing Skills — 30 skills + captured presets

A complete, client-ready video-editing skill set for AI agents. One skill per
editing style / client vertical, one look (Apple Standard), a mandatory
source → concept → prompt build order, and a copy-paste prompt that loads the
whole set into any agent.

---

## ▶ Copy-paste prompt (give this to your AI agent)

```text
You are a motion designer and video editor with full skill access. Load your
skill set from this public repository:

https://github.com/adittaya/video-editing-skills

Fetch and read these files (use the raw URLs under
https://raw.githubusercontent.com/adittaya/video-editing-skills/main/):

1. README.md                                (this file — the rules)
2. ASSET-REQUEST-GUIDE.md                   (the build order + prompt-file rules)
3. modern-editing-features-reference.md     (techniques, toolchain, recipes)
4. video-editing-styles-master-list.md      (the router: vertical -> skill)
5. EXAMPLE-ASSETS-PROMPT.md                 (a complete example prompt file)
6. presets/README.md                        (how presets work)
7. The ONE skill under skills/<name>/SKILL.md that matches my task — pick it
   using the router in file 4.

Then work strictly in this order:

- STEP 0 — SOURCE. Ask me for the source first: a video clip, the
  voiceover/audio, or a transcript/script. Analyse it and save
  SOURCE-ANALYSIS.json — video analytics (ffprobe, scene detection, loudness,
  palette, BPM) and, if there is audio, a WORD-LEVEL TRANSCRIPTION JSON
  (faster-whisper, word_timestamps=True).
- STEP 1 — CONCEPT. Write CONCEPT.md per the skill: premise, style, segment
  plan, scene table (sentence -> visual concept -> lane -> timing -> camera),
  visual-narration plan, sync map, asset manifest.
- STEP 2 — ASSETS-PROMPT. Write ASSETS-PROMPT.md: one executable brief per
  asset, addressed to YOU (you have image generation, audio generation and
  coding). Categories: images, transparent images (PNG/alpha), logos, music,
  sound effects, code components. Return ONE master zip containing MULTIPLE
  zips inside — a zip per category and a zip per component kit (each kit
  unzips to index.html, styles.css, README.md, assets/, palette as CSS
  variables).

Hard rules:
- The look is APPLE STANDARD, mandatory and the only option, unless a preset
  under presets/ is explicitly requested.
- NEVER include voiceover or video clips in ASSETS-PROMPT.md. I supply the
  A-roll (voice / footage / transcription) up front; if you need any B-roll
  clip, ask me SEPARATELY. You generate images, audio and code only — you
  cannot generate video.
- Text on screen maps the visual; it is never generic subtitles.
- Never invent facts, prices, stats, testimonials or logos.

Start by telling me which skill you will use and what source you need from me.
```

---

## What's inside

| Path | What it is |
|---|---|
| `skills/<name>/SKILL.md` | **30 skills** — one per editing style / client vertical. Each is complete and standalone: intake, the mandatory prompt file, look, edit, audio, industry benchmarks, a worked example, common mistakes, the full visual-narration spec, signature techniques, the modern editing toolkit (techniques + terminal toolchain + tested FFmpeg recipes), platform & delivery standards, QA and hard limits. |
| `presets/` | **Captured styles.** `preset-authoring/SKILL.md` turns a reference (contact-sheet PDF, video, or link) into a preset; `preset-001-zayyan-blue-glass/SKILL.md` is a full-depth preset locked to the measured "Blue Glass" look. |
| `ASSET-REQUEST-GUIDE.md` | The build order and the rules for writing `ASSETS-PROMPT.md`. |
| `EXAMPLE-ASSETS-PROMPT.md` | A complete, real example of the prompt file (returns one master zip of nested zips). |
| `modern-editing-features-reference.md` | The technique catalogue, the terminal toolchain, tested FFmpeg recipes, the hybrid premium pack, colour management/HDR, and reference cards. |
| `video-editing-styles-master-list.md` | The full landscape (editing styles, formats, 40+ client verticals) and the router: vertical → skill. |
| `AUDIT.md` | What changed in each version, with verification notes and honest limits. |
| `tools/cutlist.py` | Cut-list renderer: NLE-style edits (ripple/slip/slide/speed) → one FFmpeg run. |
| `tools/track_text.py` | Text that follows a moving object (OpenCV CSRT tracker → ASS). |

## The 30 skills

**Tier 1 — highest demand:** `apple-product-motion` · `saas-demo-explainer` ·
`short-form-retention` · `podcast-talking-head` · `corporate-brand-film` ·
`ecommerce-dtc-ads`

**Client verticals:** `youtube-long-form-essay` · `real-estate-video` ·
`esports-gaming-hype` · `education-course-video` · `healthcare-medical-video` ·
`finance-insurance-video` · `crypto-web3-launch` · `fitness-wellness-video` ·
`restaurant-hospitality-video` · `music-artist-visuals` · `event-wedding-film` ·
`personal-brand-creator` · `fashion-beauty-video` · `automotive-reveal-film` ·
`sports-athletics-highlight` · `legal-professional-services` ·
`retail-grocery-promo` · `beverage-alcohol-brand` · `pharma-medical-device` ·
`hr-recruitment-employer-brand` · `agency-showreel`

**Specialised:** `cgi-3d-architectural` · `government-nonprofit-psa` ·
`immersive-360-vr`

## The build order (mandatory)

```
STEP 0  SOURCE   ->  get a clip / audio / transcript, then analyse it
                     (video analytics + word-level transcription JSON)
STEP 1  CONCEPT  ->  write CONCEPT.md per the skill
STEP 2  PROMPTS  ->  write ASSETS-PROMPT.md (itself a prompt) -> one master
                     zip containing multiple zips
```

## The rules every skill obeys

- **Apple Standard is the only look** — the verified tokens (canvas
  `#ffffff`/`#f5f5f7`, text `#1d1d1f`/`#6e6e73`, the one blue
  `#0071e3`/`#0066cc`/`#2997ff`, the type ramp down to the 17px body, 980px pill
  buttons, the one-shadow philosophy, the spring motion). A preset is the one
  sanctioned override, and only when explicitly requested.
- **The Visual Narration Layer** — where a person speaks, the video SHOWS the
  idea (full-screen cutaway / front overlay / behind-the-subject), never just
  captions. Captions are additive, never the layer.
- **Text maps the visual** — on-screen text is design, not a subtitle track.
- **No metadata** burned into the frame.
- **Asset & Clearance Protocol** — the agent may always ask for assets, and
  hands back one prompt file.
- **No-Clank Law** — aligned, consistent, smooth, restrained, clean sound.
- **Honesty** — no voice generation, no logins or credentials, no invented
  facts, recreated UI disclosed.

## Licence

MIT (see `LICENSE`). Presets record methods, never content — never a source's
name, logo, copy or exact marks.
