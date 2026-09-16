# From Prompts to Agents — package index (Round 17)

What to open, in order. Participant materials first; instructor-only material is
marked. Everything fictional; no real company data anywhere.

## 1 · The course

| File | What it is |
|---|---|
| **From_Prompts_to_Agents_Facilitated_60_Minute.pptx** | The course: 70-slide live sequence (60:00 — 30 min foundations, 32 min protected application) + reference appendix (pages 71–101, no live time). Speaker notes on every slide: MODE / TIME / PURPOSE / LAND THIS / SAY / DO / BRIDGE / IF LATE. |
| **From_Prompts_to_Agents_Facilitation_Plan.md** | Instructor run plan: timing, anchors, protected exercises, slide-by-slide audit. *(Instructor)* |

## 2 · The workbook and exercise sources

| File | What it is |
|---|---|
| **exercise-data/Course_Workbook.xlsx** | Open its INDEX tab first. Data (raw, with the deliberate TOTAL row + "n/a" quirks) · Data_Clean (the checked 144-row detail set) · tabs **1-Analyze-Data … 5-Explain-Clearly** (the five course tasks: starter → improved prompts, requirement annotations, self-checks) · KEY-Analysis / KEY-Email *(instructor)* · legacy long-course tabs (optional). |
| exercise-data/Supplier_Data_Clean.csv | The cleaned detail records (for the dashboard task). |
| exercise-data/Packaging_Change_Thread.txt | The fictional email thread (task 4), copy-paste ready. |
| exercise-data/plain-language/ | Task 5: reusable prompt + three topics (source, sample output, key each). |
| exercise-data/Quote_*.pdf | Optional extension: three deliberately non-comparable quotations. |
| exercise-data/instructor-keys/ | Expected email brief and traps. *(Instructor)* |

## 3 · Prepared outputs (the fallbacks for every live generation)

| File | What it is |
|---|---|
| **exercise-data/Supplier_Quality_Dashboard.html** | Working offline dashboard from Data_Clean — month range, supplier/site filters, compare-by, granularity, metric selector, drill-down, sort, Reset; footer runs a visible self-check (Berlin × Bravo, 2026-03..08 → 8,575 / 21 / 0.245%). A static snapshot, not a live system. |
| **exercise-data/Supplier_Quality_Mock_Presentation.pptx** | The five-slide mock management deck produced by the task-3 prompt — every number traced to the workbook; findings separated from recommendations. |

## 4 · The tools (follow the training; never required by it)

| File | What it is |
|---|---|
| **Prompt_Template_Creator.html** | Task-first builder: pick one of the five task families → its requirement menu with acceptance checks → editable assembled prompt (manual edits survive selection changes; no "ready" while the task is empty). Advanced button opens the full legacy taxonomy + 18 templates. Works offline. |
| **Prompt_Template_Configurator.xlsx** | The same five task families on the Tasks sheet (Yes/No rows + assembled-prompt formula); element-level builder sheets remain as advanced. |

## 5 · Reference

| File | What it is |
|---|---|
| **Prompt_Anatomy_Cheat_Sheet.pdf** | One page: the requirement skeleton, the 14-type menu, quality bar, before/after supplier example, acceptance checks, ASK vs DELEGATE. |
| **Elements_of_Prompting_Field_Guide.pdf** | 20 pp: requirement quality · the elements as requirement types · menus by artifact · the five exercises worked (reusable prompts + checks) · troubleshooting · the evidence compendium. |
| **Prompt_Element_Taxonomy_Reference.pdf** | The full ontology, with the elements-to-requirement-types mapping up front; legacy template codes optional. |
| **../Requirements_by_Artifact.md** | The shared requirements catalog (source for the tools' menus; maintenance map inside). |

## Editable sources

Everything regenerates from `src/` (see the repo README): the workbook/pack
(`build_exercise_pack.py`), dashboard (`build_dashboard.py`), mock deck
(`build_mock_deck.js`), cheat sheet, field guide, taxonomy PDF, builder, and
configurator each have a build script; the 60-minute deck is maintained as a
.pptx (edit script preserved in `src/round17_deck_content_pass.py`; pristine
baseline in `notes/intake/round17/`).
