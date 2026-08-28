#!/usr/bin/env python3
"""Pull every candidate and every check out of the widening workflow's journal."""
import json, sys

P = ("/root/.claude/projects/-home-user-Claude-Works/b89adb8e-9f0b-5ee3-98ef-41549eeaaa15"
     "/subagents/workflows/wf_79afb77d-4f9/journal.jsonl")

cands, checks, notes = [], {}, []
for line in open(P):
    o = json.loads(line)
    if o.get('type') != 'result': continue
    r = o.get('result')
    if isinstance(r, str):
        try: r = json.loads(r)
        except Exception: continue
    if not isinstance(r, dict): continue
    if 'candidates' in r:
        cands.extend(r['candidates'])
        if r.get('notes'): notes.append(r['notes'])
    if 'checks' in r:
        for c in r['checks']:
            checks[c['restaurant'].strip()] = c

json.dump(cands, open('widen_raw.json', 'w'), indent=1)
json.dump(list(checks.values()), open('widen_checks.json', 'w'), indent=1)
json.dump(notes, open('widen_notes.json', 'w'), indent=1)

print(f"{len(cands)} candidates, {len(checks)} checked, {len(cands)-len(checks)} still unchecked")
from collections import Counter
print(Counter(c['verdict'] for c in checks.values()))
unchecked = [c['restaurant'] for c in cands if c['restaurant'].strip() not in checks]
if unchecked: print("awaiting check:", unchecked)
