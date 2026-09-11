# Builds the v1.6 hands-on exercise pack (all data fictional, generated, generic):
#   deliverables/exercise-data/Course_Workbook.xlsx           README + Data (raw, NO formulas - the AI
#                                                             does the math) + one named tab per exercise
#                                                             (EX1..EX8, G2-DataAnalysis, EX-Quotes,
#                                                             EX-Email, EX-Report) + PLAYBOOK (8+8+8)
#   deliverables/exercise-data/Quote_Alpha_Components.pdf     (three comparable supplier quotations,
#   deliverables/exercise-data/Quote_Bravo_Plastics.pdf        deliberately non-comparable at first
#   deliverables/exercise-data/Quote_Cardinal_Metals.pdf       glance: currency/per-1000/EXW traps)
#   deliverables/exercise-data/Email_Thread_Packaging_Change.txt / .pdf  (messy 10-message thread)
#   deliverables/exercise-data/Playbook_One_Pager.pdf         (Do / Don't / Expired on one page)
# Deterministic (seeded) so the numbers on the walkthrough slides stay true after a rebuild.
# Prompt texts in the tabs MUST match the deck (R10/R11) - edit deck_pt*.js and this file together.
import os
import random
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

OUT = os.path.join(os.path.dirname(__file__), '..', 'deliverables', 'exercise-data')
os.makedirs(OUT, exist_ok=True)
random.seed(42)

TEAL, INK, MUTE = HexColor('#0E7C7B'), HexColor('#232A31'), HexColor('#7A8790')

# ---------------------------------------------------------------- 1. XLSX dataset
MONTHS = ['2025-09', '2025-10', '2025-11', '2025-12', '2026-01', '2026-02',
          '2026-03', '2026-04', '2026-05', '2026-06', '2026-07', '2026-08']
SITES = {'Austin': (5200, 92, 3, 1.00), 'Berlin': (4300, 94, 2, 0.95),
         'Osaka': (6100, 97, 2, 0.85), 'Monterrey': (3600, 88, 4, 1.15)}
SUPS = {'Alpha Components': (0.008, 0.000, 12.40), 'Bravo Plastics': (0.016, 0.0008, 9.80),
        'Cardinal Metals': (0.010, 0.000, 14.10)}

wb = Workbook()
rd = wb.active
rd.title = 'README'
readme = [
    ['Course Workbook — "From Prompts to Agents" training'],
    [''],
    ['WHAT THIS IS', 'Your one take-home workbook: every exercise prompt from the course in a named tab (copy-paste, don\'t retype), the practice dataset for the Part 4 data walkthrough, and the full 2026 prompting playbook.'],
    ['HOW TO USE IT', 'During the course: when a slide points at a tab (e.g. "tab EX3-Tokens"), open it and copy the prompt. For the data walkthrough: upload this whole workbook to your AI and follow tab G2-DataAnalysis - profile first, then numbered questions.'],
    [''],
    ['THE TABS', 'EX1-TwoModes .. EX7-MoE = the seven numbered course prompts · G2-DataAnalysis = the data walkthrough (uses the Data tab) · EX-Quotes = the three-quotations exercise (PDFs in the pack) · EX-Email = the inbox play (thread file in the pack) · EX-Report = the Part 3 rep (your course, reported; grid + bonus rebuild drill) · BONUS-Ladder = a self-study triage drill · PLAYBOOK = Do / Don\'t / Expired, with sources.'],
    [''],
    ['THE DATA TAB', 'Twelve months of fictional supplier-delivery data across four sites and three suppliers, for practicing AI data analysis (Copilot, chat assistants with file upload, or a company RAG assistant).'],
    [''],
    ['COLUMN', 'MEANING'],
    ['Month', 'Delivery month, YYYY-MM'],
    ['Site', 'Receiving factory (Austin, Berlin, Osaka, Monterrey)'],
    ['Supplier', 'Component supplier (Alpha Components, Bravo Plastics, Cardinal Metals)'],
    ['Units_Shipped', 'Units received from the supplier that month'],
    ['Units_Returned', 'Units returned by customers due to component defects (escapes)'],
    ['Defects_Found', 'Defective units caught at incoming inspection'],
    ['Inspection_Hours', 'Hours spent on incoming inspection for that lot'],
    ['Unit_Cost_USD', 'Average cost per unit, US dollars'],
    ['On_Time_Percent', 'Share of the month’s deliveries that arrived on time'],
    [''],
    ['KNOWN QUIRKS (left in on purpose — a good analysis finds them)'],
    ['1', 'The last row of the Data tab is a TOTAL row — exclude it from any calculation.'],
    ['2', 'One Inspection_Hours cell contains the text "n/a" — decide and state how you handle it.'],
    [''],
    ['All names and numbers are fictional and generated for training. No real company data.'],
]
for row in readme:
    rd.append(row)
rd.column_dimensions['A'].width = 22
rd.column_dimensions['B'].width = 105
rd['A1'].font = Font(bold=True, size=13, color='0E7C7B')
for r in (10, 21):
    rd.cell(row=r, column=1).font = Font(bold=True)
    rd.cell(row=r, column=2).font = Font(bold=True)
for row in rd.iter_rows():
    for c in row:
        c.alignment = Alignment(vertical='top', wrap_text=True)

ws = wb.create_sheet('Data')
HDR = ['Month', 'Site', 'Supplier', 'Units_Shipped', 'Units_Returned', 'Defects_Found',
       'Inspection_Hours', 'Unit_Cost_USD', 'On_Time_Percent']
ws.append(HDR)
tot_ship = tot_ret = tot_def = 0
row_i = 1
for mi, month in enumerate(MONTHS):
    seasonal = 0.75 if month.endswith('-12') else 1.0
    for site, (base_units, base_ot, ot_sd, site_mod) in SITES.items():
        for sup, (base_def, def_trend, base_cost) in SUPS.items():
            row_i += 1
            units = int(base_units / 3 * seasonal * random.uniform(0.9, 1.1))
            def_rate = (base_def + def_trend * mi) * site_mod * random.uniform(0.85, 1.15)
            insp = round(random.uniform(14, 46), 1)
            # more inspection hours -> more defects caught, fewer escape to customers
            catch = min(0.92, 0.35 + insp / 60.0)
            defects = int(units * def_rate * catch)
            returned = int(units * def_rate * (1 - catch) * random.uniform(0.8, 1.2))
            cost = round(base_cost * random.uniform(0.97, 1.04), 2)
            on_time = round(min(100, max(70, random.gauss(base_ot - (4 if seasonal < 1 else 0), ot_sd))), 1)
            insp_val = 'n/a' if row_i == 38 else insp
            ws.append([month, site, sup, units, returned, defects, insp_val, cost, on_time])
            tot_ship += units
            tot_ret += returned
            tot_def += defects
ws.append(['TOTAL', '', '', tot_ship, tot_ret, tot_def, '', '', ''])
for c in range(1, len(HDR) + 1):
    cell = ws.cell(row=1, column=c)
    cell.font = Font(bold=True, color='FFFFFF')
    cell.fill = PatternFill('solid', fgColor='0E7C7B')
    ws.column_dimensions[get_column_letter(c)].width = 16
ws.freeze_panes = 'A2'
for c in range(1, len(HDR) + 1):
    ws.cell(row=ws.max_row, column=c).font = Font(bold=True)
n_data_rows = ws.max_row - 2  # workbook is saved at the end, after the prompt tabs are added

# ---------------------------------------------------------------- 2. Quotation PDFs
S = {
    'h1': ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=15, textColor=TEAL, spaceAfter=2),
    'sub': ParagraphStyle('sub', fontName='Helvetica', fontSize=9, textColor=MUTE, spaceAfter=10),
    'h2': ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=11, textColor=INK, spaceBefore=8, spaceAfter=4),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9.5, textColor=INK, leading=13),
    'fine': ParagraphStyle('fine', fontName='Helvetica-Oblique', fontSize=7.5, textColor=MUTE, spaceBefore=12),
}

def quote_pdf(fname, company, addr, ref, rows, notes):
    doc = SimpleDocTemplate(os.path.join(OUT, fname), pagesize=LETTER,
                            leftMargin=0.9 * inch, rightMargin=0.9 * inch,
                            topMargin=0.8 * inch, bottomMargin=0.8 * inch)
    E = [Paragraph(company, S['h1']), Paragraph(addr, S['sub']),
         Paragraph(f'QUOTATION — ref. {ref} · in response to RFQ-2026-114', S['h2']),
         Paragraph('Item: EN-450 anodized aluminum enclosure, per drawing rev. D. Requested quantity: 5,000 units (option: 10,000).', S['body']),
         Spacer(1, 8)]
    t = Table([[Paragraph(f'<b>{a}</b>', S['body']), Paragraph(b, S['body'])] for a, b in rows],
              colWidths=[1.9 * inch, 4.6 * inch])
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#DCE3E6')),
        ('BACKGROUND', (0, 0), (0, -1), HexColor('#F2F5F6')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    E.append(t)
    E.append(Paragraph('Notes: ' + notes, S['body']))
    E.append(Paragraph('Fictional document generated for the "From Prompts to Agents" training. Not a real company, offer, or price.', S['fine']))
    doc.build(E)
    print('wrote', os.path.join(OUT, fname))

quote_pdf('Quote_Alpha_Components.pdf', 'Alpha Components Inc.', '2200 Commerce Park Drive · Austin, TX · USA', 'AC-26-0912',
          [['Unit price', 'USD 13.90 / unit at 5,000 pcs · USD 12.60 / unit at 10,000 pcs'],
           ['Tooling', 'USD 8,500 one-time (3 weeks)'],
           ['Minimum order', '1,000 units'],
           ['Lead time', '4 weeks after tooling approval'],
           ['Payment terms', 'Net 30'],
           ['Warranty', '12 months, workmanship'],
           ['Shipping', 'FOB Austin (buyer arranges freight)'],
           ['Validity', '60 days']],
          'Prices include standard black anodizing. Expedite program available (+8%, lead time 2 weeks).')

quote_pdf('Quote_Bravo_Plastics.pdf', 'Bravo Plastics GmbH', 'Industriestraße 14 · Hamburg · Germany', 'BP-2026-3341',
          [['Price', 'EUR 11,900 per 1,000 units (5,000-unit tier) · EUR 10,950 per 1,000 units (10,000-unit tier)'],
           ['Tooling', 'EUR 14,000 — not included in the prices above'],
           ['Minimum order', '5,000 units'],
           ['Lead time', '9 weeks including tooling'],
           ['Payment terms', 'Net 60'],
           ['Warranty', '6 months'],
           ['Shipping', 'EXW Hamburg (buyer collects; freight and import duties not included)'],
           ['Validity', '30 days']],
          'Quoted in euros. Surface per DIN standard; color matching on request. Prices exclude VAT.')

quote_pdf('Quote_Cardinal_Metals.pdf', 'Cardinal Metals Ltd.', 'Attercliffe Works · Sheffield · United Kingdom', 'CM/26/RFQ114',
          [['Unit price', 'USD 16.40 / unit at 5,000 pcs · USD 15.20 / unit at 10,000 pcs'],
           ['Tooling', 'Waived for orders of 5,000 units or more'],
           ['Minimum order', '2,500 units'],
           ['Lead time', '6 weeks, all-in'],
           ['Payment terms', 'Net 45'],
           ['Warranty', '24 months, including anodizing defects'],
           ['Shipping', 'DDP your dock — freight and duties included'],
           ['Validity', '90 days']],
          'Price includes lot-level material certs and PPAP level 3 documentation.')

# ---------------------------------------------------------------- 3. Email thread
MSGS = [
    ('Maya Chen (Packaging Engineering)', 'Tue Sep 8, 2026 09:14', 'All',
     'Q3 packaging change — approval needed by Fri',
     'Team — proposing we switch the EN-450 line from foam inserts to molded pulp trays. Drop-test v1 passed at 1.2 m. '
     'Cost per unit drops ~9%, and it clears the plastic-reduction target. Full proposal attached (packaging_proposal_v3.pdf). '
     'I need sign-offs by Friday.'),
    ('Tom Alvarez (Procurement)', 'Tue Sep 8, 2026 11:02', 'All', 'RE: Q3 packaging change',
     'Supportive. One flag: our current quote from the tray vendor is 90 days old. I will request an updated quotation and '
     'confirm the 9% figure by Wed Sep 17.'),
    ('Jonas Weber (Operations, Berlin)', 'Tue Sep 8, 2026 11:40', 'All', 'RE: Q3 packaging change',
     'Berlin can host the pilot run. Also — anyone else going to the canteen thing Thursday? They said there will be pretzels.'),
    ('Priya Nair (Quality)', 'Wed Sep 9, 2026 08:55', 'All', 'RE: Q3 packaging change',
     'Before sign-off I need the v2 drop-test at 1.5 m per the updated spec, not 1.2. Maya, can you rerun and share the report? '
     'Also the incoming-inspection checklist will need a molded-pulp section — I can draft it once the pilot is confirmed.'),
    ('Maya Chen (Packaging Engineering)', 'Wed Sep 9, 2026 13:21', 'All', 'RE: RE: Q3 packaging change',
     'Fair. Rerunning at 1.5 m — drop_test_v2.xlsx to follow by Fri Sep 19. If it passes, no design change needed.'),
    ('Dan Brooks (Finance)', 'Wed Sep 9, 2026 16:47', 'All', 'RE: Q3 packaging change',
     'Approved from my side WITH a cap: total transition spend (tooling + obsolete foam write-off) must stay under USD 18,000. '
     'Above that it goes to the quarterly review board.'),
    ('Sofia Ruiz (Customer Success)', 'Thu Sep 10, 2026 10:05', 'All', 'RE: Q3 packaging change',
     'Two customers audit our packaging annually. Do we need to send a change-notification letter before the switch, or after the pilot? '
     'Genuinely unsure of the requirement here.'),
    ('Jonas Weber (Operations, Berlin)', 'Thu Sep 10, 2026 10:22', 'All', 'RE: Q3 packaging change',
     'Pilot logistics: we can start the week of Sep 22. Reserving line 2 for two shifts. (I am out Fri.)'),
    ('Maya Chen (Packaging Engineering)', 'Mon Sep 14, 2026 09:31', 'All', 'RE: RE: FW: Q3 packaging change',
     'Update: the 1.5 m rig is booked next week, so drop-test v2 slips to Wed Sep 23 — which moves the Berlin pilot start to '
     'Mon Oct 6. Jonas, please rebook line 2. Everything else stands: Tom’s quote check Sep 17, Dan’s 18k cap, pilot at Berlin.'),
    ('Tom Alvarez (Procurement)', 'Mon Sep 14, 2026 15:58', 'All', 'RE: Q3 packaging change',
     'Noted on the new dates. Vendor confirmed they are re-quoting against RFQ-2026-114 quantities; expecting the document tomorrow. '
     'Will circulate.'),
]
txt_path = os.path.join(OUT, 'Email_Thread_Packaging_Change.txt')
with open(txt_path, 'w') as f:
    f.write('FICTIONAL EMAIL THREAD — generated for the "From Prompts to Agents" training. No real people or companies.\n')
    f.write('=' * 100 + '\n\n')
    for who, sent, to, subj, body in MSGS:
        f.write(f'From: {who}\nSent: {sent}\nTo: {to}\nSubject: {subj}\n\n{body}\n\n' + '-' * 100 + '\n\n')
print('wrote', txt_path, f'({len(MSGS)} messages)')

doc = SimpleDocTemplate(os.path.join(OUT, 'Email_Thread_Packaging_Change.pdf'), pagesize=LETTER,
                        leftMargin=0.9 * inch, rightMargin=0.9 * inch, topMargin=0.8 * inch, bottomMargin=0.8 * inch)
E = [Paragraph('Email thread — “Q3 packaging change — approval needed by Fri”', S['h1']),
     Paragraph('Ten messages · six participants · fictional, generated for training', S['sub'])]
for who, sent, to, subj, body in MSGS:
    E.append(Paragraph(f'<b>From:</b> {who} &nbsp;·&nbsp; <b>Sent:</b> {sent} &nbsp;·&nbsp; <b>Subject:</b> {subj}', S['h2']))
    E.append(Paragraph(body, S['body']))
    E.append(Spacer(1, 6))
E.append(Paragraph('Fictional document generated for the "From Prompts to Agents" training. No real people, companies, or data.', S['fine']))
doc.build(E)
print('wrote', os.path.join(OUT, 'Email_Thread_Packaging_Change.pdf'))

# ---------------------------------------------------------------- 4. Exercise prompt tabs (R11)
# One named tab per exercise; column B is the copy-paste cell. Texts mirror the deck (R10).
TAB_FILL = PatternFill('solid', fgColor='0E7C7B')

def prompt_tab(name, title, rows, note=None):
    t = wb.create_sheet(name)
    t.append([title])
    t['A1'].font = Font(bold=True, size=12, color='0E7C7B')
    t.append([])
    t.append(['STEP', 'COPY-PASTE THIS (one cell = one prompt)', 'WHY'])
    for c in range(1, 4):
        cell = t.cell(row=3, column=c)
        cell.font = Font(bold=True, color='FFFFFF')
        cell.fill = TAB_FILL
    for r in rows:
        t.append(list(r))
        t.cell(row=t.max_row, column=1).font = Font(bold=True, color='0E7C7B')
    if note:
        t.append([])
        t.append(['NOTE', note])
        t.cell(row=t.max_row, column=1).font = Font(bold=True)
    t.column_dimensions['A'].width = 15
    t.column_dimensions['B'].width = 74
    t.column_dimensions['C'].width = 44
    for row in t.iter_rows():
        for c in row:
            c.alignment = Alignment(vertical='top', wrap_text=True)
    t.freeze_panes = 'A4'

prompt_tab('EX1-TwoModes', 'Prompt 1/7 · Two modes, felt — this chat becomes your course log', [
    ('STEP 1', 'Write a short farewell card for a coworker who is leaving.',
     'Generative mode — it writes instantly, guessing every detail it doesn\'t know.'),
    ('STEP 2', 'Now don\'t write it. Ask me everything you\'d need to know to do this perfectly, then wait for my answers.',
     'The seed of delegate mode — the AI turns around and interviews YOU.'),
], note='Run both steps in ONE chat and keep that chat all course — it is your course log.')

prompt_tab('EX2-Guesses', 'Prompt 2/7 · Narrowing the guesses — two separate sends', [
    ('SEND 1', 'Finish this sentence 5 different ways: We should move the launch date because',
     'No facts yet — watch it scatter across guesses (budget, staffing, quality...).'),
    ('SEND 2', 'Now 5 more ways, knowing: B2B software firm, competitor launches May 3, our beta ends April 20.',
     'Your facts didn\'t make it smarter — they deleted wrong guesses. Grade the directions, not the sentences.'),
])

prompt_tab('EX3-Tokens', 'Prompt 3/7 · Bricks, not letters', [
    ('STEP 1', 'Explain AI tokens to a high-school student in under 80 words: use a LEGO-brick analogy, show one word splitting into tokens, and end with why tokens set my AI\'s cost and limits.',
     'The definition lands in your course log — and the brick analogy is the one the best explainers use.'),
])

prompt_tab('EX4-Handoff', 'Prompt 4/7 · The desk — explained, then carried', [
    ('STEP 1', 'Explain your context window like I\'m a 5th grader: the desk, what fits on it, and what happens when I close this chat. Under 100 words.',
     'The AI describes its own working memory, plainly.'),
    ('STEP 2 (homework)', 'Summarize our chat so far in under 80 words, titled HANDOFF.',
     'Tonight: paste the HANDOFF into a fresh chat, ask "where was I?" — and watch it pick up your course.'),
])

prompt_tab('BONUS-Ladder', 'Bonus drill · The escalation ladder — see the rungs sort themselves (self-study)', [
    ('STEP 1', 'Give me three everyday AI problems: one fixed by a better prompt, one by giving it the right documents, one only fixable by retraining it. One line each on why.',
     'The escalation ladder — prompt it, feed it documents, retrain it — sorted live by the AI in front of you.'),
    ('EXTENDED', 'Here are six workplace AI problems. I will sort each as P (better prompt), R (give it the right documents) or F (retrain the model) — then you grade me. The diagnostic: is the AI missing knowledge (R), or misbehaving with knowledge it already has (P)? Only a deep habit needed at huge volume justifies F. Problems: 1) Its summaries are always too long and chatty. 2) It doesn\'t know our returns policy. 3) Its answers are right but in the wrong format for our tracker. 4) It can\'t answer questions about last week\'s customer complaints. 5) A support bot must answer in our house style across millions of chats, with no room to paste instructions each time. 6) It keeps writing formal English when our team writes casual Spanish. Wait for my six answers before grading.',
     'The stretch drill. Problem 6 is deliberately arguable — the argument is the lesson.'),
])

prompt_tab('EX5-TwoSpeeds', 'Prompt 5/7 · Same brain, two speeds', [
    ('STEP 1', 'Describe your fast mode vs your thinking mode like I\'m choosing between them for real work: when is each worth it, and roughly how much more does thinking cost? Under 120 words.',
     'The model explains its own two speeds — and its own bill.'),
    ('EXTENDED 1', 'Answer instantly, in one line: Five colleagues (Ana, Ben, Chloe, Dev, Ema) each present on a different weekday. Ben presents Monday. Dev presents Friday. Chloe can\'t do Monday or Wednesday. Ema presents the day after Chloe. Ana presents later in the week than Chloe. Who presents when?',
     'The fast pass — quick, cheap, and often wrong on logic like this.'),
    ('EXTENDED 2', 'Now solve the same puzzle carefully: check every rule one by one, show your reasoning, then give the final schedule.',
     'The slow pass — drafts and checks. (Unique solution exists.)'),
    ('EXTENDED 3', 'Estimate the word count of your two answers above and compute the multiple. That ratio is roughly how a thinking tier bills compared to a fast one.',
     'Most rooms land on 10-20x — the bill, felt.'),
])

prompt_tab('EX6-FeatureMenu', 'Prompt 6/7 · Ask your own product for its menu', [
    ('STEP 1', 'List the modes this app gives me — quick answer, thinking, web search, deep research, agent — one line each on what it does differently and its rough effort. Say \'unsure\' rather than guess.',
     'Your own product hands you its menu; ask again the day it changes.'),
    ('EXTENDED', 'Build a table of every mode and toggle this app offers: name · what it does differently · when to use it · relative cost or effort · does it work with uploaded files? · does it need a paid tier? Say \'unsure\' where you don\'t know.',
     'The six-column version — a personal reference card that never goes stale.'),
])

prompt_tab('EX7-MoE', 'Prompt 7/7 · The specialist hospital, explained', [
    ('STEP 1', 'Explain Mixture of Experts like a colleague: a specialist hospital where only the relevant departments wake up per question — and why that made AI dramatically cheaper in 2025. Under 120 words.',
     'The MoE cheat-note lands in your course log, told by your own assistant.'),
])

prompt_tab('G2-DataAnalysis', 'Part 4 walkthrough · AI data analysis on the Data tab of THIS workbook', [
    ('STEP 0', 'Work only with the Data tab of this workbook. Before any analysis: profile it — rows, columns, types, missing or odd values, and anything that would trip a calculation. Show me the profile and STOP. Do not analyze yet.',
     'Profile first, analyze second. A good profile finds the TOTAL row and the "n/a" cell.'),
    ('STEP 1', 'Working only on the 144 data rows (exclude the TOTAL row; treat the "n/a" as missing and say so): 1) Which supplier has the highest defect rate — (Defects_Found + Units_Returned) / Units_Shipped — overall, and is it getting better or worse across the year? 2) Is there a relationship between Inspection_Hours and Units_Returned? Compute the correlation by running code, show your working, and describe it as an association, not a cause. 3) Rank the sites by On_Time_Percent. Answer in that order, then stop.',
     'Numbered questions, quirks handled explicitly, code not mental math, then STOP.'),
    ('STEP 2', 'Build a supplier scorecard: one row per supplier — defect rate, return rate, average unit cost, average on-time % — best value per column marked. Then one paragraph: if we had to consolidate to one supplier, which one, and what does this data NOT tell us about that decision?',
     'The comparative view — and the habit of asking what the data does NOT say.'),
    ('STEP 3', 'Reconcile: sum Units_Shipped across your 144 rows and compare it to the TOTAL row you excluded. Do they match? If not, what happened?',
     'The trust check — one reconciliation anchor beats ten spot checks.'),
    ('STEP 4', 'Turn the supplier scorecard into a one-sheet spreadsheet I can circulate: a README tab explaining every column and where the numbers came from, the scorecard tab with formulas visible — not pasted values — and a short caveats section (the "n/a" cell, the excluded TOTAL row, any assumptions). Use only numbers from this chat; if one is missing, leave the cell blank and say so — do not invent it.',
     'Ship the artifact, not just the answer. Verify two formulas before it circulates.'),
], note='The generic G2 template (role/data/task/method/format blocks with blanks) is in prompt-library/ — these five steps are G2, filled in for this dataset.')

prompt_tab('EX-Quotes', 'Part 4 walkthrough · Three quotes, one table (uses the three Quote_*.pdf files in your pack)', [
    ('STEP 1', 'Extract every commercial term from these three quotations into one table: supplier, unit price, tooling, MOQ, lead time, payment terms, warranty, shipping terms, validity. Normalize prices to USD per unit at 5,000 units — state the EUR rate you use and flag it as an assumption — include tooling amortized over the 5,000 units, and note what shipping does and doesn\'t include. Flag anything that is still not comparable.',
     'Extract & normalize — the "cheapest" quote stops looking cheapest once currency, per-1000 pricing, tooling and freight are normalized.'),
    ('STEP 2', 'Now: which quote has the lowest true landed cost at 5,000 units? Which is the best overall value once warranty, lead time and payment terms count? And what would you negotiate with each supplier before deciding? Keep it to one page; separate facts from judgment.',
     'Recommendation with caveats — and the exchange rate stays a flagged assumption YOU verify.'),
], note='Attach Quote_Alpha_Components.pdf, Quote_Bravo_Plastics.pdf and Quote_Cardinal_Metals.pdf before sending STEP 1.')

prompt_tab('EX-Email', 'Part 4 walkthrough · The inbox play (uses Email_Thread_Packaging_Change.txt / .pdf)', [
    ('THE BRIEF', 'Summarize the email thread below under four headers, in order: 1) OVERVIEW — two sentences. 2) DECISIONS — bullets; write "None" if nothing was decided. 3) ACTION ITEMS — task — owner — due date; leave a slot blank rather than guess. 4) OPEN QUESTIONS — raised but never answered. Rules: use only facts in the thread · work oldest-first and flag anywhere a decision or date CHANGED later — show both, mark the latest · do not invent owners or dates. Thread: [paste, oldest first]',
     'The structured brief (shape 2 of 5) — its three rules exist because naive summaries report the first date, drop qualifiers, and invent owners.'),
    ('STEP 2', 'From the thread: List A — every question raised that was never answered. List B — WHO OWES WHAT: "X owes Y: [thing] by [date]", latest state only. Blank beats guessed.',
     'Reply prep — the thread\'s open loops, surfaced.'),
    ('STEP 3', 'Using the brief above, draft my reply: answer the open questions, confirm the decisions with their conditions, propose next steps. Do not invent commitments — leave a [bracket] where I must decide. Under 120 words, one clear next step at the end.',
     'The reply — conditions survive, commitments stay yours.'),
    ('OTHER SHAPES', 'Shape 1 TL;DR: "One sentence, max 30 words: current state or decision needed — not the history." · Shape 3 Actions table: "Task | Owner | Due | Blocked by — blank cells beat guessed ones." · Shape 4 Decisions log: "Decision | Decided by | Reasoning | Date — settled only, proposals flagged." · Shape 5 Who-owes-what: "Every unanswered question + X owes Y: [thing], latest state only."',
     'Picking the shape IS the skill — the brief is the default.'),
], note='The practice thread has four planted traps: a moved date, an approval WITH a condition, an unanswered question, and a mentioned attachment that isn\'t there. A good brief catches all four.')

prompt_tab('EX-Report', 'Part 3 rep · Your course, reported (3 minutes)', [
    ('THE GRID', 'Inspect with this — which element failed? wrong altitude, tone, or posture -> ROLE · answers a different (or vaguer) question -> TASK · generically right, specifically wrong for us -> CONTEXT · right content, unusable shape or length -> FORMAT · doesn\'t match the standard in your head -> EXAMPLES · confidently invented -> THE OUT is missing · sprawls past what you asked -> THE STOP is missing.',
     'The symptom-to-element diagnosis grid — name the failed element, fix that ONE, rerun.'),
    ('STEP 1', 'List every prompt I have run in this course log, in order — one line each: what it did, and which element or move it taught.',
     'Run in your COURSE LOG (the chat you opened with Prompt 1). The log replays your whole course.'),
    ('STEP 2', 'Now turn that into my one-page course report: the seven elements with my own example for each, the loop, and the three prompts I will reuse at work. Anything the log doesn\'t show: write UNKNOWN — don\'t invent. Deliver the report, then stop.',
     'Your examples, your report — note the Out and the Stop working inside the prompt itself. Name it, date it: your first library entry.'),
    ('RECOVERY', 'If your course log was lost mid-course: the numbered prompts EX1..EX7 in this workbook are the full list — paste the ones you ran, then run STEP 2.',
     'The HANDOFF move from Part 1 is the repair tool.'),
    ('BONUS · REBUILD', 'Self-study contrast drill. Baseline: "Summarize this report." + the practice report below. Upgrade: add a Role, a named reader in the Task, a <=80-word cap, and an Out ("anything the report doesn\'t state: write UNKNOWN — never estimate; list the gaps at the end"). Practice report: Q2 returns totaled 412 units against 28,400 shipped (1.45%), up from 1.1% in Q1. Site B drove the rise; supplier packaging changes are the suspected cause. Inspection hours were flat; two corrective actions are in draft. Full breakdown by site and supplier is in the appendix table.',
     'Four elements — watch the same report change league.'),
])

# ---------------------------------------------------------------- 5. PLAYBOOK tab (full 8+8+8, r20)
PB_TODO = [
    ('1', 'State the task precisely — verb, constraints, success criteria, and the WHY behind each rule', 'Anthropic 2026 · Yang 2026: unstated requirements guessed right only 41.1%'),
    ('2', 'Structure with delimiters (XML/Markdown) and standardize ONE tested, versioned template', 'Anthropic/OpenAI/Google guides · He 2024: wrapper alone swings up to 40%'),
    ('3', 'Zero-shot first; add 3-5 targeted, diverse examples only when format or tone matters', 'OpenAI reasoning best practices · Anthropic 2026'),
    ('4', 'Long inputs: documents at the TOP, instructions at the END — bookend BOTH ends when very long', 'Anthropic: up to ~30% · GPT-4.1 guide 2025: both ends beat either alone'),
    ('5', 'Give an out with a checkable shape ("anything not stated: write UNKNOWN — never estimate; list the gaps") + require citations', 'Omar 2025: hallucination 66%→44% · Anthropic docs'),
    ('6', 'Concrete numeric budgets for measurable outputs — words, bullets, tool calls', 'GPT-5.1 guide: adheres well to concrete length guidance · GPT-5 guide'),
    ('7', 'Persona + audience for VOICE and level — never for accuracy', 'PersonaLLM 2024: traits detectable up to 80% · Google PTCF'),
    ('8', 'Self-check against NAMED criteria, with evaluation blinded from generation', 'CoVe 2024: FactScore 55.9→71.4 · Cheng, Science 2026 (blinding)'),
]
PB_NOT = [
    ('1', 'Contradictory instructions — reasoning models burn tokens reconciling them', 'GPT-5 guide 2025'),
    ('2', 'Tips, threats, deadline pressure — null on average, ±35% per-question chaos', 'Wharton R3 2025 · Salinas & Morstatter 2024'),
    ('3', 'Bare "do not hallucinate" commands — they trigger over-refusal of facts that ARE in the context (the "Safety Tax"); use the positive out+cite pattern instead', 'arXiv:2601.02023 (Jan 2026)'),
    ('4', 'Revealing your preferred answer, or "are you sure?" as verification', 'Cheng, Science 2026: +49% affirmation · Sharma 2023'),
    ('5', 'Piling micro-rules — even frontier models degrade past ~150 simultaneous instructions, early rules win', 'IFScale, arXiv:2507.11538 · GPT-5.5 guide: smallest prompt that preserves the contract'),
    ('6', 'ALL-CAPS / ALWAYS / NEVER as an emphasis crutch — reserve absolutes for true invariants', 'GPT-5.x guides · Gemini 3 guide'),
    ('7', 'Demanding JSON/schemas a human will just read — use structured output only when a system consumes it', 'OpenAI 2024 · (do NOT teach "JSON hurts reasoning" as fact — 2025 replications)'),
    ('8', 'Concluding "the model can\'t do X" from one phrasing — formatting alone swings up to 76 points', 'Sclar ICLR 2024 · Wharton R1'),
]
PB_EXP = [
    ('1', '"Let\'s think step by step" / manual chain-of-thought → pick a reasoning model, set the effort dial', 'Kojima 2022 origin (GSM8K 10.4→40.7 — it WAS real) · OpenAI now: avoid CoT prompts · Wharton R2'),
    ('2', 'Piles of few-shot exemplars (10+) → zero-shot first, then 3-5 format-definers', 'Brown 2020 origin · DeepSeek-R1 paper 2025: few-shot degrades reasoners'),
    ('3', '"You are a world-class expert" for accuracy → task-specific instructions; persona for voice only', 'Zheng 2024 (162 personas: null) · Wharton R4 Dec 2025'),
    ('4', '"Take a deep breath" and other magic phrases → automated prompt optimization (the method won; the phrase died)', 'OPRO ICLR 2024'),
    ('5', 'Emotional appeals ("important to my career") → clarity; real stakes stated as factual context', 'EmotionPrompt recalc arXiv:2409.20303: honest average ~2.6%, null on modern models'),
    ('6', '"Instructions, ###, then text" + chopping documents for tiny windows → docs top, query end, bookend long context', 'Liu 2023 (mechanism persists) · GPT-4.1 guide'),
    ('7', 'Hand-run self-consistency (10 samples, majority vote) + micro-decomposing every task → effort settings; chain only for auditable intermediates', 'Wang ICLR 2023 origin · Anthropic 2026 · GPT-5.5: clear destination, let it choose the path'),
    ('8', 'Carrying your GPT-4-era prompt stack to each new model → re-baseline and re-test on every upgrade (PDCA)', 'GPT-5.5 guide via Willison, Apr 2026'),
]
pb = wb.create_sheet('PLAYBOOK')
pb.append(['The 2026 prompting playbook — Do / Don\'t / Expired (full 8+8+8; top five of each are on the course slide)'])
pb['A1'].font = Font(bold=True, size=12, color='0E7C7B')
pb.append(['Researched Sep 9, 2026 — full sources: notes/research/r20_do_dont_expired.md in the training repo. Re-verify before major reuse; this field moves.'])
pb['A2'].font = Font(italic=True, size=9, color='7A8790')
SECTION_FILLS = {'TO DO — reliably helps today': '1E7B34', 'NOT TO DO — hurts or wastes effort today': 'B3261E', 'EXPIRED — was right in 2022-23; do the replacement instead': '5A6570'}
for title, rows in (('TO DO — reliably helps today', PB_TODO),
                    ('NOT TO DO — hurts or wastes effort today', PB_NOT),
                    ('EXPIRED — was right in 2022-23; do the replacement instead', PB_EXP)):
    pb.append([])
    pb.append([title])
    hcell = pb.cell(row=pb.max_row, column=1)
    hcell.font = Font(bold=True, color='FFFFFF')
    hcell.fill = PatternFill('solid', fgColor=SECTION_FILLS[title])
    pb.append(['#', 'RULE', 'EVIDENCE / ANCHOR'])
    for c in range(1, 4):
        pb.cell(row=pb.max_row, column=c).font = Font(bold=True)
    for r in rows:
        pb.append(list(r))
pb.append([])
pb.append(['COHERENCE NOTES', 'Numeric caps constrain QUANTITY; ALWAYS/NEVER locks JUDGMENT — reserve absolutes for true invariants. Repeat verbatim at both ends of long context, or not at all. Task DETAIL helps; rule COUNT hurts. Chain-of-thought is expired on frontier reasoning models only — still fine on small/local ones. "Give an out" is "don\'t hallucinate" said positively — say what TO do.'])
pb.cell(row=pb.max_row, column=1).font = Font(bold=True)
pb.column_dimensions['A'].width = 6
pb.column_dimensions['B'].width = 88
pb.column_dimensions['C'].width = 52
for row in pb.iter_rows():
    for c in row:
        c.alignment = Alignment(vertical='top', wrap_text=True)

xlsx_path = os.path.join(OUT, 'Course_Workbook.xlsx')
wb.save(xlsx_path)
print('wrote', xlsx_path, f'({n_data_rows} data rows + README + 12 exercise tabs + PLAYBOOK)')

# ---------------------------------------------------------------- 6. Playbook one-pager PDF
pp_doc = SimpleDocTemplate(os.path.join(OUT, 'Playbook_One_Pager.pdf'), pagesize=LETTER,
                           leftMargin=0.55 * inch, rightMargin=0.55 * inch,
                           topMargin=0.5 * inch, bottomMargin=0.45 * inch)
tiny = ParagraphStyle('tiny', fontName='Helvetica', fontSize=7.4, textColor=INK, leading=9.2)
tinym = ParagraphStyle('tinym', fontName='Helvetica-Oblique', fontSize=6.6, textColor=MUTE, leading=8.4)
sect = ParagraphStyle('sect', fontName='Helvetica-Bold', fontSize=9.5, textColor=HexColor('#FFFFFF'), leading=12)
PE = [Paragraph('The 2026 prompting playbook — one page', S['h1']),
      Paragraph('From Prompts to Agents · researched Sep 2026 · full sources in the PLAYBOOK tab of your Course Workbook', S['sub'])]
for title, rows, col in (('TO DO — reliably helps', PB_TODO, '#1E7B34'),
                         ('NOT TO DO — hurts or wastes effort', PB_NOT, '#B3261E'),
                         ('EXPIRED — do the replacement instead', PB_EXP, '#5A6570')):
    hdr = Table([[Paragraph(title, sect)]], colWidths=[7.3 * inch])
    hdr.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), HexColor(col)),
                             ('TOPPADDING', (0, 0), (-1, -1), 2), ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
                             ('LEFTPADDING', (0, 0), (-1, -1), 6)]))
    PE.append(hdr)
    body = Table([[Paragraph(f'<b>{n}</b>', tiny), Paragraph(txt, tiny), Paragraph(ev, tinym)] for n, txt, ev in rows],
                 colWidths=[0.25 * inch, 4.55 * inch, 2.5 * inch])
    body.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.4, HexColor('#DCE3E6')),
                              ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                              ('TOPPADDING', (0, 0), (-1, -1), 1.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5)]))
    PE.append(body)
    PE.append(Spacer(1, 5))
PE.append(Paragraph('Coherence: caps constrain quantity, absolutes lock judgment · repeat verbatim at both ends of long context or not at all · task detail helps, rule count hurts · CoT expired on frontier reasoning models only · "give an out" is "don\'t hallucinate" said positively.', tinym))
pp_doc.build(PE)
print('wrote', os.path.join(OUT, 'Playbook_One_Pager.pdf'))
