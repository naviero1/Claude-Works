# Integration v06 — restored classics in the opening block

Date: 2026-09-18. Builder: `src/build_integration_v06.py` (deterministic, v05 → v06).
Deck: `notes/visual-polish/pilot/From_Prompts_to_Agents_Visual_Pilot_v06.pptx` (109 slides).

## Owner direction

1. Restored classics belong in the final deck's main flow, not the appendix (2026-09-18, in session).
2. Placement correction, same day, before the first draft shipped: "I dont want them in those
   positions, I need them within the first slides, I am not going to make it to those slides in
   the first training." → all restored slides moved into the opening stretch.
3. "Make sure you state what you did and why" → reply 18 posted to the agent channel
   (mirror: `notes/agents/2026-09-18-18-rocksteady-to-beebop.md`).

## Final placement (all within the first 23 slides)

| Pos | Slide | Origin (v05 pos) |
|---|---|---|
| 4 | Four eras: rules → learning → generative → agentic | 109 (replaces live 4, dropped) |
| 6 | The hardware story — chips, Nvidia, data centers | 110 (replaces live 6, dropped) |
| 16 | Fluency is not evidence | 106 |
| 17 | Real, public, verified — and all avoidable | 107 |
| 18 | The flattery bias — measured, and all over the news | 108 |
| 21 | Pick by task, not habit — September 2026 | 111 |
| 22 | Chat, workflow, or agent — the path decides | 104 |
| 23 | Four context failures — name it, then cure it | 105 |

Live 7–15 keep their positions; live 16–17 shift to 19–20; live 18–103 shift +6 (24–109).
Dropped live 4 and 6 map to positions 4 and 6 in the reference remap, so stale references
still land on the replacement slide.

## Builder guarantees (defects found during the pass, now handled in-script)

- Historical v1.10 CONSOLIDATION owner quotes in speaker notes are frozen — the reference
  remapper skips any run carrying the marker (they were being renumbered; historical quotes
  are records, not live references). Verified verbatim on slides 34 and 85.
- Integrated slides' appendix footers ("Restored classic" / self-referential "Related live
  slide N") are replaced with the live footer; genuine appendix pages (positions > live end)
  keep theirs.
- Every `page-number` shape renumbered; 44 textual "slide N" references remapped in visible
  text and notes (builder prints the full list each run).

## Verification (2026-09-18)

109 slides; titles at 4/6/16–18/21–23 machine-checked; zero "Restored classic" strings;
zero appendix footers in the live zone; page numbers equal positions; v1.10 quotes verbatim;
full-deck LibreOffice render clean. Contact sheet:
`review-evidence/pilot/v06-early-block-contact-sheet.png`.

## Open items

- Integrated slides still carry the "REFERENCE STUDY" top chrome from their appendix build;
  whether to relabel to teaching chrome is Oscar's call (flagged, not blocking).
- Speaker notes on the eight restored slides are empty (Beebop instruction 13, pending
  Oscar's go): source notes exist in `references/From_Prompts_to_Agents_Training.pptx`
  (old 4, 6, 14, 15, 29, 17); positions 22–23 are rebuilds and need authored notes.
- Companion documents (timing/slide-map, facilitation plan) are stale against v06 numbering.
