#!/usr/bin/env python3
"""Fold the widening sweep's accepted candidates into the set, scored on the identical model."""
import json, score

RAW = json.load(open('widen_raw.json'))
CHECKS = {c['restaurant'].strip(): c for c in json.load(open('widen_checks.json'))}
OVER = json.load(open('widen_overrides.json'))

PREP_MAP = {'smoked': 'grilled', 'baked': 'grilled'}
MILES = {}   # straight-line from RTP, filled where the sweep gave a city

out, dropped, unchecked = [], [], []
for c in RAW:
    name = c['restaurant'].strip()
    chk = CHECKS.get(name)
    if not chk:
        unchecked.append(name); continue
    if chk.get('verdict') == 'REJECT':
        dropped.append((name, c['dish'], chk.get('reason', '')))
        continue
    c = dict(c)
    c.update({k: v for k, v in OVER.get(name, {}).items() if k != 'price_note'})
    ent = score.score_entry(c)
    ent['is_new'] = True
    ent['data'] = 'PUBLISHED' if c.get('publishes_nutrition') else 'ESTIMATED'
    ent['prep'] = PREP_MAP.get(c.get('prep'), c.get('prep', 'grilled'))
    ent['miles'] = c.get('miles', 0)
    ent['store'] = (c.get('doordash_store_id') or '').strip()
    # no store id in this sweep was independently checkable - DoorDash 403s every
    # automated request - so record what was actually established, not what was claimed
    ent['store_confirmed'] = False
    ent['alternatives'] = []
    ent['price_note'] = OVER.get(name, {}).get('price_note', '')
    ent['check'] = {k: chk.get(k) for k in ('exists', 'dish_is_real', 'verdict')}
    out.append(ent)

out.sort(key=lambda d: -d['overall'])
json.dump(out, open('additions.json', 'w'), indent=1)

print(f"{len(out)} additions scored | {len(dropped)} rejected | {len(unchecked)} unchecked")
for n, dish, why in dropped:
    print(f"  REJECTED {n} ({dish[:34]}): {why[:100]}")
if unchecked: print("  UNCHECKED (excluded):", unchecked)
print()
print(f"  {'restaurant':30s} {'cuisine':26s} {'ovr':>5s} {'hlth':>5s} {'flav':>5s} {'price':>7s} {'Na':>6s} store")
for d in out:
    print(f"  {d['restaurant'][:28]:30s} {d['cuisine'][:24]:26s} {d['overall']:5.2f} "
          f"{d['health']:5.2f} {d['FLAVOR']:5.1f} {d['price']:7.2f} {d['sodium']:6,d} {d['store'] or '-'}")
