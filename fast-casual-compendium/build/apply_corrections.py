"""Apply verified corrections and rescore the affected entries on the recovered model."""
import json, score

D = json.load(open('details_cu.json'))
by = {d['rank']: d for d in D}
C = json.load(open('corrections_v1.json'))

log = []
for c in C:
    if c['action'] == 'rescore':
        d = by[c['rank']]; before = dict(d)
        d.update(c['macros'])
        d['KID']  = round(score.kidney(d['sodium']), 1)
        d['SUG']  = round(score.sugar_score(d['sugar']), 1)
        d['MUS']  = round(score.muscle(d['protein'], d['cal']), 1)
        d['LIV']  = round(score.liver(d['satfat'], d['cal']), 1)
        d['COST'] = round(score.cost(d['price'], d['protein']), 1)
        d['health']  = round((d['KID']+d['LIV']+d['MUS']+d['GUT']+d['ENE']+d['INF']+0.7*d['SUG'])/6.7, 2)
        d['overall'] = round((d['health']*6.7 + d['FLAVOR']*0.5 + d['COST']*0.5)/7.7, 2)
        d['corrected'] = True
        if c.get('retier'): d['data'] = c['retier']
        if c.get('dispute'): d['disputed'] = True
        log.append((d['restaurant'], before['overall'], d['overall'], before['sodium'], d['sodium']))
    elif c['action'] == 'dispute':
        by[c['rank']]['disputed'] = True
    elif c['action'] == 'fix_field':
        by[c['rank']][c['field']] = c['value']

new_order = sorted(D, key=lambda x: -x['overall'])
print(f"{'restaurant':22s} {'was':>6s} {'now':>6s}  {'Na was':>7s} {'Na now':>7s}  {'rank':>12s}")
old_pos = {d['restaurant']: i+1 for i, d in enumerate(sorted(D, key=lambda x: -x['rank']*0))}
for r, ob, nb, osod, nsod in log:
    pos = next(i+1 for i, d in enumerate(new_order) if d['restaurant'] == r)
    orig = next(d['rank'] for d in D if d['restaurant'] == r)
    print(f"  {r:20s} {ob:6.2f} {nb:6.2f}  {osod:7,d} {nsod:7,d}   #{orig} -> #{pos}")

print("\nNew top twelve after corrections:")
for i, d in enumerate(new_order[:12], 1):
    mark = ' *corrected' if d.get('corrected') else (' *disputed' if d.get('disputed') else '')
    print(f"  {i:2d}. {d['overall']:.2f}  {d['restaurant']:24s} (printed #{d['rank']}){mark}")

print("\nBiggest movers:")
moves = sorted(((d['rank'] - (new_order.index(d)+1), d) for d in D), key=lambda t: -abs(t[0]))[:8]
for delta, d in moves:
    print(f"  {'up' if delta>0 else 'down'} {abs(delta):2d}  {d['restaurant']:24s} #{d['rank']} -> #{new_order.index(d)+1}")

json.dump(D, open('details_corrected.json','w'), indent=1)
print(f"\nwrote details_corrected.json")
