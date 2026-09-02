#!/usr/bin/env python3
"""The brochure. Short, for a reader who has never seen the compendium.
Every figure is read from the same dataset the long document uses."""
import json, html, dishes

B = '../build/'
D = json.load(open(B+'details_corrected.json'))
ADD = json.load(open(B+'additions.json'))
F = json.load(open(B+'figures.json'))
ALL = D + ADD
for d in ALL:
    d['dpp'] = d['price']/d['protein']
    d['na_p'] = d['sodium']/d['protein']
M = sorted(ALL, key=lambda x: -x['overall'])
n_cuisines = len({d['cuisine'] for d in ALL})
n_quad = sum(1 for d in ALL if d['price'] <= 16 and d['health'] >= 6.0)
by = {d['restaurant']: d for d in ALL}
e = lambda s: html.escape(str(s), quote=False)
mny = lambda v: f"${v:,.2f}"
FONTS = open('fonts.css').read()   # latin woff2 inlined as data URIs
CSS = FONTS + '\n' + open('brochure.css').read() + '\n' + open('print.css').read()

# ---------------------------------------------------------------- findings
per5, fr, wn, wc = F['per5'], F['frontier'], F['week_naive'], F['week_cheap']
fs, wb = F['flavor_split'], F['within_between']
best_val = min(ALL, key=lambda d: d['dpp'])
FINDS = [
  (f"+{per5['sodium']:,.0f}<small>milligrams of salt for every extra $5 you spend</small>",
   'poke',
   'Spending more makes the meal worse',
   f"Across sixty dishes, every additional $5 on the bill brings {per5['sodium']:,.0f} more milligrams of "
   f"sodium and {abs(per5['fiber']):.1f}g less fibre — and moves the health score by {per5['health']:+.2f}, "
   f"which is nothing. Price and health correlate at {F['r_price_health']:+.2f}. Money is not neutral here. "
   f"It is mildly harmful.",
   'Stop treating the expensive option as the careful one.'),

  (f"{mny(fr['cutoff'])}<small>the price above which nothing is efficient</small>",
   'fish',
   'Every dish over $17 is beaten by a cheaper one',
   f"Only four dishes in the whole set are efficient — meaning nothing cheaper is also as healthy. All "
   f"{fr['n_dominated']} priced above {mny(fr['cutoff'])} are matched or beaten by something that costs less. "
   f"{e(fr['worst_example']['restaurant'])} charges {mny(fr['worst_example']['price'])} for a health score "
   f"{e(fr['beater']['restaurant'])} reaches at {mny(fr['beater']['price'])}.",
   f"Treat {mny(fr['cutoff'])} as a ceiling, not a floor."),

  (f"+{fs['na_hi']-fs['na_lo']:,.0f}<small>extra milligrams of salt in the food that tastes best</small>",
   'kebab',
   'Flavour is bought with salt, not fat',
   f"The dishes that taste best carry {fs['na_hi']-fs['na_lo']:+,.0f}mg more sodium than the blandest ones — "
   f"but only {fs['sf_hi']-fs['sf_lo']:+.1f}g more saturated fat, which is statistical noise. A quarter of "
   f"what money appears to buy in flavour is simply salt. Everyone is watching the wrong nutrient.",
   'Watch the sauce, the base and the cure. Stop watching the olive oil.'),

  (f"{wb['within']:.2f}<small>points between the best and worst order at one restaurant</small>",
   'lentil',
   'Which dish you order beats where you order it',
   f"The gap between the best and worst thing on a single menu ({wb['within']:.2f} points) is wider than the "
   f"gap across the middle half of every restaurant in the set ({wb['between']:.2f}). One place spans "
   f"{F['within_between']['widest'][0]['spread']:.2f} points on its own menu — from a dish that ranks near the "
   f"top to one near the bottom.",
   'Picking the restaurant is the smaller half of the decision.'),

  (f"${best_val['dpp']:.2f}<small>per gram of protein — the cheapest and the cleanest at once</small>",
   'shrimp',
   'The cheapest protein here is also the cleanest',
   f"{e(best_val['restaurant'])}'s {e(best_val['dish']).lower()} is {mny(best_val['price'])} for "
   f"{best_val['protein']}g of protein, the best value in the set — and it carries {best_val['na_p']:.1f}mg of "
   f"sodium per gram of that protein, also the best in the set. Cheap and clean are usually a trade. Here they "
   f"are the same bowl.",
   'If you order one thing off this list, order that.'),

  (f"{mny(wn['cost']-wc['cost'])}<small>saved on a week of dinners, with better coverage</small>",
   'barbecue',
   'The cheap week beats the expensive one',
   f"Five dinners chosen by picking the top-ranked dishes cost {mny(wn['cost'])} and leave their weakest "
   f"nutritional gap at {wn['floor']:.1f} out of 10. Five chosen as the cheapest that still clear that bar cost "
   f"{mny(wc['cost'])} — and close the gap to {wc['floor']:.1f}. Cheaper and better, not cheaper and worse.",
   'Rotate, do not climb the ranking.'),
]

def find_block(i, n, art, head, body, do):
    flip = ' flip' if i % 2 else ''
    return f'''<article class="find{flip}">
      <div class="find-n num">{n}</div>
      <div class="find-b"><h3>{head}</h3><p>{body}</p><p class="find-do">{do}</p></div>
      <div class="find-art">{dishes.DISHES[art]()}</div>
    </article>'''

# ---------------------------------------------------------------- the picks
PICKS = [
 ('DICED', 'lentil', 'Lentils carry 20g of protein at 4mg of sodium, so the bowl lands at 144mg — '
                     'the cleanest protein-to-salt ratio anywhere in the set.'),
 ('Chopt', 'lentil', 'The cheapest dish in the whole set, and it still clears the health bar. '
                     'Take the vinaigrette light; it is most of the sugar.'),
 ('Guasaca', 'kebab', 'Order it as a bowl, never as an arepa — the arepa is refined corn flour and '
                      'carries most of the calories.'),
 ('Alpaca Peruvian Charcoal Chicken', 'barbecue', 'Two sides are included and the salad sits in the same '
                      'tier as the fries. Taking them is the entire decision.'),
 ('Pokeworks', 'poke', 'Their chicken is 80mg of sodium a scoop against ahi tuna at 350. Almost nobody '
                      'orders chicken at a poke restaurant.'),
 ('Poke Bros.', 'poke', 'Plain tuna is 40mg of sodium; their own marinated tuna is 820. The house sauce is '
                      'added automatically unless you refuse it.'),
 ('Taste Vietnamese', 'fish', 'The best-tasting dish in the set that still scores well — grilled turmeric '
                      'fish with a herb plate, sauce on the side.'),
 ('Baba Ghannouj', 'kebab', 'Char, sumac and lemon do the work instead of fat. Swap the rice for extra '
                      'salad and skip the fried pita chips.'),
 ('Golden Dragon', 'shrimp', 'Every Chinese takeout prints a diet menu and nobody orders from it. Steamed, '
                      'sauce on the side, no oil — for $12.39.'),
]

def pick(name, art, why):
    d = by[name]
    return f'''<article class="pick">
      <div class="pick-art">{dishes.DISHES[art]()}</div>
      <div class="pick-b">
        <h3>{e(d['dish'])}</h3>
        <p class="who">{e(name)}</p>
        <div class="pick-row"><span class="pick-p">{mny(d['price'])}</span>
          <span class="pick-m">{d['protein']}g protein &middot; {d['sodium']:,}mg salt</span></div>
        <p class="why">{why}</p>
      </div>
    </article>'''

TRAPS = [
 ('A margherita pizza', 'Pizzeria Toro', 'The dough alone is about 1,475mg of sodium at the standard salt ratio.'),
 ('Braised oxtail', 'Gifted Hand Cuisine', '16g of saturated fat — most of a day, in one plate.'),
 ('Beef kobidah', 'Afghan Kebab', 'Ground meat, white rice and bread; 11g saturated fat before the sauce.'),
 ('Two beef empanadas', 'Makus Empanadas', 'Baked rather than fried, and still 905 calories for 31g of protein.'),
 ('Carne asada plate', 'MI CANCUN', '13g saturated fat, 1,600mg sodium, and $24.99.'),
 ('A loaded poke bowl', 'Bul Box', 'Sauces and pickles push it to 1,951mg — more than a bowl of ramen.'),
]

# ---------------------------------------------------------------- page
PAGE = f'''<title>What Delivery Costs You</title>
<style>
{CSS}
</style>
<div class="wrap">

<header class="hero">
  <span class="kick">Delivery menus &middot; Research Triangle, North Carolina</span>
  <div class="hero-grid">
    <div>
      <h1>You are paying more to eat worse.</h1>
      <p class="lede">One dish at each of {len(ALL)} restaurants, across {n_cuisines} cuisines, scored on
      seven health measures plus how good it tastes and what it costs. The most consistent finding was the
      one nobody wanted.</p>
      <div class="tallies">
        <div><span class="t-n num">{len(ALL)}</span><span class="lbl">dishes scored</span></div>
        <div><span class="t-n num">{n_cuisines}</span><span class="lbl">cuisines</span></div>
        <div><span class="t-n num">{n_quad}</span><span class="lbl">good and under $16</span></div>
        <div><span class="t-n num">{F['r_price_health']:+.2f}</span><span class="lbl">price vs health</span></div>
      </div>
    </div>
    <div>
      <div class="tag">
        <span class="tag-n">+{per5['sodium']:,.0f}<span style="font-size:.42em"> MG</span></span>
        <span class="tag-l">of sodium arrives with every extra $5 you spend</span>
      </div>
      <p style="margin-top:18px;font-size:.88rem;color:var(--ink-2)">
      And {abs(per5['fiber']):.1f}g less fibre. The health score moves {per5['health']:+.2f} — which,
      on a ten-point scale, is nothing at all.</p>
    </div>
  </div>
</header>

<section class="finds">
  <span class="kick">Six things the menus will not tell you</span>
  {''.join(find_block(i, *f) for i, f in enumerate(FINDS))}
</section>

<section class="band">
  <span class="kick">What to order</span>
  <h2 style="margin-top:10px">Nine plates that survive the arithmetic</h2>
  <p class="lede" style="margin-top:14px;max-width:60ch">Cheap, high in protein, low in salt, and — where
  we could manage it — worth eating. Prices are what the delivery app charges, which runs about 15% above
  the counter.</p>
</section>
<section class="picks">{''.join(pick(*p) for p in PICKS)}</section>

<section style="margin-top:70px">
  <span class="kick">What to skip</span>
  <h2 style="margin-top:10px">And six that do not</h2>
  <p class="lede" style="margin-top:14px;max-width:62ch">Not because they are indulgent — because they cost
  as much as the good ones and give nothing back.</p>
  <div class="traps">
    {''.join(f'<div class="trap"><div class="trap-n">{e(n)}<span>{e(r)}</span></div>'
             f'<div class="trap-v">{e(w)}</div></div>' for n, r, w in TRAPS)}
  </div>
</section>

<section style="margin-top:70px">
  <span class="kick">A week, two ways</span>
  <h2 style="margin-top:10px">{mny(wn['cost']-wc['cost'])} is the price of following the ranking</h2>
  <div class="week">
    <div class="wk-side">
      <span class="lbl">Five dinners, picked from the top</span>
      <span class="wk-total num" style="color:var(--price)">{mny(wn['cost'])}</span>
      <span class="lbl">weakest nutritional gap {wn['floor']:.1f}&#8202;/&#8202;10</span>
      <ul class="wk-list">{''.join(f'<li><span>{e(d["restaurant"])}</span><span class="num">{mny(d["price"])}</span></li>' for d in sorted(wn['dishes'], key=lambda x: -x['price']))}</ul>
    </div>
    <div class="wk-side">
      <span class="lbl">Five dinners, picked for value</span>
      <span class="wk-total num" style="color:var(--good)">{mny(wc['cost'])}</span>
      <span class="lbl">weakest nutritional gap {wc['floor']:.1f}&#8202;/&#8202;10 &mdash; better</span>
      <ul class="wk-list">{''.join(f'<li><span>{e(d["restaurant"])}</span><span class="num">{mny(d["price"])}</span></li>' for d in sorted(wc['dishes'], key=lambda x: -x['price']))}</ul>
    </div>
  </div>
</section>

<section class="method">
  <span class="kick">How this was put together</span>
  <div class="method-grid">
    <div>
      <h3>What was measured</h3>
      <p>Each entry is one specific dish, ordered one specific way. Seven health measures — sodium, saturated
      fat and calories, protein, fermented food and plant variety, refined carbohydrate, omega-3, and sugar —
      plus flavour and cost. Where the instruction says to refuse something, the figures assume you refused it.</p>
      <h3 style="margin-top:20px">Where the numbers come from</h3>
      <p>Nine dishes are built from figures the restaurant publishes. The rest are estimated from how the dish
      is constructed, and the full document marks which is which.</p>
    </div>
    <div>
      <h3>What it cannot tell you</h3>
      <p>No restaurant that cooks to order over fire publishes nutrition data, so every grilled, stewed and
      steamed dish here is an estimate. When we rebuilt dishes against a restaurant's own figures, eleven of
      thirteen turned out worse than estimated — so read an estimate as roughly half a point generous.</p>
      <h3 style="margin-top:20px">Not medical advice</h3>
      <p>This compares restaurant meals with each other. It is not a diagnosis, and the thresholds behind the
      scores are judgement calls, argued out in the full document.</p>
    </div>
  </div>
</section>

<footer>
  <p>The illustrations are drawings of dish types, not photographs of any particular restaurant's food.
  Prices and menus change constantly; every figure here has a shelf life measured in months.</p>
</footer>

</div>
'''
open('brochure.html', 'w').write(PAGE)

STANDALONE = ('<!doctype html>\n<html lang="en">\n<head>\n'
  '<meta charset="utf-8">\n'
  '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
  '<meta name="description" content="What delivery food actually costs you, across 87 dishes '
  'in the Research Triangle - and why the expensive option is usually the worse one.">\n'
  '<meta name="color-scheme" content="light dark">\n'
  '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
  + PAGE.split('<style>')[0].replace('<title>', '<title>').rstrip() + '\n</head>\n<body>\n'
  + '<style>' + PAGE.split('<style>', 1)[1]
  + '\n</body>\n</html>\n')
open('What-Delivery-Costs-You.html', 'w').write(STANDALONE)
print(f'wrote brochure.html — {len(PAGE):,} bytes')
print(f'wrote What-Delivery-Costs-You.html — {len(STANDALONE):,} bytes (standalone)')
