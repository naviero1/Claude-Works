"""The full ranked set as one tall chart - 538's candy-power-ranking device,
with a second column the candy piece did not need.

Sorted by score, the bars descend by construction; that alone shows nothing.
The price marker beside each bar is on its own independent scale, so the reader
watches the bars shrink steadily while the price column stays scattered. The
central finding is then something you see rather than something you are told,
and it needs no coefficient to carry it.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROWS = json.load(open(os.path.join(HERE, 'all87.json')))
RAMP = json.load(open(os.path.join(HERE, '..', 'build', 'ramps.json')))

SOUND = ['KID', 'LIV', 'MUS', 'SUG']
TIERS = ['Order these', 'Worth ordering', 'With reservations', 'Not recommended']
TIER_NOTE = {
    'Order these':       'strong overall, and nothing collapses on the four criteria that are plain arithmetic',
    'Worth ordering':    'a good plate with one number worth knowing about',
    'With reservations': 'edible, unremarkable, or carrying a real cost somewhere',
    'Not recommended':   'the money is better spent almost anywhere else on this list',
}

# Character widths as a fraction of font size, for the sans stack used in the
# label column. Truncating on character count alone overflowed the bar column
# for names full of wide letters, so the dish and restaurant are fitted against
# a real pixel budget and the restaurant gives up its space first.
_W = {' ': .28, 'i': .24, 'j': .24, 'l': .24, 't': .32, 'f': .30, 'r': .35,
      'I': .28, 'J': .48, 'm': .86, 'w': .74, 'M': .86, 'W': .92,
      '.': .28, ',': .28, '·': .32, '(': .33, ')': .33, '/': .28, "'": .19}
def _tw(s, size):
    return size * sum(_W.get(c, .62 if c.isupper() or c.isdigit() else .54) for c in s)

def _clip(s, size, budget):
    if _tw(s, size) <= budget: return s
    while s and _tw(s + '…', size) > budget: s = s[:-1]
    return s.rstrip(' ,-') + '…'

def fit(dish, rest, budget, d_size=12, r_size=10, gap=5):
    """Give the dish what it needs, the restaurant whatever is left."""
    d = _clip(dish, d_size, budget * 0.72)
    left = budget - _tw(d, d_size) - gap
    return d, (_clip(rest, r_size, left) if left > r_size * 1.6 else '')


def esc(s):
    return (str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))

def chart(rows=ROWS, w=740, row_h=15.4):
    """One row per dish. Left: identity. Middle: score bar. Right: price on its
    own scale, so the two columns can be compared without either being derived
    from the other."""
    L, BAR_X, BAR_W, P_X, P_W, R = 30, 292, 210, 540, 150, 22
    pad_t, head = 8, 34
    # group into tiers, keeping rank order
    groups = [(t, [r for r in rows if r['tier'] == t]) for t in TIERS]
    groups = [(t, g) for t, g in groups if g]
    h = pad_t + head + sum(len(g) * row_h + 30 for _, g in groups) + 16

    S = [f'<svg viewBox="0 0 {w} {h:.0f}" class="rank87" role="img" '
         f'aria-label="All {len(rows)} dishes ranked by overall score, with each '
         f'dish\'s price shown on a separate scale alongside; the scores fall '
         f'steadily while the prices stay scattered">']

    # --- headers and the price scale, which needs its own ticks to be honest
    S.append(f'<text x="{L}" y="{pad_t+11}" class="rk-head">RANK &amp; DISH</text>')
    S.append(f'<text x="{BAR_X}" y="{pad_t+11}" class="rk-head">OVERALL SCORE &#183; 0 TO 10</text>')
    S.append(f'<text x="{P_X}" y="{pad_t+11}" class="rk-head">WHAT IT COSTS</text>')
    for gx in (10, 20, 30, 40):
        x = P_X + (gx - 8) / 34 * P_W
        S.append(f'<line x1="{x:.1f}" y1="{pad_t+16}" x2="{x:.1f}" y2="{h-14:.0f}" class="rk-pgrid"/>')
        S.append(f'<text x="{x:.1f}" y="{pad_t+27}" class="rk-ptick" text-anchor="middle">${gx}</text>')
    for gx in (2, 4, 6, 8, 10):
        x = BAR_X + gx / 10 * BAR_W
        S.append(f'<line x1="{x:.1f}" y1="{pad_t+16}" x2="{x:.1f}" y2="{h-14:.0f}" class="rk-sgrid"/>')
        S.append(f'<text x="{x:.1f}" y="{pad_t+27}" class="rk-ptick" text-anchor="middle">{gx}</text>')

    y = pad_t + head
    for tname, g in groups:
        y += 21
        S.append(f'<text x="{L}" y="{y:.1f}" class="rk-tier">{esc(tname).upper()} '
                 f'<tspan class="rk-tier-n">{len(g)}</tspan></text>')
        S.append(f'<text x="{BAR_X}" y="{y:.1f}" class="rk-tier-note">{esc(TIER_NOTE[tname])}</text>')
        S.append(f'<line x1="{L}" y1="{y+5:.1f}" x2="{w-R}" y2="{y+5:.1f}" class="rk-rule"/>')
        y += 12
        for r in g:
            cy = y + row_h * 0.5
            step = max(0, min(6, int(round((r['health'] - 3.0) / 5.5 * 6))))
            fill = RAMP['light']['health'][step][0]
            S.append(f'<g class="rk-row"><title>{esc(r["dish"])} at {esc(r["restaurant"])} '
                     f'&#183; ${r["price"]:.2f} &#183; overall {r["overall"]:.1f}, health '
                     f'{r["health"]:.1f}</title>')
            S.append(f'<rect x="{L-8}" y="{y:.1f}" width="{w-R-L+8:.0f}" height="{row_h:.1f}" class="rk-stripe"/>')
            S.append(f'<text x="{L+13}" y="{cy+3.4:.1f}" class="rk-n" text-anchor="end">{r["rank"]}</text>')
            # A demotion flag sits at the right edge of this column, so the
            # names have to be fitted into what is left after reserving for it.
            flag = (min(SOUND, key=lambda c: r[c])
                    if r['overall'] >= 6.5 and r['tier'] != 'Order these' else None)
            nm, rs = fit(r['dish'], r['restaurant'],
                         BAR_X - (L + 21) - 10 - (52 if flag else 0))
            S.append(f'<text x="{L+21}" y="{cy+3.4:.1f}" class="rk-d">{esc(nm)}'
                     f'<tspan class="rk-r"> {esc(rs)}</tspan></text>')
            # A dish can score well overall and still be held out of the top tier
            # by one of the four sound criteria. Flag it, or the tier boundaries
            # look like sorting errors.
            if flag:
                S.append(f'<text x="{BAR_X-6:.1f}" y="{cy+3.4:.1f}" class="rk-flag" '
                         f'text-anchor="end">{flag} {r[flag]:.1f}</text>')
            bw = r['overall'] / 10 * BAR_W
            S.append(f'<rect x="{BAR_X}" y="{y+3.1:.1f}" width="{bw:.1f}" height="{row_h-6.2:.1f}" '
                     f'rx="1" fill="{fill}" class="rk-bar"/>')
            S.append(f'<text x="{BAR_X+bw+5:.1f}" y="{cy+3.4:.1f}" class="rk-v">{r["overall"]:.1f}</text>')
            px = P_X + (r['price'] - 8) / 34 * P_W
            S.append(f'<line x1="{P_X}" y1="{cy:.1f}" x2="{px:.1f}" y2="{cy:.1f}" class="rk-pstem"/>')
            S.append(f'<circle cx="{px:.1f}" cy="{cy:.1f}" r="3.2" class="rk-pdot"/>')
            S.append(f'<text x="{px+6:.1f}" y="{cy+3.4:.1f}" class="rk-p">${r["price"]:.0f}</text>')
            S.append('</g>')
            y += row_h
        y += 9
    S.append('</svg>')
    return '\n'.join(S)

if __name__ == '__main__':
    open(os.path.join(HERE, 'rank87.svg'), 'w').write(chart())
    print(f'{len(ROWS)} rows written to rank87.svg')
