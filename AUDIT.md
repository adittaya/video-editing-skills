# Audit of the original pack — findings and what changed

## Verdict
The architecture (narrow skills, asset tiers, hard limits, laws) is strong and was kept.
The weakness was depth and accuracy of the *numbers and examples*. It needed a targeted
upgrade, not a rewrite.

## Findings
1. **~30% duplication.** The identical ~1.9 KB Visual Narration block was pasted into 19 skills. Each skill now carries the full spec inline (standalone), without duplicated stray copies.
2. **No worked examples.** Zero timecoded beat sheets. Added one per skill.
3. **Loose / outdated platform numbers.** Short-form safe zones were too small (bottom 15%, right 48px); measured Shorts UI is ≈ bottom 380 px, right 200 px, top 240 px. Fixed and centralised.
4. **No true-peak spec.** Only LUFS was given. Added −1 dBTP ceiling and a loudness table by destination.
5. **Inconsistent delivery spec.** Only 3 of 20 skills had encode settings; none had colour tagging, CFR, or captions standards. Added a shared standard + per-skill delivery block.
6. **No pacing benchmarks per style.** Added ASL table and per-skill pacing conventions.
7. **Thin verticals.** Most were ~4.8 KB with generic structure. Added industry conventions, running lengths and common mistakes per vertical.
8. **Gaps (now filled):** added `youtube-long-form-essay`, `automotive-reveal-film`, `sports-athletics-highlight`, `legal-professional-services`, `crypto-web3-launch`. HDR guidance is still not covered.

## Honest limits of this upgrade
- Industry benchmarks are working conventions compiled from platform ad specs and practice; sources on safe zones and loudness conflicted, so the conservative value was used. Re-verify before paid campaigns.
- No performance statistics (retention %, CTR) were added, because I could not verify them reliably.
- Added later: `retail-grocery-promo`, `beverage-alcohol-brand`, `pharma-medical-device`, `hr-recruitment-employer-brand`, `agency-showreel`. Every master-list vertical now maps to a skill; HDR/colour-management guidance is still not covered.
- Regulated verticals (alcohol, pharma, legal, finance, crypto) use the client's approved wording verbatim; local rules vary and the client's compliance review is the gate.

## v2.1 — Modern editing toolkit
- Added to EVERY skill: a technique catalogue (what top editors use), a terminal toolchain table, 21 FFmpeg recipes (all executed on FFmpeg 6.1.1 with synthetic sources), a production loop, and premium-look rules.
- Added a per-skill **Signature techniques** list (30 tailored lists).
- Researched/verified: FFmpeg filters (xfade, zoompan, vidstab), HyperFrames (HTML→MP4, Apache-2.0), Remotion, auto-editor, MoviePy, WhisperX / rembg / Robust Video Matting / librosa / MediaPipe (as used in open-source editing pipelines).
- NOT re-verified here (general knowledge, marked 'optional' in the tables): Blender headless, MLT/melt, GStreamer, OpenTimelineIO, Demucs, ImageMagick. Model/tool licences (e.g. some matting models are non-commercial) must be checked before commercial use.
- Known limit: recipes were tested on synthetic clips; always inspect real renders (frames, contact sheet, loudness) before delivery.

## v2.2 — Hybrid style + NLE feature coverage
- Analysed six user-supplied reference videos (frame contact sheets, cut-rate, loudness, spectral balance). Findings are in each skill's H1 section. Loudness of all six was ~−14 LUFS (likely platform-normalised), so mix choices were inferred only from level/spectrum, not from isolating effects.
- Added: NLE feature → terminal map (ripple, slip, slide, copy-attributes, green screen, depth blur, sharpen, light leak/flare, emoji, tracking, proxy, loop, masks), recipes 22–36, `cutlist.py`, `track_text.py`, hybrid motion rules, hybrid dial per skill and a hybrid asset-request list.
- Tested here (FFmpeg 6.1.1, OpenCV 4.13, synthetic sources): recipes 22–34, 36, cutlist.py (duration check 5.0 s as expected), track_text.py (frame inspected: text followed the object).
- NOT tested here: 3D text arcs, particle-dissolve text, 3D hero renders, cloning, app-icon orbit, mind-map UI motion (need HTML/Three.js or supplied assets); chroma-key quality on real green-screen footage; matting model output quality/licence.

## v3 — external verification & fixes (this pass)
- **Tools re-tested on real runs:** `cutlist.py` rendered a 2-clip edit (2.5 s + 2.5 s at 2x) to exactly 3.77 s, 1080x1920, 30 fps — correct. `track_text.py` tracked a synthetic moving box for all 90 frames and produced a valid ASS with per-frame `\pos`. Both work; `track_text.py` needs `opencv-contrib-python`.
- **FIXED — non-ASCII frontmatter:** `agency-showreel` and `youtube-long-form-essay` carried en dashes (U+2013) in their `description`, the exact class of character that has caused platform bundle rejection before. Replaced with ASCII hyphens. All 30 skills now have ASCII-only frontmatter.
- **FIXED — README:** heading said "The 20 skills" while listing 30; a stray blank line split the v2 table in two. Both corrected.
- **FILLED — the flagged gap:** colour management, HDR and delivery added as Part 5 of the reference (working space, explicit colour tagging, limited range, HLG/PQ, 10-bit, HDR->SDR tone-map, 203-nit graphics white, banding prevention, ffprobe verification).
- **ADDED — the router:** the master list now ends with a Vertical -> skill map covering all 30 skills, so the index matches the pack.
