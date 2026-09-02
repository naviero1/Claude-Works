"""The entry object: everything one dish shows in the band body.

The nutrition-labelling tradition's rule is that a mark should carry the whole
scale and sit next to the input that produced it, so each criterion is drawn as
a numbered, tinted cell in a fixed position, and the raw measured value it came
from is printed beside the row. The position never varies, so after a few
entries the strip reads as a silhouette - a salty dish has a pale first cell -
rather than nine numbers to decode.

Zagat's rule supplies the other half: the price is printed as a dollar figure,
never converted into a score. A reader walking the bands sees the money and the
health numbers side by side, entry after entry, and the flatness arrives
without a chart.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
RAMP = json.load(open(os.path.join(HERE, '..', 'build', 'ramps.json')))

# The six computed from macros by arithmetic, then the three that are rubric
# judgements. The audit criticised the second group; keeping them visibly
# apart is the Burrito Bracket's algorithm-picks / human-scores disclosure.
# Labelled by the thing the reader can check on a label, not by the organ the
# criterion is named after. "Salt 4.2" beside "1,310 mg sodium" is a claim you
# can audit; "Kidney 4.2" is one you have to take on trust.
ARITHMETIC = [('KID', 'Salt',    'sodium',  '%d mg'),
              ('LIV', 'Fat',     'satfat',  '%g g sat fat'),
              ('MUS', 'Prot',    'protein', '%g g protein'),
              ('SUG', 'Sugar',   'sugar',   '%g g sugar')]
JUDGED     = [('GUT', 'Fibre',   'fiber',   '%g g fibre'),
              ('ENE', 'Fuel',    None,      None),
              ('INF', 'Inflam',  None,      None)]
TASTE      = [('FLAVOR', 'Taste', None, None), ('COST', 'Value', None, None)]

def esc(s):
    return (str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))

def tint(v, theme='light', key='health'):
    return RAMP[theme][key][max(0, min(6, int(round(v / 10 * 6))))]

def cells(d):
    """Nine cells, fixed order, never re-sorted. Solid = arithmetic on the
    macros; outlined = a rubric judgement."""
    out = []
    for group, kind, key in ((ARITHMETIC, 'calc', 'health'),
                             (JUDGED, 'judged', 'health'),
                             (TASTE, 'calc', None)):
        for code, label, macro, fmt in group:
            v = d[code]
            k = key or ('flavor' if code == 'FLAVOR' else 'cost')
            bg, fg = tint(v, 'light', k)
            raw = (fmt % d[macro]) if macro and fmt else ''
            title = f'{label} {v:.1f} of 10' + (f' — {raw}' if raw else '')
            out.append(
                f'<span class="cell c-{kind}" style="--bg:{bg};--fg:{fg}" '
                f'title="{esc(title)}"><b>{v:.1f}</b><i>{esc(label)}</i></span>')
    return ('<div class="cells">' + ''.join(out[:4]) +
            '<span class="cgap" aria-hidden="true"></span>' + ''.join(out[4:7]) +
            '<span class="cgap" aria-hidden="true"></span>' + ''.join(out[7:]) +
            '</div>')

def strong_weak(d):
    """One line naming the best and worst criterion by name, so a reader who
    reads nothing else still learns what this dish is good and bad at."""
    named = {'KID': 'salt', 'LIV': 'saturated fat', 'MUS': 'protein',
             'SUG': 'sugar', 'GUT': 'fibre', 'ENE': 'steady energy',
             'INF': 'inflammation'}
    ks = list(named)
    hi, lo = max(ks, key=lambda c: d[c]), min(ks, key=lambda c: d[c])
    return (f'<p class="sw"><b>Strong</b> on {named[hi]} ({d[hi]:.1f}). '
            f'<b>Weak</b> on {named[lo]} ({d[lo]:.1f}).</p>')

def entry(d, badge=False):
    conf = {'PUBLISHED': ('pub', 'published figures'),
            'PARTIAL': ('part', 'part published, part estimated'),
            }.get(d.get('data'), ('est', 'estimated from the build'))
    b = ('<span class="badge" title="Under $13 delivered, and health at or '
         'above 6.0">BEST BUY</span>' if badge else '')
    day = d['sodium'] / 2300 * 100
    return f'''<article class="entry">
 <header>
  <h4>{esc(d['dish'])}{b}</h4>
  <p class="who">{esc(d['restaurant'])} <span class="cu">{esc(d['cuisine'])}</span></p>
 </header>
 <p class="money"><b>${d['price']:.2f}</b> <span class="ov">{d['overall']:.1f}<i>overall</i></span>
    <span class="ov">{d['health']:.1f}<i>health</i></span></p>
 {cells(d)}
 {strong_weak(d)}
 <p class="raw">{d['cal']:.0f} kcal · {d['protein']:.0f} g protein ·
    {d['sodium']:.0f} mg sodium, <b>{day:.0f}% of a day</b> · {d['fiber']:.0f} g fibre
    <span class="conf conf-{conf[0]}">{conf[1]}</span></p>
</article>'''


def legend():
    """CAMRA prints its symbol key on the running foot of every body spread.
    One specimen here does the same job: it names all nine cells in the order
    they always appear, and says which are computed and which are judged."""
    def swatch(group, kind, key):
        out = []
        for code, label, macro, fmt in group:
            bg, fg = tint(7.4, 'light', key)
            out.append(f'<span class="cell c-{kind}" style="--bg:{bg};--fg:{fg}">'
                       f'<b>&nbsp;</b><i>{label}</i></span>')
        return ''.join(out)
    return f'''<div class="legend">
 <h3>How to read an entry</h3>
 <div class="lg-row">
  <div class="lg-part">
   <div class="cells">{swatch(ARITHMETIC, "calc", "health")}</div>
   <p><b>Solid cells are arithmetic.</b> Each is computed directly from a number on the
      label — salt from milligrams of sodium, fat from grams of saturated fat — and the
      raw figure is printed at the foot of every entry so you can check it.</p>
  </div>
  <div class="lg-part">
   <div class="cells">{swatch(JUDGED, "judged", "health")}</div>
   <p><b>Outlined cells are judgements.</b> These three score the dish against a written
      rubric rather than a measurement. Our own audit found them the weakest part of the
      model, so they are drawn differently everywhere and never carry a verdict alone.</p>
  </div>
  <div class="lg-part">
   <div class="cells">{swatch(TASTE, "calc", "flavor")}</div>
   <p><b>The last two are not health at all.</b> Taste is a rubric score for how good the
      dish is to eat; value is what it costs against what it delivers. They sit after a
      gap so they are never mistaken for the seven that precede them.</p>
  </div>
 </div>
 <p class="lg-foot">Every cell runs 0 to 10 and is tinted on the same scale, so a pale
    cell is a weak one wherever you meet it. The order never changes: after a few entries
    the strip reads as a shape rather than nine numbers.</p>
</div>'''
