#!/usr/bin/env python3
"""Small visual mockups of the ways the 87-row ranking could be shown.
Not the finished thing - enough to judge the shape of each option."""
import json, statistics as st
from collections import defaultdict

B='../build/'
ALL = json.load(open(B+'details_corrected.json')) + json.load(open(B+'additions.json'))
for d in ALL: d['dpp']=d['price']/d['protein']
M = sorted(ALL, key=lambda x: -x['overall'])
e = lambda s: str(s).replace('&','&amp;').replace('<','&lt;')
mny = lambda v: f"${v:,.2f}"

FAM={'Levantine':'Middle East','Turkish':'Middle East','Persian':'Middle East','Halal cart':'Middle East',
 'Greek':'Middle East','North Indian':'South Asia','South Indian':'South Asia','Nepali':'South Asia',
 'Keralan':'South Asia','Indian street food':'South Asia','Afghan':'South Asia','Uzbek':'South Asia',
 'Japanese':'East Asia','Korean':'East Asia','Sichuan':'East Asia','Cantonese':'East Asia',
 'Chinese-American':'East Asia','Vietnamese':'Southeast Asia','Thai/Isaan':'Southeast Asia',
 'Burmese':'Southeast Asia','Hawaiian/poke':'Bowls & poke','US bowl chain':'Bowls & poke',
 'Mexican':'Latin America','Peruvian':'Latin America','Salvadoran':'Latin America','Venezuelan':'Latin America',
 'Cuban':'Latin America','Brazilian':'Latin America','Argentine':'Latin America','Latin American':'Latin America',
 'Caribbean':'Caribbean','Jamaican':'Caribbean','Ethiopian':'Africa','West African':'Africa','Nigerian':'Africa',
 'Southern African':'Africa','North Carolina barbecue':'American South','Southern and soul food':'American South',
 'Vegan Southern':'American South','American breakfast':'American','Burgers':'American','US breakfast':'American',
 'Neapolitan pizza':'European'}

def dots(v, n=5):
    """A five-step filled mark, the Consumer Reports convention."""
    f = round(v/10*n)
    return ''.join(f'<i class="d{"f" if i < f else "e"}"></i>' for i in range(n))

def row(d, rank=None):
    r = f'<td class="r">{rank}</td>' if rank else ''
    return (f'<tr>{r}<td class="nm"><b>{e(d["restaurant"])}</b><span>{e(d["dish"])}</span></td>'
            f'<td class="sc">{d["overall"]:.2f}</td>'
            f'<td class="dt">{dots(d["health"])}</td>'
            f'<td class="dt">{dots(d["FLAVOR"])}</td>'
            f'<td class="p">{mny(d["price"])}</td>'
            f'<td class="n">{d["protein"]}g</td><td class="n">{d["sodium"]:,}</td></tr>')

def head(ranked=False):
    r = '<th class="r"></th>' if ranked else ''
    return ('<thead><tr>' + r + '<th>Restaurant and dish</th><th class="sc">Score</th>'
            '<th class="dt">Health</th><th class="dt">Flavour</th><th class="p">Price</th>'
            '<th class="n">Pro</th><th class="n">Salt</th></tr></thead>')

def opt_full():
    rows = ''.join(row(d, i+1) for i, d in enumerate(M[:14]))
    return ('<h3>A · One straight list</h3><p class="cap">All 87 in score order. Shown: first 14.</p>'
            f'<table>{head(True)}<tbody>{rows}</tbody></table>')

def opt_price():
    out = ''
    for name, lo, hi in [('Under $13',0,13),('$13 to $17',13,17),('$17 to $22',17,22),('Over $22',22,99)]:
        g = sorted([d for d in ALL if lo <= d['price'] < hi], key=lambda x: -x['overall'])
        out += (f'<h4 class="band">{name} <span>{len(g)} dishes &middot; average score '
                f'{st.mean([d["overall"] for d in g]):.2f}</span></h4>'
                f'<table>{head()}<tbody>{"".join(row(d) for d in g[:3])}</tbody></table>')
    return ('<h3>B · Grouped by what it costs</h3>'
            '<p class="cap">The average score barely moves between bands &mdash; the structure itself '
            'makes the argument. Shown: top 3 of each band.</p>' + out)

def opt_family():
    fam = defaultdict(list)
    for d in ALL: fam[FAM.get(d['cuisine'], 'Other')].append(d)
    out = ''
    for k, v in sorted(fam.items(), key=lambda kv: -max(d['overall'] for d in kv[1]))[:4]:
        g = sorted(v, key=lambda x: -x['overall'])
        out += (f'<h4 class="band">{k} <span>{len(g)} dishes</span></h4>'
                f'<table>{head()}<tbody>{"".join(row(d) for d in g[:2])}</tbody></table>')
    return ('<h3>C · Grouped by kind of food</h3>'
            '<p class="cap">Eleven families, best first inside each. Answers &ldquo;I feel like Thai&rdquo;. '
            'Shown: 4 families, top 2 each.</p>' + out)

def opt_short():
    fam = defaultdict(list)
    for d in ALL: fam[FAM.get(d['cuisine'], 'Other')].append(d)
    best = sorted([max(v, key=lambda x: x['overall']) for v in fam.values()], key=lambda x: -x['overall'])
    return ('<h3>D · A shortlist, then the table</h3>'
            '<p class="cap">The best in each of eleven families as the feature, with the full 87 as a '
            'reference table behind it. Shown: the whole shortlist.</p>'
            f'<table>{head()}<tbody>{"".join(row(d) for d in best)}</tbody></table>')

def opt_chart():
    """All 87 as one plot - the whole ranking in a brochure-sized space."""
    W,H,PL,PR,PT,PB = 860,360,52,16,22,44
    x0,x1,y0,y1 = 9,38,2.8,8.2
    X = lambda v: PL+(v-x0)/(x1-x0)*(W-PL-PR)
    Y = lambda v: H-PB-(v-y0)/(y1-y0)*(H-PT-PB)
    s=[f'<svg viewBox="0 0 {W} {H}" class="chart">']
    for gy in [3,4,5,6,7,8]:
        s.append(f'<line x1="{PL}" y1="{Y(gy):.0f}" x2="{W-PR}" y2="{Y(gy):.0f}" class="g"/>')
        s.append(f'<text x="{PL-8}" y="{Y(gy)+4:.0f}" class="ty">{gy}</text>')
    for gx in [10,15,20,25,30,35]:
        s.append(f'<text x="{X(gx):.0f}" y="{H-PB+18}" class="tx">${gx}</text>')
    # band means, which is the finding
    for name,lo,hi in [('',0,13),('',13,17),('',17,22),('',22,99)]:
        g=[d for d in ALL if lo<=d['price']<hi]
        m=st.mean([d['overall'] for d in g])
        a,b=max(x0,lo),min(x1,hi)
        s.append(f'<line x1="{X(a):.0f}" y1="{Y(m):.0f}" x2="{X(b):.0f}" y2="{Y(m):.0f}" class="mean"/>')
    for d in ALL:
        cls='pt hi' if d['overall']>=6.8 else 'pt'
        s.append(f'<circle cx="{X(min(d["price"],x1)):.1f}" cy="{Y(d["overall"]):.1f}" r="4" class="{cls}"><title>'
                 f'{e(d["restaurant"])} — {mny(d["price"])}, {d["overall"]:.2f}</title></circle>')
    for nm,dx,dy in [('Poke Bros.',8,-7),('DICED',8,4),('Chopt',-8,-7),('Pizzeria Toro',-8,4),('M Sushi',-8,-7)]:
        d=next(x for x in ALL if x['restaurant']==nm)
        an='start' if dx>0 else 'end'
        s.append(f'<text x="{X(d["price"])+dx:.0f}" y="{Y(d["overall"])+dy:.0f}" class="lb" text-anchor="{an}">{e(nm)}</text>')
    s.append(f'<text x="{PL-42}" y="{PT-6}" class="ax">SCORE</text>')
    s.append(f'<text x="{W-PR}" y="{H-6}" class="ax" text-anchor="end">PRICE</text>')
    s.append('</svg>')
    return ('<h3>E &middot; The whole set as one picture</h3>'
            '<p class="cap">All 87 dishes at once. Each dot is a dish; the horizontal bars are the average '
            'score in each price band. The bars are flat &mdash; that is the finding, drawn rather than '
            'asserted. Hover a dot for its name.</p>' + ''.join(s))

CSS = '''
body{font:15px/1.55 Georgia,serif;color:#16171B;background:#FFFDF7;margin:0;padding:34px}
.wrap{max-width:900px;margin:0 auto}
h1{font:800 26px/1.2 Helvetica,Arial,sans-serif;margin:0 0 6px}
h2{font:700 14px/1.4 Helvetica,Arial,sans-serif;letter-spacing:.12em;text-transform:uppercase;
   color:#7E8290;margin:0 0 26px}
h3{font:800 19px/1.25 Helvetica,Arial,sans-serif;margin:38px 0 4px}
h4.band{font:700 11px/1.4 Helvetica,Arial,sans-serif;letter-spacing:.1em;text-transform:uppercase;
   margin:20px 0 5px;color:#16171B;border-bottom:2px solid #16171B;padding-bottom:5px}
h4.band span{float:right;font-weight:400;color:#7E8290;letter-spacing:.04em;text-transform:none}
.cap{font-size:13px;color:#565A66;margin:0 0 12px;max-width:70ch}
table{border-collapse:collapse;width:100%;font-size:13px;margin-bottom:6px}
th{font:700 9.5px/1.3 Helvetica,Arial,sans-serif;letter-spacing:.09em;text-transform:uppercase;
   color:#7E8290;text-align:left;padding:0 8px 5px 0;border-bottom:1.5px solid #16171B}
td{padding:6px 8px 6px 0;border-bottom:1px solid #E2DECF;vertical-align:top}
td.r{color:#9A9EAA;width:2em;font:500 12px ui-monospace,monospace}
td.nm b{display:block;font-weight:600;font-size:13.5px}
td.nm span{display:block;color:#565A66;font-size:12px}
td.sc,th.sc{font:500 13px ui-monospace,monospace;text-align:right;width:3.4em}
td.p,th.p{font:500 13px ui-monospace,monospace;text-align:right;width:4.6em}
td.n,th.n{font:500 12px ui-monospace,monospace;text-align:right;width:3.6em;color:#565A66}
td.dt,th.dt{width:5em;white-space:nowrap}
.d{display:inline-block}
i{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:2px;
  border:1.2px solid #1F6F5C}
i.df{background:#1F6F5C}
i.de{background:transparent}
.chart{width:100%;height:auto;margin-top:8px}
.chart .g{stroke:#E2DECF;stroke-width:1}
.chart .ty{font:500 10px ui-monospace,monospace;fill:#7E8290;text-anchor:end}
.chart .tx{font:500 10px ui-monospace,monospace;fill:#7E8290;text-anchor:middle}
.chart .ax{font:700 9px Helvetica,Arial,sans-serif;letter-spacing:.13em;fill:#7E8290}
.chart .pt{fill:#9A9EAA;opacity:.7}
.chart .pt.hi{fill:#1F6F5C;opacity:1}
.chart .mean{stroke:#C8102E;stroke-width:2.5}
.chart .lb{font:600 10.5px Helvetica,Arial,sans-serif;fill:#16171B}
'''

HTML = f'''<!doctype html><html><head><meta charset="utf-8">
<title>Ranking display options</title><style>{CSS}</style></head><body><div class="wrap">
<h1>Four ways to show 87 ranked dishes</h1>
<h2>Sketches, not finished pages &middot; the five-dot mark is the Consumer Reports convention</h2>
{opt_full()}{opt_price()}{opt_family()}{opt_short()}{opt_chart()}
</div></body></html>'''
open('mockups.html','w').write(HTML)
print(f'wrote mockups.html — {len(HTML):,} bytes')
