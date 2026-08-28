#!/usr/bin/env python3
"""Fold the widening sweep's accepted candidates into the set, scored on the identical model."""
import json, sys, score

RAW = json.load(open('widen_raw.json'))          # [{candidates:[...]}, ...] from the workflow
CHECKS = {c['restaurant']: c for c in json.load(open('widen_checks.json'))}

PREP_MAP = {'smoked': 'grilled', 'baked': 'grilled', 'fried': 'fried'}

out, dropped = [], []
for c in RAW:
    chk = CHECKS.get(c['restaurant'])
    if not chk or chk.get('verdict') == 'REJECT':
        dropped.append((c['restaurant'], c['dish'], chk['reason'] if chk else 'no check returned'))
        continue
    # apply any macro correction the checker supplied
    for k, v in (c.get('macro_overrides') or {}).items():
        c[k] = v
    ent = score.score_entry(c)
    ent['is_new'] = True
    ent['data'] = 'PUBLISHED' if c.get('publishes_nutrition') else 'ESTIMATED'
    ent['prep'] = PREP_MAP.get(c.get('prep'), c.get('prep', 'grilled'))
    ent['miles'] = c.get('miles', 0)
    ent['store'] = c.get('doordash_store_id') or ''
    ent['alternatives'] = []
    ent['check'] = {k: chk.get(k) for k in ('exists', 'dish_is_real', 'verdict', 'price_check')}
    out.append(ent)

out.sort(key=lambda d: -d['overall'])
json.dump(out, open('additions.json', 'w'), indent=1)
print(f"{len(out)} additions scored, {len(dropped)} dropped")
for d in dropped: print(f"  DROPPED {d[0]} — {d[1]}: {d[2][:110]}")
print()
print(f"{'restaurant':28s} {'cuisine':26s} {'ovr':>5s} {'hlth':>5s} {'flav':>5s} {'price':>7s} {'Na':>6s}")
for d in out:
    print(f"  {d['restaurant']:26s} {d['cuisine'][:24]:24s} {d['overall']:5.2f} {d['health']:5.2f} {d['FLAVOR']:5.1f} {d['price']:7.2f} {d['sodium']:6,d}")
