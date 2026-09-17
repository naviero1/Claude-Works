#!/usr/bin/env python3
# Iteration-05: update the facilitation plan to the nine-step application
# sequence (deck slides 33-44), recompute the run timeline, and append the
# two new appendix pages. One-shot pass; asserts fail loudly before writing.
import re
import os

P = os.path.join(os.path.dirname(__file__), '..', 'references',
                 'From_Prompts_to_Agents_Facilitation_Plan.md')
lines = open(P).read().split('\n')
text = '\n'.join(lines)

HEADER = """# From Prompts to Agents: facilitation plan (Iteration 05 — nine-step application sequence)

The full live sequence carries about 72:50 of content for a 60-minute slot,
with an owner-approved flex rule (below) that brings a strict run back to
60:00. The deck has 103 slides: the 70-slide live sequence plus a 33-page
reference appendix (no live allocation). This plan supersedes the Round 17
baseline (archived in notes/intake/round17/); classification follows the
learning contribution.

## Outcomes and sequence

Participants explain ASK versus DELEGATE, write a usable task brief, check a result
against its source, define an approval boundary, and save a reusable prompt. One
fictional supplier dataset connects the Part 4 application block as a nine-step
sequence, and the first rule is set before any prompt: Supplier_Data_Exercise.xlsx
is uploaded once, at the very beginning, and the whole data arc flows from that
single intake — inspect + analyze (slide 34) → follow-up in the same chat (35) →
the assistant returns the workbook with native charts (36) → dashboard (37–38) →
five-slide management mock-up (39). The case then widens on its own sources:
organize the email thread (40–41), extract the supplier quotes (42), compare them
(43), and build the research workbook (44). The plain-language exercise moved to
the reference layer (appendix page 100; workbook tab 5-Explain-Clearly). Workbook
tabs follow the same training order; every prompt is single-sourced from
src/assets/course_prompts.json (deck, workbook, builder, and configurator all
carry the identical text). The requirements lesson (slide 22) precedes prompt
construction; the artifact menus live on reference pages 91–96 and in
references/Requirements_by_Artifact.md.

## Timing

| Mode | Time |
|---|---:|
| DIVIDER | 0:45 |
| TEACH | 22:55 |
| REFERENCE | 4:10 |
| DO | 45:00 |

Full-content total 72:50, including transitions and debriefs. The 60-minute
flex rule (owner-approved): the core that must be presented is the data
analytics arc (slides 33–39) and the email pair (40–41); the quotation pair
(42–43) and the research exercise (44) are extensions that may be skipped or
sent to self-study when time is short (−8:00), with the remaining minutes
recovered by skipping reference orientations and compressing non-anchor
explanation. Protect the exercises first. A two-minute generation delay
triggers the prepared-output fallback (analyzed workbook, dashboard file,
mock deck, sample workbooks) rather than consuming practice time.

## Anchors and protected exercises

Anchors: 21 · 22 · 23 · 28 · 34 · 47 · 50 · 53 · 64.
Protected application: 34 (6:00 upload + inspect + analyze, anchor) · 35 (2:30
follow-up) · 36 (4:00 returned workbook) · 38 (4:00 dashboard build) · 39 (2:30
mock-up) · 41 (3:00 Outlook exercise) · 48 (3:00 discussion) · 51 (3:00 mission
brief) · 56 (2:00 gate + hard check) · 61 (2:00 save one prompt) · 64 (5:00
capstone, anchor). Flex extensions (owner-approved skip when late): 42 (2:30
quote extraction) · 43 (2:30 quote comparison) · 44 (3:00 research workbook)."""

start = text.find('# From Prompts to Agents: facilitation plan')
end = text.find('## Round 17 structural decisions')
assert start == 0 and end > 0
text = HEADER + '\n\n' + text[end:]

# Iteration-05 section after the Round 17 history
corr = '## Correction pass (2026-09-17)'
assert corr in text
IT05 = """## Iteration 05 restructure (2026-09-17)

- The application block became a nine-step, Excel-first sequence on one dataset
  (deck slides 33–44); slide 33 is a divider-styled opener (TEACH 0:40), and the
  old Part 4 divider no longer exists as a separate slide.
- Single intake: participants open only references/exercise-data/
  Supplier_Data_Exercise.xlsx at the start of the block; every data-arc artifact
  (analysis, returned workbook, dashboard, mock-up) flows from that one upload.
- Two live steps were added for the quotation arc (extract 42, compare 43) and
  the research workbook took the final live slot (44); the course-log study aid
  moved to appendix page 102 and the old quotation-extension page to 103 (both
  REFERENCE, no live allocation). Live slide count stays 70; the deck totals 103.
- The plain-language demonstration left the live hour for the reference layer
  (appendix page 100; workbook tab 5-Explain-Clearly), with a fourth practice
  topic (household budgeting) added to the pack.
- Mode totals moved to DIVIDER 0:45 · TEACH 22:55 · REFERENCE 4:10 · DO 45:00
  = 72:50 full content, governed by the 60-minute flex rule above
  (owner-approved: the data arc and the email pair are the protected core).
- Answer keys left the participant-facing slides: they live in the speaker
  notes of the exercise slides and the instructor tabs/keys only.

"""
text = text.replace(corr, IT05 + corr)

lines = text.split('\n')

def row_index(pos):
    for i, ln in enumerate(lines):
        if ln.startswith(f'| {pos} | '):
            return i
    raise AssertionError(f'row {pos} not found')

# ---- replace rows 33..44 ----------------------------------------------------
i33, i44 = row_index(33), row_index(44)
NEW_ROWS = [
 "| 33 | 34 | Data Analytics Exercise | TEACH | 0:40 | 16:20–17:00 |  | COMPRESS | It05: divider-styled opener for the nine-step block — names the single-intake rule (upload Supplier_Data_Exercise.xlsx once) and the arc ahead. |",
 "| 34 | 36 | Upload the Data File and Run These Two Prompts | DO | 6:00 | 17:00–23:00 | Anchor Protected | KEEP | It05: the block anchor — inspect prompt, confirm the profile, then the checked analysis (tab 1-Analyze-Data). Answers live in the speaker notes and KEY-Analysis only. |",
 "| 35 | 37 | Ask a Follow-Up Question | DO | 2:30 | 23:00–25:30 | Protected | KEEP | It05: one follow-up in the same chat — pattern, not cause (tab 1-Analyze-Data). |",
 "| 36 | 35 | Add the Charts and Return the Excel File | DO | 4:00 | 25:30–29:30 | Protected | KEEP | It05: the file contract — Summary sheet, native editable charts, reconciliation (tab Excel-Charts; prepared fallback Supplier_Data_Analyzed.xlsx). |",
 "| 37 | 39 | Describe the Dashboard You Want | TEACH | 1:00 | 29:30–30:30 |  | COMPRESS | It05: behavior in plain language, from the returned workbook — the control vocabulary. |",
 "| 38 | 40 | Build and Test the Dashboard | DO | 4:00 | 30:30–34:30 | Protected | KEEP | It05: input is the returned Supplier_Data_Analyzed.xlsx; live check Berlin × Bravo 2026-03..08 = 8,575 units / 21 returns / 0.245% (the prepared page's footer runs the same self-check; tab 2-Build-Dashboard). |",
 "| 39 | 41 | Turn the Findings into a Five-Slide Management Mock-up | DO | 2:30 | 34:30–37:00 | Protected | KEEP | It05: same verified findings become the decision mock-up (tab 3-Present-Findings; prepared Supplier_Quality_Mock_Presentation.pptx; full version reference page 99). |",
 "| 40 | 42 | Organize an Email Thread in Outlook | TEACH | 1:00 | 37:00–38:00 |  | COMPRESS | It05: choose-the-result menu — five one-sentence jobs; Copilot-in-Outlook workflow with the pasted-text fallback (verified Sep 2026, r28). |",
 "| 41 | 43 | Outlook Exercise: Decisions, Actions, and Open Questions | DO | 3:00 | 38:00–41:00 | Protected | KEEP | It05: the structured brief on the planted-trap thread (tab 4-Summarize-Email; source Packaging_Change_Thread.txt; key in notes + KEY-Email). |",
 "| 42 | new (102-donor) | Extract Supplier Quotes into Excel | DO | 2:30 | 41:00–43:30 | Flex | SKIP | It05: documents → Raw Extraction sheet, verbatim + cited (tab Quote-Extract; three Quote_*.pdf). Owner-approved extension: skippable when late. |",
 "| 43 | new (103-donor) | Normalize and Compare the Supplier Quotes | DO | 2:30 | 43:30–46:00 | Flex | SKIP | It05: normalize only on a stated basis — the sample quotes force an honest \"no winner yet\" (tab Quote-Compare; prepared Quote_Comparison_Workbook.xlsx). Owner-approved extension: skippable when late. |",
 "| 44 | 44 | Turn Reference Files into a Research Spreadsheet | DO | 3:00 | 46:00–49:00 | Flex | SKIP | It05: research-pack/ → Evidence · Synthesis · Sources, conflict kept visible (tab Research; prepared Research_Workbook.xlsx). Owner-approved extension: skippable when late. |",
]
lines[i33:i44 + 1] = NEW_ROWS

# ---- shift rows 45..70 by +12:50 -------------------------------------------
def to_s(t):
    m, s = t.split(':')
    return int(m) * 60 + int(s)

def fmt(sec):
    return f'{sec // 60}:{sec % 60:02d}'

cur = to_s('49:00')
for pos in range(45, 71):
    i = row_index(pos)
    cells = lines[i].split(' | ')
    dur = to_s(cells[4])
    old_win = cells[5]
    assert re.match(r'^\d+:\d\d–\d+:\d\d$', old_win), old_win
    cells[5] = f'{fmt(cur)}–{fmt(cur + dur)}'
    cur += dur
    lines[i] = ' | '.join(cells)
assert cur == to_s('72:50'), fmt(cur)

# ---- appendix rows: window marker + two new rows ---------------------------
out = []
for ln in lines:
    if ln.startswith('|') and ' 60:00–60:00 ' in ln:
        ln = ln.replace(' 60:00–60:00 ', ' 72:50–72:50 ')
    out.append(ln)
lines = out
i101 = row_index(101)
lines[i101 + 1:i101 + 1] = [
 "| 102 | 33 | Optional practice: a course-log study aid | REFERENCE | 0:00 | 72:50–72:50 |  | SKIP | It05: relocated from live position 33 — retained for self-study with no live slot. |",
 "| 103 | 38 | Optional extension: compare supplier quotations | REFERENCE | 0:00 | 72:50–72:50 |  | SKIP | It05: relocated from live position 38 — now the reference companion to the live quotation pair (slides 42–43). |",
]

text = '\n'.join(lines)

# ---- appendix note refreshes ------------------------------------------------
old98 = 'Prompt iterations v1→v3 + the verified filtered check; copy-paste versions in workbook tab 2-Build-Dashboard.'
assert old98 in text
text = text.replace(old98, 'The dashboard exercise in full, on the returned Supplier_Data_Analyzed.xlsx workbook + the verified filtered check; copy-paste versions in workbook tab 2-Build-Dashboard.')
old100 = 'The reusable prompt + three practice topics with sources, samples, and keys.'
assert old100 in text
text = text.replace(old100, 'The reference exercise (no live slot): the reusable prompt + four practice topics with sources, samples, and checks.')

open(P, 'w').write(text)
print('facilitation plan updated: nine-step block, 72:50 timeline, 103 rows')
