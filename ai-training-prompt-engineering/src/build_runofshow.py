#!/usr/bin/env python3
# Run of Show — two 60-minute sessions (house style PDF)
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FD = '/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DV', FD + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DV-B', FD + 'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DVSer-B', FD + 'DejaVuSerif-Bold.ttf'))

INK = colors.HexColor('#232A31'); SLATE = colors.HexColor('#46545F'); MUTE = colors.HexColor('#7A8790')
TEAL = colors.HexColor('#0E7C7B'); TEAL_D = colors.HexColor('#0A5B5A'); TEAL_T = colors.HexColor('#E4F0EF')
PANEL = colors.HexColor('#F2F5F6'); LINE = colors.HexColor('#DCE3E6')
AMBER = colors.HexColor('#B96A1B'); AMBER_T = colors.HexColor('#FBF0E0'); DARK = colors.HexColor('#1C272E')
RED = colors.HexColor('#AF3230'); RED_T = colors.HexColor('#F9E9E8')

W, H = letter
M = 0.7 * inch
CW = W - 2 * M
out = os.path.join(os.path.dirname(__file__), '..', 'deliverables', 'Run_of_Show.pdf')

S = {
    'h1': ParagraphStyle('h1', fontName='DVSer-B', fontSize=15, leading=19, textColor=INK, spaceBefore=4, spaceAfter=5),
    'h2': ParagraphStyle('h2', fontName='DV-B', fontSize=10.5, leading=13.5, textColor=TEAL_D, spaceBefore=8, spaceAfter=3),
    'kicker': ParagraphStyle('k', fontName='DV-B', fontSize=7.6, leading=9.5, textColor=TEAL, spaceAfter=2),
    'body': ParagraphStyle('b', fontName='DV', fontSize=8.8, leading=12, textColor=SLATE, spaceAfter=4),
    'cell': ParagraphStyle('c', fontName='DV', fontSize=8.2, leading=10.8, textColor=SLATE),
    'cellb': ParagraphStyle('cb', fontName='DV-B', fontSize=8.2, leading=10.8, textColor=INK),
    'cellh': ParagraphStyle('ch', fontName='DV-B', fontSize=8.4, leading=11, textColor=TEAL_D),
}


def hf(cv, doc):
    cv.saveState()
    if doc.page == 1:
        cv.setFillColor(DARK); cv.rect(0, H - 0.95 * inch, W, 0.95 * inch, stroke=0, fill=1)
        cv.setFillColor(colors.HexColor('#5FB8B0')); cv.setFont('DV-B', 7.2)
        cv.drawString(M, H - 0.34 * inch, 'FROM PROMPTS TO AGENTS  ·  PRESENTER MATERIALS  ·  V1.1')
        cv.setFillColor(colors.white); cv.setFont('DVSer-B', 19)
        cv.drawString(M, H - 0.63 * inch, 'Run of Show — two one-hour sessions')
        cv.setFillColor(colors.HexColor('#A9BBC4')); cv.setFont('DV', 8.2)
        cv.drawString(M, H - 0.83 * inch, 'Minute-by-minute plan, demo scripts, contingency cuts, and the prep checklist.')
    else:
        cv.setFillColor(MUTE); cv.setFont('DV', 6.8)
        cv.drawString(M, H - 0.4 * inch, 'RUN OF SHOW · FROM PROMPTS TO AGENTS · V1.1')
    cv.setFillColor(MUTE); cv.setFont('DV', 6.8)
    cv.drawString(M, 0.3 * inch, 'Owner: Oscar Penny · deck: From_Prompts_to_Agents_Training.pptx (56 slides)')
    cv.drawRightString(W - M, 0.3 * inch, str(cv.getPageNumber()))
    cv.restoreState()


doc = BaseDocTemplate(out, pagesize=letter, leftMargin=M, rightMargin=M, topMargin=0.55 * inch, bottomMargin=0.5 * inch)
f1 = Frame(M, 0.5 * inch, CW, H - 0.95 * inch - 0.62 * inch, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
f2 = Frame(M, 0.5 * inch, CW, H - 0.5 * inch - 0.58 * inch, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id='first', frames=[f1], onPage=hf), PageTemplate(id='later', frames=[f2], onPage=hf)])
E = []


def timetable(title, rows):
    E.append(Paragraph(title, S['h1']))
    data = [[Paragraph('Clock', S['cellh']), Paragraph('Slides', S['cellh']), Paragraph('Segment', S['cellh']), Paragraph('Presenter notes', S['cellh'])]]
    for r in rows:
        data.append([Paragraph(r[0], S['cellb']), Paragraph(r[1], S['cell']), Paragraph(r[2], S['cellb']), Paragraph(r[3], S['cell'])])
    t = Table(data, colWidths=[CW * 0.09, CW * 0.09, CW * 0.28, CW * 0.54], repeatRows=1)
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), TEAL_T), ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, PANEL]),
                           ('GRID', (0, 0), (-1, -1), 0.4, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                           ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                           ('TOPPADDING', (0, 0), (-1, -1), 2.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5)]))
    E.append(t)


timetable('Session 1 — Prompts (60 min · slides 1–35)', [
    ('0:00', '1–2', 'Welcome + the map', 'The thesis in one breath: two modes, one craft. Point at the take-home card — everything shown today is theirs to keep.'),
    ('0:03', '3–6', 'Part 1 · history', 'Four eras fast (winters = earned skepticism); linger on the adoption tension stat: everyone chats, few industrialize.'),
    ('0:10', '7–12', 'Part 1 · concepts', 'Anchor three analogies hard: tokens = bricks, context = desk, RAG = open-book exam. The rest supports them.'),
    ('0:19', '13', 'Rep 1 · spot the missing elements', '3 min hard cap. Every gap the room names is an element they’ll meet in Part 3.'),
    ('0:22', '14–20', 'Part 2 · landscape', 'One line per vendor card, two rows of the matrix, then the evergreen habit: the private test set.'),
    ('0:31', '21', 'Rep 2 · private test set', 'SKIP BY DEFAULT — run only if ahead of schedule; the habit is already on slide 20.'),
    ('0:32', '22–25', 'Part 3 · anatomy + elements', 'The convergence table proves it’s not our opinion. Read two weak→strong pairs aloud — contrast teaches.'),
    ('0:40', '26–28', 'Part 3 · techniques + evidence', 'Slow down on sycophancy: “never reveal your preference” changes behavior today.'),
    ('0:46', '29–30', 'Rep 3 + Part 4 divider', 'Rebuild-one-line rep (3 min), then frame Part 4: two demos, the rest is handout.'),
    ('0:50', '31–33', 'G2 anatomy + Demo 1 · blind critique', 'The side-by-side silence moment is the punchline — let them read both answers.'),
    ('0:56', '34–35', 'Demo 2 · dashboard + handout pointer', 'If generation is slow, open the pre-built file and narrate the prompt. Close: “the other six templates work the same way.”'),
])
E.append(Spacer(1, 8))
timetable('Session 2 — Agents (60 min · slides 36–56)', [
    ('0:00', '36', 'Recap + homework check', 'Ask who ran the blind critique — one volunteer story beats any recap. 2 min, no more.'),
    ('0:03', '37–38', 'Part 5 · what an agent is', 'The loop + building blocks; agents adapt where scripts break.'),
    ('0:09', '39–40', 'The distinction + inheritance map', 'THE core content. Read two inheritance rows aloud (Task→mission, Stop→gates); the twelve blocks become inevitable.'),
    ('0:18', '41–42', 'Mission brief + worked example', 'Pick three blocks only: checks, gates, reporting. The gates story: errors caught at ascending cost.'),
    ('0:28', '43–44', 'Guardrails + standing memory', 'Reversible→act, irreversible→ask. Reuse-by-diff is the economics slide — briefs are investments.'),
    ('0:36', '45', 'Rep 5 · write one gate', 'Where the gate feels hard to write, the process was fuzzy — say it out loud.'),
    ('0:40', '46–49', 'Part 6 · managing prompts', 'The ladder + the promotion trigger (“explained it twice? package it”), storage map fast, governance card slowly.'),
    ('0:49', '50', 'Rep 6 · pick your rung', 'PROTECTED — never cut. A named prompt with a home and a version is the behavior change.'),
    ('0:53', '51–56', 'Close', 'Ten things (let them photograph it), exercises as homework, glossary/sources by pointer, the closing line.'),
])
E.append(Spacer(1, 8))

E.append(Paragraph('Demo scripts', S['h1']))
E.append(Paragraph('Demo 1 · Blind critique (6–8 min)', S['h2']))
E.append(Paragraph('Prep: a one-page fictional plan with 2–3 planted weaknesses (an unpriced assumption, a missing owner, an optimistic timeline), saved as plain text. '
                   'Live: (1) fresh chat → paste as “a colleague’s draft” → run the G3 critique preset from the Template Creator. '
                   '(2) second fresh chat → “I wrote this — what do you think?” with the same draft. '
                   '(3) Put both answers side by side; 20 seconds of silent reading; then ask the room what changed. '
                   'Land the number: models affirm users ~49% more than humans — blinding is the fix available today.', S['body']))
E.append(Paragraph('Demo 2 · Dashboard from a paste (6–8 min)', S['h2']))
E.append(Paragraph('Prep: a generic 25-row table (period, category, count) AND a pre-built copy of the finished dashboard file as backup. '
                   'Live: (1) paste the table → run the G6 preset (single file, offline, data embedded, formulas visible). '
                   '(2) While it generates, narrate the spec lines that make it trustworthy. '
                   '(3) Download, double-click, filter, sort. Say the two caveats aloud: it is a snapshot, and share the FILE, not a public link.', S['body']))

E.append(Paragraph('Contingency cuts — in order', S['h1']))
cuts = [('Running 3 min behind', 'Skip Rep 2 (already default-skip); walk the era slide in 30 seconds.'),
        ('Running 6 min behind', 'Matrix slide becomes “screenshot this” (15 seconds); cut the leaderboards slide to its callout.'),
        ('Running 10 min behind', 'Demo 2 → open the pre-built file only (2 min); handout pointer becomes one sentence.'),
        ('Session 2 behind', 'Compress guardrails to the reversibility rule + injection sentence; NEVER cut Rep 6 or the governance card.')]
data = [[Paragraph(a, S['cellb']), Paragraph(b, S['cell'])] for a, b in cuts]
t = Table(data, colWidths=[CW * 0.22, CW * 0.78])
t.setStyle(TableStyle([('ROWBACKGROUNDS', (0, 0), (-1, -1), [AMBER_T, colors.white]), ('GRID', (0, 0), (-1, -1), 0.4, LINE),
                       ('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
                       ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]))
E.append(t)
E.append(Spacer(1, 8))

E.append(Paragraph('Prep checklist (day before)', S['h1']))
for item in [
    'Demo draft (fictional plan) and demo data table staged in a text file; G3 and G6 presets tested end-to-end in the room’s actual AI tool.',
    'Pre-built dashboard file on the desktop as Demo 2 backup.',
    'Template Creator HTML opens offline on the presentation machine.',
    'Handouts ready: cheat sheet, ELEMENTS guide, taxonomy reference (print or link).',
    'Timer visible to presenter; reps are 3 minutes by the clock, not by feel.',
    'Session 2 booked within a week of Session 1 — homework (blind critique) decays fast.',
]:
    E.append(Paragraph('☐  ' + item, S['body']))

doc.build(E)
print('run of show written:', out)
