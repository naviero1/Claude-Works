"""Every number printed in the second edition is computed here. Nothing is typed by hand."""
import json, statistics as st, itertools, math, re
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
F['r_fiber_ene']    = pear([d['fiber'] for d in D], [d['ENE'] for d in D])

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
F['flavor_split']['na_median_gap'] = (st.median([d['sodium'] for d in _hi])
                                      - st.median([d['sodium'] for d in _lo]))
# leave-one-out: is the sodium gap the work of a single dish?
_loo = []
for _x in D:
    _S = [d for d in D if d is not _x]
    _h = [d['sodium'] for d in _S if d['FLAVOR'] >= 7.5]
    _l = [d['sodium'] for d in _S if d['FLAVOR'] <= 5.5]
    _loo.append((st.mean(_h) - st.mean(_l), welch(_h, _l)[0]))
F['na_gap_loo'] = dict(lo=min(g for g, _ in _loo), hi=max(g for g, _ in _loo),
                       min_t=min(t for _, t in _loo))

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
  dict(item='Farmside Kitchen seasoned quinoa', per='8 oz base portion', mg=900, protein=None,
       note='The base, before anything is put on it.'),
  dict(item='Chipotle chipotle-honey vinaigrette', per='2 fl oz', mg=850, protein=None,
       note='Also 220 calories and 12 g of sugar.'),
  dict(item='CAVA saffron basmati or brown rice', per='one base', mg=770, protein=None,
       note='Identical for both rices, and the largest sodium item among CAVA\'s bases.'),
  dict(item='Poke Bros. OG Sauce', per='one bowl', mg=730, protein=None,
       note='Added to every bowl unless you refuse it.'),
  dict(item='CAVA grilled chicken', per='one portion', mg=670, protein=28,
       note='CAVA\'s grilled steak is 280 mg for 23 g of protein.'),
  dict(item='Farmside Kitchen Signature grilled chicken', per='3.5 oz', mg=660, protein=None,
       note='A plain grilled breast is 190 mg for the same protein.'),
  dict(item='Bul Box sriracha', per='1 oz', mg=454, protein=None,
       note='The 30-calorie sauce, and four times the sodium of the 150-calorie one.'),
  dict(item='Pokeworks ahi tuna', per='2 oz scoop', mg=350, protein=14,
       note='Their chicken is 80 mg for the same scoop and 12 g of protein.'),
  dict(item='Chipotle chicken', per='4 oz', mg=310, protein=32,
       note='9.7 mg of sodium per gram of protein.'),
  dict(item='True Food Kitchen salmon add-on', per='one portion', mg=90, protein=29,
       note='3.1 mg per gram, and the cleanest protein on any menu here.'),
  dict(item='DICED grilled chicken', per='one portion', mg=69, protein=26,
       note='2.7 mg per gram.'),
  dict(item='Poke Bros. plain tuna', per='85 g', mg=40, protein=21,
       note='1.9 mg per gram. Their own marinated tuna is 820 mg.'),
]
F['salt_components'].sort(key=lambda x: -x['mg'])

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

# the market price of a flavor point, in sodium
_b, _a = (lambda x, y: (lambda mx, my: (sum((p-mx)*(q-my) for p, q in zip(x, y))/sum((p-mx)**2 for p in x),
                                        my - sum((p-mx)*(q-my) for p, q in zip(x, y))/sum((p-mx)**2 for p in x)*mx))
          (st.mean(x), st.mean(y)))([d['sodium'] for d in D], [d['FLAVOR'] for d in D])
F['flavor_price'] = dict(mg_per_point=1/_b, r=pear([d['sodium'] for d in D], [d['FLAVOR'] for d in D]),
                         slope=_b, intercept=_a)
_resid = [(d['FLAVOR'] - (_a + _b*d['sodium']), d) for d in D]
F['flavor_bargains'] = [dict(d=d, resid=r) for r, d in sorted(_resid, key=lambda t: -t[0]) if r > 1.0]
F['flavor_ripoffs'] = [dict(d=d, resid=r) for r, d in sorted(_resid, key=lambda t: t[0]) if r < -1.5]
F['flavor_bargain_grilled'] = sum(1 for x in F['flavor_bargains'] if x['d']['prep'] == 'grilled')

# the same grilled chicken, four chains, all published
F['chicken'] = sorted([
    dict(chain='Poke Bros.',   protein=29, sodium=63),
    dict(chain='DICED',        protein=26, sodium=69),
    dict(chain='Chipotle',     protein=32, sodium=310),
    dict(chain='CAVA',         protein=28, sodium=670),
], key=lambda c: c['sodium']/c['protein'])
for _c in F['chicken']: _c['per_g'] = _c['sodium']/_c['protein']
F['chicken_spread'] = F['chicken'][-1]['per_g']/F['chicken'][0]['per_g']

# do the vegetarian alternatives cost sodium per gram of protein?
_VPAT = re.compile(r'tofu|vegetarian|vegan|paneer|sofritas|no meat|grape leaves|vegetable momo'
                   r'|ban chan|root veggie|pitchfork|mushroom', re.I)
_vrows = []
for d in D:
    for _alt in d['alternatives']:
        if _VPAT.search(_alt['name'] + ' ' + _alt['change']):
            _vrows.append(dict(restaurant=d['restaurant'], alt=_alt['name'],
                               base=d['sodium']/d['protein'], new=_alt['sodium']/_alt['protein'],
                               jump=_alt['sodium']/_alt['protein'] - d['sodium']/d['protein']))
_vrows.sort(key=lambda r: -r['jump'])
F['veg_sodium'] = dict(n=len(_vrows), n_up=sum(1 for r in _vrows if r['jump'] > 0),
                       median_jump=st.median([r['jump'] for r in _vrows]), rows=_vrows[:5])

# why r(health, flavor) is near zero: decompose the covariance by criterion
_mf = st.mean([d['FLAVOR'] for d in D])
F['cov_decomp'] = []
for _c in CRIT:
    _xs = [d[_c] for d in D]; _mx = st.mean(_xs)
    _w = 0.7 if _c == 'SUG' else 1.0
    F['cov_decomp'].append(dict(crit=_c, contrib=_w/6.7*sum((a-_mx)*(b-_mf) for a, b in zip(_xs, [d['FLAVOR'] for d in D]))/len(D)))
F['cov_decomp'].sort(key=lambda r: r['contrib'])
def _health_without(d, drop):
    ks = [c for c in CRIT if c not in drop]
    t = sum(0.7 if c == 'SUG' else 1.0 for c in ks)
    return sum((0.7 if c == 'SUG' else 1.0)*d[c] for c in ks)/t
F['r_hf_variants'] = {name: pear([_health_without(d, drop) for d in D], [d['FLAVOR'] for d in D])
                      for name, drop in [('all', ()), ('no_kidney', ('KID',)),
                                         ('no_gut', ('GUT',)), ('no_kidney_no_gut', ('KID', 'GUT'))]}

# nobody publishes nutrition for food that meets fire
_cooked = [d for d in D if d['prep'] in ('grilled', 'stewed', 'steamed')]
_assembled = [d for d in D if d['prep'] in ('assembled', 'raw')]
F['verified_by_prep'] = dict(
    n_cooked=len(_cooked),
    n_cooked_verified=sum(1 for d in _cooked if d['data'] in ('PUBLISHED', 'PARTIAL')),
    n_assembled=len(_assembled),
    n_assembled_verified=sum(1 for d in _assembled if d['data'] in ('PUBLISHED', 'PARTIAL')))
_pub = [d for d in _assembled if d['data'] in ('PUBLISHED', 'PARTIAL')]
_est = [d for d in _assembled if d['data'] == 'ESTIMATED']
F['tier_controlled'] = dict(
    n_pub=len(_pub), n_est=len(_est),
    flavor_gap=st.mean([d['FLAVOR'] for d in _pub]) - st.mean([d['FLAVOR'] for d in _est]),
    sodium_gap=st.mean([d['sodium'] for d in _pub]) - st.mean([d['sodium'] for d in _est]),
    health_gap=st.mean([d['health'] for d in _pub]) - st.mean([d['health'] for d in _est]),
    raw_flavor_gap=F['tiers']['PUBLISHED']['flavor'] - F['tiers']['ESTIMATED']['flavor'],
    raw_sodium_gap=F['tiers']['PUBLISHED']['sodium'] - F['tiers']['ESTIMATED']['sodium'])

# what if the gut criterion were scored on fiber instead of ferments?
_mxf = max(d['fiber'] for d in D)
def _h_fiber(d):
    g = min(10.0, d['fiber']/_mxf*10)
    return (d['KID']+d['LIV']+d['MUS']+g+d['ENE']+d['INF']+0.7*d['SUG'])/6.7
_old = sorted(D, key=lambda d: -d['overall'])
_new = sorted(D, key=lambda d: -((_h_fiber(d)*6.7 + d['FLAVOR']*0.5 + d['COST']*0.5)/7.7))
F['gut_fiber_swap'] = dict(
    mean_move=st.mean([abs(_old.index(d)-_new.index(d)) for d in D]),
    max_move=max(abs(_old.index(d)-_new.index(d)) for d in D),
    movers=[dict(name=d['restaurant'], fiber=d['fiber'], gut=d['GUT'],
                 was=_old.index(d)+1, now=_new.index(d)+1)
            for d in sorted(D, key=lambda d: -abs(_old.index(d)-_new.index(d)))[:5]])

# coverage: what the first edition's sample over- and under-weights
_cu = defaultdict(list)
for d in D: _cu[d['cuisine']].append(d)
F['coverage'] = sorted([dict(name=k, n=len(v), share=len(v)/len(D),
                             overall=st.mean([d['overall'] for d in v]))
                        for k, v in _cu.items()], key=lambda r: -r['n'])
_bowlish = [d for d in D if d['cuisine'] in ('US bowl chain', 'Hawaiian/poke')]
F['bowl_share'] = dict(n=len(_bowlish), pct=len(_bowlish)/len(D)*100,
                       in_top10=sum(1 for d in sorted(D, key=lambda x: -x['overall'])[:10]
                                    if d in _bowlish))
F['absent'] = [
  'North Carolina barbecue', 'Southern and soul food', 'Greek', 'Persian',
  'Chinese-American takeout', 'West African', 'Brazilian', 'Filipino',
  'Colombian, Cuban or Puerto Rican', 'Burmese', 'Malaysian or Indonesian',
  'Taiwanese', 'Halal cart', 'Chaat and Indian street food', 'Pakistani or Bangladeshi',
  'Seafood and raw bar', 'Pizza', 'Burgers and sandwiches', 'Wings',
  'A dedicated vegan kitchen',
]

# price-health efficient frontier
_S = sorted(D, key=lambda d: (d['price'], -d['health']))
_front, _best = [], -1
for _d in _S:
    if _d['health'] > _best: _front.append(_d); _best = _d['health']
_cut = _front[-1]['price']
_over = [d for d in D if d['price'] > _cut]
_dom = [d for d in _over if any(x['price'] <= d['price'] and x['health'] >= d['health'] and x is not d for x in D)]
# the dominated dish whose cheaper equal saves the most money
_pairs = []
for _d in _over:
    _b = min([x for x in D if x['health'] >= _d['health'] and x is not _d], key=lambda x: x['price'], default=None)
    if _b: _pairs.append((_d['price'] - _b['price'], _d, _b))
_pairs.sort(key=lambda t: -t[0])
F['frontier'] = dict(dishes=_front, cutoff=_cut, n_over=len(_over), n_dominated=len(_dom),
                     worst_example=_pairs[0][1], beater=_pairs[0][2], gap=_pairs[0][0])

# what an extra five dollars buys
def _ols(x, y):
    mx, my = st.mean(x), st.mean(y)
    return sum((a-mx)*(c-my) for a, c in zip(x, y))/sum((a-mx)**2 for a in x)
_P = [d['price'] for d in D]
F['per5'] = dict(sodium=_ols(_P, [d['sodium'] for d in D])*5,
                 fiber=_ols(_P, [d['fiber'] for d in D])*5,
                 health=_ols(_P, [d['health'] for d in D])*5,
                 flavor=_ols(_P, [d['FLAVOR'] for d in D])*5)
_t = sorted(D, key=lambda d: d['price']); _n = len(_t)//3
F['terciles'] = [dict(label=lab,
                      price=st.median([d['price'] for d in g]),
                      sodium=st.median([d['sodium'] for d in g]),
                      KID=st.median([d['KID'] for d in g]),
                      health=st.median([d['health'] for d in g]),
                      flavor=st.median([d['FLAVOR'] for d in g]))
                 for lab, g in [('cheapest third', _t[:_n]), ('middle third', _t[_n:2*_n]),
                                ('priciest third', _t[2*_n:])]]

# is the price-flavor link really a price-salt link?
_rpf, _rfn, _rpn = (pear(_P, [d['FLAVOR'] for d in D]),
                    pear([d['FLAVOR'] for d in D], [d['sodium'] for d in D]),
                    pear(_P, [d['sodium'] for d in D]))
F['r_flavor_sodium'] = _rfn
F['partial_price_flavor'] = (_rpf - _rpn*_rfn)/math.sqrt((1-_rpn**2)*(1-_rfn**2))

# does which dish beat which restaurant?
_sp = []
for d in D:
    if d.get('corrected') or d.get('disputed') or not d['alternatives']: continue
    _sc = [d['overall']] + [a['score'] for a in d['alternatives']]
    _sp.append(dict(name=d['restaurant'], spread=max(_sc)-min(_sc), hi=max(_sc), lo=min(_sc)))
_sp.sort(key=lambda r: -r['spread'])
_all = sorted(d['overall'] for d in D)
F['within_between'] = dict(within=st.median([r['spread'] for r in _sp]),
                           between=_all[3*len(_all)//4] - _all[len(_all)//4],
                           n=len(_sp), widest=_sp[:3])

# meat-free dishes cost more per gram of protein
_VEG = {'Abol Ethiopian', "Naga's South Indian", 'Goorsha', 'Southern Spice', 'Udupi Cafe',
        'Szechuan Mansion Hotpot', 'First Watch', 'Panera Bread'}
_veg = [d for d in D if d['restaurant'] in _VEG]; _rest = [d for d in D if d['restaurant'] not in _VEG]
F['veg'] = {k: dict(n=len(g), dpp=st.median([d['price']/d['protein'] for d in g]),
                    protein=st.median([d['protein'] for d in g]),
                    health=st.median([d['health'] for d in g]))
            for k, g in [('meat_free', _veg), ('rest', _rest)]}

# the price band that contains everything
_band = [d for d in D if 15.50 <= d['price'] <= 17.00]
F['shelf'] = dict(n=len(_band), lo=15.50, hi=17.00,
                  health_lo=min(d['health'] for d in _band), health_hi=max(d['health'] for d in _band),
                  set_lo=min(d['health'] for d in D), set_hi=max(d['health'] for d in D),
                  best=max(_band, key=lambda d: d['health']), worst=min(_band, key=lambda d: d['health']))

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
