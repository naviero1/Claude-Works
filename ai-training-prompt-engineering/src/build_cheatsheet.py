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
    cv.drawRightString(W - M, 0.18 * inch, 'Menus: references/Requirements_by_Artifact.md · source: src/build_cheatsheet.py')
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
    ('Missing info & boundaries:', 'if [gap or conflict]: state it, ask, or stop. Actions needing review: [actions].'),
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
    ('After:', '“Data tab, detail rows only (exclude the TOTAL row; the “n/a” is missing, not zero). Return rate = total returns ÷ total shipped per supplier, 2025-09 to 2026-08 — sums, never averaged percentages; defects stay separate. Rank, show numerator and denominator, reconcile to the TOTAL row, state one limitation, stop.”'),
    ('Why it wins:', 'each added line is a requirement type fixing one named weakness.'),
], AMBER_T, AMBER))

# ---------------- RIGHT: the tasks + checking + delegation ----------------
E.append(FrameBreak())
E.append(Paragraph('RUN IT — five tasks, one habit', S_mode))
E.append(Paragraph('produce the artifact, then check it against its own acceptance evidence', S_modesub))

E.append(box('THE FIVE COURSE TASKS (workbook tabs 1–5)', [
    ('1 Analyze data', '— define the metric and denominator; reconcile; state limits.'),
    ('2 Build a dashboard', '— specify behavior in plain language: range, filters, grouping, metric switch, drill-down, Reset; one selection re-scopes every view.'),
    ('3 Present findings', '— one message per slide; findings separated from recommendations; nothing invented.'),
    ('4 Summarize email', '— current state; decisions WITH conditions; owners and dates; “Not stated” for gaps; replies stay drafts.'),
    ('5 Explain clearly', '— fifth-grade reading level, adult tone; analogy limits stated; meaning preserved; 3-question check.'),
], TEAL_T))
E.append(gap)

E.append(box('ACCEPTANCE CHECKS — BEFORE YOU TRUST IT', [
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
    ('The boundary:', 'prompt instructions request compliance — actual permissions and configured controls determine what a tool can DO. Reversible → proceed; irreversible → ask.'),
], AMBER_T, AMBER))
E.append(gap)

E.append(box('SAVE WHAT WORKS', [
    ('Each reusable prompt:', 'name · owner · version · the example that proved it · its acceptance check.'),
    ('Where:', 'the Course Workbook carries the five course prompts; the Template Creator and Configurator offer the same five task families with their requirement menus.'),
    ('Refresh:', 'facts about products and models expire — date them and re-verify before big reuse.'),
], GREEN_T, GREEN))

doc.build(E)
print('cheat sheet written:', out)
