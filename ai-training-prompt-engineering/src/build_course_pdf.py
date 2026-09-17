#!/usr/bin/env python3
# From_Prompts_to_Agents_Course.pdf — the extended written edition of the
# 60-minute course. Content lives in src/assets/course_content.json (one
# chapter object per entry; see BLOCKS below); this script only renders.
# Rebuild: python3 build_course_pdf.py
#
# Block vocabulary (course_content.json):
#   {"type":"p","text":...}            paragraph (<b>/<i> inline only)
#   {"type":"h3","text":...}           sub-heading
#   {"type":"bullets","items":[...]}
#   {"type":"mono","text":...,"caption":...}   verbatim prompt box
#   {"type":"table","cols":[...],"rows":[[...]],"note":...}
#   {"type":"callout","kind":"works|myth|expired|try|trap|key|check",
#    "title":...,"body":...}
import json
import os
import re

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, PageBreak, KeepTogether)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FD = '/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DV', FD + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DV-B', FD + 'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DV-O', FD + 'DejaVuSans-Oblique.ttf'))
pdfmetrics.registerFont(TTFont('DVSer', FD + 'DejaVuSerif.ttf'))
pdfmetrics.registerFont(TTFont('DVSer-B', FD + 'DejaVuSerif-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Mono', FD + 'DejaVuSansMono.ttf'))
pdfmetrics.registerFont(TTFont('Mono-B', FD + 'DejaVuSansMono-Bold.ttf'))
pdfmetrics.registerFontFamily('DV', normal='DV', bold='DV-B', italic='DV-O')

INK = colors.HexColor('#232A31'); SLATE = colors.HexColor('#46545F'); MUTE = colors.HexColor('#7A8790')
TEAL = colors.HexColor('#0E7C7B'); TEAL_D = colors.HexColor('#0A5B5A'); TEAL_T = colors.HexColor('#E4F0EF')
PANEL = colors.HexColor('#F2F5F6'); LINE = colors.HexColor('#DCE3E6')
AMBER = colors.HexColor('#B96A1B'); AMBER_T = colors.HexColor('#FBF0E0')
RED = colors.HexColor('#AF3230'); RED_T = colors.HexColor('#F9E9E8')
GREEN = colors.HexColor('#3B8560'); GREEN_T = colors.HexColor('#E7F2EC')
DARK = colors.HexColor('#1C272E')

W, H = letter
M = 0.75 * inch
AVAIL = W - 2 * M

here = os.path.dirname(__file__)
out = os.path.join(here, '..', 'deliverables', 'From_Prompts_to_Agents_Course.pdf')
content_path = os.path.join(here, 'assets', 'course_content.json')

S = {
    'kicker': ParagraphStyle('kicker', fontName='DV-B', fontSize=9.5, leading=12,
                             textColor=TEAL, spaceAfter=6),
    'h1': ParagraphStyle('h1', fontName='DVSer-B', fontSize=23, leading=27,
                         textColor=INK, spaceAfter=10),
    'chintro': ParagraphStyle('chintro', fontName='DV-O', fontSize=10.6, leading=15.4,
                              textColor=SLATE, spaceAfter=14),
    'h2': ParagraphStyle('h2', fontName='DV-B', fontSize=13.5, leading=16.5,
                         textColor=TEAL_D, spaceBefore=16, spaceAfter=6),
    'h3': ParagraphStyle('h3', fontName='DV-B', fontSize=10.8, leading=13.5,
                         textColor=INK, spaceBefore=10, spaceAfter=3),
    'body': ParagraphStyle('body', fontName='DV', fontSize=9.7, leading=14.1,
                           textColor=INK, spaceAfter=6),
    'bullet': ParagraphStyle('bullet', fontName='DV', fontSize=9.7, leading=13.6,
                             textColor=INK, leftIndent=14, bulletIndent=4, spaceAfter=2.5),
    'mono': ParagraphStyle('mono', fontName='Mono', fontSize=8.2, leading=11.6,
                           textColor=INK),
    'monocap': ParagraphStyle('monocap', fontName='DV-O', fontSize=8.2, leading=10.5,
                              textColor=MUTE, spaceBefore=2, spaceAfter=8),
    'cell': ParagraphStyle('cell', fontName='DV', fontSize=8.6, leading=11.6,
                           textColor=SLATE),
    'cellh': ParagraphStyle('cellh', fontName='DV-B', fontSize=8.6, leading=11.6,
                            textColor=colors.white),
    'tnote': ParagraphStyle('tnote', fontName='DV-O', fontSize=8.2, leading=10.5,
                            textColor=MUTE, spaceBefore=2, spaceAfter=8),
    'callt': ParagraphStyle('callt', fontName='DV-B', fontSize=9.0, leading=11.5),
    'callb': ParagraphStyle('callb', fontName='DV', fontSize=8.9, leading=12.3,
                            textColor=INK),
    'toch1': ParagraphStyle('toch1', fontName='DV-B', fontSize=10.5, leading=15.5,
                            textColor=INK),
    'toch2': ParagraphStyle('toch2', fontName='DV', fontSize=9.2, leading=13.2,
                            textColor=SLATE, leftIndent=14),
}

CALLOUT = {  # kind: (label, title color, background)
    'works':   ('WORKS',   GREEN,  GREEN_T),
    'myth':    ('MYTH',    RED,    RED_T),
    'expired': ('EXPIRED', AMBER,  AMBER_T),
    'try':     ('TRY IT',  TEAL_D, TEAL_T),
    'trap':    ('TRAP',    RED,    RED_T),
    'key':     ('KEY',     colors.white, DARK),
    'check':   ('CHECK',   TEAL_D, TEAL_T),
}


def sanitize(text, markup=True):
    """Escape for Paragraph. markup=True keeps <b>/<i> tags."""
    t = text.replace('&', '&amp;')
    if markup:
        t = re.sub(r'<(?!/?[bi]>)', '&lt;', t)
    else:
        t = t.replace('<', '&lt;').replace('>', '&gt;')
    return t


def col_widths(n):
    if n == 2:
        return [AVAIL * 0.30, AVAIL * 0.70]
    if n == 3:
        return [AVAIL * 0.26, AVAIL * 0.37, AVAIL * 0.37]
    return [AVAIL / n] * n


def render_block(b):
    t = b['type']
    if t == 'p':
        return [Paragraph(sanitize(b['text']), S['body'])]
    if t == 'h3':
        return [Paragraph(sanitize(b['text']), S['h3'])]
    if t == 'bullets':
        return [Paragraph(sanitize(i), S['bullet'], bulletText='•') for i in b['items']] + [Spacer(1, 3.5)]
    if t == 'mono':
        body = sanitize(b['text'], markup=False).replace('\n', '<br/>')
        tbl = Table([[Paragraph(body, S['mono'])]], colWidths=[AVAIL])
        tbl.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), PANEL),
            ('BOX', (0, 0), (-1, -1), 0.7, LINE),
            ('LEFTPADDING', (0, 0), (-1, -1), 9), ('RIGHTPADDING', (0, 0), (-1, -1), 9),
            ('TOPPADDING', (0, 0), (-1, -1), 7), ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ]))
        flow = [Spacer(1, 3), tbl]
        if b.get('caption'):
            flow.append(Paragraph(sanitize(b['caption']), S['monocap']))
        else:
            flow.append(Spacer(1, 7))
        return flow
    if t == 'table':
        cols = b['cols']
        data = [[Paragraph(sanitize(c), S['cellh']) for c in cols]]
        for row in b['rows']:
            data.append([Paragraph(sanitize(c), S['cell']) for c in row])
        tbl = Table(data, colWidths=col_widths(len(cols)), repeatRows=1)
        tbl.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), TEAL_D),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, PANEL]),
            ('GRID', (0, 0), (-1, -1), 0.4, LINE),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
            ('TOPPADDING', (0, 0), (-1, -1), 3.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ]))
        flow = [Spacer(1, 3), tbl]
        if b.get('note'):
            flow.append(Paragraph(sanitize(b['note']), S['tnote']))
        else:
            flow.append(Spacer(1, 7))
        return flow
    if t == 'callout':
        label, tcol, bg = CALLOUT.get(b.get('kind', 'key'), CALLOUT['key'])
        dark = b.get('kind') == 'key'
        title_style = ParagraphStyle('ct', parent=S['callt'],
                                     textColor=colors.white if dark else tcol)
        body_style = ParagraphStyle('cb', parent=S['callb'],
                                    textColor=colors.HexColor('#E8EDF0') if dark else INK)
        head = f"{label} — {sanitize(b['title'])}" if b.get('title') else label
        tbl = Table([[Paragraph(head, title_style)], [Paragraph(sanitize(b['body']), body_style)]],
                    colWidths=[AVAIL])
        tbl.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), bg),
            ('BOX', (0, 0), (-1, -1), 0.7, tcol if not dark else DARK),
            ('LEFTPADDING', (0, 0), (-1, -1), 9), ('RIGHTPADDING', (0, 0), (-1, -1), 9),
            ('TOPPADDING', (0, 0), (0, 0), 6), ('BOTTOMPADDING', (0, 0), (0, 0), 1),
            ('TOPPADDING', (0, 1), (0, 1), 1), ('BOTTOMPADDING', (0, 1), (0, 1), 6),
        ]))
        return [Spacer(1, 4), KeepTogether(tbl), Spacer(1, 7)]
    raise ValueError(f'unknown block type: {t}')


class CourseDoc(BaseDocTemplate):
    def afterFlowable(self, fl):
        if isinstance(fl, Paragraph):
            if fl.style.name == 'h1':
                self.notify('TOCEntry', (0, fl.getPlainText(), self.page))
            elif fl.style.name == 'h2':
                self.notify('TOCEntry', (1, fl.getPlainText(), self.page))


def on_page(cv, doc):
    if doc.page == 1:
        return
    cv.saveState()
    cv.setFont('DV-B', 7.2); cv.setFillColor(MUTE)
    cv.drawString(M, H - 0.45 * inch, 'FROM PROMPTS TO AGENTS  ·  THE COURSE')
    cv.drawRightString(W - M, H - 0.45 * inch, 'ALL EXAMPLES FICTIONAL')
    cv.setFont('DV', 7.6)
    cv.drawCentredString(W / 2, 0.42 * inch, str(doc.page))
    cv.restoreState()


chapters = json.load(open(content_path))

story = []

# ---- cover -------------------------------------------------------------
story.append(Spacer(1, 2.1 * inch))
story.append(Paragraph('THE EXTENDED COURSE  ·  SEPTEMBER 2026', S['kicker']))
story.append(Paragraph('From Prompts to Agents',
                       ParagraphStyle('cover', parent=S['h1'], fontSize=34, leading=40)))
story.append(Spacer(1, 6))
story.append(Paragraph(
    'Writing prompts as small work specifications — and delegating work you can check. '
    'The written edition of the facilitated course, complete with the five worked tasks: '
    'analyze the data, build a dashboard, present the findings, summarize the thread, '
    'and explain it clearly.',
    ParagraphStyle('coversub', parent=S['chintro'], fontSize=11.5, leading=17)))
story.append(Spacer(1, 0.55 * inch))
cover_rows = [
    ('THIS BOOK', 'The course, cover to cover, for self-study or review after the live session.'),
    ('THE DECK', 'From_Prompts_to_Agents_Facilitated_60_Minute.pptx — the 60-minute live course.'),
    ('THE WORKBOOK', 'Course_Workbook.xlsx — the data and the five task tabs this book works through.'),
    ('THE BUILDER', 'Prompt_Template_Creator.html — assembles prompts from the same requirement menus.'),
    ('ONE PAGE', 'From_Prompts_to_Agents_Cheat_Sheet.pdf — the skeleton and the menus, printable.'),
]
ct = Table([[Paragraph(a, ParagraphStyle('ca', parent=S['cellh'], textColor=TEAL_D)),
             Paragraph(b, S['cell'])] for a, b in cover_rows],
           colWidths=[AVAIL * 0.22, AVAIL * 0.78])
ct.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LINEABOVE', (0, 0), (-1, 0), 0.7, LINE),
    ('LINEBELOW', (0, -1), (-1, -1), 0.7, LINE),
    ('LINEBELOW', (0, 0), (-1, -2), 0.3, LINE),
    ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))
story.append(ct)
story.append(Spacer(1, 0.5 * inch))
story.append(Paragraph(
    'All names, companies, and numbers in this book are fictional and generated for practice. '
    'Your organization’s AI policy and approved-tool list outrank anything written here.',
    S['tnote']))
story.append(PageBreak())

# ---- contents ----------------------------------------------------------
story.append(Paragraph('CONTENTS', S['kicker']))
toc = TableOfContents()
toc.levelStyles = [S['toch1'], S['toch2']]
toc.dotsMinLevel = 0
story.append(toc)
story.append(PageBreak())

# ---- chapters ----------------------------------------------------------
for ci, ch in enumerate(chapters):
    if ci:
        story.append(PageBreak())
    story.append(Paragraph(sanitize(ch.get('kicker', '')), S['kicker']))
    story.append(Paragraph(sanitize(ch['title']), S['h1']))
    if ch.get('intro'):
        story.append(Paragraph(sanitize(ch['intro']), S['chintro']))
    for sec in ch['sections']:
        story.append(Paragraph(sanitize(sec['heading']), S['h2']))
        for b in sec['blocks']:
            story.extend(render_block(b))

doc = CourseDoc(out, pagesize=letter,
                leftMargin=M, rightMargin=M,
                topMargin=0.72 * inch, bottomMargin=0.62 * inch,
                title='From Prompts to Agents — The Course',
                author='Oscar Penny')
frame = Frame(M, 0.62 * inch, AVAIL, H - 0.72 * inch - 0.62 * inch, id='main')
doc.addPageTemplates([PageTemplate(id='page', frames=[frame], onPage=on_page)])
doc.multiBuild(story)

print(f'course pdf written: {out} ({doc.page} pages, {len(chapters)} chapters)')
