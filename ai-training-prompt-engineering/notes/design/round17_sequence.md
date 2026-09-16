# Round 17 — Revised instructional sequence (design record)

Owner direction (notes/intake/round17/Package_Instructions.md): the training determines
the exercises; the exercises determine the reusable prompts; the builder supports those
prompts. Baseline = the uploaded 96-slide facilitated 60-minute deck (70 live + 26
reference), NOT the 69-slide long-format deck (which remains in the repo as the source
of the reference layer). Part 4 = "Putting Prompts to Work". ASK vs DELEGATE, the
speaker-note fields (MODE/TIME/PURPOSE/LAND THIS/SAY/DO/BRIDGE/IF LATE), and the
TEACH/DO/REFERENCE/DIVIDER visual system are preserved.

## The connected case

One business question carried through five artifacts, all on the same fictional
supplier dataset (Course_Workbook.xlsx, seeded — data is stable across rebuilds):

> **Which supplier has the highest return rate, and what should we investigate next?**
> Return rate = total Units_Returned ÷ total Units_Shipped within the same scope.
> Never an average of row percentages. Defects and returns stay separate measures.

Verified case facts (independently recomputed 2026-09-16, pandas/openpyxl):
144 detail rows + 1 TOTAL row · shipped 224,902 · returns 432 · defects 2,207 ·
Alpha 75,060 / 74 / 0.099% · Bravo 75,184 / 262 / 0.349% · Cardinal 74,658 / 96 /
0.129% · one missing Inspection_Hours ("n/a" ≠ 0) · period 2025-09..2026-08 ·
grain = month × site × supplier · no delivery counts → monthly On_Time_Percent
averages are NOT an overall delivery rate.

Sequence: **1 Analyze** (live exercises) → **2 Dashboard** (live demonstration, same
cleaned data) → **3 Present** (self-study demonstration, same verified findings) →
**4 Email** (live exercise, packaging thread) → **5 Explain clearly** (short live
demonstration). Full-length practice versions of 2, 3, 5 live in the reference layer
and the workbook — five complete workshops do NOT fit in 30 minutes and are not
pretended to.

## Slide architecture changes (edits in place; additions appended → live numbering stable)

| Slide | Was | Becomes |
|---|---|---|
| 34 | Part 4 divider | Same; subtitle names the connected case. |
| 35 | A data-analysis brief (TEACH 1:00) | "One question, one improving prompt" — starter prompt → three weaknesses → improved prompt with requirement types named; announces the five-artifact arc. |
| 36 | Exercise: inspect (DO 3:00) | Kept; names the file + Data tab. |
| 37 | Exercise: compare + check (DO·anchor 5:00) | Kept; already carries the verified numbers. |
| 38 | Optional quotations ext. (REF 0:10) | Kept, corrected: the three Quote_*.pdf files ARE in this package (+ workbook tab EX-Quotes) — usable now, with its key noted as workbook-based. |
| 39 | Artifact requirements (TEACH 0:45) | Kept; names the five artifacts of the case. |
| 40 | Dashboard demo (DO 4:00) | Connected to the supplier case: prepared Supplier_Quality_Dashboard.html from Data_Clean, behavior vocabulary, one filtered total verified live. |
| 41 | Email TEACH 0:30 | Kept. |
| 42 | Email exercise (DO 3:00) | Kept; points at the standalone thread file + workbook tab; reusable prompt in workbook/appendix. |
| 43 | "Pick what we drill next" (REF 0:10) | "Self-study demonstration: present the findings" — five-slide mock presentation prompt + prepared Supplier_Quality_Mock_Presentation.pptx. Old content preserved on a new appendix page. |
| 44 | Reference recap (REF 0:10, stale block framing) | **DO 2:00 "Demonstration: explain it clearly"** — the plain-language reusable prompt run on one topic; samples + variations in the pack. Old recap content already archived in its source notes; stale previous-session framing resolved. |

Appendix additions (appended after 96; zero live allocation; REFERENCE styling):
97 "More plays we can drill next" (relocated old slide 43 content) ·
98 Full exercise: build the supplier dashboard (prompt iterations v1→v3 + checks) ·
99 Full exercise: the five-slide mock presentation (refined prompt + checklist) ·
100 Full exercise: plain-language documents (prompt + three topic variations + keys) ·
101 The email reusable prompt, in full (+ Copilot/Outlook access dependency note).

## Timing rebalance (total stays 60:00)

Slide 44 REF 0:10 → DO 2:00 (+1:50 DO, −0:10 REF). Compensating TEACH compressions
(non-anchor first, per the plan's own if-late ladder): S2 0:45→0:35 · S7 1:25→1:00 ·
S9 1:00→0:50 · S10 1:00→0:50 · S14 1:00→0:50 · S29 0:45→0:30 · S46 1:00→0:45 ·
S58 0:45→0:40 · S60 0:45→0:40. Net −1:40 TEACH… plus S19 0:50→0:45 and S63
0:30→0:25 → −1:50. New totals: DIVIDER 0:50 · TEACH 22:30 · REFERENCE 4:40 ·
DO 32:00 · **60:00**. Application ≥ 30:00 protected; foundations ≈ 28:00.

## Exercise → prompt → builder mapping

Each exercise's improved prompt is the reusable prompt; the builder's five task
families expose exactly those prompts' requirement types (from
Requirements_by_Artifact.md):

| Task family (builder + configurator + workbook tab) | Reusable prompt source | Key requirement types surfaced |
|---|---|---|
| Analyze spreadsheet data (1-Analyze-Data) | improved supplier prompt | source scope · row grain · period · metric definition · denominators · missing data · reconciliation · limitations |
| Build an interactive dashboard (2-Build-Dashboard) | dashboard v3 prompt | input contract · date range · category controls · grouping · metric selection · coordinated views · states · reset · delivery |
| Prepare a presentation (3-Present-Findings) | mock-deck prompt | purpose/audience · scope/slide count · story · message hierarchy · data fidelity · chart semantics · notes · editability |
| Summarize an email conversation (4-Summarize-Email) | packaging-thread prompt | source scope · current state · decisions/conditions · actions/ownership · date meaning · evidence · attachments · authority |
| Explain a topic clearly (5-Explain-Clearly) | fifth-grade prompt | reader/purpose · vocabulary · structure · examples/analogies · fidelity/caveats · comprehension check · tone |

Legacy G1–G8/A1–A5 templates: optional reference at the end (prompt-library/ retained;
G-number navigation removed from the live sequence and demoted in the tools).

## Package rules carried through

No company data (all fictional; footers say so) · every currency-sensitive claim dated ·
participant materials separated from instructor keys (KEY-* tabs; appendix marked) ·
prepared-output fallback for every live generation step (dashboard file, mock deck,
sample outputs) · verification = meets written criteria; validation = serves the need.
