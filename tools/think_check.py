#!/usr/bin/env python3
"""
think_check.py — scaffold a CONCEPT.md from a raw script.

Runs the "only-a-script" thinking pass mechanically: splits the script into
sentences and beats, and emits a CONCEPT.md skeleton pre-filled with the beat
map, the two-column (said | shown), the visual plan, the style pass, the
sentence table and the feature map (all 11 groups) for the agent to complete.

Usage:
    python think_check.py SCRIPT [--out CONCEPT.md] [--title "My Video"]

Deps: standard library only. No network. Writes only --out.
"""
import argparse, os, re, sys

FEATURE_GROUPS = [
    "Camera & framing", "Motion & animation", "Speed & time", "Transitions & cutting",
    "Text & titling", "Colour", "Compositing & VFX", "Audio", "AI & smart",
    "Stills & design", "Workflow & delivery",
]

def sentences(text):
    # strip markdown headings/bullets, split on sentence enders
    text = re.sub(r"^[#>\-\*\d\.\)\s]+", "", text, flags=re.M)
    text = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p.strip() for p in parts if len(p.strip()) > 2]

def beats(sents, per=2):
    # a beat ~ one idea; group sentences in small clusters
    return [sents[i:i+per] for i in range(0, len(sents), per)]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--out", default="CONCEPT.md")
    ap.add_argument("--title", default="Untitled")
    ap.add_argument("--per-beat", type=int, default=2)
    a = ap.parse_args()

    try:
        raw = open(a.script, encoding="utf-8", errors="ignore").read()
    except Exception as e:
        sys.exit(f"cannot read script: {e}")
    sents = sentences(raw)
    if not sents:
        sys.exit("no sentences found")
    bs = beats(sents, a.per_beat)

    L = []
    L.append(f"# CONCEPT — {a.title}\n")
    L.append("> Scaffolded by `tools/think_check.py`. Complete every table. "
             "Follow `THINKING-SYSTEM.md`.\n")

    L.append("## THINKING PASS (mandatory)\n")
    L.append("### The stack (top-down)\n")
    L.append("| Layer | Answer |\n|---|---|")
    for k in ["Goal", "Audience", "Angle", "Concept", "Script/outline",
              "Visual beats", "Shot cards", "Style pass", "Feature pass", "Logistics"]:
        L.append(f"| {k} | _fill_ |")
    L.append("\n### Target emotion per section (EZRA)\n")
    L.append("| Section | Target emotion | Rhythm (cuts/min) |\n|---|---|---|")
    for i in range(1, 4):
        L.append(f"| Section {i} | _fill_ | _fill_ |")
    L.append("\n### Beat map — two-column (said | shown)\n")
    L.append("| # | Said (narration) | Shown (what is on screen) | Viewer question | Lane | Duration |\n|---|---|---|---|---|---|")
    for i, b in enumerate(bs, 1):
        said = " ".join(b).replace("|", "/")
        L.append(f"| {i} | {said} | _what is on screen_ | _viewer question_ | _A/B_ | _s_ |")
    L.append("\n### Visual plan (the review document for meaning)\n")
    L.append("| Script beat | Viewer question | Visual evidence | Risk to review | Final asset |\n|---|---|---|---|---|")
    for i in range(1, len(bs) + 1):
        L.append(f"| {i} | _fill_ | _fill_ | _date / quote / licence / causation_ | _asset_ |")
    L.append("\n### Retention check\n")
    L.append("- Most likely drop-off point: _fill_\n- The fix: _fill_\n")

    L.append("## STYLE PASS (mandatory)\n")
    L.append("| Slot | Choice | Failure mode to avoid |\n|---|---|---|")
    for k in ["Motion style", "UI style", "Caption style", "Colour / grade", "Motion system"]:
        L.append(f"| {k} | _from MOTION-UI-STYLE-LIBRARY.md / CAPTION-STYLES.md_ | _fill_ |")
    L.append("")

    L.append("## SENTENCE TABLE (Sentence Law)\n")
    L.append("| # | Sentence | Visual concept | Lane | Stressed word | Camera (reason) |\n|---|---|---|---|---|---|")
    for i, s in enumerate(sents, 1):
        L.append(f"| {i} | {s.replace('|','/')} | _visual_ | _A/B_ | _word_ | _READ/EMPHASIZE/REVEAL_ |")
    L.append("")

    L.append("## CAMERA-TRACK PLAN (Camera Law)\n")
    L.append("| Time | Reason | Target | Zoom | Hold |\n|---|---|---|---|---|")
    L.append("| _0:00_ | _READ_ | _selector_ | _1.2_ | _while-read_ |\n")

    L.append("## FEATURE MAP — the Feature Pass (mandatory, every group)\n")
    L.append("| Group | Feature | Applies? | Where | How | Why |\n|---|---|---|---|---|---|")
    for g in FEATURE_GROUPS:
        L.append(f"| {g} | _see ADVANCED-FEATURE-USE-CASES.md_ | _yes/no_ | _timecode_ | _implementation_ | _the job_ |")
    L.append("")

    L.append("## Contact-sheet plan\n")
    L.append("Build V1 Classic Grid / V2 Storyboard Filmstrip / V3 Pro QC Sheet. "
             "Record the user's pick here.\n")
    L.append("## Sync map\n_word-level timings_\n")
    L.append("## Asset manifest\n- images:\n- transparent (PNG/alpha):\n- logos:\n- music:\n- sound effects:\n- code components:\n")

    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"wrote {a.out}  ({len(sents)} sentences, {len(bs)} beats, "
          f"{len(FEATURE_GROUPS)} feature groups)")

if __name__ == "__main__":
    main()
