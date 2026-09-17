# Companion coherence audit — checkpoint 1

Read-only assessment by Beebop, 2026-09-17. No course source, deck, workbook, or PDF (Portable Document Format) was modified by this read-only audit. Oscar explicitly reconfirmed upload of the completed review package after the earlier automatic approval rejection. This authorization covers review publication only. Local downloads and this assessment are review evidence only. All suggested changes below are **separate content/build decisions for owner approval**, not automatic additions to the visual-polish scope.

## Verified snapshot and limits

Repository: `naviero1/Claude-Works`; branch: `claude/training-course-polish-oxohwj`; examined commit: `6e829b82bcd92653f0daa68fcdbbf1d60664a4cb`. Repository paths below are relative to `ai-training-prompt-engineering/`.

Actual current files fetched and inspected:

| File | Git blob | Evidence |
|---|---|---|
| `deliverables/From_Prompts_to_Agents_Course.pdf` | `00cc627572877aeca3588521a943a31d15ab2b9f` | Downloaded bytes match blob; **83 pages**; extracted text and section order inspected. |
| `src/assets/course_content.json` | `28f1e13448ea3d7d3e642e9131e99ca913261d50` | Current source fetched. Parsed content equals older local `course_content_775.json`; byte-level difference does not imply content change. |
| `deliverables/Course_Workbook.xlsx` | `5a6ca157da0f57821c5d43652041285ed8eae9c3` | Actual worksheet order and INDEX/README contents inspected. |
| `references/exercise-data/Supplier_Data_Exercise.xlsx` | `e2f6e8ed096983a610e05273ddacc31910e7efa5` | Actual file has **Data only**. |
| `references/exercise-data/Supplier_Data_Analyzed.xlsx` | `0d625bdd9bf28a528b7da2a39a62375ef951c1e0` | Actual file has **Data + Summary**, two native charts, source-linked formulas. |

Current dashboard and mock-deck generators, builder generator, exercise-asset generator, package indices, and relevant PDF source sections were inspected. This is a **source/structure/lineage audit**. It does not claim a fresh full visual review of all 83 PDF pages, fresh browser execution, or a new independent verification of every exercise answer. The earlier reconstructed PDF was not substituted for the current repository artifact.

## What should stay

The extended course exists and its main application sequence is already coherent. Preserve its depth and the newer summarized slide sequence; no rollback is justified by this audit.

| Step | Current PDF section | Printed PDF page |
|---|---|---:|
| 1 | Inspect, then analyze | 27 |
| 2 | One follow-up, in the same chat | 29 |
| 3 | The assistant returns your workbook | 30 |
| 4 | A dashboard from the returned workbook | 30 |
| 5 | Five slides from the same findings | 32 |
| 6 | Organize the email thread | 34 |
| 7 | Extract the quotes | 37 |
| 8 | Compare the quotes — and refuse to pick a winner | 38 |
| 9 | Reference files become a research workbook | 39 |

The workbook INDEX and current primary worksheet order follow the same sequence, with plain-language explanation after Research as the reference exercise. The builder source has eight primary workflow cards in that order, plus the explanation card last; follow-up questions remain part of analysis, so eight cards do not contradict nine teaching steps. `src/build_builder.py:82–119` establishes that order. Do not redesign the builder to force a one-card-per-slide correspondence.

The returned workbook contains the correct structural progression: original Data cell values remain equal to the participant input; Summary contains formulas; its two native charts read `Summary!$A$7:$A$9` / `Summary!$D$7:$D$9` and `Summary!$G$7:$G$18` / `Summary!$H$7:$H$18`. Preserve these editable charts and their calculation links. The dashboard generator reads `Supplier_Data_Analyzed.xlsx`, sheet Data, excludes TOTAL, and retains 144 detail rows (`src/build_dashboard.py:12–20`). This part of the promised lineage is implemented.

## Approval decisions, by priority

### C01 — P1: finish the promised lineage at the management presentation

**Evidence:** `REFERENCES.md:22` and `src/assets/course_content.json:1338` say the returned workbook feeds both dashboard and presentation. The dashboard complies. The mock generator instead reads `Supplier_Data_Clean.csv` directly (`src/build_mock_deck.js:3–16`) and labels that source in its generated footer (`:75`, `:92`). It recomputes all numbers from that parallel file rather than from the returned workbook.

**Impact:** Current numbers can agree while the exercise still teaches a different lineage from the prepared fallback. A revised returned workbook could feed the dashboard but leave the mock presentation stale.

**Proposed bounded repair:** Make the prepared mock generator read the returned workbook's detail data through the same defined schema, or use an explicitly generated and traceable intermediate exported from that workbook. Preserve its verified calculations, native charts, reporting period, and narrative. Add one focused dependency check showing that the mock source is actually the returned workbook. Update provenance footers accordingly. Do not merely relabel the existing comma-separated values (CSV) source as workbook-derived.

**Separate approval required:** build input and provenance wording change. This is not layout polish.

### C02 — P1: remove the conflicting instruction to upload the answer-bearing course workbook

**Evidence:** Current `Course_Workbook.xlsx` INDEX!B6 correctly identifies `Supplier_Data_Exercise.xlsx` as the participant input. INDEX!B14 classifies README and older exercises as legacy/optional. However README!B4 still says “upload this whole workbook” and follow `G2-DataAnalysis`; the same current file includes `KEY-Analysis` and `KEY-Email`. INDEX!B10 says to keep the keys out of participant handouts. `src/build_exercise_pack.py:45` contains the old upload instruction. PDF page 27 (`src/assets/course_content.json:1160`) also tells the reader that the single-sheet participant workbook has a README tab; actual `Supplier_Data_Exercise.xlsx` contains only Data.

**Impact:** A self-study reader following the old README can upload answer keys and use the wrong prompts. A reader following the PDF can look for a nonexistent worksheet.

**Proposed bounded repair:** Preserve all legacy exercises but label the legacy README instruction explicitly as superseded for this live course, route data uploads to `Supplier_Data_Exercise.xlsx`, and point column-definition readers to the actual course-workbook README or existing PDF definitions without implying that another upload is needed. Decide whether the distributed course workbook is intentionally an after-course resource containing keys, or whether a separate participant copy is required; do not silently delete/hide sheets.

**Separate approval required:** instructional copy and distribution policy, not slide rearrangement.

### C03 — P2: make package navigation accurately identify participant inputs

**Evidence:** `REFERENCES.md:3–5` says nothing in references is required in participants' hands. The same file identifies all live inputs under `references/exercise-data/` at lines 21–30. `DELIVERABLES.md:3–5` calls everything in deliverables participant-facing and self-contained, although the workbook includes instructor key tabs and the live exercises use separate input files.

**Impact:** Someone downloading only deliverables can lack the spreadsheet, thread, quotations, and research files needed to run the exercises.

**Proposed bounded repair:** Keep current file locations and distinguish three roles in the existing index: participant inputs, prepared outputs, and instructor/reference materials. State clearly that the PDF is complete for reading, while performing file-based exercises uses the separately supplied files. Do not relocate the entire package or add a new packaging scheme without approval.

**Separate approval required:** index/distribution wording.

### C04 — P2: reconcile stale extended-course narration with the summarized prompts

**Evidence:**

- PDF page 26, chapter title/intro (`src/assets/course_content.json:1060–1062`) describes one dataset carried across all nine steps. The very next section correctly says that only the data arc through the management mock-up shares the upload and that email, quotes, and research bring their own sources (`:1073`).
- PDF page 42 (`:2008`) says the builder uses “the same five task families”; current builder source has eight primary workflow cards plus the optional explanation (`src/build_builder.py:82–119`). This is stale explanatory copy, not a wrong builder order.
- The email explanation (`src/assets/course_content.json:1659`) says the prompt ends by requesting the next clarification and a no-send boundary. The actual immediately preceding short prompt (`:1654`) ends with source citation by sender and date. These safeguards may appear elsewhere, but they are not in that quoted prompt ending.

**Proposed bounded repair:** Change only the surrounding explanatory sentences to describe the existing summarized prompts and current source transitions accurately. Retain the concise prompt wording and nine-step order. Do not expand every live prompt to satisfy commentary left over from an earlier version.

**Separate approval required:** narrowly listed content corrections in the extended course and any matching index copy.

### C05 — P2: clarify the scope of the all-in-one answer appendix

**Evidence:** Appendix B intro at PDF page 79 (`src/assets/course_content.json:4925`) calls itself the worked keys for every exercise. Its four sections cover supplier analysis, email, quotation comparison, and research. Supplier analysis includes the filtered-dashboard check, but the appendix does not collect the full acceptance criteria for the returned editable-chart workbook, dashboard behavior, presentation quality, mission-brief/gate exercises, and capstone. Some checks are already supplied in the teaching chapters. Plain-language samples and their keys are embedded in Appendix A rather than separately at the end.

**Impact:** The book is substantial and useful, but “every exercise” overstates the answer appendix's standalone coverage and makes instructor/self-study navigation less dependable.

**Proposed bounded repair:** Prefer a compact exercise-to-check index referencing existing pages and files over duplicating whole chapters. Label optional sample answers clearly and keep them after the learner attempts the relevant exercise. Decide whether to amend the broad coverage claim or add only the missing acceptance checks. Do not remove reference detail to meet a page-count target.

**Separate approval required:** appendix navigation and narrowly scoped coverage change.

## Additional wording observation

The returned Summary!A2 says “the TOTAL row and the one missing Inspection_Hours value are excluded from calculations” (`src/build_pass05_assets.py:82`). Its formulas correctly include other values from the record containing the missing inspection-hours cell. If C02/C04 wording corrections are approved, clarify that the **missing field is not zero-filled and its otherwise usable record is retained**. No calculation change is indicated by the inspected formulas.

## Recommended disposition

Keep the extended course, current application order, returned native charts, and summarized prompt approach. The visual pilot can preserve all existing content while the owner separately considers C01–C05. Do not report that the PDF needs rebuilding from scratch, and do not treat these content findings as permission to rewrite slide text or alter font sizes. For final release, recheck the actual exported PDF after approved corrections; this audit establishes source/sequence evidence, not whole-document visual readiness.
