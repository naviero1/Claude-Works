#!/usr/bin/env python3
"""Does the central finding depend on the weighting we chose?

Food Compass is this tradition's cautionary tale: a composite produced a
counterintuitive result, the authors had not published how sensitive it was to
their weighting, and the result was picked apart. The same objection is the
obvious one here - "you only got 'price does not buy health' because you
weighted sodium at 1.0 and flavour at 0.5."

So: re-run the correlation under deliberate variants, under 2,000 random
weightings, and finally with no model at all, on the raw macros.

The result is a qualified survival, not a clean one. The median weighting puts
r near +0.09 and the four undisputed criteria put it slightly negative, but
about one weighting in ten does push it past +0.2, and the most favourable of
2,000 reaches +0.35. So the defensible claim is not "no weighting makes price
predict health" - it is that the best case any weighting can manage still
leaves price explaining roughly a tenth of the variation, and the typical case
leaves it explaining none. The raw-macro result below carries more weight than
any of this, because it involves no weighting at all.
"""
import json, statistics as st, random

CR = ['KID', 'LIV', 'MUS', 'GUT', 'ENE', 'INF', 'SUG']
BASE = {c: 1.0 for c in CR}; BASE['SUG'] = 0.7

def pear(x, y):
    mx, my = st.mean(x), st.mean(y)
    return sum((a-mx)*(b-my) for a, b in zip(x, y))/len(x)/(st.pstdev(x)*st.pstdev(y))

def health(d, w):
    t = sum(w.values())
    return sum(w[c]*d[c] for c in CR)/t if t else 0

def run(ALL, n=2000, seed=7):
    P = [d['price'] for d in ALL]
    random.seed(seed)
    # One weighting per simulation, applied to every dish. Drawing the weights
    # inside the comprehension over dishes gives each dish its own weighting,
    # which is not a weighting at all: it destroys the correlation structure
    # and understates the spread badly.
    rs = []
    for _ in range(n):
        w = {c: random.uniform(0.25, 2.0) for c in CR}
        rs.append(pear(P, [health(d, w) for d in ALL]))
    rs.sort()
    return dict(
        published=pear(P, [health(d, BASE) for d in ALL]),
        sound_only=pear(P, [health(d, {c: (BASE[c] if c in ('KID','LIV','MUS','SUG') else 0)
                                       for c in CR}) for d in ALL]),
        random_lo=rs[0], random_hi=rs[-1], random_median=st.median(rs),
        random_p95=rs[int(n*0.95)],
        share_above_02=sum(1 for r in rs if r > 0.2)/n,
        # and with no model at all - the raw macros against price
        raw={k: pear(P, [d[k] for d in ALL])
             for k in ('sodium', 'protein', 'fiber', 'satfat', 'cal')})

if __name__ == '__main__':
    B = '../build/'
    ALL = json.load(open(B+'details_corrected.json')) + json.load(open(B+'additions.json'))
    r = run(ALL)
    print(f"  as published                  r = {r['published']:+.3f}")
    print(f"  four sound criteria only      r = {r['sound_only']:+.3f}")
    print(f"  2,000 random weightings       median {r['random_median']:+.3f}, "
          f"range {r['random_lo']:+.3f} to {r['random_hi']:+.3f}")
    print(f"  weightings giving r > 0.2     {r['share_above_02']*100:.1f}%")
    print(f"  the most price-favourable of the 2,000 reaches r = {r['random_hi']:+.3f}, which")
    print(f"  still leaves price explaining {r['random_hi']**2*100:.0f}% of the variation in health.")
    print("\n  with no model at all, price against the raw macros:")
    for k, v in sorted(r['raw'].items(), key=lambda kv: -abs(kv[1])):
        print(f"    {k:9s} {v:+.3f}")
    print("\n  Money buys a bigger, richer plate - more protein, but more salt and more")
    print("  saturated fat and less fibre with it. Net effect on health: nothing.")
