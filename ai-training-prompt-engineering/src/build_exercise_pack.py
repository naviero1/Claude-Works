# Builds the v1.6 hands-on exercise pack (all data fictional, generated, generic):
#   deliverables/exercise-data/Course_Workbook.xlsx           README + Data (raw, NO formulas - the AI
#                                                             does the math) + one named tab per exercise
#                                                             (EX1..EX7, G2-DataAnalysis, EX-Quotes,
#                                                             EX-Email, EX-Dashboard, EX-Report,
#                                                             BONUS-Ladder) + PLAYBOOK (8+8+8)
#   deliverables/exercise-data/Quote_Alpha_Components.pdf     (three comparable supplier quotations,
#   deliverables/exercise-data/Quote_Bravo_Plastics.pdf        deliberately non-comparable at first
#   deliverables/exercise-data/Quote_Cardinal_Metals.pdf       glance: currency/per-1000/EXW traps)
#   deliverables/exercise-data/Email_Thread_Packaging_Change.txt / .pdf  (messy 10-message thread)
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
    ['THE TABS', 'EX1-TwoModes .. EX7-MoE = the seven numbered course prompts · G2-DataAnalysis = the data walkthrough (uses the Data tab) · EX-Quotes = the three-quotations exercise (PDFs in the pack) · EX-Email = the inbox play (thread file in the pack) · EX-Dashboard = the dashboard build: shape it, build it, check it, refine it (uses the Data tab; includes the dashboard vocabulary) · EX-Report = the Part 3 rep (your course, reported; grid + bonus rebuild drill) · BONUS-Ladder = a self-study triage drill · PLAYBOOK = Do / Don\'t / Expired, with sources.'],
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

prompt_tab('EX-Dashboard', 'Part 4 follow-on · A dashboard from data — shape it, build it, check it, refine it (uses the Data tab of THIS workbook)', [
    ('STEP 0 · SHAPE', 'Work with the Data tab of this workbook (144 data rows; exclude the TOTAL row; one Inspection_Hours cell is "n/a" — treat it as missing and say so). I want a monthly supplier-quality dashboard for a plant manager who has 60 seconds. Before you build ANYTHING, propose the shape: 1) the 3-4 KPIs worth tracking — for each: a name, its exact formula from these columns, its current value for the latest month in the data, and a sensible target; for any percentage column, state whether your formula weights by Units_Shipped or takes a simple average; 2) one chart per question the manager will actually ask — name the chart type and what is on each axis; 3) a one-line layout sketch: what sits top-left, and why. Show me the proposal and STOP — no code yet.',
     'Design is a gate: approve KPIs and layout as PLAIN TEXT before anything renders. A wrong KPI caught here costs a sentence; caught after the dashboard circulates, it costs a retraction.'),
    ('STEP 1 · BUILD', 'Approved, with these changes: [your edits — or "none"]. Build it as ONE self-contained HTML file: the Data tab embedded in the file — no server, no external calls; it must open from disk, offline, on a work laptop. Views: 1) a KPI row — the tiles we agreed, each showing the value, its state vs target as a label or icon plus color — never color alone — and a trend arrow with the change vs the prior month; 2) the charts we agreed, units on the axes; 3) a sortable, searchable data table of the underlying rows; 4) one Site + Supplier filter row at the top that re-scopes EVERYTHING — tiles, charts, and table — so every number on screen always agrees. Design: legible, color-blind-safe. Every number computed from the embedded data — nothing hard-coded; show each KPI\'s formula in a tooltip or footnote so it can be audited. Anything that cannot be computed from the data: show "—", never a guess. Footer: the as-of month, the data source ("Course Workbook Data tab — fictional training data"), and an owner-and-refresh line.',
     'The G6 pattern. Four constraints make an AI-built tool trustworthy: single file · offline · data embedded · formulas visible.'),
    ('STEP 2 · CHECK', 'Before I trust it: 1) reconcile — sum Units_Shipped across the data embedded in your dashboard and compare it to the TOTAL row of the Data tab; show both numbers; 2) filter to one site, pick one month, and recompute one KPI tile by hand, showing the arithmetic; 3) list every assumption the dashboard makes (the "n/a" cell, the excluded TOTAL row, any rounding, and how percentage columns like On_Time_Percent were aggregated — unit-weighted or simple average). Fix any mismatch before answering.',
     'The trust check, same as the data walkthrough: one reconciliation anchor plus one hand-recomputed tile beats admiring the design.'),
    ('STEP 3 · REFINE', 'One improvement pass: [name ONE change — e.g. "add a 12-month sparkline inside each tile" or "add a site-by-month heatmap of on-time %"]. Change only that. Tell me what you changed, and re-verify any number the change touched.',
     'Fix one element and re-run — the improvement loop, applied to software instead of prose. (Both examples are in the vocabulary below — ask for parts by name.)'),
], note='Needs a tool that can write and package code into a downloadable HTML file — Claude (Artifacts), ChatGPT (Canvas), Gemini (Canvas), typically paid tiers; in Copilot that means Pages, not plain chat. If your AI only chats: hand this same spec to IT, or ask for the Excel version. Two cautions: the file EMBEDS the data — classify and share it like the spreadsheet it came from (share the FILE, not a public link) · it is a snapshot, not a live system — for refreshing data you need a BI tool. The generic template behind this exercise is G6 in prompt-library/.')

# EX-Dashboard extras: what makes a KPI + the dashboard vocabulary (owner request, Round 16)
td = wb['EX-Dashboard']
td.append([])
td.append(['WHAT MAKES A KPI', 'A KPI is a number someone ACTS on — not decoration. Each one needs four things:', ''])
td.cell(row=td.max_row, column=1).font = Font(bold=True, color='FFFFFF')
td.cell(row=td.max_row, column=1).fill = TAB_FILL
td.cell(row=td.max_row, column=2).font = Font(bold=True)
for k, v in (
        ('A decision', 'If nobody would do anything differently when it moves, it is trivia, not a KPI — cut it.'),
        ('A formula', 'Named columns, exact arithmetic — e.g. defect rate = (Defects_Found + Units_Returned) / Units_Shipped. If you can\'t write the formula, you can\'t track the number.'),
        ('A target', 'A value is a fact; value-vs-target is a status. Targets turn a dashboard from a report into an alarm.'),
        ('The trio of views', 'Every KPI answers three questions: LEVEL (where are we) · TREND (which way is it moving) · GAP (how far from target). Tiles show level+gap; the chart shows trend.'),
):
    td.append([k, v])
    td.cell(row=td.max_row, column=1).font = Font(bold=True, color='0E7C7B')
td.append([])
td.append(['THE VOCABULARY', 'Name the parts and you can ask for them — this vocabulary carries across all data-analytics and BI tools (Power BI, Tableau, Excel dashboards alike).', 'ASK FOR IT LIKE THIS'])
td.cell(row=td.max_row, column=1).font = Font(bold=True, color='FFFFFF')
td.cell(row=td.max_row, column=1).fill = TAB_FILL
td.cell(row=td.max_row, column=2).font = Font(bold=True)
td.cell(row=td.max_row, column=3).font = Font(bold=True)
DASH_VOCAB = [
    ('KPI', 'Key Performance Indicator — a number tied to a decision, with a formula and a target.', '"Propose 3-4 KPIs with formula, current value and target — then stop."'),
    ('KPI tile / stat tile', 'The big-number card in the headline row: value + vs-target state + trend arrow.', '"A KPI row of four tiles across the top."'),
    ('Hero number', 'The single most important figure, oversized — the one number a skimmer leaves with.', '"Make on-time % the hero number."'),
    ('Delta', 'The change vs the previous period, shown beside the value (▲ +0.3 pt).', '"Each tile shows the delta vs last month."'),
    ('Sparkline', 'A tiny, axis-less trend line inside a tile or table row — trend without a full chart.', '"Add a 12-month sparkline inside each tile."'),
    ('Time series', 'A line chart of a value over time — the "is it getting better?" view.', '"A monthly time series of defect rate, one line per supplier."'),
    ('Ranked bars', 'A bar chart sorted by value — the "who is biggest / worst?" view.', '"Ranked bars of return rate by site, worst first."'),
    ('Stacked bar', 'One bar split into parts — composition and total in the same mark.', '"Stack the bar by supplier so I see each site\'s mix."'),
    ('Heatmap', 'A grid colored by value — patterns across two dimensions at a glance (site × month).', '"A site-by-month heatmap of on-time %."'),
    ('Target line', 'The reference line a metric should stay above or below; also called a threshold.', '"Draw the 2% target line on the trend chart."'),
    ('Traffic-light status', 'Color that encodes state — on target / warning / breach — ALWAYS paired with an icon or label, never color alone.', '"Traffic-light the tiles vs target, with a label, not just color."'),
    ('Filter / slicer', 'The control that narrows every view at once (site, supplier). "Slicer" is the Power BI / Excel word.', '"Site and Supplier filters that apply to all views."'),
    ('Date-range picker', 'The filter for time — from/to, or presets like "last 3 months".', '"A date-range picker with a last-quarter preset."'),
    ('Cross-filtering', 'Clicking a mark in one chart filters the other views to match.', '"Clicking a site\'s bar should filter the trend chart."'),
    ('Drill-down / drill-through', 'Drill-DOWN steps a chart down a hierarchy (year → month, site → supplier). Opening the raw rows behind a number is drill-THROUGH (Power BI) or View Data (Tableau). In an AI-built file either word works; in BI tools they are different buttons.', '"Drill down from site to supplier; drill through from each tile to its rows."'),
    ('Tooltip', 'The detail card that appears on hover — exact values without cluttering the chart.', '"Tooltips with exact value, n, and the formula."'),
    ('Legend', 'The key mapping colors/shapes to series — every multi-series chart needs one.', '"A legend, plus direct labels on the last points."'),
    ('Detail grid', 'The sortable, searchable table of raw rows behind the charts — the digger\'s view.', '"A sortable detail grid under the charts."'),
    ('Grain', 'What ONE row of the data represents (here: one month × site × supplier). Every correct denominator depends on it.', '"State the grain before proposing any KPI."'),
    ('As-of date', 'When the data was last refreshed, stated on the page. A dashboard without one is stale-but-credible.', '"Footer: as-of date, source, owner, refresh cadence."'),
]
for term, what, ask in DASH_VOCAB:
    td.append([term, what, ask])
    td.cell(row=td.max_row, column=1).font = Font(bold=True, color='0E7C7B')
for row in td.iter_rows():
    for c in row:
        c.alignment = Alignment(vertical='top', wrap_text=True)

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

# ================================================================ R17: the five-task
# course sequence (60-minute facilitated course). The training determines the
# exercises; these tabs carry the reusable prompts; the builder mirrors them.
# Legacy tabs (README, EX1..EX7, G2, EX-Quotes, EX-Email, EX-Dashboard, EX-Report,
# BONUS-Ladder, PLAYBOOK) stay for the long-format course — INDEX marks them optional.

# -- Data_Clean: the 144 detail rows, TOTAL excluded, 'n/a' -> blank (missing stays missing)
dc = wb.create_sheet('Data_Clean')
dc.append(HDR)
detail_rows = []
for r in ws.iter_rows(min_row=2, values_only=True):
    if r[0] == 'TOTAL':
        continue
    rr = list(r)
    if rr[6] == 'n/a':
        rr[6] = None
    detail_rows.append(rr)
    dc.append(rr)
for c in range(1, len(HDR) + 1):
    cell = dc.cell(row=1, column=c)
    cell.font = Font(bold=True, color='FFFFFF')
    cell.fill = PatternFill('solid', fgColor='1E2761')
    dc.column_dimensions[get_column_letter(c)].width = 16
dc.freeze_panes = 'A2'

# -- independently computed key numbers (never hardcoded twice)
def _agg(rows_, keyfn):
    out = {}
    for r in rows_:
        d = out.setdefault(keyfn(r), {'u': 0, 'ret': 0, 'def': 0, 'cost_w': 0.0, 'ot': []})
        d['u'] += r[3]; d['ret'] += r[4]; d['def'] += r[5]
        d['cost_w'] += r[3] * r[7]; d['ot'].append(r[8])
    return out
SUP_AGG = _agg(detail_rows, lambda r: r[2])
TOT_U = sum(v['u'] for v in SUP_AGG.values()); TOT_R = sum(v['ret'] for v in SUP_AGG.values())
TOT_D = sum(v['def'] for v in SUP_AGG.values())
assert (TOT_U, TOT_R) == (tot_ship, tot_ret)

prompt_tab('1-Analyze-Data', 'Task 1 of 5 · Analyze the data — one question, one improving prompt (Data tab of THIS workbook)', [
    ('STEP 0 · STARTER', 'Analyze the supplier data and tell me which supplier is worst.',
     'Run it once, then list what it decided FOR you: which rows, which metric, what "worst" means. Those gaps are the requirements you add next.'),
    ('STEP 1 · IMPROVED', 'Use Course_Workbook.xlsx, Data tab, detail rows only — exclude the TOTAL row (144 rows; one Inspection_Hours cell is "n/a": treat it as missing, not zero, and disclose it). One row = one month × site × supplier; period 2025-09 to 2026-08 inclusive. Question: which supplier has the highest RETURN RATE, defined as total Units_Returned ÷ total Units_Shipped per supplier over the full period — computed from sums, never by averaging monthly percentages. Keep Defects_Found separate from returns; do not add them together. Rank the three suppliers showing numerator and denominator, reconcile total shipped and returned against the TOTAL row, and state one limitation of the comparison. Then stop.',
     'Each added line fixes one named weakness: source scope · row grain · period · metric definition · denominator rule · missing-data rule · separate measures · reconciliation · limitation. (Requirement types: data & provenance, method & business rules, quality & acceptance.)'),
    ('STEP 2 · TREND', 'For the highest-return supplier: monthly return rate (that month\'s returns ÷ that month\'s shipments) for 2025-09 to 2026-08, as a table. Is it improving, worsening, or volatile? Describe the pattern only — do not claim a cause.',
     'Change over time, with the denominator stated per month and causal claims off-limits.'),
    ('STEP 3 · SITES', 'Return rate by site (same definition, same period), ranked. Do particular sites drive the supplier difference? Compare only on equal scope.',
     'Segmentation — every comparison on the same filter scope.'),
    ('STEP 4 · DENOMINATORS', 'Can this data support an overall on-time delivery rate? Explain using only the columns available, and name the extra data that would be needed.',
     'Expected answer: NO. On_Time_Percent is a monthly percentage with no delivery counts, so its average is not a true overall delivery rate. This is the denominator lesson.'),
    ('TRANSFER', 'Rewrite the improved prompt for a dataset from your own work: keep every requirement type, change only the specifics.',
     'The requirement types are the transferable part; the filled prompt is your reusable asset.'),
], note=f'Check yourself (expected output): 144 detail rows · {TOT_U:,} shipped · {TOT_R} returns · {TOT_D:,} defect occurrences (a separate measure). Highest return rate: Bravo Plastics ≈ {SUP_AGG["Bravo Plastics"]["ret"]/SUP_AGG["Bravo Plastics"]["u"]*100:.3f}%. Full worked key: tab KEY-Analysis (instructor). The analysis feeds tasks 2 and 3 — save it.')

prompt_tab('2-Build-Dashboard', 'Task 2 of 5 · Build the dashboard — specify behavior in plain language (uses Supplier_Data_Clean.csv)', [
    ('PROMPT V1 · CORE', 'From the attached Supplier_Data_Clean.csv (144 rows, one per month × site × supplier, period 2025-09 to 2026-08; one Inspection_Hours value is blank — missing, not zero), build ONE self-contained HTML file that works offline from disk. Views: summary tiles (units shipped, units returned, return rate, defect rate — rates = sums ÷ sums), one chart, and a sortable table of the records. Embed the data in the file; compute every number from the embedded records — nothing hard-coded. Footer: metric definitions, the snapshot date, and "static data snapshot, not a live system".',
     'The core artifact: input contract, metric definitions, delivery constraints. Interactions come as revisions.'),
    ('PROMPT V2 · BEHAVIOR', 'Add these controls, wired so one selection re-scopes EVERY view — tiles, chart, and table always agree: a month-range selector, inclusive endpoints, defaulting to the full range ("show records between the selected start and end months") · Supplier and Site filters ("let me select one or more suppliers or sites") · a comparison switch ("switch the comparison between supplier and site") · a granularity switch ("switch the trend between monthly and quarterly views") · a metric selector ("switch between units shipped, defect rate, and return rate") · drill-down ("click a chart segment to show its underlying records") · ranking ("rank suppliers from highest to lowest on the selected measure") · Reset ("clear all selections and restore the full dataset").',
     'The behavior vocabulary — every quoted phrase is reusable wording. Use Type/Class/Status controls only when the source really has those fields; this dataset does not.'),
    ('PROMPT V3 · STATES', 'Show the active selections at all times. An empty selection must say "no matching records" — distinguish it from a real zero. Missing values stay blank; a zero denominator shows "—", never an error.',
     'Empty, missing, and zero are three different situations; the dashboard must say which one is on screen.'),
    ('THE CHECK', 'Filter to Site = Berlin, Supplier = Bravo Plastics, months 2026-03 to 2026-08. Expect exactly 6 records, 8,575 units shipped, 21 returns, return rate 0.245% — in the tiles, the chart, AND the table. Verify independently by filtering the Data tab the same way.',
     'One verified filtered result beats admiring the design. The prepared output runs this exact self-check in its footer.'),
    ('WHEN EACH CONTROL HELPS', 'Month range + granularity answer "when did it change?" · category filters and compare-by answer "who is different?" · the metric selector answers "different on what?" · drill-down answers "which records back this number?" · Reset makes exploration safe.',
     'Add a control only when its business question matters — controls are questions, not decoration.'),
], note='The page provides the structure (HTML); JavaScript supplies the interactive behavior — you specify behavior in plain language and let the assistant write the code. Prepared output: Supplier_Quality_Dashboard.html (open it offline; footer self-check must say PASSED). Needs a code-capable tool — if yours only chats, hand this spec to IT.')

prompt_tab('3-Present-Findings', 'Task 3 of 5 · Present the findings — a five-slide mock management deck (uses Task 1\'s verified analysis)', [
    ('THE PROMPT', 'Create an editable five-slide management presentation using only the verified supplier analysis. The audience must decide what follow-up is warranted. Cover: the business question and scope · the supplier comparison · one useful time or site view · a proposed follow-up · limitations with next steps. Give each slide one main message, readable evidence, accurate units and reporting period, and brief speaker notes. Preserve uncertainty and missing-data limits. Do not invent causes or unsupported benefits. Check every number against the analysis and inspect the exported slides for clipping and readability.',
     'Requirement types: purpose & audience · scope & slide count · story structure · message hierarchy · data fidelity · chart semantics · speaker notes · editability & delivery.'),
    ('THE SEPARATION RULE', 'Findings are what the workbook supports; recommendations are labeled proposals. No invented causes, benefits, or commitments anywhere.',
     'The trust move that survives every audience question.'),
    ('THE CHECKS', 'Count five slides and map each to the coverage list. Reconcile every displayed number to the analysis. Read only the titles — do they tell the story alone? Open the exported file: clipping, readability at projection size, notes present on every slide.',
     'Acceptance evidence, artifact-shaped: coverage, fidelity, narrative, delivery.'),
], note='Prepared output: Supplier_Quality_Mock_Presentation.pptx — the sample this prompt produced; audit it against THE CHECKS before reusing the prompt. Keep the mock business deck visually distinct from the course deck.')

prompt_tab('4-Summarize-Email', 'Task 4 of 5 · Summarize the email conversation (uses Packaging_Change_Thread.txt)', [
    ('THE PROMPT', 'Review the selected conversation about [topic] using only the messages and attachments you can access. Create a brief of the current situation, followed by tables of decisions and actions. For each decision: status, conditions, supporting message. For each action: task, explicitly stated owner, due date, status, supporting message. Distinguish current dates from superseded dates. List unanswered questions, conflicts, missing information, and referenced attachments you cannot access. Preserve approval conditions. Write "Not stated" for missing details. Separate source facts from your interpretation. End with the next clarification needed. If requested, draft a reply for review; do not send it.',
     'Requirement types: source scope · current state · decisions & conditions · actions & ownership · date meaning · evidence traceability · attachments · authority boundary.'),
    ('FOLLOW-UP · REPLY', 'Draft my reply for review: answer what the thread can answer, confirm decisions WITH their conditions, and propose one next step per unresolved item. Leave [brackets] where I must decide. Do not send anything.',
     'The optional follow-up. A draft is the boundary — sending stays human.'),
    ('THE TRAPS', 'A good summary catches all of these: the change date moved Sep 25 → Oct 2, conditional on quality sign-off · the trial date is Sep 25 (superseding Sep 18) · the 18,000 cap still applies and freight is NOT approved · Luis\'s revised plan is due Sep 16 · freight responsibility is unresolved · the drawing is referenced but not accessible.',
     'Compare with the deck\'s answer key (slides 88–89) or tab KEY-Email.'),
], note='Source: Packaging_Change_Thread.txt (paste it into any approved assistant). Native path, verified Sep 2026 (notes/research/r28): Outlook\'s "Summary by Copilot" on an open thread, with numbered citations — availability depends on your organization\'s Copilot license, and the pasted-text version always works. Never practice on real confidential threads.')

prompt_tab('5-Explain-Clearly', 'Task 5 of 5 · Explain a topic clearly — plain language with fidelity (uses exercise-data/plain-language/)', [
    ('THE PROMPT', 'Using [source], explain [topic] so a reader at a fifth-grade reading level can understand it. State the main idea first. Use familiar words, short sentences, meaningful headings, and one concrete example. Define necessary technical terms when first used. Use an analogy only if it is accurate, and explain where it stops being useful. Preserve important conditions and uncertainty. Do not invent facts or use a childish tone. End with three comprehension questions and a short answer key. Check the explanation against the source and identify any simplification that changes the meaning.',
     'Requirement types: reader & purpose · vocabulary · structure · examples & analogies · fidelity & caveats · tone · comprehension check.'),
    ('LIVE TOPIC', 'Source: exercise-data/plain-language/inventory_replenishment.md (its SOURCE section). Topic: reorder points and safety stock.',
     'The demonstration topic — a sample output with its own fidelity note sits in the same file.'),
    ('VARIATIONS', 'The water cycle · how an internet message travels — sources, sample outputs, and keys in exercise-data/plain-language/.',
     'Different content, identical requirement types — that is the point.'),
    ('THE CHECK', 'Main idea in the first sentence? Every surviving technical term defined at first use? Analogy limit stated? Conditions preserved (compare sentence by sentence)? Three questions answerable from the text alone? Clear adult tone?',
     'Readability scores are supporting evidence; a human comprehension check is the real test.'),
], note='Respectful language for adult readers throughout — plain is not childish. Simplifications that change meaning are defects, and finding them is part of the exercise.')

# -- instructor keys (clearly separated)
def key_tab(name, title, rows):
    t = wb.create_sheet(name)
    t.append([title]); t['A1'].font = Font(bold=True, size=12, color='AF3230')
    t.append(['INSTRUCTOR MATERIAL — do not distribute before the exercise.'])
    t['A2'].font = Font(bold=True, color='AF3230')
    t.append([])
    for r in rows:
        t.append(list(r))
        t.cell(row=t.max_row, column=1).font = Font(bold=True, color='0A5B5A')
    t.column_dimensions['A'].width = 26
    t.column_dimensions['B'].width = 100
    for row in t.iter_rows():
        for c in row:
            c.alignment = Alignment(vertical='top', wrap_text=True)
    return t

_sup_line = lambda s: (f'{SUP_AGG[s]["u"]:,} units · {SUP_AGG[s]["ret"]} returns · return rate '
                       f'{SUP_AGG[s]["ret"]/SUP_AGG[s]["u"]*100:.3f}% · {SUP_AGG[s]["def"]:,} defect occurrences · '
                       f'units-weighted cost ${SUP_AGG[s]["cost_w"]/SUP_AGG[s]["u"]:.4f} · '
                       f'unweighted mean monthly on-time {sum(SUP_AGG[s]["ot"])/len(SUP_AGG[s]["ot"]):.2f}% (NOT an overall delivery rate)')
key_tab('KEY-Analysis', 'Instructor key · Task 1 — supplier analysis (all values computed from the Data tab at build time)', [
    ('TOTALS', f'{TOT_U:,} units shipped · {TOT_R} returns (overall {TOT_R/TOT_U*100:.3f}%) · {TOT_D:,} defect occurrences. 144 detail rows; the TOTAL row reconciles exactly.'),
    ('Alpha Components', _sup_line('Alpha Components')),
    ('Bravo Plastics', _sup_line('Bravo Plastics')),
    ('Cardinal Metals', _sup_line('Cardinal Metals')),
    ('STEP 2 · TREND', 'Bravo Plastics monthly return rate is elevated and volatile — peak ≈0.737% (2026-04), quiet months ≈0.14% (2026-06/07), most recent ≈0.465% (2026-08). Accept "volatile, no steady improvement"; reject any causal claim.'),
    ('STEP 4 · DENOMINATORS', 'Correct answer: an overall on-time delivery rate CANNOT be computed — On_Time_Percent has no delivery counts to weight by. Needed: deliveries (or shipments) per month as the denominator. An averaged percentage must be labeled "unweighted mean of monthly percentages".'),
    ('COMMON WRONG TURNS', 'Averaging monthly return-rate percentages (wrong denominator) · adding defects + returns as "defective units" (double counting different measures) · treating the "n/a" as zero · including the TOTAL row (double counting) · claiming Bravo\'s packaging CAUSES returns (not in the data).'),
    ('MISSING VALUE', 'Exactly one Inspection_Hours cell is "n/a". Missing ≠ zero; it does not affect return-rate math, and any analysis that excludes it must say so.'),
])
key_tab('KEY-Email', 'Instructor key · Task 4 — packaging-change thread', [
    ('EXPECTED BRIEF', 'Change planned for Oct 2 (supersedes Sep 25), pending Ben\'s quality sign-off, which waits on the drawing. Trial targeted Sep 25 (supersedes Sep 18); Luis\'s revised plan due Sep 16; material arrives Sep 23. Finance approval only within the 18,000 cap; freight responsibility unresolved.'),
    ('DECISIONS', 'Oct 2 change: proposed/planned, NOT finally approved (conditional on sign-off) · budget: approved ≤18,000 + quality condition, freight extras explicitly not approved · trial Sep 25: current plan.'),
    ('ACTIONS', 'Luis — revised trial plan — Sep 16 — committed · Ben — quality sign-off — "Not stated" — open, depends on drawing access · freight decision — owner "Not stated" — open · drawing to Ben — claimed sent, attachment not accessible.'),
    ('THE FOUR TRAPS', '1) Two different date changes (change date vs trial date — do not conflate Oct 2 and Sep 25). 2) Conditional approval (18,000 + sign-off; bare "approved" is wrong). 3) Freight question never answered. 4) Drawing referenced but not supplied — its content must not be summarized.'),
    ('FULL VERSION', 'deliverables/exercise-data/instructor-keys/Packaging_Change_Expected_Brief.md and deck slides 88–89.'),
])

# -- INDEX tab, placed first
ix = wb.create_sheet('INDEX', 0)
IX = [
    ['FROM PROMPTS TO AGENTS — PACKAGE INDEX (60-minute facilitated course)'],
    [''],
    ['OPEN IN THIS ORDER', ''],
    ['1', 'From_Prompts_to_Agents_Facilitated_60_Minute.pptx — the course (70 live slides + reference appendix; speaker notes carry MODE/TIME/purpose).'],
    ['2', 'This workbook — tabs 1-Analyze-Data … 5-Explain-Clearly are the five course tasks, in order; Data = raw records, Data_Clean = the checked detail set the tasks use.'],
    ['3', 'Prepared outputs — Supplier_Quality_Dashboard.html (task 2) and Supplier_Quality_Mock_Presentation.pptx (task 3): every live demonstration has a fallback.'],
    ['4', 'Sources — Supplier_Data_Clean.csv · Packaging_Change_Thread.txt · plain-language/ (task 5 topics) · Quote_*.pdf (optional extension).'],
    ['5', 'Reference — Elements_of_Prompting_Field_Guide.pdf · Prompt_Anatomy_Cheat_Sheet.pdf · Prompt_Element_Taxonomy_Reference.pdf · Prompt_Template_Creator.html (the builder) · Requirements_by_Artifact.md.'],
    [''],
    ['INSTRUCTOR ONLY', 'Tabs KEY-Analysis and KEY-Email · exercise-data/instructor-keys/ · the facilitation plan. Keep these out of participant hand-outs.'],
    [''],
    ['THE FIVE TASKS', 'Analyze spreadsheet data → build an interactive dashboard → prepare a presentation → summarize an email conversation → explain a topic clearly. One fictional supplier case connects tasks 1–3; the builder (Prompt_Template_Creator.html) offers the same five task families.'],
    [''],
    ['LEGACY / OPTIONAL', 'Tabs README, EX1-TwoModes … EX7-MoE, G2-DataAnalysis, EX-Quotes, EX-Email, EX-Dashboard, EX-Report, BONUS-Ladder and PLAYBOOK belong to the long-format course and remain usable as optional extensions.'],
    [''],
    ['DATA NOTE', 'All data and names are fictional, generated for training (seeded — stable across rebuilds). The Data tab TOTAL row and one "n/a" Inspection_Hours cell are deliberate teaching quirks.'],
]
for row in IX:
    ix.append(row)
ix['A1'].font = Font(bold=True, size=13, color='0E7C7B')
for rn in (3, 10, 12, 14, 16):
    ix.cell(row=rn, column=1).font = Font(bold=True)
    ix.cell(row=rn, column=2).font = Font(bold=True)
ix.column_dimensions['A'].width = 20
ix.column_dimensions['B'].width = 118
for row in ix.iter_rows():
    for c in row:
        c.alignment = Alignment(vertical='top', wrap_text=True)

# -- sheet order: INDEX · Data · Data_Clean · tasks 1-5 · keys · legacy
ORDER = ['INDEX', 'Data', 'Data_Clean', '1-Analyze-Data', '2-Build-Dashboard', '3-Present-Findings',
         '4-Summarize-Email', '5-Explain-Clearly', 'KEY-Analysis', 'KEY-Email', 'README']
rest = [s.title for s in wb._sheets if s.title not in ORDER]
wb._sheets = [wb[t] for t in ORDER + rest]

xlsx_path = os.path.join(OUT, 'Course_Workbook.xlsx')
wb.save(xlsx_path)
print('wrote', xlsx_path, f'({n_data_rows} data rows · {len(wb.sheetnames)} tabs: INDEX + Data/Data_Clean + 5 tasks + 2 instructor keys + legacy)')

# NOTE (v1.13, owner request): the standalone Playbook_One_Pager.pdf was retired — the
# playbook now lives merged in the Field Guide (part 5, the full works/myth/expired
# compendium with the why per line) and the cheat sheet (compact box). The PLAYBOOK tab
# above remains the sources reference the slides point to.
