> **SUPERSEDED — 2026-09-17:** The owner now prefers the summarized version. Stop the rollback and mandatory 101-slide rebuild below. Follow [instruction 07: Keep the summaries; improve the visual presentation](2026-09-17-07-beebop-to-rocksteady.md). Preserve useful work already done and follow the owner's review process. The text below remains only as a historical record.

# Beebop → Rocksteady — Emergency stabilization and controlled slide rebuild

The owner has rejected the latest application-slide build and has authorized a rollback and controlled rebuild. Complete only the work below, commit it, report the evidence, and stop.

## 1. Freeze the current broad update

Do not modify the course PDF, workbook, builder, configurator, dashboard, prepared outputs, indexes, or reference documents in this iteration. Preserve the current 83-page all-in-one PDF and the new exercise assets as frozen inputs. They are not yet approved and will be synchronized only after the presentation is approved.

Do not continue editing the 103-slide presentation produced in commit `5afda8e`.

## 2. Restore the last visually coherent presentation baseline

Restore only:

`ai-training-prompt-engineering/deliverables/From_Prompts_to_Agents_Facilitated_60_Minute.pptx`

from commit:

`50c729ebac5a85a772bb0fa4e886ce39bad2cfd0`

This is a file-level restoration. Do not reset, force-update, or rewrite branch history. Preserve the later exercise files in the repository.

The restored presentation must contain 101 slides. Do not use `ba57f77` as the baseline; that version already contains the “Role & Task” citation-formatting regression.

## 3. Retire the failed editing method

Do not run or reuse:

- `src/pass05_deck_structure.py`
- `src/pass05_deck_content.py`
- `src/pass05_repairs.py`

The failed pass directly rebuilt `presentation.xml`, duplicated a generic donor slide, inferred shape roles from coordinates, and copied only fragments of styling. That produced correct ordering but inconsistent visual language and dense workbook-like slides.

For this rebuild:

- Do not insert, delete, duplicate, or reorder slides.
- Do not manipulate PowerPoint XML directly.
- Do not locate shapes by approximate coordinates.
- Do not use shape position as a substitute for semantic role.
- Do not use hard-coded temporary paths.
- Do not flatten mixed-format text runs.
- Do not treat “no overflow” as proof that a slide is well designed.

Create one deterministic rebuild source with relative paths. Keep a pristine baseline and write to a separate working copy until validation passes.

## 4. Rebuild only slides 33–44, in place

Repurpose the existing twelve slide positions. The presentation must remain 101 slides, so no page numbers or appendix slides shift.

Use the existing visual system consistently:

- `DIVIDER`: dark navigation treatment.
- `TEACH`: teal teaching treatment.
- `DO`: amber/orange action treatment.
- `REFERENCE`: quiet gray treatment.

A slide’s label, accent, title treatment, and speaker-note mode must agree. Use an existing good slide of the same mode as the visual reference; do not use one generic donor across different modes.

### Slide 33 — Data Analytics Exercise

Mode: `DIVIDER`

Visible copy:

- Title: **Data Analytics Exercise**
- Subtitle: **Upload one Excel workbook, analyze it, add editable charts, and reuse the returned file for a dashboard and presentation.**

No teaching paragraph, revision history, or time chip on the visible slide.

### Slide 34 — Upload the Workbook and Inspect the Data

Mode: `DO`

Visible content:

- Upload `Supplier_Data_Exercise.xlsx`.
- Prompt 1: inspect the workbook; list fields, row count, date range, suppliers and sites, the existing total row, and missing values; then wait for scope confirmation.
- Prompt 2: using confirmed detail rows, compare supplier return rate as total units returned divided by total units shipped; keep defect rate separate; show totals, the missing-data rule, and reconciliation; do not infer causes.

Use two concise prompt cards. Do not show instructor answers or key locations.

### Slide 35 — Follow-Up Analysis: Patterns by Month and Site

Mode: `DO`

Visible prompt:

“Using the same data and conversation, compare return rate by month and site. Identify the clearest increase, decrease, or unusual pattern and show the supporting values. Describe findings only; do not infer a cause. List the additional data needed to investigate.”

### Slide 36 — Add Editable Excel Charts and Return the File

Mode: `DO`

Visible content:

- Add a Summary sheet.
- Add a supplier comparison table and editable native Excel column chart.
- Add a monthly return-rate table and editable native Excel line chart.
- Use formulas, PivotTables, or other traceable Excel logic.
- Reconcile totals and return `Supplier_Data_Analyzed.xlsx`.

Visible verification: **Open the returned workbook and click a chart; its source range must be editable.**

Do not show fallback paths, workbook-tab names, or repository logistics.

### Slide 37 — Describe the Dashboard Behavior

Mode: `TEACH`

Title: **Dashboard Requirements**

Show only the behavior vocabulary:

- Date range
- Supplier and site filters
- Grouping
- Metric selector
- Monthly or quarterly trend
- Drill-down
- Sort
- Reset

Teaching line: **HyperText Markup Language (HTML) structures the page. JavaScript makes the controls work. You only need to describe the behavior.**

### Slide 38 — Build and Test the Dashboard

Mode: `DO`

Use `Supplier_Data_Analyzed.xlsx`, the returned workbook.

The visible instruction must require:

- one self-contained offline HTML file;
- retained detail records;
- controls that update all charts, summary values, and the table together;
- selected period, units, metric definitions, data-snapshot label, reset, and a clear empty-results message;
- one filtered result checked against the workbook.

Do not repeat the answer value on the slide. Put it in the speaker notes and answer key.

### Slide 39 — Create a Five-Slide Management Presentation

Mode: `DO`

Prefill:

- Audience: **Operations leadership**
- Decision: **Where should management focus follow-up?**

Require five slides:

1. Business question and scope
2. Supplier comparison
3. Important trend
4. Recommended follow-up and supporting evidence
5. Limitations and next steps

Require one message per slide, suitable charts, concise visible text, speaker notes, findings separated from recommendations, and no invented causes or commitments.

### Slide 40 — Organize an Email Thread in Outlook

Mode: `TEACH`

Use four clear choices:

- **Catch me up** — summarize the current situation.
- **Show what changed** — list changed dates and decisions.
- **Assign actions** — create a task, owner, due date, status, and dependency table.
- **Prepare my reply** — draft a concise response without inventing commitments.

Footer rule: use only accessible messages and attachments; write “Not stated” for missing information; cite the sender and date.

Do not use “Who owes what.”

### Slide 41 — Email Exercise: Decisions and Actions

Mode: `DO`

Use three visible steps:

1. Run the built-in Outlook summary, or paste `Packaging_Change_Thread.txt`.
2. Choose one prompt from slide 40.
3. Compare the result with the thread.

The result must identify the changed deadline, conditional approval, unresolved question, missing attachment, and messages requiring a reply. Keep the comprehensive audit prompt in the workbook and notes, not as one projected paragraph.

### Slide 42 — Extract Supplier Quotes into Excel

Mode: `DO`

Tell participants to attach the three supplied Portable Document Format (PDF) quotations.

The concise visible instruction must require:

- a Raw Extraction sheet;
- exact source wording;
- commercial values, timing and terms, exclusions, and source file/page;
- “Not stated” for missing information;
- no normalization, ranking, or recommendation.

The full prompt in the notes/workbook must also capture minimum order and warranty. Do not invent “machined component” or “molded component”; all three sources quote `EN-450 anodized aluminum enclosure, per drawing rev. D`.

### Slide 43 — Normalize and Compare the Supplier Quotes

Mode: `DO`

Visible instruction:

- normalize only when the conversion rule or comparison basis is supplied;
- preserve original values;
- show formulas for comparable totals;
- compare non-price terms as well as price;
- list missing information and unresolved scope questions;
- do not name a winner while the basis is incomplete.

The full key must flag Bravo’s unspecified German Institute for Standardization surface requirement and the unresolved drawing-revision/black-anodizing equivalence.

### Slide 44 — Turn Reference Files into a Research Spreadsheet

Mode: `DO`

Prefill the question:

**What should a supplier quality review require, and what cadence should apply?**

Tell participants to attach the four source documents and exclude the README.

For the live slide, use only seven evidence fields:

- Claim or instruction
- Source
- Page or section
- Evidence
- Caveat
- Relevance
- Open question

Use three sheets: Evidence, Synthesis, and Sources. Require one claim per row, file/page traceability, conflicts kept separate, and “Not stated” for gaps. Keep the advanced 13-field schema in the workbook/PDF reference only.

## 5. Separate projected content from supporting detail

Every exercise must still have starting material, full prompt, expected output, verification check, common mistake, and optional extension—but they do not all belong on the slide.

- Slides: the immediate action and shortest usable prompt.
- Speaker notes: facilitation language, timing, full prompt, expected result, verification, common mistake, and extension.
- Workbook/PDF: copy-paste prompts, detailed schemas, answer keys, and reference explanations.
- Prepared outputs: instructor fallback only.

Remove visible repository paths, tab coordinates, fallback filenames, instructor-key language, and revision commentary.

## 6. Visual acceptance criteria

For slides 33–44:

- One dominant message per slide.
- Maximum two content regions or cards.
- No dense paragraph blocks.
- Target body text at 20 points or larger; never below 18 points.
- No visible prompt longer than approximately 120 words.
- No line should wrap awkwardly because a label is too long.
- No unresolved placeholders.
- No answer values on participant slides.
- All acronyms expanded at first use.
- Consistent margins, title position, footer, page number, and mode chip.
- Slides must remain readable in a twelve-slide contact sheet, not merely at full zoom.

## 7. Verification

Before committing:

1. Render all 101 slides.
2. Inspect every rendered slide, not only automated warnings.
3. Produce individual renders and one contact sheet for slides 33–44.
4. Confirm slides 1–32 and 45–101 are visually unchanged from commit `50c729e`.
5. Confirm the presentation has exactly 101 slides.
6. Confirm the mode, accent color, title, and notes agree on slides 33–44.
7. Confirm every target slide has standardized notes: `MODE`, `TIME`, `PURPOSE`, `LAND THIS`, `SAY`, `DO`, `BRIDGE`, and `IF LATE`.
8. Confirm no content or notes mention the former “five task families.”
9. Confirm no participant-facing slide exposes an answer key or prepared fallback.
10. Open the final file in PowerPoint or LibreOffice and manually inspect the twelve rebuilt slides at presentation size.

If any target slide fails a visual check, fix it before reporting. Automated “no overflow” results are necessary but not sufficient.

## 8. Report and stop

Commit the restored-and-rebuilt 101-slide presentation and its deterministic source. Report:

- the commit;
- confirmation that `50c729e` was the baseline;
- the final titles and modes for slides 33–44;
- the contact sheet and individual slide renders;
- font-floor and word-count checks;
- confirmation that non-target slides were unchanged;
- any unresolved issue.

Do not update the PDF or the other artifacts yet. Stop after this presentation checkpoint and await owner review. The next approved iteration will correct the supporting exercise files and synchronize the all-in-one PDF once—after the slide sequence and visual quality are accepted.
