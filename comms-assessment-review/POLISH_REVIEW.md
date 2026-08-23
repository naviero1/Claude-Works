# Communication Process Assessment — Polish Review

Review of the delivered artifacts (full workbook, lite workbook, Concept Cheat Sheet,
Framework Course, Full Workbook Manual) against the project's own spec, standing
decisions, and engineering constraints. Every finding carries an exact location.
Fixes belong in the **generators** (`analysis/make_workbook.py`,
`analysis/make_workbook_lite.py`) — never hand-edit the xlsx — followed by the full
§4 regeneration + verification loop.

Reviewed copies: `comms_assessment_workbook_1.xlsx` · `comms_assessment_lite.xlsx` ·
manuals/course/cheat-sheet PDFs v1.1. Date: 2026-08-23.

---

## A. Verified healthy — do not touch

- **Structure**: all 16 sheets present in the spec'd fixed order; tab colors correct
  (blue views, green README, gray computed); Lists hidden.
- **Content correctness**: cached results reproduce the planted story exactly —
  coverage 60%, 6 open defects led by FR04 (Gandalf → Frodo, `missing`, priority 15),
  theater = R9 on G1+G3, unclaimed = R3 on G2, 3 decision defects, 1 disputed
  quarantined. BY GOAL rollup numbers all check out.
- **Aesthetic system (full workbook)**: Arial in 100% of styled cells; input pale
  yellow `FFF7DE` on every input cell **including empty pre-wired rows**; computed
  gray `F2F2F0` + italic; header rows at 30pt with freeze panes on all data sheets;
  GoalLens picker present and validated (`GoalIds`).
- **No regression of the fixed bug**: every numeric conditional format found uses the
  guarded `AND(ISNUMBER(x), x>0)` FormulaRule pattern (Findings F9:H14, GoalLens
  E59:E64, lite Heatmaps). No conditional-format bleed below data anywhere.
- **No stray values** on empty pre-wired rows (Flows 33–100, Carriers 21–100 fully
  blank in cached pass). No `#NAME?`/`#REF!`/`#VALUE!` in either delivered file.
- **Print setup** on the three view sheets: landscape, fit-to-width, explicit print
  areas.

## B. Full workbook — functional polish (priority order)

1. **`GoalIds` named range is hard-coded to the seed** — `Goals!$A$2:$A$5`.
   The README's documented extension path ("add the goal row, then copy one
   involvement column…") silently fails at step 1: a fifth goal never appears in the
   GoalLens picker dropdown. Fix: define `GoalIds` as `Goals!$A$2:$A$20` (matches the
   sheet's capacity; blank cells are ignored by list validation).

2. **Status conditional formats stop at the seed rows, not the pre-wired rows.**
   - Flows status colors: `T2:T32` — rows 33–101 are pre-wired ("statuses appear as
     you type", per the manual) but new rows compute a status **with no color**.
     Extend to `T2:T101`. The five `cellIs equal "<status>"` rules are safe to
     extend as-is (text equality, no blank-row hazard).
   - Decisions defect flag: `L2:L6` vs 30 pre-wired rows. **Warning on the fix**: the
     current rule is `cellIs notEqual "aligned"`, which on an empty-string formula
     row evaluates TRUE (`"" ≠ "aligned"`) — extending it naively repaints the
     red-below-data bug this project already fixed once. Convert to the guarded
     FormulaRule `AND($L2<>"", $L2<>"aligned")`, then extend to `L2:L31`.
   - Same audit for Alignment `J2:J37` (currently exact-fit; fine today, but
     regenerate-time ranges should track row counts, not constants).

3. **Findings hyperlinks embed the workbook's own filename.** All six section links
   target `comms_assessment_workbook.xlsx` + location. The moment the file is
   renamed or emailed (the reviewed copy is already `…_1.xlsx`), every link breaks.
   Fix: internal location-only links (openpyxl: `Hyperlink(ref=…, location="'Flows'!A1")`
   with no target, or `target="#'Flows'!A1"`). Also: the manual promises "every row
   hyperlinks back to its source tab" — reality is six *section-header* links. Either
   generate per-row `=HYPERLINK("#…")` cells or soften the manual's claim (D4).

4. **The highest-risk input columns have no dropdowns.** The manual's own "three
   entry mistakes that cost an afternoon" are vocabulary/typo mistakes, and none of
   the columns involved is validated:
   - Flows: `topic_id` (C), `from` (D), `to` (E) — free text; a typo splits the
     required/actual match, the exact failure mode the manual warns about.
     `criticality` (F) unvalidated (1–5).
   - Carriers: `flow_id` (A), `carrier_id` (C) — free text.
   - Decisions: RACI actor columns and `actual_venue_id` — free text.
   - Rituals: `owner_actor_id` — free text (attendee_ids is a `;`-list, fair to skip).
   Fix: add named ranges `TopicIds`, `ActorIds`, `FlowIds`, `RitualIds`, `ChannelIds`
   over the pre-wired extents and attach list validations. Ten minutes in the
   generator; eliminates the workbook's most likely real-world data-quality failure.

5. **Two boolean styles on Rituals.** `compliance_required` = lowercase text
   `'true'/'false'` (validation `"true,false"`), CR1–CR6 = `=TRUE()` formulas
   (validation `"TRUE,FALSE"`). The score formula `COUNTIF(M2:R2,TRUE())` counts
   booleans; an entry LibreOffice stores as *text* `"TRUE"` silently doesn't count —
   an invisible under-score. Unify on one representation (booleans everywhere, or
   text everywhere plus a text-tolerant COUNTIF) and make both validations match.

## C. Lite workbook — polish

6. **Calibri leak — violates "Arial everywhere".** 211 cells: **Heatmaps (195 —
   the flagship view)** and hidden Lists (16). The generator's font isn't applied on
   those writes. This is the single most visible aesthetic defect in the deliverable
   set.

7. **Header row heights are inconsistent**: 15.0 (Stakeholders, Channels, Criteria),
   23.85 (Topics, Carriers, Decisions, Start area), 35.05 (Rituals). The full
   workbook standardizes at 30; the lite should standardize too (Oscar's aesthetics
   requirement names "consistent header bars/heights" explicitly).

8. **Near-duplicate named ranges**: `CarrierL = Carriers!$A$2:$A$36` vs
   `VenueL = Carriers!$A$2:$A$38`. If the two-row difference is intentional
   (venues include the last two rows; carriers don't), comment it in the generator;
   if not, unify — silent range drift here will bite a future edit.

Verified healthy in lite: CF ranges cover the full pre-wired extents (N2:N60,
N2:N31, G2:G30) — the pattern B2 asks the full workbook to adopt; Topics capture row
has 7 dropdowns including goal/stakeholder/carrier ID lists — the pattern B4 asks the
full workbook to adopt; Carriers is a computed view (correctly not an input sheet).

## D. Documentation drift (cheap to fix, expensive if B spots them first)

1. Manual p.1: "**Fifteen sheets** keyed by short IDs" — the workbook has **16**
   (handoff agrees: 16).
2. Manual §8: `verify_workbook.py` "**46 checks**" vs handoff "**56 checks**" —
   align both to the actual count.
3. Source-count triangle: manual says "**22-source** Frameworks library", course says
   "**25 lessons** — one per row of the Frameworks tab", the tab has **26 data
   rows**. Pick the real number and align all three.
4. Manual §Findings: "every row hyperlinks back to its source tab" — currently six
   section-header links (see B3).
5. Handoff's lite sheet list omits the Stakeholders and Channels sheets that exist.

## E. Worthwhile next-level polish (candidates, not defects)

- **Mendelow power/interest grid** — the already-acknowledged gap; `power`/`interest`
  fields exist on Stakeholders. Natural next feature and pitch-friendly.
- **AutoFilter on Flows/Carriers/Rituals** header rows — zero-risk usability.
- **Sheet protection with inputs unlocked** — would eliminate the "gray cell shows
  typed text" failure mode the troubleshooting table documents. Offer as an option;
  protection annoys power users.
- **`print_title_rows` on data sheets** (repeat header row when Flows spans pages).
- **Lite Start sheet**: add the same cell-legend line the full README carries, so the
  capture companion is self-explaining in the room.

## Suggested fix order

B1 → C6 (two one-liners, both user-visible) → B2 → B3 → B4 → C7 → D1–D5 (one doc
pass) → B5 → C8 → E as appetite allows. After generator changes: full §4 loop
(`run_analysis.py`, both `make_workbook*.py`, LibreOffice recalc, all three
verifiers green, zero formula errors).
