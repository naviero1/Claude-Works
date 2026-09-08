#!/usr/bin/env python3
# The Prompt Element Taxonomy — reference PDF generated from prompt-library/taxonomy/*.json
import json, os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, KeepTogether, PageBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FD = '/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DV', FD + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DV-B', FD + 'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DVSer-B', FD + 'DejaVuSerif-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Mono', FD + 'DejaVuSansMono.ttf'))
pdfmetrics.registerFont(TTFont('Mono-B', FD + 'DejaVuSansMono-Bold.ttf'))

INK = colors.HexColor('#232A31'); SLATE = colors.HexColor('#46545F'); MUTE = colors.HexColor('#7A8790')
TEAL = colors.HexColor('#0E7C7B'); TEAL_D = colors.HexColor('#0A5B5A'); TEAL_T = colors.HexColor('#E4F0EF')
PANEL = colors.HexColor('#F2F5F6'); LINE = colors.HexColor('#DCE3E6')
AMBER = colors.HexColor('#B96A1B'); AMBER_T = colors.HexColor('#FBF0E0')
RED = colors.HexColor('#AF3230'); DARK = colors.HexColor('#1C272E')

W, H = letter
M = 0.7 * inch
CW = W - 2 * M

here = os.path.dirname(os.path.abspath(__file__))
tax_dir = os.path.join(here, '..', 'prompt-library', 'taxonomy')
out = os.path.join(here, '..', 'deliverables', 'Prompt_Element_Taxonomy_Reference.pdf')


def load(name):
    with open(os.path.join(tax_dir, name)) as f:
        return json.load(f)


meta = load('meta.json'); gen = load('generative.json'); agn = load('agentic.json'); pre = load('presets.json')

S = {
    'h1': ParagraphStyle('h1', fontName='DVSer-B', fontSize=16, leading=20, textColor=INK, spaceBefore=2, spaceAfter=5),
    'h2': ParagraphStyle('h2', fontName='DVSer-B', fontSize=13, leading=16, textColor=TEAL_D, spaceBefore=8, spaceAfter=3),
    'h3': ParagraphStyle('h3', fontName='DV-B', fontSize=9.6, leading=12.5, textColor=INK, spaceBefore=6, spaceAfter=1.5),
    'kicker': ParagraphStyle('k', fontName='DV-B', fontSize=7.6, leading=9.5, textColor=TEAL, spaceAfter=2),
    'body': ParagraphStyle('b', fontName='DV', fontSize=8.8, leading=12, textColor=SLATE, spaceAfter=4),
    'oop': ParagraphStyle('o', fontName='Mono', fontSize=7.2, leading=9.5, textColor=TEAL_D, spaceAfter=2),
    'cell': ParagraphStyle('c', fontName='DV', fontSize=7.6, leading=10, textColor=SLATE),
    'cellb': ParagraphStyle('cb', fontName='DV-B', fontSize=7.6, leading=10, textColor=INK),
    'cellm': ParagraphStyle('cm', fontName='Mono', fontSize=7.0, leading=9.6, textColor=SLATE),
    'celli': ParagraphStyle('ci', fontName='DV', fontSize=7.2, leading=9.6, textColor=TEAL_D),
    'anti': ParagraphStyle('a', fontName='DV', fontSize=8.0, leading=10.5, textColor=RED, spaceBefore=2),
    'why': ParagraphStyle('w', fontName='DV', fontSize=8.2, leading=11, textColor=TEAL_D, spaceAfter=4, backColor=TEAL_T, borderPadding=(3, 5, 3, 5)),
    'tech': ParagraphStyle('t', fontName='DV', fontSize=8.0, leading=10.8, textColor=SLATE, spaceBefore=1.5),
}


def hf(cv, doc):
    cv.saveState()
    if doc.page == 1:
        cv.setFillColor(DARK); cv.rect(0, H - 1.02 * inch, W, 1.02 * inch, stroke=0, fill=1)
        cv.setFillColor(colors.HexColor('#5FB8B0')); cv.setFont('DV-B', 7.2)
        cv.drawString(M, H - 0.36 * inch, 'FROM PROMPTS TO AGENTS  ·  PROMPT LIBRARY  ·  V%s · %s' % (meta['meta']['version'], meta['meta']['date'].upper()))
        cv.setFillColor(colors.white); cv.setFont('DVSer-B', 20)
        cv.drawString(M, H - 0.66 * inch, 'The Prompt Element Taxonomy')
        cv.setFillColor(colors.HexColor('#A9BBC4')); cv.setFont('DV', 8.3)
        cv.drawString(M, H - 0.88 * inch, 'Every element, attribute, and option behind the Template Creator — with the research-backed why on every slot.')
    else:
        cv.setFillColor(MUTE); cv.setFont('DV', 6.8)
        cv.drawString(M, H - 0.4 * inch, 'PROMPT ELEMENT TAXONOMY · REFERENCE')
    cv.setFillColor(MUTE); cv.setFont('DV', 6.8)
    cv.drawString(M, 0.3 * inch, 'Source of truth: prompt-library/taxonomy/ · Tools: Prompt_Template_Creator.html · Configurator .xlsx')
    cv.drawRightString(W - M, 0.3 * inch, str(cv.getPageNumber()))
    cv.restoreState()


doc = BaseDocTemplate(out, pagesize=letter, leftMargin=M, rightMargin=M, topMargin=0.58 * inch, bottomMargin=0.5 * inch)
f_first = Frame(M, 0.5 * inch, CW, H - 1.02 * inch - 0.64 * inch, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
f_later = Frame(M, 0.5 * inch, CW, H - 0.5 * inch - 0.58 * inch, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id='first', frames=[f_first], onPage=hf),
                      PageTemplate(id='later', frames=[f_later], onPage=hf)])

E = []

# ---------- intro + legend ----------
E.append(Paragraph('This reference prints the complete ontology behind the Prompt Template Creator: '
                   '<b>19 elements</b> (7 generative, 12 agentic), their <b>attributes</b>, and every vetted <b>option</b> with its guidance. '
                   'New in v1.1: every attribute carries a shaded <b>Why it matters</b> note — what that dial actually does to the output, '
                   'with the study or vendor guidance it traces to (full citations: notes/research/ in the training repo). '
                   'Solid rows are core picks; rows marked ◇ are the extended menu. Everything here is editable in '
                   '<font face="Mono">prompt-library/taxonomy/</font> — the HTML builder, this PDF, and the XLSX configurator all regenerate from the same files.', S['body']))
leg = [[Paragraph('Term', S['cellb']), Paragraph('OOP reading', S['cellb'])]]
for k, v in meta['oop_legend'].items():
    leg.append([Paragraph(k.capitalize(), S['cellb']), Paragraph(v, S['cell'])])
t = Table(leg, colWidths=[CW * 0.14, CW * 0.86])
t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), TEAL_T), ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, PANEL]),
                       ('GRID', (0, 0), (-1, -1), 0.5, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                       ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
                       ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]))
E.append(t); E.append(Spacer(1, 8))


def opt_table(attr):
    rows = [[Paragraph('Option', S['cellb']), Paragraph('Pick when', S['cellb']), Paragraph('Emits into the prompt', S['cellb'])]]
    for o in attr.get('options', []):
        ext = '◇ ' if o.get('tier') == 'extended' else ''
        rows.append([Paragraph(ext + o['label'], S['cellb']),
                     Paragraph(o.get('when', '—'), S['celli']),
                     Paragraph(o.get('phrase', '—').replace('{{', '{{<font color="#B96A1B">').replace('}}', '</font>}}'), S['cellm'])])
    if attr.get('custom', True):
        rows.append([Paragraph('✎ custom', S['cellb']), Paragraph('always available', S['celli']),
                     Paragraph(attr.get('placeholder', 'free text'), S['cellm'])])
    t = Table(rows, colWidths=[CW * 0.17, CW * 0.21, CW * 0.62], repeatRows=1)
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), TEAL_T), ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, PANEL]),
                           ('GRID', (0, 0), (-1, -1), 0.4, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                           ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                           ('TOPPADDING', (0, 0), (-1, -1), 2.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5)]))
    return t


def emit_attr(attr, depth=0):
    ind = '&nbsp;' * (depth * 6)
    pick = {'one': 'pick one', 'many': 'pick any', 'text': 'free text'}.get(attr.get('pick', 'many'), '')
    head = Paragraph(f"{ind}{attr['name']}  <font face='Mono' size='6.6' color='#0A5B5A'>{attr.get('oop','')}</font>  <font size='6.6' color='#7A8790'>[{pick}]</font>", S['h3'])
    flow = [head]
    if attr.get('guidance'):
        flow.append(Paragraph(ind + '<i>' + attr['guidance'] + '</i>', S['body']))
    if attr.get('why'):
        flow.append(Paragraph(ind + '<b>Why it matters —</b> ' + attr['why'], S['why']))
    table = opt_table(attr) if (attr.get('options') or attr.get('custom', True)) else None
    if table is not None and len(attr.get('options', [])) <= 6:
        E.append(KeepTogether(flow + [table]))
    else:
        E.append(KeepTogether(flow))
        if table is not None:
            E.append(table)
    for ch in attr.get('children', []):
        emit_attr(ch, depth + 1)


def emit_mode(mode_id, elements):
    mode = next(m for m in meta['modes'] if m['id'] == mode_id)
    E.append(PageBreak())
    E.append(Paragraph(('PART 1 — GENERATIVE ELEMENTS' if mode_id == 'generative' else 'PART 2 — AGENTIC ELEMENTS'), S['kicker']))
    E.append(Paragraph(mode['name'] + ' mode', S['h1']))
    E.append(Paragraph(mode['tagline'], S['body']))
    for el in sorted(elements, key=lambda e: e['order']):
        E.append(Spacer(1, 6))
        E.append(KeepTogether([
            Paragraph(f"{el['name']}  <font face='Mono' size='7.4' color='#0A5B5A'>{el.get('oop','')}</font>", S['h2']),
            Paragraph(f"<b>{el.get('definition','')}</b> {el.get('mechanism','')} "
                      + (f"<font color='#AF3230'>Prevents: {el['prevents']}</font>" if el.get('prevents') else ''), S['body']),
        ]))
        for a in el.get('attributes', []):
            emit_attr(a)
        for tch in el.get('techniques', []):
            E.append(Paragraph(f"<font face='Mono-B' size='7.4' color='#B96A1B'>{tch['name']}</font> — {tch['what']}"
                               + (f" <i>Use when: {tch['when']}.</i>" if tch.get('when') else ''), S['tech']))
        if el.get('antipatterns'):
            E.append(Paragraph('⚠ Anti-patterns: ' + ' · '.join(el['antipatterns']), S['anti']))


emit_mode('generative', gen['elements'])
emit_mode('agentic', agn['elements'])

# ---------- presets ----------
E.append(PageBreak())
E.append(Paragraph('PART 3 — INSTANCES', S['kicker']))
E.append(Paragraph('The template library as saved configurations', S['h1']))
E.append(Paragraph('Each library template is an <b>instance</b> of the class system — a saved set of element choices. '
                   'Load any of these in the Template Creator (the "Start from a template" menu) and inspect which options it picked; '
                   'that inspection is the fastest way to learn the taxonomy.', S['body']))
rows = [[Paragraph('Instance', S['cellb']), Paragraph('Mode', S['cellb']), Paragraph('Elements in play', S['cellb']), Paragraph('Options pre-selected', S['cellb'])]]
for p in pre['presets']:
    n_sel = sum(len(v) if isinstance(v, list) else 1 for v in p.get('select', {}).values())
    rows.append([Paragraph(p['name'], S['cellb']), Paragraph(p['mode'], S['cell']),
                 Paragraph(str(len(p.get('elements', []))), S['cell']),
                 Paragraph(f"{n_sel} options + {len(p.get('custom', {}))} custom blocks", S['cell'])])
t = Table(rows, colWidths=[CW * 0.42, CW * 0.14, CW * 0.16, CW * 0.28], repeatRows=1)
t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), TEAL_T), ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, PANEL]),
                       ('GRID', (0, 0), (-1, -1), 0.4, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                       ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                       ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]))
E.append(t)

# ---------- appendix: how code models the same ideas ----------
E.append(Spacer(1, 10))
E.append(Paragraph('APPENDIX — THE DECOMPOSITION, VALIDATED AGAINST CODE', S['kicker']))
E.append(Paragraph('Engineering systems already model prompts this way', S['h1']))
rows = [[Paragraph('Our concept', S['cellb']), Paragraph('DSPy', S['cellb']), Paragraph('LangChain', S['cellb']), Paragraph('Vendor APIs', S['cellb'])]]
mapping = [
    ('Element (class)', 'Signature class (docstring = task instructions)', 'ChatPromptTemplate (message roles)', 'system / developer / user message roles'),
    ('Attribute (property)', 'InputField / OutputField — “field naming is the cheapest optimization”', 'template variables', 'request parameters (tone, format live in the text)'),
    ('Option (allowed value)', 'Literal["spring","summer",…] — typed enums the LM must respect', 'few-shot example selectors', 'structured outputs / JSON schema enums'),
    ('Technique (method)', 'Module: Predict, ChainOfThought, ReAct — strategy separate from contract', 'chains / runnables', 'reasoning-effort & verbosity parameters'),
    ('Template (instance)', 'a compiled program', 'a filled PromptTemplate', 'a saved prompt / GPT / Gem / skill'),
]
for row in mapping:
    rows.append([Paragraph(row[0], S['cellb'])] + [Paragraph(c, S['cell']) for c in row[1:]])
t = Table(rows, colWidths=[CW * 0.2, CW * 0.3, CW * 0.22, CW * 0.28], repeatRows=1)
t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), AMBER_T), ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, PANEL]),
                       ('GRID', (0, 0), (-1, -1), 0.4, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                       ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                       ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]))
E.append(t)
E.append(Spacer(1, 6))
E.append(Paragraph('The separation this taxonomy makes — WHAT you want (elements/attributes) vs. HOW the model should work on it (techniques) — '
                   'is the same separation DSPy makes between Signatures and Modules, and the pattern literature makes between a pattern’s '
                   '“fundamental contextual statements” and its usage. The full sources live in notes/research/ (t1–t6).', S['body']))

doc.build(E)
print('taxonomy PDF written:', out)
