"""Every number the hybrid report prints, computed on all 87 dishes.

The compendium's figures.py is scoped to the original sixty on purpose - the
twenty-seven additions were chosen to fill named gaps, so pooling them into a
correlation measures the selection. That caution applies to CORRELATIONS. It
does not apply to descriptive statements about the set the reader is holding:
if the report shows 87 entries, then "41 of them cost under $13" has to be
true of those 87. Correlations below are therefore reported on the original
sixty and labelled as such; counts, medians and bands are on all 87.
"""
import json, os, statistics as st, random

HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, 'all87.json')))
ORIG = [d for d in R if d['cohort'] == 'first edition']
CRIT = ['KID', 'LIV', 'MUS', 'GUT', 'ENE', 'INF', 'SUG']
BANDS = ['under $12', '$12 to $16', '$16 to $20', '$20 and up']

def pear(xs, ys):
    mx, my = st.mean(xs), st.mean(ys)
    return sum((x-mx)*(y-my) for x, y in zip(xs, ys))/len(xs)/(st.pstdev(xs)*st.pstdev(ys))

def slope(xs, ys):
    mx, my = st.mean(xs), st.mean(ys)
    return sum((x-mx)*(y-my) for x, y in zip(xs, ys))/sum((x-mx)**2 for x in xs)

def rescore(d, w):
    """Re-run the composite under an alternative weighting of the nine criteria."""
    h = sum(w[c]*d[c] for c in CRIT)/sum(w[c] for c in CRIT)
    tot = sum(w[c] for c in CRIT) + w['FLAVOR'] + w['COST']
    return (sum(w[c]*d[c] for c in CRIT) + w['FLAVOR']*d['FLAVOR'] + w['COST']*d['COST'])/tot, h

BASE = dict(KID=1.0, LIV=1.0, MUS=1.0, GUT=1.0, ENE=1.0, INF=1.0, SUG=0.7, FLAVOR=0.5, COST=0.5)
ALTS = [
    ('as published',      BASE),
    ('flavour weighted equal to health', {**BASE, 'FLAVOR': 1.0}),
    ('cost ignored entirely',            {**BASE, 'COST': 0.0}),
    ('health only',                      {**BASE, 'FLAVOR': 0.0, 'COST': 0.0}),
    ('all nine weighted equally',        {k: 1.0 for k in BASE}),
]

F = {}
F['n'] = len(R)
F['n_restaurants'] = len({d['restaurant'] for d in R})
F['n_cuisines'] = len({d['cuisine'] for d in R})

# --- the hook: the best cheap dish, against the worst dish costing at least
# twice as much. Both ends are picked by a stated rule, not by eye.
F['cheap'] = max([d for d in R if d['price'] <= 12], key=lambda d: d['overall'])
F['dear'] = min([d for d in R if d['price'] >= 2*F['cheap']['price']],
                key=lambda d: d['overall'])
F['gap_money'] = F['dear']['price'] - F['cheap']['price']
F['gap_score'] = F['cheap']['overall'] - F['dear']['overall']

# --- bands
F['bands'] = []
for b in BANDS:
    g = sorted([d for d in R if d['band'] == b], key=lambda d: -d['overall'])
    F['bands'].append(dict(
        name=b, n=len(g),
        med_health=round(st.median([d['health'] for d in g]), 2),
        mean_price=round(st.mean([d['price'] for d in g]), 2),
        best=g[0], worst=g[-1],
        lo=round(min(d['health'] for d in g), 1),
        hi=round(max(d['health'] for d in g), 1)))

# --- the badge. Bib Gourmand: a published price cap plus a quality floor.
# Bib Gourmand: a published price cap plus a quality floor. The floor is the
# same compound rule the tiers use - a good health score AND no collapse on any
# criterion that is plain arithmetic on the macros - so a dish cannot be badged
# on a strong average while carrying most of a day's sodium.
CAP, FLOOR, SOUND_MIN = 13.0, 6.0, 4.0
SOUND = ['KID', 'LIV', 'MUS', 'SUG']
F['cap'], F['floor'], F['sound_min'] = CAP, FLOOR, SOUND_MIN
F['badged'] = sorted([d for d in R if d['price'] < CAP and d['health'] >= FLOOR
                      and min(d[c] for c in SOUND) >= SOUND_MIN],
                     key=lambda d: -d['overall'])
F['n_under_cap'] = sum(1 for d in R if d['price'] < CAP)

# --- what an extra five dollars actually buys, on all 87
F['per5'] = {k: round(slope([d['price'] for d in R], [d[k] for d in R])*5, 1)
             for k in ('sodium', 'fiber', 'satfat', 'protein', 'cal')}
F['r_price_health_orig'] = round(pear([d['price'] for d in ORIG], [d['health'] for d in ORIG]), 3)
F['r_price_health_all']  = round(pear([d['price'] for d in R], [d['health'] for d in R]), 3)

# --- frontier and domination
def frontier(rows):
    return [a for a in rows if not any(
        b['price'] <= a['price'] and b['health'] >= a['health']
        and (b['price'], -b['health']) != (a['price'], -a['health']) for b in rows)]
F['frontier'] = sorted(frontier(R), key=lambda d: d['price'])
F['n_over_17'] = sum(1 for d in R if d['price'] > 17)
F['n_over_17_dominated'] = sum(1 for d in R if d['price'] > 17 and d not in F['frontier'])

# --- the sensitivity defence
# Health ignores the flavour and cost weights by construction, so an
# alternative weighting of those two moves the OVERALL score and leaves
# r(price, health) untouched. Report the correlation against overall, which
# is the number a reader would actually recompute, and keep health beside it.
F['alts'] = []
for name, w in ALTS:
    ranked = sorted(R, key=lambda d: -rescore(d, w)[0])
    F['alts'].append(dict(
        name=name,
        r_overall=round(pear([d['price'] for d in ORIG],
                             [rescore(d, w)[0] for d in ORIG]), 3),
        r_health=round(pear([d['price'] for d in ORIG],
                            [rescore(d, w)[1] for d in ORIG]), 3),
        top3=[d['dish'] for d in ranked[:3]],
        cheap_rank=ranked.index(F['cheap'])+1,
        dear_rank=ranked.index(F['dear'])+1))

# Run the weighting sweep on both populations and print both. The sixty are
# the representative sample, so they are the fair test; the eighty-seven are
# what the reader is holding. They disagree in the tail - some weightings of
# the sixty do reach +0.34 - and reporting only the flattering one would be
# the exact failure this test exists to guard against.
def sweep(pop, seed, n=2000):
    rng = random.Random(seed)
    P = [d['price'] for d in pop]
    sims = []
    for _ in range(n):
        # One weighting per simulation, applied to every dish. Drawing inside
        # the loop over dishes would give each dish its own weighting, which
        # is not a weighting at all - it destroys the correlation structure
        # and reports a spuriously narrow spread.
        w = {k: rng.uniform(0.25, 2.0) for k in BASE}
        sims.append(pear(P, [rescore(d, w)[1] for d in pop]))
    sims.sort()
    return dict(n=n, median=round(st.median(sims), 3), lo=round(sims[0], 3),
                hi=round(sims[-1], 3),
                p95=round(sims[int(n*0.95)], 3),
                p_over_2=round(100*sum(1 for s in sims if s > 0.2)/n, 1))

F['mc60'] = sweep(ORIG, 20260902)
F['mc87'] = sweep(R, 20260902)

# --- with no model at all
F['raw'] = {k: round(pear([d['price'] for d in R], [d[k] for d in R]), 3)
            for k in ('protein', 'satfat', 'cal', 'sodium', 'fiber')}

# --- the week: five dinners picked for value against five picked from the top
_by_r = {}
for d in sorted(R, key=lambda d: -d['hpd']):
    _by_r.setdefault(d['restaurant'], d)
F['week_value'] = list(_by_r.values())[:5]
_top = {}
for d in sorted(R, key=lambda d: -d['overall']):
    _top.setdefault(d['restaurant'], d)
F['week_top'] = list(_top.values())[:5]
for k in ('week_value', 'week_top'):
    F[k + '_cost'] = round(sum(d['price'] for d in F[k]), 2)
    F[k + '_health'] = round(st.mean([d['health'] for d in F[k]]), 2)

if __name__ == '__main__':
    print(f"{F['n']} dishes · {F['n_restaurants']} restaurants · {F['n_cuisines']} cuisines\n")
    print(f"HOOK  {F['dear']['restaurant']} {F['dear']['dish'][:30]}  ${F['dear']['price']:.2f} -> {F['dear']['overall']:.2f}")
    print(f"      {F['cheap']['restaurant']} {F['cheap']['dish'][:30]}  ${F['cheap']['price']:.2f} -> {F['cheap']['overall']:.2f}")
    print(f"      ${F['gap_money']:.2f} more for {F['gap_score']:.2f} points fewer\n")
    print(f"BADGE under ${F['cap']:.0f} and health {F['floor']}+: {len(F['badged'])} of {F['n_under_cap']} under the cap\n")
    print('BANDS                n   med health   range      mean price')
    for b in F['bands']:
        print(f"  {b['name']:<16} {b['n']:>3}     {b['med_health']:>5.2f}    {b['lo']:.1f}-{b['hi']:.1f}     ${b['mean_price']:>6.2f}")
    print(f"\nEVERY EXTRA $5 BUYS: {F['per5']}")
    print(f"r(price,health) original 60 = {F['r_price_health_orig']}, all 87 = {F['r_price_health_all']}")
    print(f"\nFRONTIER {len(F['frontier'])} of {F['n']}; dishes over $17: {F['n_over_17']}, dominated: {F['n_over_17_dominated']}")
    print('\nSENSITIVITY, 2000 random weightings of the nine criteria:')
    for lab, m in (('the representative 60', F['mc60']), ('all 87', F['mc87'])):
        print(f"  {lab:<22} median {m['median']:+.3f}  range {m['lo']:+.3f} to {m['hi']:+.3f}"
              f"  95th pct {m['p95']:+.3f}  {m['p_over_2']}% above +0.2")
    print('\nNAMED ALTERNATIVE WEIGHTINGS      r(price,overall)  r(price,health)  cheap/dear rank')
    for a in F['alts']:
        print(f"  {a['name']:<32} {a['r_overall']:+.3f}           {a['r_health']:+.3f}"
              f"         #{a['cheap_rank']} / #{a['dear_rank']}")
    print(f"\nRAW MACROS vs PRICE (no model): {F['raw']}")
    print(f"\nWEEK  five dinners picked for value: ${F['week_value_cost']:.2f}, mean health {F['week_value_health']}")
    print(f"      five picked from the top:     ${F['week_top_cost']:.2f}, mean health {F['week_top_health']}")
    print(f"      -> ${F['week_top_cost']-F['week_value_cost']:.2f} more for "
          f"{F['week_top_health']-F['week_value_health']:+.2f} health points. At the extremes money "
          f"does buy something;\n         the finding is that across the middle of the market it does not.")
