#!/usr/bin/env python3
"""The tier rule, derived from the consumer-testing precedent.

Cook's Illustrated groups results into named tiers rather than ranking flat,
because a flat 1-to-N implies a precision the model does not have. Which? gates
its top mark on a compound rule - a composite score AND a floor on the criterion
that matters - so a dish cannot buy its way in on one strong column.

Applying that floor to all seven health criteria is wrong here, and the document
says why: its own audit found the gut criterion ignores fibre and the omega-3
ladder treats plant ALA as marine. A floor across all seven mostly penalises
dishes for not containing kimchi, and it throws out the top-ranked dish. The
floor therefore applies only to the four criteria that are arithmetic on the
macros and went undisputed: kidney, liver, muscle, sugar.
"""
import json

SOUND = ['KID', 'LIV', 'MUS', 'SUG']       # arithmetic on the macros, undisputed
DISPUTED = ['GUT', 'INF', 'ENE']           # rubric judgements the audit criticised

def tier(d):
    worst = min(d[c] for c in SOUND)
    if d['overall'] >= 6.5 and worst >= 4.0:  return 'Order these'
    if d['overall'] >= 6.0:                   return 'Worth ordering'
    if d['overall'] >= 5.0:                   return 'With reservations'
    return 'Not recommended'

if __name__ == '__main__':
    B = '../build/'
    ALL = json.load(open(B+'details_corrected.json')) + json.load(open(B+'additions.json'))
    from collections import Counter
    c = Counter(tier(d) for d in ALL)
    for t in ['Order these', 'Worth ordering', 'With reservations', 'Not recommended']:
        print(f'  {t:20s} {c[t]:2d}')
    print(f'\n  blocked from the top tier by the floor:')
    for d in sorted(ALL, key=lambda x: -x['overall']):
        if d['overall'] >= 6.5 and min(d[k] for k in SOUND) < 4.0:
            w = min((d[k], k) for k in SOUND)
            print(f'    {d["restaurant"]:24s} {d["overall"]:.2f}  {w[1]} {w[0]:.1f}')
