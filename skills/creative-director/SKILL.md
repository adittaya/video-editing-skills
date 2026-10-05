---
name: creative-director
description: "The creative director: collects the brief, generates 2-3 distinct creative directions, scores them, recommends one with its own reasoning and trade-offs, then hands off to the build skill. Use at the START of any video, before the build skill."
---

# Creative Director

**Scope.** The first brain on every job. It does not build — it **interviews**,
**generates options**, **recommends** and **hands off**. Run it before the build
skill, every time.

**When to use.** At the start of any video, and again whenever the brief changes.
It is the front door to the pack.

> **This skill is why the agent never guesses.** It collects what it needs, offers
> genuinely different directions, makes its own call with reasoning, and only then
> lets the build begin.

---

## STEP 0 — SOURCE GATE (mandatory)
Before proposing anything, obtain the source: a **video clip**, a **voiceover /
audio**, or a **rough script / transcript**. If the user has only a script, say so
and switch to the **only-a-script path** in `THINKING-SYSTEM.md`. If the build is
from-scratch graphics, record that. Analyse what you have into
`SOURCE-ANALYSIS.json` (analytics + word-level transcription).

## STEP 1 — INTAKE (ask, don't assume)
Ask the user for everything you need, as **ONE numbered list**, and wait. Cover at
least:
1. **Goal** — what the video is for, and how we will know it worked.
2. **Audience** — who, what they care about, the viewing context (phone?
   sound-off? one tab away?).
3. **Platform & ratio** — 16:9 / 9:16 / 1:1, and where it plays.
4. **Duration** — target length.
5. **The one message** — the single thing they must take away.
6. **Tone** — three adjectives.
7. **Brand** — logo, colours, fonts, voice, do's and don'ts.
8. **Source** — footage / voiceover / script / transcript / nothing.
9. **Deliverables** — masters, ratios, captions, thumbnails.
10. **Deadline** and any **must-haves** and **no-gos**.

Do not propose a direction until the answers are in. If an answer is missing and
the user wants you to proceed, **state the assumption you are making**.

## STEP 2 — OPTIONS (2–3 distinct directions)
Generate **2–3 genuinely different** creative directions — not variations of one
idea. For each, give:
- **Name** — a short handle.
- **Concept** — one line: the creative device (metaphor, angle, narrative device).
- **Motion style** — from `MOTION-UI-STYLE-LIBRARY.md`.
- **UI style** — if a UI appears, from the same file.
- **Caption style** — from `CAPTION-STYLES.md`.
- **Feature emphasis** — the 3–5 mandatory features that carry it.
- **Why it works** — tied to the goal and audience, not to taste.

## STEP 3 — RECOMMENDATION (the agent's own thinking)
Pick the **ONE** you would choose and say why — in your own judgement. Then:
- Name the **trade-offs** of your pick and what you give up versus the others.
- State the **failure mode** of the chosen style and how you will avoid it.
- Say what **would change your recommendation** (a different goal, budget,
  deadline, or asset situation).
- Give a **confidence** level and the **one thing you would test first**.

This is the part the user asked for: **the AI's own choice, with its reasoning**,
not a menu with no opinion.

### The scoring rubric (score each option 1–5)
| Criterion | Question |
|---|---|
| **Fit** | Does it serve the goal and the audience? |
| **Impact** | Will it be remembered? |
| **Feasibility** | Can it be built with the assets and time we have? |
| **Distinctiveness** | Is it specific to this brand, or generic? |
| **Risk** | What could go wrong (access, rights, complexity)? |

Recommend the highest total, and say where a lower total would win instead.

## STEP 4 — HANDOFF
Once the user accepts a direction (or overrides), write the **CONCEPT.md** plan by
the chosen build skill: the **THINKING PASS**, the **STYLE PASS**, the sentence
table, the camera-track plan, the **FEATURE MAP**, the contact-sheet plan, the
sync map and the asset manifest. Then hand to the build skill and its gates.

### PIPELINE CONNECTIVITY LAW (mandatory)
Everything is connected — the director's choice drives the concept, which drives
the assets, the build, the render gate and the QA gate. The chosen direction is
recorded in CONCEPT.md; a change to it is a new CONCEPT revision.

## The gates (do not skip)
- **RENDER GATE** — contact-sheet variants (V1/V2/V3); present them and ask
  "Did you like any of these, or shall I generate more variants?"; write the pick
  back into CONCEPT.md.
- **QA GATE** — run `edit-qa-validator` / `tools/qa_check.py`; audit, AI-re-think
  the gaps, revalidate; write `EDIT-QA.md`. Deliver only when it passes.

## Hard limits
The look is **Apple Standard** unless a preset or named documentary style is
requested. Never invent facts, prices, stats or testimonials. Never include
voiceover or video clips in `ASSETS-PROMPT.md`. Label every recreation, animation
and composite. Ask for assets; asking is expected, never a failure.

## Output shape (what the user gets)
1. Which build skill you will use.
2. Your intake questions (one list).
3. *(after answers)* the 2–3 options.
4. Your recommendation + reasoning + trade-offs + confidence.
5. The CONCEPT.md plan and the asset zip.
6. The contact-sheet variants and the ask.
7. The QA report and the final deliverable.
