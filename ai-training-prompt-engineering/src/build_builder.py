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

tpl = open(tpl_path).read()
payload = json.dumps(tax, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
html = tpl.replace('/*__TAXONOMY_JSON__*/', payload)
assert html != tpl, 'placeholder not found'
open(out_path, 'w').write(html)
print(f'builder written: {out_path} ({len(html)//1024} KB) — '
      f'{len(tax["elements"])} elements, {n_attrs} attributes, {n_opts} options, {len(tax["presets"])} presets')
