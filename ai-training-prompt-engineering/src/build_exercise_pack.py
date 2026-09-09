# Builds the v1.5 hands-on exercise pack (all data fictional, generated, generic):
#   deliverables/exercise-data/Data_Analytics_Practice.xlsx   (raw data, NO formulas - the AI does the math)
#   deliverables/exercise-data/Quote_Alpha_Components.pdf     (three comparable supplier quotations,
#   deliverables/exercise-data/Quote_Bravo_Plastics.pdf        deliberately non-comparable at first
#   deliverables/exercise-data/Quote_Cardinal_Metals.pdf       glance: currency/per-1000/EXW traps)
#   deliverables/exercise-data/Email_Thread_Packaging_Change.txt / .pdf  (messy 10-message thread)
# Deterministic (seeded) so the numbers on the walkthrough slides stay true after a rebuild.
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
    ['Data Analytics Practice File — "From Prompts to Agents" training'],
    [''],
    ['WHAT THIS IS', 'Twelve months of fictional supplier-delivery data across four sites and three suppliers. Built for practicing AI data analysis (Copilot, chat assistants with file upload, or a company RAG assistant).'],
    ['HOW TO USE IT', 'Upload the file (or paste the deliveries sheet), then follow the prompt sequence from the Part 4 walkthrough slides: profile first, then ask numbered questions.'],
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
    ['1', 'The last row of the deliveries sheet is a TOTAL row — exclude it from any calculation.'],
    ['2', 'One Inspection_Hours cell contains the text "n/a" — decide and state how you handle it.'],
    [''],
    ['All names and numbers are fictional and generated for training. No real company data.'],
]
for row in readme:
    rd.append(row)
rd.column_dimensions['A'].width = 22
rd.column_dimensions['B'].width = 105
rd['A1'].font = Font(bold=True, size=13, color='0E7C7B')
for r in (6, 17):
    rd.cell(row=r, column=1).font = Font(bold=True)
    rd.cell(row=r, column=2).font = Font(bold=True)
for row in rd.iter_rows():
    for c in row:
        c.alignment = Alignment(vertical='top', wrap_text=True)

ws = wb.create_sheet('deliveries')
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
xlsx_path = os.path.join(OUT, 'Data_Analytics_Practice.xlsx')
wb.save(xlsx_path)
print('wrote', xlsx_path, f'({ws.max_row - 2} data rows + header + TOTAL quirk row)')

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
