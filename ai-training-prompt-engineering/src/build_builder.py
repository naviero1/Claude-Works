#!/usr/bin/env python3
# Merge prompt-library/taxonomy/*.json and inject into builder_template.html
# -> deliverables/Prompt_Template_Creator.html
import json, os

here = os.path.dirname(os.path.abspath(__file__))
tax_dir = os.path.join(here, '..', 'prompt-library', 'taxonomy')
tpl_path = os.path.join(here, 'builder_template.html')
out_path = os.path.join(here, '..', 'deliverables', 'Prompt_Template_Creator.html')


def load(name):
    with open(os.path.join(tax_dir, name)) as f:
        return json.load(f)


meta = load('meta.json')
gen = load('generative.json')
agn = load('agentic.json')
pre = load('presets.json')

tax = {
    'meta': meta['meta'],
    'oop_legend': meta['oop_legend'],
    'modes': meta['modes'],
    'elements': gen['elements'] + agn['elements'],
    'presets': pre['presets'],
}

# ---- validation ----
ids = {}
for e in tax['elements']:
    key = (e['mode'], e['id'])
    assert key not in ids, f'duplicate element {key}'
    ids[key] = e

paths = {}   # mode -> path -> attr dict
for e in tax['elements']:
    for a in e.get('attributes', []):
        paths.setdefault(e['mode'], {})[f"{e['id']}.{a['id']}"] = a
        for ch in a.get('children', []):
            paths[e['mode']][f"{e['id']}.{a['id']}.{ch['id']}"] = ch

for mode_paths in paths.values():
    for path, a in mode_paths.items():
        assert a.get('why'), f'attribute {path} is missing its "why it matters" note'

for p in tax['presets']:
    mp = paths.get(p['mode'], {})
    for el in p.get('elements', []):
        assert (p['mode'], el) in ids, f"preset {p['id']}: unknown element {el}"
    for path, labels in p.get('select', {}).items():
        assert path in mp, f"preset {p['id']}: unknown path {path}"
        have = {o['label'] for o in mp[path].get('options', [])}
        for l in (labels if isinstance(labels, list) else [labels]):
            assert l in have, f"preset {p['id']}: label '{l}' not in {path} (has: {sorted(have)[:6]}…)"
    for path in p.get('custom', {}):
        assert path in mp, f"preset {p['id']}: unknown custom path {path}"

n_attrs = sum(len(v) for v in paths.values())
n_opts = sum(len(a.get('options', [])) for v in paths.values() for a in v.values())

# ---- The task families, in training order (shared catalog + course prompts) ----
def parse_catalog_table(md, heading):
    """Return [(type, example, check)] from the pipe table under a '## heading'."""
    i = md.find('## ' + heading)
    assert i >= 0, f'catalog heading not found: {heading}'
    rows = []
    for line in md[i:].split('\n')[1:]:
        if line.startswith('## '):
            break
        if line.startswith('|') and not set(line) <= set('|- '):
            cells = [c.strip() for c in line.strip('|').split('|')]
            if len(cells) >= 3 and cells[0] not in ('Requirement type',):
                rows.append({'type': cells[0], 'example': cells[1], 'check': cells[2]})
    assert len(rows) >= 10, f'{heading}: only {len(rows)} rows parsed'
    return rows


catalog = open(os.path.join(here, '..', 'references', 'Requirements_by_Artifact.md')).read()
prompts = json.load(open(os.path.join(here, 'assets', 'course_prompts.json')))
TASKS = [
    {'id': 'analyze', 'name': 'Analyze spreadsheet data',
     'blurb': 'Upload one data file, inspect before calculating, compute checked rates. The supplier case is the worked example.',
     'taskHint': 'Help [reader] decide [decision] using [file], detail rows only — inspect first, then wait.',
     'prompt': 'PROMPT 1 — INSPECT:\n' + prompts['inspect'] + '\n\nPROMPT 2 — ANALYZE:\n' + prompts['analyze'],
     'reqs': parse_catalog_table(catalog, 'Spreadsheet analysis: requirements to choose')},
    {'id': 'excel_charts', 'name': 'Excel Analysis and Charts',
     'blurb': 'The assistant returns your workbook — Summary sheet, native editable charts, traceable formulas.',
     'taskHint': 'Update [workbook] and return it as [name].xlsx with a Summary sheet and native editable charts.',
     'prompt': prompts['excel_charts'], 'reqs': parse_catalog_table(catalog, 'Excel analysis and charts: requirements to choose')},
    {'id': 'dashboard', 'name': 'Build an interactive dashboard',
     'blurb': 'Feed the returned workbook in; describe behavior in plain language — filters, views, states.',
     'taskHint': 'A self-contained offline dashboard from [returned workbook] for [audience] to answer [question].',
     'prompt': prompts['dashboard'], 'reqs': parse_catalog_table(catalog, 'HTML dashboards: requirements to choose')},
    {'id': 'present', 'name': 'Prepare a presentation',
     'blurb': 'Verified findings become a five-slide decision mock-up — findings separated from recommendations.',
     'taskHint': 'A five-slide deck for [audience] to support [decision], using only the verified findings.',
     'prompt': prompts['present'], 'reqs': parse_catalog_table(catalog, 'Presentations: requirements to choose')},
    {'id': 'email', 'name': 'Summarize an email conversation',
     'blurb': 'Status, decisions with conditions, actions with owners — “Not stated” for gaps, a citation per claim.',
     'taskHint': 'Organize the thread about [topic]: choose the result you need, then run the structured brief.',
     'prompt': prompts['email'], 'reqs': parse_catalog_table(catalog, 'Email summaries: requirements to choose')},
    {'id': 'quote_extract', 'name': 'Quote Extraction',
     'blurb': 'Documents to spreadsheet, step one: verbatim values, original currencies, a citation per value.',
     'taskHint': 'Extract the attached quotation files into a Raw Extraction sheet — no normalizing or ranking yet.',
     'prompt': prompts['quote_extract'], 'reqs': parse_catalog_table(catalog, 'Quotation extraction: requirements to choose')},
    {'id': 'quote_compare', 'name': 'Quote Comparison',
     'blurb': 'Step two: normalize only what has a stated basis — and no best quote while gaps remain.',
     'taskHint': 'From the Raw Extraction sheet, build a Normalized Comparison — formulas visible, gaps listed.',
     'prompt': prompts['quote_compare'], 'reqs': parse_catalog_table(catalog, 'Quotation comparison: requirements to choose')},
    {'id': 'research', 'name': 'Research Spreadsheet',
     'blurb': 'Reference files become a traceable Evidence / Synthesis / Sources workbook — conflicts stay visible.',
     'taskHint': 'Build a research workbook for [research question] from the attached references — traceable only.',
     'prompt': prompts['research'], 'reqs': parse_catalog_table(catalog, 'Research workbooks: requirements to choose')},
    {'id': 'explain', 'name': 'Explain a topic clearly',
     'blurb': 'Plain language that preserves meaning, conditions, and caveats — with a comprehension check.',
     'taskHint': 'Explain [topic] from [source] at about a fifth-grade reading level — fidelity preserved.',
     'prompt': prompts['explain'], 'reqs': parse_catalog_table(catalog, 'Plain-language documents: requirements to choose')},
]

tpl = open(tpl_path).read()
payload = json.dumps(tax, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
tasks_payload = json.dumps(TASKS, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
html = tpl.replace('/*__TAXONOMY_JSON__*/', payload)
assert html != tpl, 'taxonomy placeholder not found'
html2 = html.replace('/*__TASKS_JSON__*/', tasks_payload)
assert html2 != html, 'tasks placeholder not found'
open(out_path, 'w').write(html2)
print(f'builder written: {out_path} ({len(html2)//1024} KB) — {len(TASKS)} task families '
      f'({sum(len(t["reqs"]) for t in TASKS)} requirement rows) + legacy: '
      f'{len(tax["elements"])} elements, {n_attrs} attributes, {n_opts} options, {len(tax["presets"])} presets')
