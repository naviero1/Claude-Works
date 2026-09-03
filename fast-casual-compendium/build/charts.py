"""Inline SVG charts. Colors come from CSS custom properties so both themes work."""
import json, statistics as st

def esc(s): return (str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;'))

def linreg(xs, ys):
    mx, my = st.mean(xs), st.mean(ys)
    den = sum((x-mx)**2 for x in xs)
    m = sum((x-mx)*(y-my) for x, y in zip(xs, ys))/den
    return m, my - m*mx

def scatter_price_health(D, w=760, h=440, quad_n=None):
    pad_l, pad_r, pad_t, pad_b = 54, 18, 22, 46
    xs = [d['price'] for d in D]; ys = [d['health'] for d in D]
    x0, x1 = 8, 38; y0, y1 = 3.5, 8.5
    X = lambda v: pad_l + (v-x0)/(x1-x0)*(w-pad_l-pad_r)
    Y = lambda v: h-pad_b - (v-y0)/(y1-y0)*(h-pad_t-pad_b)
    s = [f'<svg viewBox="0 0 {w} {h}" class="chart" role="img" aria-label="Price against health score for all sixty dishes; the fitted line is flat">']
    # quadrant shade: cheap and good
    s.append(f'<rect x="{X(x0):.1f}" y="{Y(8.5):.1f}" width="{X(16)-X(x0):.1f}" height="{Y(6.0)-Y(8.5):.1f}" class="q-good"/>')
    s.append(f'<line x1="{X(16):.1f}" y1="{pad_t}" x2="{X(16):.1f}" y2="{h-pad_b}" class="q-line"/>')
    s.append(f'<line x1="{pad_l}" y1="{Y(6.0):.1f}" x2="{w-pad_r}" y2="{Y(6.0):.1f}" class="q-line"/>')
    for gy in [4,5,6,7,8]:
        s.append(f'<line x1="{pad_l}" y1="{Y(gy):.1f}" x2="{w-pad_r}" y2="{Y(gy):.1f}" class="grid"/>')
        s.append(f'<text x="{pad_l-10}" y="{Y(gy)+4:.1f}" class="tick tick-y">{gy}.0</text>')
    for gx in [10,15,20,25,30,35]:
        s.append(f'<text x="{X(gx):.1f}" y="{h-pad_b+20}" class="tick tick-x">${gx}</text>')
    m, b = linreg(xs, ys)
    s.append(f'<line x1="{X(x0):.1f}" y1="{Y(m*x0+b):.1f}" x2="{X(x1):.1f}" y2="{Y(m*x1+b):.1f}" class="fit"/>')
    LABEL = {4:('DICED',7,4),32:('Chopt',-7,-9),16:('Guasaca',-8,16),1:('Poke Bros.',9,5),
             2:('El Cuscatleco',9,17),5:('M Sushi',-9,-9),38:('Chengdu 7',-9,-9),
             59:('Gifted Hand',-9,15),27:('Namu',-9,-9),30:('Udupi',-7,15)}
    for d in D:
        cls = 'pt pt-good' if (d['price'] <= 16 and d['health'] >= 6.0) else 'pt'
        s.append(f'<circle cx="{X(d["price"]):.1f}" cy="{Y(d["health"]):.1f}" r="4.6" class="{cls}"><title>{esc(d["restaurant"])} — ${d["price"]:.2f}, health {d["health"]:.1f}</title></circle>')
    for rk,(lab,dx,dy) in LABEL.items():
        d = next(x for x in D if x['rank'] == rk)
        anchor = 'start' if dx > 0 else 'end'
        s.append(f'<text x="{X(d["price"])+dx:.1f}" y="{Y(d["health"])+dy:.1f}" class="pt-label" text-anchor="{anchor}">{esc(lab)}</text>')
    n = quad_n if quad_n is not None else sum(1 for d in D if d['price'] <= 16 and d['health'] >= 6.0)
    s.append(f'<text x="{X(8.4):.1f}" y="{Y(8.42):.1f}" class="q-label">CHEAP AND GOOD &#183; {n} OF {len(D)}</text>')
    s.append(f'<text x="{pad_l-40}" y="{pad_t-6}" class="axis-title">HEALTH</text>')
    s.append(f'<text x="{w-pad_r}" y="{h-6}" class="axis-title" text-anchor="end">DOORDASH PRICE</text>')
    s.append('</svg>')
    return '\n'.join(s)

def cuisine_map(F, w=760, h=460):
    C = F['cuisines']
    pad_l, pad_r, pad_t, pad_b = 54, 18, 22, 46
    x0, x1 = 4.0, 9.0; y0, y1 = 4.0, 7.6
    X = lambda v: pad_l + (v-x0)/(x1-x0)*(w-pad_l-pad_r)
    Y = lambda v: h-pad_b - (v-y0)/(y1-y0)*(h-pad_t-pad_b)
    s = [f'<svg viewBox="0 0 {w} {h}" class="chart" role="img" aria-label="Mean flavor against mean health for each cuisine; the trend runs downward">']
    for gy in [4,5,6,7]:
        s.append(f'<line x1="{pad_l}" y1="{Y(gy):.1f}" x2="{w-pad_r}" y2="{Y(gy):.1f}" class="grid"/>')
        s.append(f'<text x="{pad_l-10}" y="{Y(gy)+4:.1f}" class="tick tick-y">{gy}.0</text>')
    for gx in [4,5,6,7,8,9]:
        s.append(f'<text x="{X(gx):.1f}" y="{h-pad_b+20}" class="tick tick-x">{gx}.0</text>')
    xs = [c['flavor'] for c in C]; ys = [c['health'] for c in C]
    m, b = linreg(xs, ys)
    s.append(f'<line x1="{X(x0):.1f}" y1="{Y(m*x0+b):.1f}" x2="{X(x1):.1f}" y2="{Y(m*x1+b):.1f}" class="fit fit-down"/>')
    OFF = {'Hawaiian/poke':(0,-16),'US bowl chain':(0,16),'Japanese':(0,-16),'Peruvian':(0,16),
           'Levantine':(0,-16),'Ethiopian':(0,17),'Korean':(-14,-15),'North Indian':(10,20),
           'Sichuan':(0,-16),'Vietnamese':(0,17),'South Indian':(0,-16),'Mexican':(-6,17),'Caribbean':(14,-15)}
    for c in C:
        r = 5 + c['n']*1.15
        s.append(f'<circle cx="{X(c["flavor"]):.1f}" cy="{Y(c["health"]):.1f}" r="{r:.1f}" class="bub"><title>{esc(c["name"])} — n={c["n"]}, flavor {c["flavor"]:.1f}, health {c["health"]:.1f}, mean sodium {c["sodium"]:.0f} mg</title></circle>')
        dx, dy = OFF.get(c['name'], (0, -16))
        s.append(f'<text x="{X(c["flavor"])+dx:.1f}" y="{Y(c["health"])+dy:.1f}" class="bub-label" text-anchor="middle">{esc(c["name"])}</text>')
    s.append(f'<text x="{pad_l-40}" y="{pad_t-6}" class="axis-title">HEALTH</text>')
    s.append(f'<text x="{w-pad_r}" y="{h-6}" class="axis-title" text-anchor="end">FLAVOR</text>')
    s.append('</svg>')
    return '\n'.join(s)

def sodium_ladder(F, w=760):
    rows = F['na_best'] + [None] + F['na_worst']
    rh, pad_t, pad_l = 26, 26, 190
    h = pad_t + len(rows)*rh + 46
    mx = max(d['sodium']/d['protein'] for d in F['na_worst'])
    step = 10 if mx <= 80 else 20
    ticks = list(range(0, int(mx//step)*step + 1, step))
    s = [f'<svg viewBox="0 0 {w} {h}" class="chart" role="img" aria-label="Milligrams of sodium per gram of protein, best ten and worst six">']
    for gx in ticks:
        x = pad_l + gx/mx*(w-pad_l-60)
        s.append(f'<line x1="{x:.1f}" y1="{pad_t-8}" x2="{x:.1f}" y2="{h-42}" class="grid"/>')
        s.append(f'<text x="{x:.1f}" y="{h-28}" class="tick tick-x">{gx}</text>')
    for i, d in enumerate(rows):
        y = pad_t + i*rh
        if d is None:
            s.append(f'<line x1="{pad_l}" y1="{y+rh/2:.1f}" x2="{w-60}" y2="{y+rh/2:.1f}" class="break"/>')
            s.append(f'<text x="{pad_l-10}" y="{y+rh/2+4:.1f}" class="row-label dim" text-anchor="end">the other 44 dishes</text>')
            continue
        v = d['sodium']/d['protein']
        bw = v/mx*(w-pad_l-60)
        good = v <= 25
        s.append(f'<rect x="{pad_l}" y="{y+4:.1f}" width="{bw:.1f}" height="{rh-11}" class="{"bar bar-good" if good else "bar bar-bad"}"><title>{esc(d["restaurant"])} — {d["sodium"]} mg over {d["protein"]} g protein</title></rect>')
        s.append(f'<text x="{pad_l-10}" y="{y+rh/2+4:.1f}" class="row-label" text-anchor="end">{esc(d["restaurant"])}</text>')
        s.append(f'<text x="{pad_l+bw+8:.1f}" y="{y+rh/2+4:.1f}" class="row-val">{v:.1f}</text>')
    s.append(f'<text x="{pad_l}" y="{h-6}" class="axis-title">MILLIGRAMS OF SODIUM PER GRAM OF PROTEIN</text>')
    s.append('</svg>')
    return '\n'.join(s)

# ---- score cells -------------------------------------------------------------
# The nine criteria used to render as an unlabelled bar sparkline: it showed a
# shape but the reader could not tell which bar was which. They are now nine real
# table cells sitting under nine labelled column headers, each printing its score
# on a tint from that criterion group's sequential ramp. That makes the row
# self-labelling, makes the columns comparable down the table, and keeps the
# number itself on the page. Ramps and their ink are generated and contrast-
# checked in ramps.py.
import json as _json, os as _os
_RAMPS = _json.load(open(_os.path.join(_os.path.dirname(__file__), 'ramps.json'))) \
    if _os.path.exists(_os.path.join(_os.path.dirname(__file__), 'ramps.json')) else None

CRITERIA = [
    ('KID', 'Kidney',       'health', 'Sodium alone'),
    ('LIV', 'Liver',        'health', 'Saturated fat and calorie load'),
    ('MUS', 'Muscle',       'health', 'Protein density and absolute protein'),
    ('GUT', 'Gut',          'health', 'Live ferments and plant-type count'),
    ('ENE', 'Energy',       'health', 'Refined-carb load, fiber, protein'),
    ('INF', 'Inflammation', 'health', 'Omega-3 and plant diversity'),
    ('SUG', 'Sugar',        'health', 'Total sugars, at 0.7 weight'),
    ('FLAVOR', 'Flavor',    'flavor', 'Where the intensity comes from, at 0.5 weight'),
    ('COST', 'Cost',        'cost',   'Price and price per gram of protein, at 0.5 weight'),
]

def score_cells(d, compact=False):
    """Nine tinted, numbered cells - one per criterion, in header order."""
    out = []
    for i, (key, name, group, _) in enumerate(CRITERIA):
        v = d[key]
        step = min(6, max(0, int(round(v/10*6))))
        gap = ' sc-gap' if key == 'FLAVOR' else ''
        out.append(f'<td class="sc-td{gap}"><span class="sc sc-{group}" '
                   f'data-step="{step}" title="{name}: {v:.1f} of 10">{v:.1f}</span></td>')
    return ''.join(out)

def score_headers():
    """The nine column headers the cells sit under."""
    out = []
    for key, name, group, why in CRITERIA:
        gap = ' sc-gap' if key == 'FLAVOR' else ''
        out.append(f'<th class="sc-h sc-h-{group}{gap}" title="{name} - {why}">'
                   f'<abbr>{key[:3]}</abbr></th>')
    return ''.join(out)

def ramp_css():
    """Emit the tint and ink for every step of every ramp, both themes."""
    if not _RAMPS: return ''
    lines = [':root{']
    for g, steps in _RAMPS['light'].items():
        for i, (bg, ink) in enumerate(steps):
            lines.append(f'  --sc-{g}-{i}:{bg}; --sc-{g}-{i}-ink:{ink};')
    lines.append('}')
    dark = []
    for g, steps in _RAMPS['dark'].items():
        for i, (bg, ink) in enumerate(steps):
            dark.append(f'  --sc-{g}-{i}:{bg}; --sc-{g}-{i}-ink:{ink};')
    body = '\n'.join(dark)
    lines.append('@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){\n'
                 + body + '\n}}')
    lines.append(':root[data-theme="dark"]{\n' + body + '\n}')
    rules = []
    for g in _RAMPS['light']:
        for i in range(7):
            rules.append(f'.sc-{g}[data-step="{i}"]{{background:var(--sc-{g}-{i});'
                         f'color:var(--sc-{g}-{i}-ink)}}')
    return '\n'.join(lines + rules)

def legend():
    """A key naming every column, so the abbreviations never need decoding."""
    items = ''.join(
        f'<div class="lg-item lg-{g}"><span class="lg-k">{k[:3]}</span>'
        f'<span class="lg-n">{n}</span><span class="lg-w">{w}</span></div>'
        for k, n, g, w in CRITERIA)
    return ('<div class="lg"><div class="lg-scale">'
            + ''.join(f'<i class="sc-health" data-step="{i}"></i>' for i in range(7))
            + '<span class="lg-scale-t">0 &rarr; 10, pale to deep</span></div>'
            f'<div class="lg-grid">{items}</div></div>')
