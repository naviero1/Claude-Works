#!/usr/bin/env python3
# Iteration-05 exercise assets (owner-approved pass). Builds:
#   references/exercise-data/Supplier_Data_Exercise.xlsx   participant INPUT:
#       the raw Data tab only (incl. the intentional TOTAL row and the one
#       missing Inspection_Hours value). No prompts, keys, or other tabs.
#   references/exercise-data/Supplier_Data_Analyzed.xlsx   prepared fallback
#       for "Add the Charts and Return the Excel File": original Data sheet
#       unchanged + a Summary sheet whose table uses SUMIFS/ratio FORMULAS
#       (traceable, recalculable) + native editable Excel column & line
#       charts + period, definitions, reconciliation and limitations notes.
#   references/exercise-data/Quote_Comparison_Workbook.xlsx prepared fallback
#       for the two quotation steps: Raw Extraction (verbatim values, source
#       file/page, "Not stated" for gaps) + Normalized Comparison (per-currency
#       comparable totals with visible formulas; currencies NOT converted —
#       no conversion basis is supplied — and the missing information that
#       blocks a fair recommendation listed).
#   references/exercise-data/research-pack/                 four small fictional
#       sources + README for the closing research exercise.
#   references/exercise-data/Research_Workbook.xlsx         prepared example:
#       Evidence / Synthesis / Sources sheets per the course prompt.
# All content fictional. Values derived from the same sources that generate
# the quotation PDFs, so extraction is verifiable against them.
import os

import openpyxl
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'references', 'exercise-data')
KEYS = os.path.join(OUT, 'instructor-keys')
os.makedirs(KEYS, exist_ok=True)

TEAL_D = '0A5B5A'
F_HEAD = Font(name='Arial', size=10, bold=True, color='FFFFFF')
FILL_HEAD = PatternFill('solid', fgColor=TEAL_D)
F_TITLE = Font(name='Arial', size=13, bold=True, color=TEAL_D)
F_NOTE = Font(name='Arial', size=9, italic=True, color='7A8790')
WRAP = Alignment(wrap_text=True, vertical='top')

src = openpyxl.load_workbook(os.path.join(HERE, '..', 'deliverables', 'Course_Workbook.xlsx'))
data = src['Data']
ROWS = [[c.value for c in r] for r in data.iter_rows()]
assert len(ROWS) == 146 and ROWS[-1][0] == 'TOTAL', (len(ROWS), ROWS[-1][0])
# The Course_Workbook Data tab renders the one missing Inspection_Hours value
# as the text 'n/a'; the exercise files plant it as a genuinely BLANK cell
# (missing, not zero — and not a string that a naive SUM would silently skip
# for a different reason). Exactly one such cell must exist.
_na = [(ri, 6) for ri, r in enumerate(ROWS) if r[6] == 'n/a']
assert len(_na) == 1, _na
ROWS[_na[0][0]][6] = None

# ---------- 1. Supplier_Data_Exercise.xlsx (data only) ----------------------
wb = openpyxl.Workbook()
ws = wb.active
ws.title = 'Data'
for row in ROWS:
    ws.append(row)
for c in ws[1]:
    c.font = Font(name='Arial', size=10, bold=True)
for i, w in enumerate((10, 11, 17, 13, 14, 13, 15, 13, 14), 1):
    ws.column_dimensions[get_column_letter(i)].width = w
ws.freeze_panes = 'A2'
p_exercise = os.path.join(OUT, 'Supplier_Data_Exercise.xlsx')
wb.save(p_exercise)
print('wrote', p_exercise, f'({ws.max_row - 1} rows incl. TOTAL)')

# ---------- 2. Supplier_Data_Analyzed.xlsx ----------------------------------
wb = openpyxl.Workbook()
ws = wb.active
ws.title = 'Data'
for row in ROWS:
    ws.append(row)
for c in ws[1]:
    c.font = Font(name='Arial', size=10, bold=True)
ws.freeze_panes = 'A2'

sm = wb.create_sheet('Summary')
sm['A1'] = 'SUPPLIER QUALITY — ANALYSIS SUMMARY'
sm['A1'].font = F_TITLE
sm['A2'] = 'Reporting period: 2025-09 to 2026-08 (inclusive) · 144 detail rows; the TOTAL row and the one missing Inspection_Hours value are excluded from calculations.'
sm['A2'].font = F_NOTE
sm['A3'] = 'Definitions: Return rate = SUM(Units_Returned) ÷ SUM(Units_Shipped) per group (sums, never averaged percentages). Defect rate = SUM(Defects_Found) ÷ SUM(Units_Shipped). Defects and returns are separate measures.'
sm['A3'].font = F_NOTE
sm['A3'].alignment = WRAP
sm.row_dimensions[3].height = 26

# supplier comparison table (formulas over detail rows Data!2:145 only)
sm['A5'] = 'Supplier comparison'
sm['A5'].font = Font(name='Arial', size=11, bold=True, color=TEAL_D)
hdr = ['Supplier', 'Units shipped', 'Units returned', 'Return rate', 'Defect rate']
for j, h in enumerate(hdr, 1):
    c = sm.cell(6, j, h)
    c.font = F_HEAD
    c.fill = FILL_HEAD
SUPS = ['Alpha Components', 'Bravo Plastics', 'Cardinal Metals']
for i, s in enumerate(SUPS, 7):
    sm.cell(i, 1, s)
    sm.cell(i, 2, f'=SUMIFS(Data!$D$2:$D$145,Data!$C$2:$C$145,$A{i})')
    sm.cell(i, 3, f'=SUMIFS(Data!$E$2:$E$145,Data!$C$2:$C$145,$A{i})')
    sm.cell(i, 4, f'=C{i}/B{i}')
    sm.cell(i, 5, f'=SUMIFS(Data!$F$2:$F$145,Data!$C$2:$C$145,$A{i})/B{i}')
    sm.cell(i, 4).number_format = '0.000%'
    sm.cell(i, 5).number_format = '0.000%'
    sm.cell(i, 2).number_format = '#,##0'
    sm.cell(i, 3).number_format = '#,##0'
sm.cell(10, 1, 'All suppliers').font = Font(name='Arial', size=10, bold=True)
sm.cell(10, 2, '=SUM(B7:B9)').number_format = '#,##0'
sm.cell(10, 3, '=SUM(C7:C9)').number_format = '#,##0'
sm.cell(10, 4, '=C10/B10').number_format = '0.000%'
sm.cell(10, 5, '=SUMIFS(Data!$F$2:$F$145,Data!$C$2:$C$145,"<>")/B10')
sm.cell(10, 5).number_format = '0.000%'
sm['A11'] = 'Reconciliation: summary units vs the source TOTAL row →'
sm['A11'].font = F_NOTE
sm['B11'] = '=IF(AND(B10=Data!D146,C10=Data!E146),"RECONCILED","MISMATCH — investigate")'
sm['B11'].font = Font(name='Arial', size=9, bold=True, color='3B8560')

# monthly return-rate table (feeds the line chart)
sm['G5'] = 'Return rate by month (all suppliers)'
sm['G5'].font = Font(name='Arial', size=11, bold=True, color=TEAL_D)
sm.cell(6, 7, 'Month').font = F_HEAD
sm.cell(6, 7).fill = FILL_HEAD
sm.cell(6, 8, 'Return rate').font = F_HEAD
sm.cell(6, 8).fill = FILL_HEAD
MONTHS = ['2025-09', '2025-10', '2025-11', '2025-12', '2026-01', '2026-02',
          '2026-03', '2026-04', '2026-05', '2026-06', '2026-07', '2026-08']
for i, m in enumerate(MONTHS, 7):
    sm.cell(i, 7, m)
    sm.cell(i, 8, f'=SUMIFS(Data!$E$2:$E$145,Data!$A$2:$A$145,$G{i})/SUMIFS(Data!$D$2:$D$145,Data!$A$2:$A$145,$G{i})')
    sm.cell(i, 8).number_format = '0.000%'

# native, editable charts referencing the formula cells
bar = BarChart()
bar.type = 'col'
bar.title = 'Return rate by supplier (2025-09 to 2026-08)'
bar.y_axis.numFmt = '0.00%'
bar.y_axis.title = 'Return rate'
bar.add_data(Reference(sm, min_col=4, min_row=6, max_row=9), titles_from_data=True)
bar.set_categories(Reference(sm, min_col=1, min_row=7, max_row=9))
bar.height, bar.width = 8, 14
sm.add_chart(bar, 'A14')

line = LineChart()
line.title = 'Return rate by month (all suppliers)'
line.y_axis.numFmt = '0.00%'
line.y_axis.title = 'Return rate'
line.add_data(Reference(sm, min_col=8, min_row=6, max_row=18), titles_from_data=True)
line.set_categories(Reference(sm, min_col=7, min_row=7, max_row=18))
line.height, line.width = 8, 14
sm.add_chart(line, 'I14')

sm['A31'] = ('Limitations: descriptive comparison only — the data show which supplier has the highest return rate, '
             'not why. Monthly delivery counts are absent, so no true overall on-time delivery rate is computed. '
             'One Inspection_Hours value is missing (missing ≠ zero); it does not affect return-rate math.')
sm['A31'].font = F_NOTE
sm['A31'].alignment = WRAP
sm.merge_cells('A31:H32')
for col, w in zip('ABCDEFGH', (20, 13, 13, 11, 11, 3, 10, 12)):
    sm.column_dimensions[col].width = w

p_analyzed = os.path.join(OUT, 'Supplier_Data_Analyzed.xlsx')
wb.save(p_analyzed)
print('wrote', p_analyzed, '(Data unchanged + Summary: SUMIFS table, monthly table, native bar+line charts)')

# ---------- 3. Quote_Comparison_Workbook.xlsx -------------------------------
wb = openpyxl.Workbook()
rx = wb.active
rx.title = 'Raw Extraction'
COLS = ['Supplier', 'Quoted scope', 'Currency', 'Quoted quantity basis', 'Unit price (as stated)',
        'Tooling / one-time', 'Freight', 'Taxes', 'Lead time', 'Payment terms', 'Quote validity',
        'Exclusions / notes', 'Source file', 'Source page', 'Missing information']
for j, h in enumerate(COLS, 1):
    c = rx.cell(1, j, h)
    c.font = F_HEAD
    c.fill = FILL_HEAD
    c.alignment = WRAP
QUOTES = [
    ['Alpha Components Inc.', 'Machined component, standard black anodizing included', 'USD',
     'Tiered: 5,000 pcs and 10,000 pcs',
     'USD 13.90 / unit at 5,000 pcs · USD 12.60 / unit at 10,000 pcs',
     'USD 8,500 one-time (3 weeks)', 'FOB Austin — buyer arranges freight; amount Not stated',
     'Not stated', '4 weeks after tooling approval', 'Net 30', '60 days',
     'Expedite program available (+8%, lead time 2 weeks)',
     'Quote_Alpha_Components.pdf', '1', 'Freight cost; tax treatment'],
    ['Bravo Plastics GmbH', 'Molded component, surface per DIN standard', 'EUR',
     'Per 1,000 units; tiers at 5,000 and 10,000 units',
     'EUR 11,900 per 1,000 units (5,000-unit tier) · EUR 10,950 per 1,000 units (10,000-unit tier)',
     'EUR 14,000 — not included in the prices above',
     'EXW Hamburg — buyer collects; freight and import duties not included; amounts Not stated',
     'Prices exclude VAT', '9 weeks including tooling', 'Net 60', '30 days',
     'Color matching on request; quoted in euros',
     'Quote_Bravo_Plastics.pdf', '1', 'Freight and duty costs; EUR→USD conversion basis'],
    ['Cardinal Metals Ltd.', 'Machined component incl. lot-level material certs and PPAP level 3', 'USD',
     'Tiered: 5,000 pcs and 10,000 pcs',
     'USD 16.40 / unit at 5,000 pcs · USD 15.20 / unit at 10,000 pcs',
     'Waived for orders of 5,000 units or more', 'DDP your dock — freight and duties included',
     'Not stated', '6 weeks, all-in', 'Net 45', '90 days',
     '24-month warranty including anodizing defects',
     'Quote_Cardinal_Metals.pdf', '1', 'None material — most complete quote'],
]
for i, row in enumerate(QUOTES, 2):
    for j, v in enumerate(row, 1):
        c = rx.cell(i, j, v)
        c.alignment = WRAP
    rx.row_dimensions[i].height = 64
for j, w in enumerate((20, 26, 8, 20, 34, 22, 30, 14, 16, 11, 11, 26, 24, 7, 26), 1):
    rx.column_dimensions[get_column_letter(j)].width = w
rx.freeze_panes = 'A2'
rx.auto_filter.ref = f'A1:{get_column_letter(len(COLS))}{len(QUOTES) + 1}'

nc = wb.create_sheet('Normalized Comparison')
nc['A1'] = 'NORMALIZED COMPARISON — at the 5,000-unit tier'
nc['A1'].font = F_TITLE
nc['A2'] = ('Currencies are NOT converted: no EUR→USD conversion rule or basis is supplied with the quotes, '
            'so Bravo is compared in EUR and flagged. Original extracted values stay visible on the Raw Extraction sheet.')
nc['A2'].font = F_NOTE
nc['A2'].alignment = WRAP
nc.merge_cells('A2:G3')
hdr = ['Supplier', 'Currency', 'Unit price @5,000', 'Tooling amortized / unit (÷5,000)',
       'Comparable unit total (price + tooling)', 'Freight in total?', 'Scope differences to weigh']
for j, h in enumerate(hdr, 1):
    c = nc.cell(5, j, h)
    c.font = F_HEAD
    c.fill = FILL_HEAD
    c.alignment = WRAP
rows = [
    ['Alpha Components Inc.', 'USD', 13.90, '=8500/5000', '=C6+D6', 'No — FOB, freight Not stated',
     'Anodizing included; 12-month warranty; expedite option'],
    ['Bravo Plastics GmbH', 'EUR', '=11900/1000', '=14000/5000', '=C7+D7', 'No — EXW, freight and duties Not stated',
     'Shortest warranty (6 months); VAT excluded; 5,000 MOQ'],
    ['Cardinal Metals Ltd.', 'USD', 16.40, 0, '=C8+D8', 'Yes — DDP, freight and duties included',
     'Certs + PPAP included; 24-month warranty; tooling waived'],
]
for i, row in enumerate(rows, 6):
    for j, v in enumerate(row, 1):
        c = nc.cell(i, j, v)
        c.alignment = WRAP
        if j in (3, 4, 5):
            c.number_format = '0.00'
    nc.row_dimensions[i].height = 40
nc['A10'] = ('No best quote is identified: the comparison basis is incomplete. Blocking gaps — '
             '1) EUR→USD conversion basis for Bravo; 2) freight (and, for Bravo, import duty) cost to destination '
             'for Alpha and Bravo; 3) tax treatment for Alpha and Cardinal. Resolve these, then compare '
             'like-for-like landed cost alongside warranty, lead time, and payment terms.')
nc['A10'].font = F_NOTE
nc['A10'].alignment = WRAP
nc.merge_cells('A10:G12')
for j, w in enumerate((20, 9, 16, 18, 20, 24, 34), 1):
    nc.column_dimensions[get_column_letter(j)].width = w

p_quote = os.path.join(OUT, 'Quote_Comparison_Workbook.xlsx')
wb.save(p_quote)
print('wrote', p_quote)

# ---------- 4. research pack + Research_Workbook.xlsx -----------------------
RP = os.path.join(OUT, 'research-pack')
os.makedirs(RP, exist_ok=True)
packs = {
'README.md': """# Research pack (fictional) — the closing exercise

Research question: **What should a quarterly supplier quality review require?**

Four short fictional sources, deliberately imperfect: they overlap, one pair
conflicts on review frequency, and several details are simply not stated.
Feed them to the research-workbook prompt (workbook tab Research); the
prepared example is Research_Workbook.xlsx and the key is
instructor-keys/Research_Workbook_Key.md. All organizations and documents are
fictional training material.
""",
'src1_quality_manual_excerpt.md': """# Source 1 — Supplier Quality Manual, section 7 (excerpt)
Fictional Manufacturing Co. · Rev C · dated 2026-02-10 · pages 12-13

7.1 Each approved supplier shall be reviewed **quarterly**. The review shall
cover: delivered quality (return rate computed as total units returned divided
by total units shipped in the period), inspection findings (defects found at
incoming inspection, reported separately from returns), on-time performance,
and the status of open corrective actions.

7.2 Return rate and defect rate shall never be added together: they measure
different failure points (escaped versus caught).

7.3 A supplier whose return rate exceeds twice the site average for two
consecutive reviews shall be placed on a corrective-action plan with a named
owner and a re-measurement date. The plan format is defined in section 9.

7.4 Data used in the review must reconcile to the receiving system's period
totals before the meeting. Unreconciled figures shall not be presented.
""",
'src2_quality_newsletter.md': """# Source 2 — Plant quality newsletter (excerpt)
Fictional Manufacturing Co. · issue 2026-06 · page 2

"Since January the supplier board reviews scores **monthly** — the quarterly
cycle hid slow drifts for up to ninety days," writes the plant quality lead.
The newsletter credits the shorter cycle with catching one supplier's packaging
issue two months earlier than the previous cadence would have.

It also reminds readers that a review pack "is a decision document, not a data
dump": one page per supplier, the trend chart first, and a recommendation the
plant manager can approve or reject in the meeting.

The newsletter does not say whether the monthly cadence applies to every
supplier or only to those already on a corrective-action plan.
""",
'src3_scorecard_guideline.txt': """Source 3 - Supplier scorecard guideline (one-page internal aid)
Fictional Manufacturing Co. - undated

- Score each supplier on four measures: return rate, defect rate, on-time
  percent, and responsiveness to corrective actions.
- Weight by units shipped when combining periods; never average monthly
  percentages.
- Show numerator and denominator next to every rate.
- Missing data is shown as missing, never as zero.
- The scorecard states the reporting period and the data source on its face.
- Responsiveness is scored from corrective-action closure dates; the guideline
  does not define the scale.
""",
}
for fn, txt in packs.items():
    open(os.path.join(RP, fn), 'w').write(txt)

# source 4 as a small PDF (so the pack mixes formats)
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
S_t = ParagraphStyle('t', fontName='Helvetica-Bold', fontSize=13, leading=16)
S_b = ParagraphStyle('b', fontName='Helvetica', fontSize=9.5, leading=13)
doc = SimpleDocTemplate(os.path.join(RP, 'src4_8d_onepager.pdf'), pagesize=LETTER,
                        topMargin=0.8 * inch, bottomMargin=0.8 * inch)
doc.build([
    Paragraph('Source 4 — Eight-Discipline (8D) problem solving, one-pager (fictional)', S_t),
    Spacer(1, 8),
    Paragraph('Fictional Manufacturing Co. · training aid · dated 2025-11-03 · page 1', S_b),
    Spacer(1, 8),
    Paragraph('When a supplier issue is confirmed, open an 8D: D1 team · D2 problem description with '
              'the data behind it (period, numerator, denominator) · D3 containment · D4 root cause '
              '· D5-D6 corrective action chosen and implemented · D7 prevention · D8 closure with '
              're-measurement. A supplier review that raises an issue without opening a numbered 8D, '
              'or closes one without re-measurement, is incomplete.', S_b),
    Spacer(1, 8),
    Paragraph('The one-pager does not state who may close an 8D, and gives no target closure time.', S_b),
])

# prepared Research_Workbook.xlsx
wb = openpyxl.Workbook()
ev = wb.active
ev.title = 'Evidence'
EC = ['ID', 'Topic', 'Claim or instruction', 'Source file', 'Author / organization', 'Date',
      'Page or section', 'Supporting excerpt (short)', 'Plain-language interpretation',
      'Caveat / limitation', 'Relevance to the research question', 'Confidence / status', 'Open question']
for j, h in enumerate(EC, 1):
    c = ev.cell(1, j, h)
    c.font = F_HEAD
    c.fill = FILL_HEAD
    c.alignment = WRAP
EV = [
    ['E1', 'Cadence', 'Approved suppliers reviewed quarterly', 'src1_quality_manual_excerpt.md',
     'Fictional Manufacturing Co. (quality manual)', '2026-02-10', '§7.1',
     '"Each approved supplier shall be reviewed quarterly."', 'The formal standard is a quarterly review.',
     'Conflicts with Source 2', 'Sets the required cadence', 'Stated policy', 'Which document governs today?'],
    ['E2', 'Cadence', 'Supplier board reviews scores monthly since January', 'src2_quality_newsletter.md',
     'Fictional Manufacturing Co. (newsletter)', '2026-06', 'p.2',
     '"the supplier board reviews scores monthly"', 'Practice moved to monthly reviews in 2026.',
     'Scope unclear: all suppliers or only those on plans — Not stated', 'Conflicts with E1; newer date',
     'Reported practice', 'Does monthly apply to all suppliers?'],
    ['E3', 'Metrics', 'Review covers return rate, inspection findings, on-time, open corrective actions',
     'src1_quality_manual_excerpt.md', 'Fictional Manufacturing Co. (quality manual)', '2026-02-10', '§7.1',
     '"delivered quality … inspection findings … on-time performance … corrective actions"',
     'Four content areas are mandatory.', '', 'Defines required content', 'Stated policy', ''],
    ['E4', 'Metrics', 'Return rate and defect rate are never added together', 'src1_quality_manual_excerpt.md',
     'Fictional Manufacturing Co. (quality manual)', '2026-02-10', '§7.2',
     '"shall never be added together"', 'Escaped and caught failures are separate measures.',
     '', 'Metric definition rule', 'Stated policy', ''],
    ['E5', 'Method', 'Weight by units shipped; never average monthly percentages', 'src3_scorecard_guideline.txt',
     'Fictional Manufacturing Co. (guideline)', 'Not stated', 'bullet 2',
     '"never average monthly percentages"', 'Rates come from sums, not averaged percentages.',
     'Document is undated', 'Calculation method', 'Stated guideline', ''],
    ['E6', 'Method', 'Show numerator and denominator next to every rate', 'src3_scorecard_guideline.txt',
     'Fictional Manufacturing Co. (guideline)', 'Not stated', 'bullet 3',
     '"Show numerator and denominator"', 'Every rate is traceable on its face.', '', 'Presentation rule',
     'Stated guideline', ''],
    ['E7', 'Method', 'Missing data shown as missing, never as zero', 'src3_scorecard_guideline.txt',
     'Fictional Manufacturing Co. (guideline)', 'Not stated', 'bullet 4', '"never as zero"',
     'Blanks are disclosed, not zero-filled.', '', 'Data-handling rule', 'Stated guideline', ''],
    ['E8', 'Escalation', 'Return rate > 2× site average for two consecutive reviews → corrective-action plan',
     'src1_quality_manual_excerpt.md', 'Fictional Manufacturing Co. (quality manual)', '2026-02-10', '§7.3',
     '"exceeds twice the site average for two consecutive reviews"', 'A numeric escalation trigger exists.',
     'Plan format lives in a section not supplied (§9)', 'Escalation criterion', 'Stated policy',
     'What does section 9 require?'],
    ['E9', 'Escalation', 'Issues raised must open a numbered 8D; closure needs re-measurement',
     'src4_8d_onepager.pdf', 'Fictional Manufacturing Co. (training aid)', '2025-11-03', 'p.1',
     '"raises an issue without opening a numbered 8D … is incomplete"',
     'Every raised issue becomes a tracked 8D with re-measurement.', 'No closure authority or target time stated',
     'Links reviews to problem-solving', 'Stated training aid', 'Who may close an 8D, and by when?'],
    ['E10', 'Data quality', 'Figures must reconcile to period totals before the meeting',
     'src1_quality_manual_excerpt.md', 'Fictional Manufacturing Co. (quality manual)', '2026-02-10', '§7.4',
     '"Unreconciled figures shall not be presented."', 'Reconciliation is a gate for the meeting.',
     '', 'Data-quality gate', 'Stated policy', ''],
    ['E11', 'Format', 'One page per supplier; trend first; end on an approvable recommendation',
     'src2_quality_newsletter.md', 'Fictional Manufacturing Co. (newsletter)', '2026-06', 'p.2',
     '"a decision document, not a data dump"', 'The review pack is built for a decision.',
     'Editorial guidance, not policy', 'Format guidance', 'Reported practice', ''],
    ['E12', 'Scoring', 'Responsiveness scored from corrective-action closure dates; scale undefined',
     'src3_scorecard_guideline.txt', 'Fictional Manufacturing Co. (guideline)', 'Not stated', 'bullet 6',
     '"does not define the scale"', 'A fourth measure exists but is under-specified.',
     'Scale Not stated', 'Gap to resolve', 'Stated guideline', 'What scale applies?'],
]
for i, row in enumerate(EV, 2):
    for j, v in enumerate(row, 1):
        c = ev.cell(i, j, v)
        c.alignment = WRAP
    ev.row_dimensions[i].height = 52
for j, w in enumerate((5, 11, 34, 26, 26, 12, 11, 32, 30, 24, 22, 14, 24), 1):
    ev.column_dimensions[get_column_letter(j)].width = w
ev.freeze_panes = 'A2'
ev.auto_filter.ref = f'A1:{get_column_letter(len(EC))}{len(EV) + 1}'

sy = wb.create_sheet('Synthesis')
sy['A1'] = 'SYNTHESIS — from foundations to implications'
sy['A1'].font = F_TITLE
SY = [
    ('Foundations (agreed across sources)',
     'Reviews are periodic and data-gated: figures reconcile before the meeting (E10); rates come from sums with visible '
     'numerator/denominator (E5, E6); returns and defects stay separate (E4); missing data stays visible (E7).'),
    ('Required content (agreed)',
     'Delivered quality, inspection findings, on-time performance, and open corrective actions (E3), presented as a '
     'one-page decision document per supplier (E11).'),
    ('Escalation (agreed, with gaps)',
     'A numeric trigger exists (E8) and every raised issue opens a tracked 8D closed only with re-measurement (E9).'),
    ('CONFLICT to resolve',
     'Cadence: the manual requires quarterly (E1, dated 2026-02) but the newsletter reports monthly practice since '
     'January 2026 (E2, dated 2026-06). The newer source describes practice, the older one policy — the review '
     'requirement cannot cite both. Decision needed: update §7.1 or scope the monthly cadence.'),
    ('GAPS (open questions)',
     'Whether monthly applies to all suppliers (E2) · section 9 plan format not supplied (E8) · 8D closure authority '
     'and target time (E9) · responsiveness scale (E12).'),
    ('Implication for the research question',
     'A quarterly (or resolved-cadence) review should require: reconciled sums-based rates with visible numerators, '
     'the four content areas, separate return/defect measures, disclosed gaps, the escalation trigger, and a tracked '
     '8D for every raised issue — closing only on re-measurement.'),
]
r = 3
for head, body in SY:
    sy.cell(r, 1, head).font = Font(name='Arial', size=10, bold=True, color=TEAL_D)
    c = sy.cell(r + 1, 1, body)
    c.alignment = WRAP
    sy.merge_cells(start_row=r + 1, start_column=1, end_row=r + 1, end_column=8)
    sy.row_dimensions[r + 1].height = 44
    r += 3
sy.column_dimensions['A'].width = 110

so = wb.create_sheet('Sources')
for j, h in enumerate(['File', 'Type', 'Author / organization', 'Date', 'What it is'], 1):
    c = so.cell(1, j, h)
    c.font = F_HEAD
    c.fill = FILL_HEAD
SO = [
    ['src1_quality_manual_excerpt.md', 'Policy excerpt', 'Fictional Manufacturing Co.', '2026-02-10',
     'Supplier Quality Manual §7 — review cadence, content, escalation, reconciliation gate'],
    ['src2_quality_newsletter.md', 'Newsletter', 'Fictional Manufacturing Co.', '2026-06',
     'Reported monthly-review practice + decision-document format guidance'],
    ['src3_scorecard_guideline.txt', 'Guideline', 'Fictional Manufacturing Co.', 'Not stated',
     'Scorecard measures and calculation/presentation rules'],
    ['src4_8d_onepager.pdf', 'Training aid', 'Fictional Manufacturing Co.', '2025-11-03',
     '8D problem-solving structure linked to supplier reviews'],
]
for i, row in enumerate(SO, 2):
    for j, v in enumerate(row, 1):
        so.cell(i, j, v).alignment = WRAP
for j, w in enumerate((30, 13, 24, 12, 70), 1):
    so.column_dimensions[get_column_letter(j)].width = w
so.freeze_panes = 'A2'

p_research = os.path.join(OUT, 'Research_Workbook.xlsx')
wb.save(p_research)
print('wrote', p_research, 'and research-pack/ (4 sources + README)')

# ---------- keys ------------------------------------------------------------
open(os.path.join(KEYS, 'Quote_Comparison_Key.md'), 'w').write("""# Instructor key — quotation extraction and comparison

Step 1 (extraction) is complete when every commercial value is verbatim,
cited to its source file, and gaps read "Not stated" — notably: Alpha freight
amount and taxes; Bravo freight, duties, and the EUR→USD basis; Cardinal taxes.

Step 2 (comparison) at the 5,000-unit tier, tooling amortized over 5,000:
- Alpha: USD 13.90 + 8,500/5,000 = **USD 15.60 / unit**, freight NOT included.
- Bravo: EUR 11,900/1,000 + 14,000/5,000 = **EUR 14.70 / unit**, freight and
  duties NOT included, VAT excluded — NOT convertible without a supplied rate.
- Cardinal: USD 16.40 + 0 = **USD 16.40 / unit**, freight and duties INCLUDED
  (DDP), certs + PPAP included, longest warranty and validity.

The correct conclusion is that NO best quote can be named yet: the blocking
gaps are the EUR→USD basis, Alpha/Bravo freight (and Bravo duties), and tax
treatment. A submission that crowns a winner without resolving these fails
the exercise; one that ranks by stated unit price alone falls for the trap.
""")
open(os.path.join(KEYS, 'Research_Workbook_Key.md'), 'w').write("""# Instructor key — research workbook

Traceability: every Evidence row cites file + page/section and quotes a short
excerpt; nothing appears that cannot be traced (12 expected rows, ±2).

Must-catch items:
1. The CADENCE CONFLICT — manual quarterly (2026-02) vs newsletter monthly
   (2026-06). Kept as two rows, surfaced in Synthesis as a decision, never
   silently merged.
2. "Not stated" entries — undated guideline; responsiveness scale; 8D closure
   authority and target time; monthly-cadence scope; §9 plan format.
3. Separate-measures and sums-not-averages rules carried into the synthesis.
4. Synthesis ordered foundations → content → escalation → conflict → gaps →
   implication; Sources sheet indexes all four files.

A workbook that invents a fifth source, fills gaps with guesses, or resolves
the cadence conflict by picking one side without flagging it fails the check.
""")
print('wrote instructor keys (quotes, research)')
