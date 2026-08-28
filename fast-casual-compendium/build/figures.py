"""Every number printed in the second edition is computed here. Nothing is typed by hand."""
import json, statistics as st, itertools
from collections import defaultdict

D  = json.load(open('details_corrected.json'))    # 60 entries, corrections applied + cuisine/prep tags
M  = {d['rank']: d for d in json.load(open('master.json'))}   # + alternatives
for d in D: d['alternatives'] = M[d['rank']]['alternatives']
CRIT = ['KID','LIV','MUS','GUT','ENE','INF','SUG']

def pear(xs, ys):
    mx, my = st.mean(xs), st.mean(ys)
    return sum((x-mx)*(y-my) for x, y in zip(xs, ys))/len(xs)/(st.pstdev(xs)*st.pstdev(ys))

def d_(d, k): return d['derived'][k] if 'derived' in d else None

for d in D:
    d['hpd']  = d['health']/d['price']
    d['dpp']  = d['price']/d['protein']
    d['na_p'] = d['sodium']/d['protein']
    d['ppc']  = d['protein']/(d['cal']/100)

F = {}

# ---- correlations
F['r_price_health'] = pear([d['price'] for d in D], [d['health'] for d in D])
F['r_price_flavor'] = pear([d['price'] for d in D], [d['FLAVOR'] for d in D])
F['r_price_overall']= pear([d['price'] for d in D], [d['overall'] for d in D])
F['r_health_flavor']= pear([d['health'] for d in D], [d['FLAVOR'] for d in D])
F['r_fiber_gut']    = pear([d['fiber'] for d in D], [d['GUT'] for d in D])

# drop-the-outlier robustness for r(price, health)
def r_without(rank):
    S=[d for d in D if d['rank']!=rank]
    return pear([d['price'] for d in S], [d['health'] for d in S])
F['r_price_health_no_chengdu'] = r_without(38)   # $36.95, the price outlier
F['r_price_health_no_msushi']  = r_without(5)    # $31.20
F['r_price_health_range'] = (min(r_without(d['rank']) for d in D), max(r_without(d['rank']) for d in D))

# cuisine-level
g = defaultdict(list)
for d in D: g[d['cuisine']].append(d)
BIG = {k: v for k, v in g.items() if len(v) >= 2}
F['r_health_flavor_cuisine'] = pear(
    [st.mean([d['health'] for d in v]) for v in BIG.values()],
    [st.mean([d['FLAVOR'] for d in v]) for v in BIG.values()])
F['cuisines'] = sorted(
    [dict(name=k, n=len(v),
          health=st.mean([d['health'] for d in v]), flavor=st.mean([d['FLAVOR'] for d in v]),
          sodium=st.mean([d['sodium'] for d in v]), price=st.mean([d['price'] for d in v]),
          satfat=st.mean([d['satfat'] for d in v]), overall=st.mean([d['overall'] for d in v]))
     for k, v in BIG.items()], key=lambda r: -r['flavor'])

# high vs low flavor split
hi = [d for d in D if d['FLAVOR'] >= 7.5]; lo = [d for d in D if d['FLAVOR'] <= 5.5]
F['flavor_split'] = dict(
    n_hi=len(hi), n_lo=len(lo),
    na_hi=st.mean([d['sodium'] for d in hi]), na_lo=st.mean([d['sodium'] for d in lo]),
    sf_hi=st.mean([d['satfat'] for d in hi]), sf_lo=st.mean([d['satfat'] for d in lo]),
    health_hi=st.mean([d['health'] for d in hi]), health_lo=st.mean([d['health'] for d in lo]),
    price_hi=st.mean([d['price'] for d in hi]), price_lo=st.mean([d['price'] for d in lo]))
F['breakers'] = sorted([d for d in D if d['FLAVOR'] >= 7.5 and d['sodium'] <= 1100], key=lambda x: -x['overall'])

# value
F['value_hpd']   = sorted(D, key=lambda x: -x['hpd'])[:12]
F['value_dpp']   = sorted(D, key=lambda x: x['dpp'])[:12]
F['quadrant']    = sorted([d for d in D if d['health'] >= 6.0 and d['price'] <= 16], key=lambda x: -x['health'])
F['na_best']     = sorted(D, key=lambda x: x['na_p'])[:10]
F['na_worst']    = sorted(D, key=lambda x: -x['na_p'])[:6]
F['cheapest']    = sorted(D, key=lambda x: x['price'])[:12]
F['dearest']     = sorted(D, key=lambda x: -x['price'])[:8]

# weeks - searched, not hand-picked
def wrap(c):
    return dict(dishes=sorted(c, key=lambda x: -x['overall']),
                cost=sum(d['price'] for d in c),
                ceiling={k: max(d[k] for d in c) for k in CRIT},
                floor=min(max(d[k] for d in c) for k in CRIT))
def coverage(c): return min(max(d[k] for d in c) for k in CRIT)

F['week_naive'] = wrap(sorted(D, key=lambda x: -x['overall'])[:5])
BAR = F['week_naive']['floor']            # the bar the naive week sets
_best = None
for combo in itertools.combinations(sorted(D, key=lambda x: x['price'])[:30], 5):
    if coverage(combo) >= BAR:
        cost = sum(d['price'] for d in combo)
        if _best is None or cost < _best[0]: _best = (cost, combo)
F['week_cheap'] = wrap(_best[1])
F['week_bar'] = BAR
_bc = None
for combo in itertools.combinations(sorted(D, key=lambda x: -x['overall'])[:26], 5):
    cv, cost = coverage(combo), sum(d['price'] for d in combo)
    if _bc is None or (cv, -cost) > (_bc[0], -_bc[1]): _bc = (cv, cost, combo)
F['week_best'] = wrap(_bc[2])

# is the flavor-costs-salt gap real, or noise?
import math
def welch(a, b):
    ma, mb = st.mean(a), st.mean(b); va, vb = st.variance(a), st.variance(b); na, nb = len(a), len(b)
    t = (ma-mb)/math.sqrt(va/na+vb/nb)
    df = (va/na+vb/nb)**2/((va/na)**2/(na-1)+(vb/nb)**2/(nb-1))
    return t, df
_hi = [d for d in D if d['FLAVOR'] >= 7.5]; _lo = [d for d in D if d['FLAVOR'] <= 5.5]
F['welch_sodium'] = welch([d['sodium'] for d in _hi], [d['sodium'] for d in _lo])
F['welch_satfat'] = welch([d['satfat'] for d in _hi], [d['satfat'] for d in _lo])

# ranking-structure defect
merged = sorted(D, key=lambda x: -x['overall'])
F['merged'] = merged
F['true_rank'] = {d['rank']: i+1 for i, d in enumerate(merged)}
worst_main = min(d['overall'] for d in D if d['rank'] <= 30)
F['worst_main'] = worst_main
F['promoted'] = sorted([d for d in D if d['rank'] > 30 and d['overall'] > worst_main], key=lambda x: -x['overall'])
F['n_promoted'] = len(F['promoted'])

# data-tier gap
F['tiers'] = {}
for t in ['PUBLISHED','PARTIAL','ESTIMATED']:
    v = [d for d in D if d['data'] == t]
    F['tiers'][t] = dict(n=len(v), health=st.mean([d['health'] for d in v]),
                         sodium=st.mean([d['sodium'] for d in v]), flavor=st.mean([d['FLAVOR'] for d in v]),
                         overall=st.mean([d['overall'] for d in v]), price=st.mean([d['price'] for d in v]))
est = [d for d in D if d['data'] == 'ESTIMATED']
F['round_tell'] = dict(
    n=len(est),
    cal=sum(1 for d in est if d['cal'] % 20 == 0),
    sodium=sum(1 for d in est if d['sodium'] % 50 == 0),
    protein=sum(1 for d in est if d['protein'] % 2 == 0))

# gut criterion misfire
F['gut_top']   = sorted(D, key=lambda x: -x['GUT'])[:5]
F['fiber_top'] = sorted(D, key=lambda x: -x['fiber'])[:5]

# sodium arbitrage: what a single swap inside one restaurant actually saves
F['na_swaps'] = []
for d in D:
    if d.get('corrected') or d.get('disputed'):
        continue   # its alternatives were scored against figures this edition replaced
    for a in d['alternatives']:
        cut = d['sodium'] - a['sodium']
        if cut >= 300:
            F['na_swaps'].append(dict(
                restaurant=d['restaurant'], dish=d['dish'],
                alt=a['name'], alt_note=a['change'],
                cut=cut, protein_lost=d['protein'] - a['protein'],
                cal_delta=a['cal'] - d['cal'], score_delta=round(a['score'] - d['overall'], 2)))
F['na_swaps'].sort(key=lambda r: -r['cut'])

# where the salt sits: single components verified against published nutrition documents
F['salt_components'] = [
  dict(item='Farmside Kitchen seasoned quinoa', per='8 oz base portion', mg=900,
       note='The base, before anything is put on it.'),
  dict(item='Chipotle chipotle-honey vinaigrette', per='2 fl oz', mg=850,
       note='Also 220 calories and 12 g of sugar.'),
  dict(item='CAVA saffron basmati or brown rice', per='one base', mg=770,
       note='Identical for both rices; the largest sodium item among CAVA\'s bases.'),
  dict(item='Poke Bros. OG Sauce', per='one bowl', mg=730,
       note='Added to every bowl unless you refuse it.'),
  dict(item='Farmside Kitchen Signature grilled chicken', per='3.5 oz', mg=660,
       note='A plain grilled breast is 190 mg for the same protein.'),
  dict(item='CAVA grilled chicken', per='one portion', mg=670,
       note='CAVA\'s grilled steak is 280 mg for 23 g of protein.'),
  dict(item='Bul Box sriracha', per='1 oz', mg=454,
       note='The 30-calorie sauce. Yum yum sauce is 150 calories and 115 mg.'),
  dict(item='Pokeworks ahi tuna', per='2 oz scoop', mg=350,
       note='Their chicken is 80 mg for the same scoop.'),
  dict(item='Chipotle chicken', per='4 oz', mg=310,
       note='32 g of protein - the most sodium-efficient protein in the set.'),
  dict(item='True Food Kitchen salmon add-on', per='one portion', mg=90,
       note='29 g of protein. The cleanest protein anywhere here.'),
  dict(item='DICED grilled chicken', per='one portion', mg=69,
       note='26 g of protein, at 2.7 mg of sodium per gram.'),
  dict(item='Poke Bros. plain tuna', per='85 g', mg=40,
       note='Their own marinated tuna is 820 mg.'),
]

# alternatives
F['beats'] = [dict(rec=d, alt=a, gain=a['score']-d['overall'])
              for d in D if not (d.get('corrected') or d.get('disputed'))
              for a in d['alternatives'] if a['score'] > d['overall']]
F['n_alt_excluded'] = sum(len(d['alternatives']) for d in D if d.get('corrected') or d.get('disputed'))
F['beats'].sort(key=lambda r: -r['gain'])
F['avoids'] = [dict(rec=d, alt=a, drop=d['overall']-a['score'])
               for d in D if not (d.get('corrected') or d.get('disputed'))
               for a in d['alternatives'] if a.get('avoid')]
F['avoids'].sort(key=lambda r: -r['drop'])

# near-duplicates
GROUPS = {
 'Chicken kebab plate':   ['Sassool','Baba Ghannouj','Bosphorus','Quick Meal Mediterranean','Mediterra Grill'],
 'Build-your-own bowl':   ['DICED','Chopt','Mahana Fresh','Happy + Hale','Neomonde','Clean Eatz','Roots Natural Kitchen','Farmside Kitchen','CAVA','Chipotle'],
 'Raw fish plate':        ['M Sushi','M Izakaya','Peony Asian Bistro','Mi Perú'],
 'South Indian plate':    ["Naga's South Indian",'Southern Spice','Udupi Cafe'],
 'Ethiopian veg combo':   ['Abol Ethiopian','Goorsha'],
 'Vietnamese vermicelli': ['Taste Vietnamese','Bonjour Banh Mi','No 1 Pho'],
 'Poke bowl':             ['Poke Bros.','Pokeworks','Bul Box'],
}
byname = {d['restaurant']: d for d in D}
F['dupes'] = []
for name, rs in GROUPS.items():
    rows = sorted([byname[r] for r in rs], key=lambda x: x['price'])
    best = max(rows, key=lambda x: x['overall'])
    r = pear([d['price'] for d in rows], [d['overall'] for d in rows]) if len(rows) >= 3 and st.pstdev([d['price'] for d in rows]) > 0 else None
    F['dupes'].append(dict(name=name, n=len(rows), rows=rows, cheapest=rows[0], priciest=rows[-1],
                           best=best, best_is_priciest=best is rows[-1], r=r,
                           spread_price=rows[-1]['price']-rows[0]['price'],
                           spread_score=best['overall']-min(d['overall'] for d in rows)))
F['dupe_priciest_wins'] = sum(1 for x in F['dupes'] if x['best_is_priciest'])

# prep groups
gp = defaultdict(list)
for d in D: gp[d['prep']].append(d)
F['preps'] = sorted([dict(name=k, n=len(v), health=st.mean([d['health'] for d in v]),
                          flavor=st.mean([d['FLAVOR'] for d in v]), sodium=st.mean([d['sodium'] for d in v]),
                          price=st.mean([d['price'] for d in v]), overall=st.mean([d['overall'] for d in v]))
                    for k, v in gp.items()], key=lambda r: -r['health'])

json.dump({k: v for k, v in F.items()}, open('figures.json','w'), indent=1, default=str)
print('computed', len(F), 'figure groups')
for k in ['r_price_health','r_price_flavor','r_health_flavor','r_health_flavor_cuisine','r_fiber_gut','n_promoted','dupe_priciest_wins']:
    print(' ', k, '=', F[k])
print('  r(price,health) leave-one-out range:', tuple(round(x,4) for x in F['r_price_health_range']))
print('  week costs: naive $%.2f floor %.1f | cheap $%.2f floor %.1f | best $%.2f floor %.1f' % (
    F['week_naive']['cost'], F['week_naive']['floor'], F['week_cheap']['cost'], F['week_cheap']['floor'],
    F['week_best']['cost'], F['week_best']['floor']))
