# Gap analysis — training v1.0 → v1.1

**Purpose:** the delta between the original deliverable (v1.0, 49 slides, commit `84bb431`)
and v1.1, mapped to the owner's decisions. This document gated the merge to `main` (decision D11).

## Deck: 49 → 56 slides

| Change | Decision | What moved |
|---|---|---|
| Welcome + Map merged into one slide | A4 | −1 slide; the map now shows the **two-session split** (B5) and the take-home card |
| Embeddings sidebar cut from the escalation-ladder slide | A4 | ladder cards widened; the analogy survives in speaker notes |
| **"The elements, defined"** slide pair added to Part 3 | A1 | five elements with weak→strong pairs + the safety valves & diagnosis grid — promoted from the ELEMENTS handout |
| **Inheritance map** slide added to Part 5 | A1 | the generative→agentic mapping table — the training's deepest idea, now presented |
| Part 4 catalog (4 slides) → **2 live-demo slides + handout pointer** | A2 | blind critique (G3) and dashboard-from-a-paste (G6) demo scripts on-slide; the 8-template catalog is now a 60-second pointer; full content unchanged in `prompt-library/` |
| **Five "three-minute rep" mini-slides** (Parts 1, 2, 3, 5, 6) | A3 | each marked skippable on-slide; Part 4's rep = the demos; Rep 6 marked protected |
| **Session-2 recap slide** added before Part 5 | B5 | 60-second re-entry + homework check |
| Cross-references made relative ("two slides ahead", "later this part") | — | absolute slide numbers removed so future edits can't orphan them |
| Quarterly-refresh markers on dated slides' notes (assistants, gallery, matrix) | A4/D12 | owner: Oscar |

**Not changed:** all Part 1/2 content slides, the distinction table, mission brief, worked
example, guardrails, Part 6, and the close — the audit rated these Core/Keep and they stand.

## Beyond the deck

- **Run_of_Show.pdf** (new, B6): minute-by-minute for both sessions, both demo scripts,
  ordered contingency cuts, prep checklist.
- **Presets 14 → 18** (C9): comparison study → decision deck · scored comparison workbook ·
  versioned model/report update · master-doc → audience variants. All three tools regenerated;
  configurator recalculated with zero formula errors.
- **No follow-up mechanism** built (B7 — declined).
- **Pilot** deferred until after the training (C8).
- **PROJECT_STATE.md** (new): continuation brief so any future session resumes cleanly.

## Verification

- Deck rebuilt and every new/changed slide render-checked as images.
- Builder exercised (presets load; prompt assembles); xlsx recalc: `success, 0 errors`.
- Company-data scrub (predates v1.1, commits `ca5f865`/`81214ef`) intact: zero identifier
  hits in all sources.

## Merge disposition (D11)

v1.1 is a strict superset of v1.0's content with the approved deletions above, all of which
survive in handouts. Nothing in v1.0 is lost that the owner didn't explicitly retire.
**Cleared to merge to `main`; iteration continues on `main` thereafter.**
