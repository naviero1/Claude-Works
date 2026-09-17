#!/usr/bin/env python3
# Prompt Template Configurator (.xlsx) — generated from prompt-library/taxonomy/*.json
# Sheets: README · Builder_Gen · Builder_Agent · Prompt_Gen · Prompt_Agent · Options · Taxonomy
import json, os, re
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

here = os.path.dirname(os.path.abspath(__file__))
tax_dir = os.path.join(here, '..', 'prompt-library', 'taxonomy')
out = os.path.join(here, '..', 'references', 'Prompt_Template_Configurator.xlsx')


def load(name):
    with open(os.path.join(tax_dir, name)) as f:
        return json.load(f)


meta = load('meta.json'); gen = load('generative.json'); agn = load('agentic.json')

INK = '232A31'; SLATE = '46545F'; TEAL = '0E7C7B'; TEAL_D = '0A5B5A'
TEAL_T = 'E4F0EF'; PANEL = 'F2F5F6'; LINEC = 'DCE3E6'; AMBER_T = 'FBF0E0'; YELLOW = 'FFF2CC'

F_BODY = Font(name='Arial', size=10, color=SLATE)
F_BODY_I = Font(name='Arial', size=9, italic=True, color='7A8790')
F_HEAD = Font(name='Arial', size=10, bold=True, color='FFFFFF')
F_ELEM = Font(name='Arial', size=11, bold=True, color=TEAL_D)
F_ATTR = Font(name='Arial', size=10, bold=True, color=INK)
F_MONO = Font(name='Courier New', size=9, color=SLATE)
FILL_HEAD = PatternFill('solid', fgColor=TEAL)
FILL_ELEM = PatternFill('solid', fgColor=TEAL_T)
FILL_PANEL = PatternFill('solid', fgColor=PANEL)
FILL_INPUT = PatternFill('solid', fgColor=YELLOW)
THIN = Border(*[Side(style='thin', color=LINEC)] * 4)
WRAP = Alignment(wrap_text=True, vertical='top')

wb = Workbook()

# ---------------- Options sheet (flat, contiguous per attribute) ----------------
opt_ws = wb.active
opt_ws.title = 'Options'
opt_headers = ['Mode', 'Element', 'Attribute', 'Option', 'Pick when', 'Emits into the prompt', 'Tier']
for c, h in enumerate(opt_headers, 1):
    cell = opt_ws.cell(1, c, h); cell.font = F_HEAD; cell.fill = FILL_HEAD
opt_ws.freeze_panes = 'A2'
for c, wdt in enumerate([10, 14, 22, 24, 28, 70, 9], 1):
    opt_ws.column_dimensions[get_column_letter(c)].width = wdt

spans = {}  # (mode, path) -> (row_first, row_last)
r = 2
def walk_attrs(mode, elem, attr, parent=None):
    global r
    path = elem['id'] + '.' + (parent['id'] + '.' if parent else '') + attr['id']
    opts = attr.get('options', [])
    if opts:
        first = r
        for o in opts:
            vals = [mode, elem['name'], attr['name'], o['label'], o.get('when', ''), o.get('phrase', ''), o.get('tier', 'core')]
            for c, v in enumerate(vals, 1):
                cell = opt_ws.cell(r, c, v); cell.font = F_BODY; cell.alignment = WRAP; cell.border = THIN
            r += 1
        spans[(mode, path)] = (first, r - 1)
    for ch in attr.get('children', []):
        walk_attrs(mode, elem, ch, attr)

for data, mode in [(gen, 'generative'), (agn, 'agentic')]:
    for elem in sorted(data['elements'], key=lambda e: e['order']):
        for attr in elem.get('attributes', []):
            walk_attrs(mode, elem, attr)

# ---------------- Builder sheets ----------------
def rows_for(attr):
    if attr.get('pick') == 'many':
        return min(4, max(2, len([o for o in attr.get('options', []) if o.get('tier') != 'extended']) // 2 + 1))
    return 1


def build_builder(ws_name, data, mode):
    ws = wb.create_sheet(ws_name)
    headers = ['Element', 'Attribute', 'Guidance', 'Your choice (dropdown)', 'Custom text (overrides/adds)', 'Emitted text (auto)']
    for c, h in enumerate(headers, 1):
        cell = ws.cell(1, c, h); cell.font = F_HEAD; cell.fill = FILL_HEAD
    ws.freeze_panes = 'A2'
    for c, wdt in enumerate([16, 24, 34, 26, 34, 60], 1):
        ws.column_dimensions[get_column_letter(c)].width = wdt

    row = 2
    attr_dvs = {}
    elem_ranges = []  # (elem, first_row, last_row)
    for elem in sorted(data['elements'], key=lambda e: e['order']):
        efirst = row
        ecell = ws.cell(row, 1, elem['name'] + ('  ★' if elem.get('required') else ''))
        ecell.font = F_ELEM; ecell.fill = FILL_ELEM
        ws.cell(row, 2, elem.get('definition', '')).font = F_BODY_I
        ws.cell(row, 2).alignment = WRAP
        for c in range(1, 7):
            ws.cell(row, c).fill = FILL_ELEM; ws.cell(row, c).border = THIN
        row += 1

        def emit_rows(attr, parent=None, depth=0):
            nonlocal row
            path = elem['id'] + '.' + (parent['id'] + '.' if parent else '') + attr['id']
            n = rows_for(attr)
            span = spans.get((mode, path))
            for i in range(n):
                ws.cell(row, 2, ('    ' * depth) + attr['name'] + (f' · choice {i+1}' if n > 1 else '')).font = F_ATTR
                ws.cell(row, 2).alignment = WRAP
                if i == 0:
                    g = attr.get('guidance', '')
                    if attr.get('why'):
                        g = (g + '\n' if g else '') + 'WHY IT MATTERS: ' + attr['why']
                    ws.cell(row, 3, g).font = F_BODY_I
                    ws.cell(row, 3).alignment = WRAP
                dcell = ws.cell(row, 4, '')
                ccell = ws.cell(row, 5, '')
                dcell.fill = FILL_INPUT; ccell.fill = FILL_INPUT
                dcell.alignment = WRAP; ccell.alignment = WRAP
                ccell.font = F_BODY
                if span:
                    key = (mode, path)
                    dv = attr_dvs.get(key)
                    if dv is None:
                        dv = DataValidation(type='list', formula1='=' + dv_names[key], allow_blank=True, showErrorMessage=False)
                        ws.add_data_validation(dv)
                        attr_dvs[key] = dv
                    dv.add(dcell)
                    lookup = (f'INDEX(Options!$F${span[0]}:$F${span[1]},'
                              f'MATCH($D{row},Options!$D${span[0]}:$D${span[1]},0))')
                    formula = (f'=IF($E{row}<>"",$E{row},IF($D{row}="","",IFERROR({lookup},"")))')
                else:
                    formula = f'=$E{row}'
                fcell = ws.cell(row, 6, formula)
                fcell.font = F_MONO; fcell.alignment = WRAP
                for c in range(1, 7):
                    ws.cell(row, c).border = THIN
                row += 1
            for ch in attr.get('children', []):
                emit_rows(ch, attr, depth + 1)

        for attr in elem.get('attributes', []):
            emit_rows(attr)
        elem_ranges.append((elem, efirst, row - 1))
    return ws, elem_ranges


# workbook-level named ranges for dropdown lists (cross-sheet DV needs names)
from openpyxl.workbook.defined_name import DefinedName
dv_names = {}
for (mode, path), (r1, r2) in spans.items():
    nm = 'DV_' + re.sub(r'[^A-Za-z0-9]', '_', mode[:1] + '_' + path)
    wb.defined_names.add(DefinedName(nm, attr_text=f"Options!$D${r1}:$D${r2}"))
    dv_names[(mode, path)] = nm

gb_ws, gen_ranges = build_builder('Builder_Gen', gen, 'generative')
ab_ws, agn_ranges = build_builder('Builder_Agent', agn, 'agentic')


# ---------------- Prompt sheets ----------------
def build_prompt(ws_name, builder_name, elem_ranges, mode_label):
    ws = wb.create_sheet(ws_name)
    ws.column_dimensions['A'].width = 110
    c = ws.cell(1, 1, f'ASSEMBLED {mode_label.upper()} PROMPT — copy cell A4 (it recalculates from {builder_name})')
    c.font = Font(name='Arial', size=11, bold=True, color='FFFFFF'); c.fill = FILL_HEAD
    ws.cell(2, 1, 'Fill the yellow cells on the builder sheet; blank rows are skipped automatically. '
                  'Search the result for {{ — unfilled placeholders mean you are not done.').font = F_BODY_I
    ws.cell(2, 1).alignment = WRAP
    parts = []
    hidden_col = 3  # per-element staging in column C, hidden
    for i, (elem, r1, r2) in enumerate(elem_ranges):
        tag = elem.get('emit_tag', elem['id'])
        stage = ws.cell(4 + i, hidden_col,
                        f'=IF(_xlfn.TEXTJOIN(CHAR(10),TRUE,{builder_name}!$F${r1}:$F${r2})="","",'
                        f'"<{tag}>"&CHAR(10)&_xlfn.TEXTJOIN(CHAR(10),TRUE,{builder_name}!$F${r1}:$F${r2})&CHAR(10)&"</{tag}>")')
        stage.font = F_MONO
        parts.append(f'$C${4 + i}')
    final = ws.cell(4, 1, f'=_xlfn.TEXTJOIN(CHAR(10)&CHAR(10),TRUE,{",".join(parts)})')
    final.font = Font(name='Courier New', size=9, color=INK)
    final.alignment = WRAP
    ws.row_dimensions[4].height = 620
    ws.column_dimensions['C'].hidden = True
    return ws


build_prompt('Prompt_Gen', 'Builder_Gen', gen_ranges, 'generative')
build_prompt('Prompt_Agent', 'Builder_Agent', agn_ranges, 'agentic')

# ---------------- Taxonomy sheet ----------------
tx = wb.create_sheet('Taxonomy')
tx_headers = ['Mode', 'Element', 'OOP', 'Definition', 'Prevents']
for c, h in enumerate(tx_headers, 1):
    cell = tx.cell(1, c, h); cell.font = F_HEAD; cell.fill = FILL_HEAD
for c, wdt in enumerate([11, 16, 40, 55, 45], 1):
    tx.column_dimensions[get_column_letter(c)].width = wdt
r = 2
for data, mode in [(gen, 'generative'), (agn, 'agentic')]:
    for elem in sorted(data['elements'], key=lambda e: e['order']):
        vals = [mode, elem['name'], elem.get('oop', ''), elem.get('definition', ''), elem.get('prevents', '')]
        for c, v in enumerate(vals, 1):
            cell = tx.cell(r, c, v); cell.font = F_BODY if c != 3 else F_MONO; cell.alignment = WRAP; cell.border = THIN
        r += 1
tx.freeze_panes = 'A2'

# ---------------- README ----------------
rd = wb.create_sheet('README', 0)
rd.column_dimensions['A'].width = 4
rd.column_dimensions['B'].width = 110
rows = [
    ('h', 'Prompt Template Configurator'),
    ('b', f"v{meta['meta']['version']} · {meta['meta']['date']} · owner {meta['meta']['owner']} · generated from prompt-library/taxonomy/ (the source of truth — edit there, rebuild with src/build_configurator_xlsx.py)"),
    ('s', ''),
    ('h2', 'How to use'),
    ('b', 'START ON THE Tasks SHEET: pick one of the nine course task families (listed in training order), mark the requirements you need Yes, edit the yellow wording, and copy the assembled prompt (or the course prompt directly). The sheets below are the advanced, element-level builder.'),
    ('b', '1. Advanced: open Builder_Gen (chat prompts) or Builder_Agent (agent mission briefs).'),
    ('b', '2. Fill the YELLOW cells only: pick options from the dropdowns; add or override with custom text. Attributes marked "choice 1/2/3" accept several picks.'),
    ('b', '3. The prompt assembles itself on Prompt_Gen / Prompt_Agent — copy cell A4 into your AI tool.'),
    ('b', '4. Search the assembled prompt for {{ before you run — placeholders left unfilled mean you are not done.'),
    ('s', ''),
    ('h2', 'Legend'),
    ('b', 'YELLOW fill = cells you edit (dropdown choice, custom text). Everything else is generated — leave it.'),
    ('b', '★ next to an element name = keep this element; it is what makes the prompt reliable.'),
    ('b', 'The Options sheet is the full menu with guidance (core + extended); Taxonomy defines every element.'),
    ('s', ''),
    ('h2', 'Example'),
    ('b', 'Builder_Gen ships with a worked example already selected (a data-analysis prompt): Role = Careful analyst, Task = Analyze, plus custom scope. Clear those yellow cells to start fresh.'),
    ('s', ''),
    ('b', 'Companion tools: Prompt_Template_Creator.html (the interactive builder — same taxonomy, richer experience) · Prompt_Element_Taxonomy_Reference.pdf (the printed ontology).'),
]
r = 2
for kind, text in rows:
    cell = rd.cell(r, 2, text)
    if kind == 'h':
        cell.font = Font(name='Arial', size=16, bold=True, color=TEAL_D)
    elif kind == 'h2':
        cell.font = Font(name='Arial', size=12, bold=True, color=INK)
    else:
        cell.font = F_BODY
    cell.alignment = WRAP
    r += 1

# ---------------- worked example prefill (Builder_Gen) ----------------
def set_choice(ws, elem_name, attr_contains, value, custom=None):
    for row in ws.iter_rows(min_row=2, max_col=6):
        if row[1].value and attr_contains in str(row[1].value) and (row[3].value in (None, '')):
            row[3].value = value
            if custom is not None:
                row[4].value = custom
            return True
    return False

set_choice(gb_ws, 'Role', 'Identity / posture', 'Careful analyst')
set_choice(gb_ws, 'Role', 'Accuracy behaviors', 'Never invent')
set_choice(gb_ws, 'Task', 'Action starter', 'Analyze')
set_choice(gb_ws, 'Task', 'Task statement', None, None)
for row in gb_ws.iter_rows(min_row=2, max_col=6):
    if row[1].value == 'Task statement':
        row[4].value = 'Example (replace): what is the return rate by site for Q2 vs the 2.0% target?'
        break

# ---------------- Tasks sheet (the course task families, training order) ----------------
def parse_catalog_table(md, heading):
    i = md.find('## ' + heading)
    assert i >= 0, heading
    rows_ = []
    for line in md[i:].split('\n')[1:]:
        if line.startswith('## '):
            break
        if line.startswith('|') and not set(line) <= set('|- '):
            cells = [c.strip() for c in line.strip('|').split('|')]
            if len(cells) >= 3 and cells[0] != 'Requirement type':
                rows_.append((cells[0], cells[1], cells[2]))
    assert len(rows_) >= 10, heading
    return rows_

catalog = open(os.path.join(here, '..', 'references', 'Requirements_by_Artifact.md')).read()
cps = json.load(open(os.path.join(here, 'assets', 'course_prompts.json')))
TASKS_CFG = [
    ('Analyze spreadsheet data', 'analyze', 'Spreadsheet analysis: requirements to choose',
     'Help [reader] decide [decision] using [file], detail rows only — inspect first, then wait.'),
    ('Excel Analysis and Charts', 'excel_charts', 'Excel analysis and charts: requirements to choose',
     'Update [workbook] and return it as [name].xlsx with a Summary sheet and native editable charts.'),
    ('Build an interactive dashboard', 'dashboard', 'HTML dashboards: requirements to choose',
     'A self-contained offline dashboard from [returned workbook] for [audience] to answer [question].'),
    ('Prepare a presentation', 'present', 'Presentations: requirements to choose',
     'A five-slide deck for [audience] to support [decision], using only the verified findings.'),
    ('Summarize an email conversation', 'email', 'Email summaries: requirements to choose',
     'Organize the thread about [topic]: choose the result you need, then run the structured brief.'),
    ('Quote Extraction', 'quote_extract', 'Quotation extraction: requirements to choose',
     'Extract the attached quotation files into a Raw Extraction sheet — no normalizing or ranking yet.'),
    ('Quote Comparison', 'quote_compare', 'Quotation comparison: requirements to choose',
     'From the Raw Extraction sheet, build a Normalized Comparison — formulas visible, gaps listed.'),
    ('Research Spreadsheet', 'research', 'Research workbooks: requirements to choose',
     'Build a research workbook for [research question] from the attached references — traceable only.'),
    ('Explain a topic clearly', 'explain', 'Plain-language documents: requirements to choose',
     'Explain [topic] from [source] at about a fifth-grade reading level — fidelity preserved.'),
]
ts = wb.create_sheet('Tasks', 1)
ts.column_dimensions['A'].width = 10
ts.column_dimensions['B'].width = 26
ts.column_dimensions['C'].width = 70
ts.column_dimensions['D'].width = 46
ts.column_dimensions['E'].width = 90
ts.column_dimensions['F'].width = 2
yn = DataValidation(type='list', formula1='"Yes,No"', allow_blank=True)
ts.add_data_validation(yn)
tr = 1
c0 = ts.cell(tr, 1, 'THE COURSE TASK FAMILIES, IN TRAINING ORDER — mark Include? = Yes, edit the yellow wording, copy the ASSEMBLED PROMPT (column E). A simple task needs only a few rows.')
c0.font = Font(name='Arial', size=12, bold=True, color=TEAL_D); tr += 2
for name, pid, heading, hint in TASKS_CFG:
    reqs = parse_catalog_table(catalog, heading)
    h = ts.cell(tr, 1, name.upper())
    h.font = F_HEAD; h.fill = FILL_HEAD
    for c in range(2, 6):
        ts.cell(tr, c).fill = FILL_HEAD
    tr += 1
    ts.cell(tr, 2, 'The course prompt (copy-ready):').font = F_ATTR
    cp_text = cps[pid] if pid != 'analyze' else ('PROMPT 1 — INSPECT:\n' + cps['inspect'] + '\n\nPROMPT 2 — ANALYZE:\n' + cps['analyze'])
    pc = ts.cell(tr, 3, cp_text); pc.font = F_MONO; pc.alignment = WRAP
    # row height sized to the prompt (~86 chars/line at this width) so no line clips
    ts.row_dimensions[tr].height = max(88, 14 * (len(cp_text) // 86 + 2))
    tr += 1
    ts.cell(tr, 2, 'Your task line (edit):').font = F_ATTR
    tl = ts.cell(tr, 3, hint); tl.fill = FILL_INPUT; tl.alignment = WRAP; tl.border = THIN
    task_cell = f'C{tr}'
    tr += 1
    hdr_r = tr
    for c, htxt in enumerate(['Include?', 'Requirement type', 'Your instruction (edit)', 'How to check it'], 1):
        cell = ts.cell(tr, c, htxt); cell.font = F_ATTR; cell.fill = FILL_ELEM; cell.border = THIN
    tr += 1
    first = tr
    for rtype, rex, rchk in reqs:
        inc = ts.cell(tr, 1, 'No'); inc.fill = FILL_INPUT; inc.border = THIN
        yn.add(inc)
        ts.cell(tr, 2, rtype).font = F_ATTR
        ic = ts.cell(tr, 3, rex); ic.fill = FILL_INPUT; ic.alignment = WRAP; ic.border = THIN
        ck = ts.cell(tr, 4, rchk); ck.font = F_BODY_I; ck.alignment = WRAP
        ts.cell(tr, 6, f'=IF(AND($A{tr}="Yes",TRIM($C{tr})<>""),"- "&TRIM($C{tr}),"")')
        ts.cell(tr, 7, f'=IF($A{tr}="Yes","- "&$D{tr},"")')
        tr += 1
    last = tr - 1
    ts.cell(tr, 2, 'Free-form additions (optional):').font = F_ATTR
    fc = ts.cell(tr, 3, ''); fc.fill = FILL_INPUT; fc.border = THIN
    free_cell = f'C{tr}'
    tr += 1
    ts.cell(tr, 2, 'ASSEMBLED PROMPT →').font = Font(name='Arial', size=10, bold=True, color=TEAL_D)
    # Same blocks, order, and wording as the browser builder's assembleTask():
    # task line -> Requirements -> Also -> How I will check the result.
    jf = f'_xlfn.TEXTJOIN(CHAR(10),TRUE,F{first}:F{last})'
    jg = f'_xlfn.TEXTJOIN(CHAR(10),TRUE,G{first}:G{last})'
    af = (f'=_xlfn.TEXTJOIN(CHAR(10)&CHAR(10),TRUE,{task_cell},'
          f'IF({jf}="","","Requirements:"&CHAR(10)&{jf}),'
          f'IF({free_cell}="","","Also:"&CHAR(10)&{free_cell}),'
          f'IF({jg}="","","How I will check the result:"&CHAR(10)&{jg}))')
    ac = ts.cell(tr, 5, af); ac.alignment = WRAP; ac.font = F_MONO
    ts.row_dimensions[tr].height = 170
    tr += 2
ts.column_dimensions['F'].hidden = True
ts.column_dimensions['G'].hidden = True
ts.freeze_panes = 'A3'

wb.save(out)
print('configurator written:', out, f'(Tasks sheet: {len(TASKS_CFG)} task families,',
      sum(len(parse_catalog_table(catalog, h)) for _, _, h, _ in TASKS_CFG), 'requirement rows)')
