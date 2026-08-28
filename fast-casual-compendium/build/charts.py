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
    LABEL = {4:('DICED',7,4),32:('Chopt',-7,-9),16:('Guasaca',7,15),1:('Poke Bros.',9,5),
             2:('El Cuscatleco',9,4),5:('M Sushi',-9,-9),38:('Chengdu 7',-9,-9),
             59:('Gifted Hand',-9,15),27:('Namu',-9,-9),30:('Udupi',-7,15)}
    for d in D:
        cls = 'pt pt-good' if (d['price'] <= 16 and d['health'] >= 6.0) else 'pt'
        s.append(f'<circle cx="{X(d["price"]):.1f}" cy="{Y(d["health"]):.1f}" r="4.6" class="{cls}"><title>{esc(d["restaurant"])} — ${d["price"]:.2f}, health {d["health"]:.1f}</title></circle>')
    for rk,(lab,dx,dy) in LABEL.items():
        d = next(x for x in D if x['rank'] == rk)
        anchor = 'start' if dx > 0 else 'end'
        s.append(f'<text x="{X(d["price"])+dx:.1f}" y="{Y(d["health"])+dy:.1f}" class="pt-label" text-anchor="{anchor}">{esc(lab)}</text>')
    n = quad_n if quad_n is not None else sum(1 for d in D if d['price'] <= 16 and d['health'] >= 6.0)
    s.append(f'<text x="{X(8.4):.1f}" y="{Y(8.42):.1f}" class="q-label">CHEAP AND GOOD FOR YOU &#183; {n} of {len(D)}</text>')
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

def crit_bars(d, w=132, h=26):
    """Compact nine-bar sparkline for one dish, in ranking rows."""
    keys = [('KID','h'),('LIV','h'),('MUS','h'),('GUT','h'),('ENE','h'),('INF','h'),('SUG','h'),('FLAVOR','f'),('COST','c')]
    bw, gap = 11, 2.6
    s = [f'<svg viewBox="0 0 {w} {h}" class="bars" aria-hidden="true">']
    x = 0
    for k, kind in keys:
        v = d[k]; bh = max(1.2, v/10*(h-4))
        if kind == 'f': x += 5
        s.append(f'<rect x="{x:.1f}" y="{h-2-bh:.1f}" width="{bw}" height="{bh:.1f}" class="b b-{kind}"/>')
        x += bw+gap
    s.append('</svg>')
    return '\n'.join(s)
