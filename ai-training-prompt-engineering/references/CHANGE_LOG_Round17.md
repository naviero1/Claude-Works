# Change log — Round 17 (2026-09-16)

> Superseded in part by the correction pass of 2026-09-17 (live order now
> dashboard → present → email → explain; Bravo rate displays 0.348%): see the
> facilitation plan’s "Correction pass" section and PENDING_CHANGES.md.

Baseline: the uploaded 96-slide facilitated 60-minute deck + facilitation plan +
Requirements_by_Artifact catalog (preserved unmodified in notes/intake/round17/).
Principle applied throughout: the training determines the exercises; the exercises
determine the reusable prompts; the builder supports those prompts.

## The deck (96 → 101 slides; live total stays 60:00)

- **Part 4 "Putting Prompts to Work" is now one connected case** — the supplier
  question carried through analyze → dashboard → present → email → explain.
- Slide 35 rebuilt: basic prompt → three named weaknesses → improved prompt, each
  addition a requirement type; announces the five-artifact arc.
- Slide 38: quotation extension corrected — the three Quote PDFs and workbook tab
  ARE in this package.
- Slide 40: dashboard demonstration now runs on the supplier data with a verified
  live check (Berlin × Bravo, 2026-03..08 → 8,575 units / 21 returns / 0.245%).
- Slide 43 repurposed: self-study presentation demonstration (mock deck +
  workbook tab); its former "More plays" content preserved as reference page 97.
- Slide 44 repurposed: **new DO 2:00 documents demonstration** (plain-language
  prompt, live topic + fallback samples); stale block-recap framing resolved.
  Funded by −1:50 of non-anchor TEACH compression (slides 2, 7, 9, 10, 14, 29,
  46, 58, 60, 63). New totals: TEACH 22:30 · DO 32:00 · REFERENCE 4:40 ·
  DIVIDER 0:50 = 60:00.
- Reference pages 98–101 added: full dashboard/presentation/plain-language
  exercises + the email prompt in full. All appendix pages keep zero live time.
- Notes updated on every touched slide (same MODE/TIME/… fields); validated
  against the baseline and render-checked. No G-codes in the live sequence.

## Exercise materials (all numbers independently recomputed)

- Supplier_Data_Clean.csv — 144 detail rows, TOTAL excluded, missing value kept
  blank and disclosed. The generator is seeded: data identical across rebuilds.
- Supplier_Quality_Dashboard.html — working offline dashboard with every taught
  control; coordinated views; empty/missing/zero states; visible footer
  self-check; verified headlessly and in a real browser run.
- Supplier_Quality_Mock_Presentation.pptx — the task-3 sample, built only from
  verified numbers; findings and recommendations visibly separated; validated
  and render-checked.
- Packaging_Change_Thread.txt + instructor-keys/Packaging_Change_Expected_Brief.md
  — the deck's canonical thread as a standalone file, with the four-trap key.
- plain-language/ — reusable prompt + three topics (source, sample, fidelity
  note, comprehension key each).
- Copilot-in-Outlook path verified against Microsoft's current support pages
  (notes/research/r28, retrieved 2026-09-16); the pasted-text fallback is primary.

## Workbook (Course_Workbook.xlsx)

- New INDEX (open-order + participant/instructor separation) · Data_Clean tab ·
  five task tabs (1-Analyze-Data … 5-Explain-Clearly) with starter→improved
  prompt iterations, requirement-type annotations, and self-check rows ·
  KEY-Analysis / KEY-Email instructor tabs whose numbers are computed from the
  data at build time. Legacy long-course tabs retained as an optional group.

## Tools

- **Template Creator**: task-first landing view — five task families whose
  requirement menus (instruction + acceptance check per row) are generated from
  Requirements_by_Artifact.md; editable wording; free-form box; honest status
  (never "ready" with an empty task); manual edits survive selection changes via
  an explicit rebuild bar (fixed in the legacy view too). Full taxonomy + 18
  legacy templates behind "Advanced". All behaviors machine-tested.
- **Configurator**: new Tasks sheet with the same five families (Yes/No rows,
  editable wording, computed assembled prompt — recalc-verified).

## Reference documents

- Cheat sheet rebuilt: requirement skeleton · 14-type menu · quality bar ·
  before/after supplier example · acceptance checks · ASK vs DELEGATE. One page.
- Field guide reorganized (20 pp): Part 1 requirement quality (NASA/INCOSE
  framing, verification vs validation) → elements as requirement types → menus
  by artifact → the five exercises worked → troubleshooting → evidence
  compendium.
- Taxonomy reference: elements-to-requirement-types mapping added; legacy
  template codes made optional ("no template code needed" path first).
- Requirements_by_Artifact.md now carries its maintenance map (what consumes it).
- Facilitation plan fully regenerated (101 rows, recomputed times).

## Known gaps, stated

- The 60-minute deck is maintained as a .pptx (baseline was built outside the
  repo's generator); its edit script and pristine baseline are preserved.
- Copilot feature names/licensing churn — r28 documents the verified state and
  the always-works fallback; re-verify quarterly.
- The legacy long-course deck and its tabs remain in the repo untouched; the
  60-minute course is the delivered package.
