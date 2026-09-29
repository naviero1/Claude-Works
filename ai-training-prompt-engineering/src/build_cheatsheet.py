#!/usr/bin/env python3
# One-page printable cheat sheet — "From Prompts to Agents" (R17: requirements-first).
# Editable source: this file. Rebuild: python3 build_cheatsheet.py
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, FrameBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FD = '/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DV', FD + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DV-B', FD + 'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DV-I', FD + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVSer-B', FD + 'DejaVuSerif-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Mono-B', FD + 'DejaVuSansMono-Bold.ttf'))
pdfmetrics.registerFontFamily('DV', normal='DV', bold='DV-B', italic='DV-I')

INK = colors.HexColor('#232A31'); SLATE = colors.HexColor('#46545F'); MUTE = colors.HexColor('#7A8790')
TEAL = colors.HexColor('#0E7C7B'); TEAL_D = colors.HexColor('#0A5B5A'); TEAL_T = colors.HexColor('#E4F0EF')
PANEL = colors.HexColor('#F2F5F6'); LINE = colors.HexColor('#DCE3E6')
AMBER = colors.HexColor('#B96A1B'); AMBER_T = colors.HexColor('#FBF0E0')
RED = colors.HexColor('#AF3230'); RED_T = colors.HexColor('#F9E9E8')
GREEN = colors.HexColor('#3B8560'); GREEN_T = colors.HexColor('#E7F2EC')
DARK = colors.HexColor('#1C272E')

W, H = letter
M = 0.38 * inch
HEADER_H = 0.62 * inch
FOOTER_H = 0.32 * inch
GUT = 0.22 * inch
colw = (W - 2 * M - GUT) / 2

out = os.path.join(os.path.dirname(__file__), '..', 'deliverables', 'From_Prompts_to_Agents_Cheat_Sheet.pdf')

S_head = ParagraphStyle('h', fontName='DV-B', fontSize=8.4, leading=10.8, textColor=TEAL_D, spaceAfter=2)
S_body = ParagraphStyle('b', fontName='DV', fontSize=7.4, leading=9.9, textColor=SLATE, spaceAfter=1.5)
S_mode = ParagraphStyle('m', fontName='DV-B', fontSize=10, leading=12, textColor=TEAL_D, spaceAfter=1)
S_modesub = ParagraphStyle('ms', fontName='DV-I', fontSize=7.0, leading=8.8, textColor=MUTE, spaceAfter=4)


def box(title, rows, fill, title_color=TEAL_D):
    flow = [Paragraph(title, ParagraphStyle('t', parent=S_head, textColor=title_color))]
    for k, v in rows:
        txt = f'<font face="DV-B" color="#232A31">{k}</font> {v}' if k else v
        flow.append(Paragraph(txt, S_body))
    t = Table([[flow]], colWidths=[colw])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), fill),
        ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
    ]))
    return t


def header_footer(cv, doc):
    cv.saveState()
    cv.setFillColor(DARK)
    cv.rect(0, H - HEADER_H, W, HEADER_H, stroke=0, fill=1)
    cv.setFillColor(colors.HexColor('#5FB8B0')); cv.setFont('DV-B', 7)
    cv.drawString(M, H - 0.24 * inch, 'FROM PROMPTS TO AGENTS  ·  CHEAT SHEET  ·  SEPTEMBER 2026')
    cv.setFillColor(colors.white); cv.setFont('DVSer-B', 14.5)
    cv.drawString(M, H - 0.48 * inch, 'A prompt is a small work specification')
    cv.setFillColor(MUTE); cv.setFont('DV', 6.2)
    # measured at 6.2pt: left+right leave a >15pt gap — the two lines cannot collide
    cv.drawString(M, 0.18 * inch, 'Verification = meets the written criteria · Validation = serves the actual need.')
    cv.drawRightString(W - M, 0.18 * inch, 'Full menus per artifact: references/Requirements_by_Artifact.md')
    cv.restoreState()


doc = BaseDocTemplate(out, pagesize=letter, leftMargin=M, rightMargin=M,
                      topMargin=HEADER_H + 0.12 * inch, bottomMargin=FOOTER_H)
fh = H - HEADER_H - 0.12 * inch - FOOTER_H
f1 = Frame(M, FOOTER_H, colw, fh, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
f2 = Frame(M + colw + GUT, FOOTER_H, colw, fh, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id='two', frames=[f1, f2], onPage=header_footer)])

E = []
gap = Spacer(1, 6)

# ---------------- LEFT: write the specification ----------------
E.append(Paragraph('WRITE IT — like a requirement', S_mode))
E.append(Paragraph('task and audience first · then only the requirements that resolve ambiguity', S_modesub))

E.append(box('THE SKELETON — EVERY PROMPT', [
    ('Purpose & audience:', 'help [reader] make [decision] or complete [task].'),
    ('Sources & scope:', 'use [source / version / period]; include [scope]; exclude [items].'),
    ('Selected requirements:', 'only the types that resolve ambiguity for THIS artifact — a simple task needs a few, not all.'),
    ('Acceptance evidence:', 'check [specific result] against [source, calculation, or observable test].'),
    ('Missing info & finish line:', 'if [gap]: write “Not stated” and list it; if [conflict]: ask or stop. Answer, report limitations, then stop. Actions needing review: [actions].'),
], TEAL_T))
E.append(gap)

E.append(box('REQUIREMENT TYPES — THE MENU (pick, don’t fill)', [
    ('Functional behavior', '— what it must do: filter, calculate, extract, compare, explain.'),
    ('Data & provenance', '— allowed inputs, definitions, period, traceability.'),
    ('Scope & exclusions', '— in, out, and explicitly outside the task.'),
    ('Audience & use', '— who uses it, for which decision.'),
    ('Role & working behavior', '— a perspective plus observable conduct; a title alone is weak.'),
    ('Content & completeness', '— required topics, fields, limitations.'),
    ('Method & business rules', '— formulas, denominators, missing-data treatment.'),
    ('Structure & interface', '— sections, tabs, slides, columns, controls.'),
    ('Tone & presentation', '— voice, reading level, units, formats.'),
    ('Accessibility & usability', '— labels, contrast, keyboard, understandable language.'),
    ('Quality & acceptance', '— observable correctness and completeness criteria.'),
    ('Constraints & authority', '— allowed tools, approvals, stop conditions.'),
    ('Delivery & compatibility', '— file type, editability, offline use, destination.'),
    ('Maintenance & reuse', '— refresh procedure, versions, reusable parameters.'),
], PANEL))
E.append(gap)

E.append(box('REQUIREMENT QUALITY — IS EACH ONE…', [
    ('', 'necessary · clear · complete enough · consistent · feasible · singular · <b>verifiable</b>. A requirement you cannot check is a wish. Separate required outcomes from preferences; make trade-offs explicit.'),
], GREEN_T, GREEN))
E.append(gap)

E.append(box('BEFORE / AFTER — THE SUPPLIER CASE', [
    ('Before:', '“Analyze the supplier data and tell me which supplier is worst.” — the model picks the rows, the metric, and “worst” for you, silently.'),
    ('After — inspect:', '“Before calculating anything, inspect the file. Tell me what one row represents, how many detail rows it contains, whether any values are missing, and whether any total or summary row could be counted twice. Tell me what you would include or exclude, then wait.”'),
    ('After — analyze:', '“Using detail rows only, calculate each supplier’s return rate as total Units_Returned divided by total Units_Shipped. Rank suppliers from highest to lowest. Show the totals used, reconcile the overall totals to the source file, and state one limitation of the comparison.”'),
    ('Why it wins:', 'each added line is a requirement type fixing one named weakness — and nothing is calculated before the scope is agreed.'),
], AMBER_T, AMBER))

# ---------------- RIGHT: the tasks + checking + delegation ----------------
E.append(FrameBreak())
E.append(Paragraph('RUN IT — the course tasks, one habit', S_mode))
E.append(Paragraph('produce the artifact, then check it against its own acceptance evidence', S_modesub))

E.append(box('THE COURSE TASKS (deck order · workbook tab)', [
    ('Analyze data', '— inspect first, then wait; return rate from totals, detail rows only; rank, reconcile to the source, state one limitation; follow-up = findings, not causes · 1-Analyze-Data.'),
    ('Excel charts', '— the returned workbook: Summary sheet, native editable charts, traceable formulas, totals reconciled before it returns · Excel-Charts.'),
    ('Build a dashboard', '— describe the behavior: date range, supplier and site filters, metric selector, trend chart, sortable table, reset; every filter updates every view · 2-Build-Dashboard.'),
    ('Present findings', '— five slides, one main message each; findings separated from recommendations; no invented causes or commitments · 3-Present-Findings.'),
    ('Summarize email', '— current status; decisions WITH conditions; owners and due dates; “Not stated” for gaps; cite sender and date; send nothing · 4-Summarize-Email.'),
    ('Extract quotes', '— values verbatim, original currencies, “Not stated” when absent, source file and page per value; no ranking yet · Quote-Extract.'),
    ('Compare quotes', '— normalize only with a supplied basis; formulas visible; no best quote until the basis is complete · Quote-Compare.'),
    ('Self-study', '— research workbook (Research) · explain a topic clearly (5-Explain-Clearly) — same discipline; Reference Deck.'),
], TEAL_T))
E.append(gap)

E.append(box('ACCEPTANCE CHECKS — BEFORE YOU TRUST IT', [
    ('The loop', '— PLAN the task and the success check · DO run the prompt against the supplied source · CHECK the result against evidence or a known calculation · ACT: fix the specific failure and rerun the affected check.'),
    ('Trace', '— one output number back to its source records.'),
    ('Recompute', '— one calculation independently (code or by hand).'),
    ('Reconcile', '— totals against a number you already trust.'),
    ('Exercise', '— every requested behavior once (filter, sort, reset, empty case).'),
    ('Coverage', '— compare against the requirement list; missing = not done.'),
    ('Read as the reader', '— can the audience act on it? That is validation.'),
    ('', 'Never accept “looks done”: ask for evidence — the test it ran and what it returned.'),
], PANEL))
E.append(gap)

E.append(box('ASK vs DELEGATE', [
    ('ASK', '— request an answer or draft; you read, check, decide. The specification above is enough.'),
    ('DELEGATE', '— assign bounded work: add the inputs register, the checks that stop the run, permissions, gates for irreversible steps, and the finished-report format.'),
    ('The boundary:', 'a prompt requests behavior; configured permissions and approvals restrict available actions. Reversible? proceed. Irreversible? ask.'),
], AMBER_T, AMBER))
E.append(gap)

E.append(box('SAVE WHAT WORKS', [
    ('Each reusable prompt:', 'name · owner · version · the example that proved it · its acceptance check.'),
    ('Where:', 'the Course Workbook carries every course prompt in a named tab, in deck order; the Prompt Template Creator (one HTML file) offers the same task families, plus explain-a-topic, with their requirement menus.'),
    ('Refresh:', 'facts about products and models expire — date them and re-verify before big reuse.'),
], GREEN_T, GREEN))

doc.build(E)
print('cheat sheet written:', out)
