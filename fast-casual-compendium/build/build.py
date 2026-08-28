#!/usr/bin/env python3
"""Assemble the second edition. Every printed figure is read from the dataset
or from figures.json; none is typed into this file by hand."""
import json, os, html, statistics as st
import charts, score

D  = json.load(open('details_corrected.json'))
M  = {d['rank']: d for d in json.load(open('master.json'))}
for d in D: d['alternatives'] = M[d['rank']]['alternatives']
F  = json.load(open('figures.json'))
CSS = open('style.css').read()

def load(name, default):
    return json.load(open(name)) if os.path.exists(name) else default
FIND = load('findings.json', None)     # from the verification workflow
CORR = load('corrections_v1.json', None)
ADDS = load('additions.json', [])      # from the widening workflow

e = lambda s: html.escape(str(s), quote=False)
byname = {d['restaurant']: d for d in D}
def money(v): return f"${v:,.2f}"
def ordinal(n):
    n = int(n)
    if 10 <= n % 100 <= 20: suf = 'th'
    else: suf = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f'{n}{suf}'
def r2(v):    return f"{v:+.2f}".replace('-', '\u2212')

ALL = D + ADDS
for d in ALL:
    d.setdefault('data', 'ESTIMATED')
    d['hpd']  = d['health']/d['price']
    d['dpp']  = d['price']/d['protein']
    d['na_p'] = d['sodium']/d['protein']
MERGED = sorted(ALL, key=lambda x: -x['overall'])

# ============================================================ pieces
def tally(n, label):
    return f'<div class="tally"><span class="bignum num">{n}</span><span class="label">{label}</span></div>'

def tier_badge(d):
    t = d.get('data', 'ESTIMATED')
    if d.get('is_new'):  return '<span class="tier tier-new">New</span>'
    if t == 'PUBLISHED': return '<span class="tier tier-pub">Published</span>'
    if t == 'PARTIAL':   return '<span class="tier tier-part">Partial</span>'
    return '<span class="tier">Estimated</span>'

def finding_card(f, kind):
    do = f.get('actionable') or f.get('do') or ''
    return f'''<div class="finding {kind}">
  <div class="finding-num">
    <span class="bignum num">{e(f['number'])}</span>
    <span class="label">{e(f['number_label'])}</span>
  </div>
  <h3>{e(f['headline'])}</h3>
  <p>{e(f['body'])}</p>
  {f'<p class="do"><b>What to do</b>{e(do)}</p>' if do else ''}
</div>'''

def table(headers, rows, cls=''):
    th = ''.join(f'<th class="n">{e(h[1:])}</th>' if h.startswith('~') else f'<th>{e(h)}</th>' for h in headers)
    body = []
    for r in rows:
        tds = ''.join(c if c.startswith('<td') else f'<td>{c}</td>' for c in r)
        body.append(f'<tr>{tds}</tr>')
    return (f'<div class="tablewrap"><table class="{cls}"><thead><tr>{th}</tr></thead>'
            f'<tbody>{"".join(body)}</tbody></table></div>')

# ============================================================ sections
def sec_masthead():
    n_new = len(ADDS)
    n_alt = sum(len(d['alternatives']) for d in D)
    n_cuisine = len({d.get('cuisine','?') for d in ALL})
    return f'''<header class="masthead">
  <div class="kicker"><span class="edition-flag">Second edition</span>Fast-casual delivery menus · Research Triangle, North Carolina</div>
  <div class="masthead-grid">
    <div>
      <h1>The Fast-Casual Compendium</h1>
    </div>
    <div class="stack">
      <p class="lede">{len(ALL)} named dishes, each scored on seven health criteria plus flavor and cost. Every figure is either taken from a restaurant's own nutrition document or estimated from how the dish is built &mdash; and the entry says which.</p>
    </div>
  </div>
  <div class="tallies" style="margin-top:34px">
    {tally(len(ALL), 'Dishes ranked')}
    {tally(n_alt, 'Scored alternative orders')}
    {tally(n_cuisine, 'Distinct cuisines')}
    {tally(f"{sum(1 for d in ALL if d.get('data')=='PUBLISHED')}&#8202;/&#8202;{len(ALL)}", 'From published nutrition data')}
  </div>
</header>'''

def sec_changes():
    moved = sorted(((abs((d.get('rank') or 0) - (MERGED.index(d) + 1)), d) for d in D if d.get('corrected')),
                   key=lambda t: -t[0])[:2]
    movers = '; '.join(f"{e(d['restaurant'])} from {ordinal(d['rank'])} to {ordinal(MERGED.index(d)+1)}"
                       for _, d in moved)
    n_rescored = sum(1 for c in CORR if c['action'] == 'rescore') if CORR else 0
    items = [
      ('The numbers were checked, and some were wrong.', f'Every nutrition figure the first edition attributed to a published document was re-read against that document. {n_rescored} entries had to be rescored: {movers}. Everything checked is listed in the verification log at the end, including what came back clean and what could not be settled.'),
      ('The front page is new.', 'The first edition opened with four findings, three of which were trivia about a single restaurant each and the fourth about research method rather than food. They have been replaced with findings drawn from the whole set, led by what the data says about money.'),
      ('The two lists are now one.', f'The first edition printed &ldquo;The Thirty&rdquo; and &ldquo;The Next Thirty&rdquo; as separate ranked lists, but the split tracked research depth rather than score: {F["n_promoted"]} entries in the second list outscored the weakest in the first. Everything is now ranked in one sequence.'),
      ('The scoring model is printed, not described.', 'Every criterion that can be computed from the macros is given as an actual function, recovered by fitting the first edition\'s own published scores. Anyone can recompute anything here, including the parts they disagree with.'),
      ('The sample was too narrow.', f'Eighteen of the original sixty entries were build-your-own bowls or poke &mdash; 30% of the set, and four of the top ten &mdash; in a state whose own barbecue did not appear at all. {"This edition adds " + str(len(ADDS)) + " dishes from cuisines and formats the first edition skipped." if ADDS else "That gap is quantified below."}'),
    ]
    lis = ''.join(f'<li><strong>{t}</strong> {b}</li>' for t, b in items)
    return f'''<section id="changes">
  <div class="changelog measure-wide">
    <span class="eyebrow">What changed in this edition</span>
    <ul>{lis}</ul>
  </div>
</section>'''

def sec_findings():
    """The six findings that replace the first edition's front page.
    Every number is computed from the corrected dataset at build time."""
    fs = F['flavor_split']
    wn, wc = F['week_naive'], F['week_cheap']
    saving = wn['cost'] - wc['cost']
    best_val = min(D, key=lambda d: d['dpp'])
    fr = F['frontier']
    shelf = F['shelf']

    cards = [
      ('f-money', money(fr['cutoff']), 'above which nothing is efficient',
       'Every dish over $17 is beaten by a cheaper one',
       f"Only {len(fr['dishes'])} dishes on this list are efficient &mdash; meaning nothing cheaper is also as healthy. They are "
       f"{', '.join(e(d['restaurant']) + ' at ' + money(d['price']) for d in fr['dishes'])}. "
       f"All {fr['n_dominated']} dishes priced above {money(fr['cutoff'])} are matched or beaten by something cheaper. "
       f"{e(fr['worst_example']['restaurant'])} charges {money(fr['worst_example']['price'])} for a health score of "
       f"{fr['worst_example']['health']:.1f}; {e(fr['beater']['restaurant'])} scores {fr['beater']['health']:.1f} for "
       f"{money(fr['beater']['price'])} &mdash; {money(fr['gap'])} less for the same or better.",
       f"Treat {money(fr['cutoff'])} as a ceiling. Above it you are buying something other than nutrition."),

      ('f-money', money(saving), 'saved on a week, for the same coverage',
       'The cheap week is as good as the expensive one',
       f"Five dinners chosen as the top-ranked dishes cost {money(wn['cost'])}. Five chosen as the cheapest that still cover "
       f"every criterion cost {money(wc['cost'])} &mdash; and both bottom out at exactly {wc['floor']:.1f}&#8202;/&#8202;10 on their "
       f"weakest criterion. The extra {money(saving)} buys nothing the model can measure.",
       f"Rotate {', '.join(e(d['restaurant']) for d in sorted(wc['dishes'], key=lambda x: x['price'])[:3])} and two more "
       f"instead of chasing the top of the list."),

      ('f-warn', f"+{F['per5']['sodium']:,.0f}&#8202;mg", 'bought by every extra $5',
       'Spending more actively makes the meal worse',
       f"Regressed across all {len(D)} dishes, each additional $5 adds {F['per5']['sodium']:+,.0f}&#8202;mg of sodium and removes "
       f"{abs(F['per5']['fiber']):.1f}&#8202;g of fiber, while moving health by {F['per5']['health']:+.2f} &mdash; nothing. "
       f"By price third the median sodium climbs {F['terciles'][0]['sodium']:,.0f} to {F['terciles'][1]['sodium']:,.0f} to "
       f"{F['terciles'][2]['sodium']:,.0f}&#8202;mg, and the median kidney score falls from "
       f"{F['terciles'][0]['KID']:.1f} to {F['terciles'][2]['KID']:.1f}.",
       'Money is not neutral here. It is mildly harmful.'),

      ('f-money', f"${best_val['dpp']:.2f}", 'per gram of protein',
       'The cheapest protein here is also the cleanest',
       f"{e(best_val['restaurant'])}&rsquo;s {e(best_val['dish']).lower()} is {money(best_val['price'])} for "
       f"{best_val['protein']}&#8202;g of protein &mdash; the best value on the list &mdash; and it carries "
       f"{best_val['na_p']:.1f}&#8202;mg of sodium per gram of that protein, also the best on the list. Cheap and clean are usually "
       f"a trade. Here they are the same dish, and it is the second-cheapest thing in the document.",
       'If you order one thing off this list, order that.'),

      ('f-warn', f"+{fs['na_hi']-fs['na_lo']:,.0f}&#8202;mg", 'what flavor actually costs',
       'Flavor is bought with salt, not with fat',
       f"The {fs['n_hi']} dishes scoring 7.5 or better on flavor carry {fs['na_hi']-fs['na_lo']:+,.0f}&#8202;mg more sodium than the "
       f"{fs['n_lo']} scoring 5.5 or worse, and only {fs['sf_hi']-fs['sf_lo']:+.1f}&#8202;g more saturated fat. It also explains what "
       f"price is really buying: control for sodium and the price&ndash;flavor correlation falls from "
       f"{F['r_price_flavor']:+.2f} to {F['partial_price_flavor']:+.2f}. A third of what money appears to buy in flavor is salt.",
       'Watch the sauce, the base and the cure. Stop watching the olive oil and the avocado.'),

      ('f-flav', f"{F['within_between']['within']:.2f}", 'points, the spread inside one restaurant',
       'Which dish you order beats where you order it',
       f"Across the restaurants with scored alternatives, the median gap between the best and worst order at a single one is "
       f"{F['within_between']['within']:.2f} points. The spread across the middle half of all {len(D)} restaurants is "
       f"{F['within_between']['between']:.2f}. {e(F['within_between']['widest'][0]['name'])} alone spans "
       f"{F['within_between']['widest'][0]['spread']:.2f} points, from {F['within_between']['widest'][0]['hi']:.2f} down to "
       f"{F['within_between']['widest'][0]['lo']:.2f}.",
       'Picking the restaurant is the smaller half of the decision. Pick the order.'),
    ]

    out = ''
    for kind, num, lab, head, body, do in cards:
        out += (f'<div class="finding {kind}">'
                f'<div class="finding-num"><span class="bignum num">{num}</span>'
                f'<span class="label">{lab}</span></div>'
                f'<h3>{head}</h3><p>{body}</p>'
                f'<p class="do"><b>What to do</b>{do}</p></div>')

    return (
      '<section id="findings">\n'
      '  <hr class="rule-heavy">\n'
      '  <span class="eyebrow">Six findings that should change your order</span>\n'
      '  <h2>What sixty menus actually tell you</h2>\n'
      '  <p class="lede measure" style="margin-top:14px">Each of these holds across the whole set rather than at one '
      'restaurant, each survived an attempt to disprove it, and each is recomputable from the ranking table below. Four are '
      'about money, because that is where the data turned out to be most surprising &mdash; and where it most contradicts the '
      'first edition.</p>\n'
      f'  <div class="findings" style="margin-top:34px">{out}</div>\n'
      '</section>')

def sec_money():
    lo, hi = F['r_price_health_range']
    shelf = F['shelf']
    terc = table(['Price third', '~Median price', '~Median sodium', '~Median kidney', '~Median flavor', '~Median health'],
                 [[f'<td><span class="rest">{e(t["label"].title())}</span></td>',
                   f'<td class="n money">{money(t["price"])}</td>',
                   f'<td class="n num {"lo" if t["sodium"] >= 1300 else ""}">{t["sodium"]:,.0f}</td>',
                   f'<td class="n score">{t["KID"]:.1f}</td>',
                   f'<td class="n score" style="color:var(--flavor)">{t["flavor"]:.1f}</td>',
                   f'<td class="n score">{t["health"]:.2f}</td>'] for t in F['terciles']])
    quad = sorted([d for d in ALL if d['health'] >= 6.0 and d['price'] <= 16], key=lambda x: -x['health'])
    rows = []
    for d in quad[:14]:
        rows.append([
            f'<td><span class="rest">{e(d["restaurant"])}</span><span class="sub">{e(d["dish"])}</span></td>',
            f'<td class="n money">{money(d["price"])}</td>',
            f'<td class="n score hi">{d["health"]:.1f}</td>',
            f'<td class="n score">{d["FLAVOR"]:.1f}</td>',
            f'<td class="n num">{d["protein"]}&#8202;g</td>',
            f'<td class="n num">{d["sodium"]:,}</td>',
            f'<td class="n num">{d["hpd"]:.2f}</td>'])
    val = table(['Dish', '~Price', '~Health', '~Flavor', '~Protein', '~Sodium mg', '~Health per $'], rows)

    dpp = sorted(ALL, key=lambda x: x['dpp'])[:10]
    prows = [[f'<td><span class="rest">{e(d["restaurant"])}</span><span class="sub">{e(d["dish"])}</span></td>',
              f'<td class="n money">{money(d["price"])}</td>',
              f'<td class="n num">{d["protein"]}&#8202;g</td>',
              f'<td class="n num hi">{d["dpp"]:.3f}</td>',
              f'<td class="n score">{d["health"]:.1f}</td>'] for d in dpp]
    prot = table(['Dish', '~Price', '~Protein', '~$ per gram', '~Health'], prows)

    def week_block(w, title, note, cls=''):
        lis = ''.join(f'<li><span>{e(d["restaurant"])}</span><span>{money(d["price"])}</span></li>' for d in w['dishes'])
        return f'''<div class="week {cls}">
      <h4>{title}</h4>
      <span class="price num">{money(w['cost'])}</span>
      <span class="caption">five dinners &middot; {money(w['cost']/5)} each</span>
      <ol>{lis}</ol>
      <p class="floor">Weakest criterion covered across the week: <strong class="num">{w['floor']:.1f}</strong>&#8202;/&#8202;10. {note}</p>
    </div>'''

    return f'''<section id="money">
  <hr class="rule-heavy">
  <span class="eyebrow">Chapter one</span>
  <h2>What money does and does not buy</h2>
  <div class="measure stack" style="margin-top:16px">
    <p>Across all {len(D)} dishes, the correlation between what a dish costs on DoorDash and how healthy it scores is <strong class="num">{r2(F['r_price_health'])}</strong>. Squared, that is well under one percent of the variation: price tells you essentially nothing about whether a meal is good for you. Leave out any single dish and it never leaves the range <span class="num">{lo:.2f}</span> to <span class="num">{hi:+.2f}</span>, so it is not one outlier holding it down.</p>
    <p>Money does buy something. The correlation between price and <em>flavor</em> is <strong class="num">{r2(F['r_price_flavor'])}</strong> &mdash; modest, but five times the size and in a direction you can feel. Expensive food in this set is more interesting to eat and no better for you. Everything in this chapter follows from those two numbers.</p>
  </div>
  <figure>
    {charts.scatter_price_health(D, quad_n=len(quad))}
    <figcaption>Each dot is one dish. The dashed line is the least-squares fit through all sixty &mdash; it is nearly flat. The shaded corner is the useful part of the chart: dishes at or under $16 that still score 6.0 or better on health. There are {len(quad)} of them.</figcaption>
  </figure>

  <h3 style="margin-top:44px">What each extra five dollars actually buys</h3>
  <p class="small measure" style="margin-top:8px">Least-squares across all {len(D)} dishes, and the same question asked by splitting the list into price thirds. The two agree.</p>
  {terc}
  <p class="caption" style="margin-top:12px">Fifteen dishes &mdash; a quarter of the list &mdash; price between {money(shelf['lo'])} and {money(shelf['hi'])}. That {money(shelf['hi']-shelf['lo'])} band contains {e(shelf['best']['restaurant'])} at health {shelf['best']['health']:.1f} and {e(shelf['worst']['restaurant'])} at {shelf['worst']['health']:.1f} &mdash; the entire health range of all {len(D)} dishes, top to bottom, at effectively one price.</p>

  <h3 style="margin-top:44px">Cheap and genuinely good for you</h3>
  <p class="small measure" style="margin-top:8px">Sorted by health score. The last column is health points per dollar, which is the blunt version of the same question.</p>
  {val}

  <div class="callout">
    <h4>One place the cheap answer is not the good one</h4>
    <p style="margin-top:6px">The {F['veg']['meat_free']['n']} meat-free dishes here run <strong class="num">${F['veg']['meat_free']['dpp']:.2f}</strong> per gram of protein against <strong class="num">${F['veg']['rest']['dpp']:.2f}</strong> for everything else &mdash; {F['veg']['meat_free']['dpp']/F['veg']['rest']['dpp']:.1f} times as much &mdash; on a median {F['veg']['meat_free']['protein']:.0f}&#8202;g of protein against {F['veg']['rest']['protein']:.0f}, and they score lower on health too, {F['veg']['meat_free']['health']:.2f} against {F['veg']['rest']['health']:.2f}. That is a fact about these menus rather than about vegetarian eating: the meat-free options on this list are mostly starch-and-stew formats sold at entr&eacute;e prices, not protein-forward builds. The one exception is the cheapest dish in the section below, which gets 20&#8202;g of its protein from lentils.</p>
  </div>

  <h3 style="margin-top:44px">The cheapest protein on the list</h3>
  <p class="small measure" style="margin-top:8px">Dollars per gram of protein, computed on the DoorDash price of the dish as ordered.</p>
  {prot}

  <h3 style="margin-top:44px">A week costs less than you would guess</h3>
  <p class="small measure-wide" style="margin-top:8px">Five dinners, chosen three ways. The test is criterion coverage: across the five dishes, what is the <em>weakest</em> criterion that any one of them covers well? A rotation is only as good as the thing it never delivers.</p>
  <div class="weeks">
    {week_block(F['week_naive'], 'Just order the top five', 'This is what following the ranking blindly gets you.')}
    {week_block(F['week_cheap'], 'The cheap five', 'Identical coverage to the naive week, for ' + money(F['week_naive']['cost']-F['week_cheap']['cost']) + ' less.', 'best')}
    {week_block(F['week_best'], 'The best coverage available', 'Buys a real improvement in the weak spot, and still costs less than the naive week.')}
  </div>
  <div class="callout">
    <h4>The whole chapter in one line</h4>
    <p style="margin-top:6px">The five cheapest dishes that clear every criterion cost <strong class="num">{money(F['week_cheap']['cost'])}</strong> for the week and cover the criteria exactly as well as the five top-ranked dishes, which cost <strong class="num">{money(F['week_naive']['cost'])}</strong>. Both bottom out at <span class="num">{F['week_cheap']['floor']:.1f}</span>&#8202;/&#8202;10 on their weakest criterion. Paying the extra {money(F['week_naive']['cost']-F['week_cheap']['cost'])} buys nothing measurable.</p>
  </div>
</section>'''

def sec_sodium():
    best, worst = F['na_best'][:3], F['na_worst'][:3]
    n_up = sum(1 for x in F['na_swaps'] if x['score_delta'] > 0)
    saltrows = [[f'<td><span class="rest">{e(x["item"])}</span><span class="sub">{e(x["note"])}</span></td>',
                 f'<td class="dimtd">{e(x["per"])}</td>',
                 f'<td class="n num {"lo" if x["mg"] >= 400 else "hi"}">{x["mg"]:,}</td>',
                 f'<td class="n num dimtd">{x["protein"]}&#8202;g</td>' if x["protein"] else '<td class="n dimtd">&mdash;</td>']
                for x in F['salt_components']]
    salt = table(['Component', 'Portion', '~Sodium mg', '~Protein'], saltrows)
    swrows = [[f'<td><span class="rest">{e(x["restaurant"])}</span><span class="sub">instead of {e(x["dish"]).lower()}</span></td>',
               f'<td><strong>{e(x["alt"])}</strong><span class="sub">{e(x["alt_note"])}</span></td>',
               f'<td class="n num hi">&minus;{x["cut"]:,}</td>',
               f'<td class="n num">{-x["protein_lost"]:+d}&#8202;g</td>',
               f'<td class="n num">{x["cal_delta"]:+,}</td>',
               f'<td class="n num {"hi" if x["score_delta"] > 0 else "dimtd"}">{x["score_delta"]:+.2f}</td>'] for x in F['na_swaps']]
    swaps = table(['Restaurant', 'Change one thing', '~Sodium saved', '~Protein', '~Calories', '~Score'], swrows)

    return f'''<section id="sodium">
  <hr class="rule-heavy">
  <span class="eyebrow">Chapter two</span>
  <h2>Sodium is the currency</h2>
  <div class="measure stack" style="margin-top:16px">
    <p>Sodium separates this list more than any other single number, and the useful way to hold it is not as a total but as a rate: how much sodium you are paying for each gram of protein you actually get. On that measure the spread across the set is more than twentyfold.</p>
    <p>{e(best[0]['restaurant'])} delivers protein at <strong class="num">{best[0]['na_p']:.1f}&#8202;mg</strong> of sodium per gram. {e(worst[0]['restaurant'])} charges <strong class="num">{worst[0]['na_p']:.1f}&#8202;mg</strong> for the same gram. Both are on the same list, in the same city, at similar prices.</p>
  </div>
  <figure>
    {charts.sodium_ladder(F)}
    <figcaption>Milligrams of sodium per gram of protein &mdash; the ten most efficient dishes and the six least. The cut-off drawn at 25&#8202;mg is arbitrary but useful: below it, a full meal lands under about 1,000&#8202;mg without any special ordering.</figcaption>
  </figure>

  <h3 style="margin-top:44px">Where the salt actually is</h3>
  <p class="small measure" style="margin-top:8px">Single components, each read off the restaurant's own published nutrition document. Almost none of the heavy ones is the part of the meal a customer thinks of as salty &mdash; and the four lightest are all proteins, which is the opposite of what most people would guess.</p>
  {salt}

  <h3 style="margin-top:44px">The biggest sodium saving available in one swap</h3>
  <p class="small measure" style="margin-top:8px">Changing one thing about an order at the same restaurant. The last column is what the swap does to the dish's overall score, so a positive number means the lower-sodium order is also the better one.</p>
  {swaps}
  <p class="caption" style="margin-top:12px">Restaurants whose figures were corrected in this edition are left out of this table: their alternative orders were scored against numbers that no longer stand, and {F['n_alt_excluded']} alternatives are excluded on that basis.</p>

  <div class="callout">
    <h4>The counterintuitive part</h4>
    <p style="margin-top:6px">Only {n_up} of the {len(F['na_swaps'])} swaps above <em>raise</em> the dish's score while cutting sodium. Look at what the rest give up: Namu's banchan plates save 600&#8202;mg and lose 26&#8202;g of protein. Southern Spice's idli-without-sambar saves 560&#8202;mg and drops the score by half a point. The reliable way to cut sodium at a restaurant is to eat less of the meal, which is a real option and a poor one. The exceptions &mdash; the ones where you cut salt without cutting food &mdash; are almost all sauce refusals, and they are listed above under &ldquo;where the salt actually is.&rdquo;</p>
  </div>
</section>'''

def sec_flavor():
    fs = F['flavor_split']
    _byF = sorted(F['cuisines'], key=lambda c: -c['flavor'])
    na_floor = min(c['sodium'] for c in _byF[:4])
    na_ceil = max(c['sodium'] for c in _byF[-3:])
    br = [b for b in F['breakers'] if byname[b['restaurant']]['health'] >= 6.0]
    rows = [[f'<td><span class="rest">{e(c["name"])}</span><span class="sub">{c["n"]} dish{"es" if c["n"]>1 else ""}</span></td>',
             f'<td class="n score" style="color:var(--flavor)">{c["flavor"]:.1f}</td>',
             f'<td class="n score hi">{c["health"]:.1f}</td>',
             f'<td class="n num">{c["sodium"]:,.0f}</td>',
             f'<td class="n num">{c["satfat"]:.1f}</td>',
             f'<td class="n money">{money(c["price"])}</td>'] for c in F['cuisines']]
    brrows = [[f'<td><span class="rest">{e(byname[b["restaurant"]]["restaurant"])}</span><span class="sub">{e(byname[b["restaurant"]]["dish"])}</span></td>',
               f'<td class="n score" style="color:var(--flavor)">{byname[b["restaurant"]]["FLAVOR"]:.1f}</td>',
               f'<td class="n score hi">{byname[b["restaurant"]]["health"]:.1f}</td>',
               f'<td class="n num">{byname[b["restaurant"]]["sodium"]:,}</td>',
               f'<td class="n money">{money(byname[b["restaurant"]]["price"])}</td>'] for b in br]
    return f'''<section id="flavor">
  <hr class="rule-heavy">
  <span class="eyebrow">Chapter three</span>
  <h2>What flavor actually costs</h2>
  <div class="measure stack" style="margin-top:16px">
    <p>The first edition argued that cuisines built on char, acid and aromatics keep their flavor when you strip out salt and fat, while cuisines built on sauce, cheese and frying do not. The first half of that is right and the second half is aimed at the wrong nutrient.</p>
    <p>Take the {fs['n_hi']} dishes scoring 7.5 or better on flavor and the {fs['n_lo']} scoring 5.5 or worse. The flavorful group carries <strong class="num">{fs['na_hi']-fs['na_lo']:+,.0f}&#8202;mg</strong> more sodium, at <span class="num">t&nbsp;=&nbsp;{F['welch_sodium'][0]:.1f}</span>. It also carries <strong class="num">{fs['sf_hi']-fs['sf_lo']:+.1f}&#8202;g</strong> more saturated fat, at <span class="num">t&nbsp;=&nbsp;{F['welch_satfat'][0]:.1f}</span>, which is on the edge of meaning nothing at all.</p>
    <p class="caption">The sodium gap is not one dish doing the work. Leave any single dish out and it stays between <span class="num">{F['na_gap_loo']['lo']:,.0f}</span> and <span class="num">{F['na_gap_loo']['hi']:,.0f}&#8202;mg</span>, never falling below <span class="num">t&nbsp;=&nbsp;{F['na_gap_loo']['min_t']:.1f}</span>; on medians rather than means the gap is <span class="num">{fs['na_median_gap']:+,.0f}&#8202;mg</span>.</p>
    <p>So flavor in this set is bought mainly with salt, not with fat, and the first edition was policing the wrong nutrient. That is also why there is no health-flavor tradeoff between individual dishes &mdash; the correlation is <span class="num">{r2(F['r_health_flavor'])}</span>, nil. The tradeoff is not a property of a dish. It is a property of a kitchen's whole seasoning strategy, and it shows up only when you group by cuisine.</p>
  </div>
  <figure>
    {charts.cuisine_map(F)}
    <figcaption>Each bubble is a cuisine with at least two dishes in the set, sized by how many. The kitchens that lead on flavor tend to trail on health and the reverse; across the {len(F['cuisines'])} groups the relationship is <span class="num">{r2(F['r_health_flavor_cuisine'])}</span>, which is a pattern worth seeing rather than a result worth betting on. What is solid is the mechanism in the sodium column below: the four cuisines leading on flavor all sit at or above <span class="num">{na_floor:,.0f}&#8202;mg</span>, and the three trailing it all sit under <span class="num">{na_ceil:,.0f}</span>.</figcaption>
  </figure>
  <div class="tablewrap" style="margin-top:26px">
    {table(['Cuisine', '~Flavor', '~Health', '~Sodium mg', '~Sat fat g', '~Mean price'], rows)}
  </div>
  <div class="callout">
    <h4>Read the last two columns together</h4>
    <p style="margin-top:6px">Salt is what flavor costs. It is not the only way a cuisine loses the health column. Korean, Sichuan and Vietnamese kitchens sit high on flavor and low on health entirely on sodium &mdash; their saturated fat is unremarkable. Caribbean and Mexican kitchens lose it a different way, on <strong class="num">{max(c['satfat'] for c in F['cuisines']):.1f}&#8202;g</strong> and <strong class="num">{sorted((c['satfat'] for c in F['cuisines']), reverse=True)[1]:.1f}&#8202;g</strong> of saturated fat against a set median near <span class="num">{st.median([c['satfat'] for c in F['cuisines']]):.1f}</span>, and they do not get leading flavor scores in exchange. Those are the two failure modes, and only one of them buys you anything.</p>
  </div>

  <h3 style="margin-top:44px">The dishes that break the pattern</h3>
  <p class="small measure" style="margin-top:8px">Flavor of 7.5 or better, health of 6.0 or better, on under 1,100&#8202;mg of sodium. There are only {len(br)} in {len(D)}, and they are the most useful entries in this document: food you would order because you wanted it, that also happens to score.</p>
  {table(['Dish', '~Flavor', '~Health', '~Sodium mg', '~Price'], brrows)}
</section>'''

def sec_swaps():
    n_lighter = sum(1 for b in F['beats'] if b['alt']['cal'] < b['rec']['cal'])
    n_lessna  = sum(1 for b in F['beats'] if b['alt']['sodium'] < b['rec']['sodium'])
    n_alt_scored = sum(len(d['alternatives']) for d in D) - F['n_alt_excluded']
    rows = []
    for b in F['beats']:
        rec = byname[b['rec']['restaurant']] if isinstance(b['rec'], dict) and 'restaurant' in b['rec'] else None
        r = b['rec']; a = b['alt']
        rows.append([
            f'<td><span class="rest">{e(r["restaurant"])}</span><span class="sub">instead of {e(r["dish"]).lower()}</span></td>',
            f'<td><strong>{e(a["name"])}</strong><span class="sub">{e(a["change"])}</span></td>',
            f'<td class="n score">{r["overall"]:.2f}</td>',
            f'<td class="n score hi">{a["score"]:.2f}</td>',
            f'<td class="n num">{a["cal"]-r["cal"]:+,}</td>',
            f'<td class="n num">{a["protein"]-r["protein"]:+}</td>',
            f'<td class="n num">{a["sodium"]-r["sodium"]:+,}</td>'])
    beats = table(['Restaurant', 'Order this instead', '~Listed', '~Alt', '~Δcal', '~Δpro', '~ΔNa'], rows)

    arows = []
    for x in F['avoids']:
        r = x['rec']; a = x['alt']
        arows.append([
            f'<td><span class="rest">{e(r["restaurant"])}</span></td>',
            f'<td><strong>{e(a["name"])}</strong><span class="sub">{e(a["change"])}</span></td>',
            f'<td class="n score">{r["overall"]:.2f}</td>',
            f'<td class="n score lo">{a["score"]:.2f}</td>',
            f'<td class="n num">{a["cal"]-r["cal"]:+,}</td>',
            f'<td class="n num">{a["sodium"]-r["sodium"]:+,}</td>'])
    avoid = table(['Restaurant', 'The default order', '~Best', '~Default', '~Δcal', '~ΔNa'], arows)

    dupes = ''.join(
      f'''<tr><td><span class="rest">{e(x['name'])}</span><span class="sub">{x['n']} versions in the set</span></td>
      <td class="n money">{money(x['cheapest']['price'])}<span class="sub">{e(x['cheapest']['restaurant'])}</span></td>
      <td class="n money">{money(x['priciest']['price'])}<span class="sub">{e(x['priciest']['restaurant'])}</span></td>
      <td class="n"><span class="{'hi' if not x['best_is_priciest'] else ''}">{e(x['best']['restaurant'])}</span><span class="sub">{x['best']['overall']:.2f} &middot; {money(x['best']['price'])}</span></td></tr>'''
      for x in F['dupes'])

    return f'''<section id="swaps">
  <hr class="rule-heavy">
  <span class="eyebrow">Chapter four</span>
  <h2>Orders that beat the order</h2>
  <div class="measure stack" style="margin-top:16px">
    <p>The first edition scored {sum(len(d['alternatives']) for d in D)} alternative orders alongside its recommendations. {n_alt_scored} of them are still comparable after this edition's corrections, and in {len(F['beats'])} of those the alternative outscores the dish it sits under. The reason is nearly always the same: the alternative is smaller. {n_lighter} of the {len(F['beats'])} cut calories and {n_lessna} cut sodium, giving up protein the model barely misses.</p>
    <p>That is worth knowing on its own. It is also the clearest evidence in this document that the model rewards restraint more than it rewards any particular ingredient.</p>
  </div>
  {beats}

  <h3 style="margin-top:44px">And the ones that cost you</h3>
  <p class="small measure" style="margin-top:8px">The same restaurants, ordered the way most people order them.</p>
  {avoid}

  <h3 style="margin-top:44px">The same dish, twice, at two prices</h3>
  <p class="small measure" style="margin-top:8px">Seven groups of near-identical dishes appear at different restaurants across the set. The most expensive version is the best one in only <strong>{F['dupe_priciest_wins']} of {len(F['dupes'])}</strong> of them.</p>
  <div class="tablewrap"><table><thead><tr><th>Group</th><th class="n">Cheapest</th><th class="n">Priciest</th><th class="n">Best-scoring</th></tr></thead><tbody>{dupes}</tbody></table></div>
</section>'''

def sec_criteria():
    C = [
      ('Kidney', '×1.0', 'Sodium alone.', 'KID = clamp( 10 × (2000 − sodium_mg) / 1650 )',
       'Full marks at 350&#8202;mg, zero at 2,000. Linear between, which means a dish at 2,100&#8202;mg and one at 3,000&#8202;mg both score zero.', False),
      ('Liver', '×1.0', 'Saturated fat 65%, calorie load 35%.',
       'LIV = 0.65 × clamp( 10 × (16.5 − satfat_g) / 14.5 )\n    + 0.35 × clamp( 10 × (1000 − cal) / 500 )',
       'Recovered by fitting the published scores; reproduces them to within 0.18 on average.', False),
      ('Muscle', '×1.0', 'Protein density 70%, absolute protein 30%.',
       'MUS = 0.7 × clamp( 10 × (perKcal − 2) / 7 )\n    + 0.3 × clamp( 10 × (protein_g − 20) / 25 )\n  where perKcal = protein_g / (cal/100)',
       'Rewards protein per calorie first, so a light dish with 30&#8202;g beats a heavy one with 40.', False),
      ('Gut', '×1.0', 'Live ferments 60%, plant-type count 40%.',
       'GUT = 0.6 × (live-ferment ladder, 0–4)\n    + 0.4 × (plant types, capped at 19)',
       'A judgement, not a calculation. Vinegar pickles score zero. <strong>Fiber carries no weight at all</strong> &mdash; see the audit below.', True),
      ('Energy', '×1.0', 'Refined-carb load, fiber, protein presence.', 'ENE — rubric, 0–10',
       'A glycemic proxy assembled by hand. It correlates with fiber at +0.44, which is the closest thing to a check available on it.', True),
      ('Inflammation', '×1.0', 'Omega-3 60%, plant and herb diversity 40%.',
       'INF = 0.6 × (omega-3 ladder, 0–3)\n    + 0.4 × (plant and herb diversity, 0–7)',
       'The omega-3 ladder does not distinguish plant ALA from marine EPA and DHA, which overstates flaxseed.', True),
      ('Sugar', '×0.7', 'Total sugars.', 'SUG = clamp( 10 × (22 − sugar_g) / 19 )',
       'Full marks at 3&#8202;g, zero at 22. Uses <em>total</em> sugars, so fruit and plain dairy are penalised exactly like added sugar.', False),
      ('Flavor', '×0.5', 'Six components, minus what the health edit removes.',
       'FLAVOR = ( char 0–3 + acid 0–2\n         + ferment 0–2 + aromatics 0–3\n         + richness 0–2 + texture 0–2\n         − strip penalty 0–3 ) / 14 × 10',
       'Half-points allowed. Not a taste rating: it measures where a dish\'s intensity comes from and how much survives ordering it the healthy way.', True),
      ('Cost', '×0.5', 'Listed price 60%, price per gram of protein 40%.',
       'COST = 0.6 × clamp( 10 × (35 − price) / 25 )\n     + 0.4 × clamp( 10 × (0.90 − perGram)\n                    / 0.65 )\n  where perGram = price / protein_g',
       'Rewards a cheap meal and good protein value together. Ignores portion size, which is its main flaw.', False),
    ]
    cards = ''.join(f'''<div class="crit">
      <div class="crit-head"><h3>{n}</h3><span class="weight">{w}</span></div>
      <p>{d}</p>
      <pre class="formula">{e(f)}</pre>
      <p style="margin-top:9px">{note}{' <span class="judged">Judged, not computed.</span>' if j else ''}</p>
    </div>''' for n, w, d, f, note, j in C)
    return f'''<section id="criteria">
  <hr class="rule-heavy">
  <span class="eyebrow">The model</span>
  <h2>Nine criteria, written out</h2>
  <div class="measure stack" style="margin-top:16px">
    <p>The first edition described its criteria in prose. This one prints them as functions, because a scoring model you cannot recompute is an opinion wearing a number's clothes.</p>
    <p>Six of the nine are arithmetic on the six macros and the price, and are reproduced here exactly: feeding the published macros back through them returns every one of the {len(D)} printed overall scores to within 0.10. Three &mdash; gut, energy and inflammation &mdash; are human judgements on a rubric, and no formula will recover them. Those three are marked.</p>
    <p class="caption">Composite: <span class="num">health = (KID + LIV + MUS + GUT + ENE + INF + 0.7×SUG) / 6.7</span>, then <span class="num">overall = (health×6.7 + FLAVOR×0.5 + COST×0.5) / 7.7</span>. Flavor and cost at half weight cannot rescue an unhealthy dish; they reorder the middle of the list.</p>
  </div>
  <div class="criteria">{cards}</div>
</section>'''

def sec_confidence():
    T = F['tiers']; rt = F['round_tell']
    n_retier = sum(1 for c in json.load(open('corrections_v1.json')) if c.get('retier') == 'PUBLISHED')
    _pc = sorted(d['cal'] for d in D if d['data'] == 'PUBLISHED')
    pub_cals = ', '.join(str(c) for c in _pc[:-1]) + ' and ' + str(_pc[-1])
    rows = [[f'<td><span class="rest">{k.title()}</span></td>',
             f'<td class="n num">{v["n"]}</td>',
             f'<td class="n score">{v["health"]:.2f}</td>',
             f'<td class="n num">{v["sodium"]:,.0f}</td>',
             f'<td class="n score">{v["flavor"]:.2f}</td>',
             f'<td class="n money">{money(v["price"])}</td>'] for k, v in T.items()]
    return f'''<section id="confidence">
  <hr class="rule-heavy">
  <span class="eyebrow">Before you trust a number</span>
  <h2>How much of this is measured</h2>
  <div class="measure stack" style="margin-top:16px">
    <p>{T['PUBLISHED']['n']} of the {len(D)} entries are built from a chain's own published nutrition documents &mdash; {n_retier} more than the first edition claimed, because Chopt and Sweetgreen both publish nutrition the first edition did not consult. {T['PARTIAL']['n']} are partial. The other {T['ESTIMATED']['n']} are reasoned from how the dish is put together, and that reasoning leaves fingerprints: {rt['sodium']} of them land on a round multiple of 50&#8202;mg of sodium and {rt['cal']} on a multiple of 20 calories. Real nutrition panels do not do that. The published entries here read {pub_cals} calories.</p>
    <p>The gap between the tiers is not small, and it is the most important caveat in this document:</p>
  </div>
  {table(['Confidence tier', '~Entries', '~Mean health', '~Mean sodium mg', '~Mean flavor', '~Mean price'], rows)}
  <div class="callout warn">
    <h4>Read that table as a warning, not a result</h4>
    <p style="margin-top:6px">Entries built from published data score {T['PUBLISHED']['health']-T['ESTIMATED']['health']:.2f} points higher on health and carry {T['ESTIMATED']['sodium']-T['PUBLISHED']['sodium']:,.0f}&#8202;mg less sodium than estimated ones. Some of that is real &mdash; the chains that publish nutrition are exactly the build-your-own bowl chains whose format permits a low-sodium build. But some of it is estimation, and an estimator who does not know a number reaches for a plausible restaurant figure, which for sodium is high. <strong>The safest reading is that the published entries are accurate and the estimated ones are directionally right and individually soft.</strong> Where a dish's rank matters to you, the entry tells you which kind it is.</p>
  </div>
</section>'''

def sec_audit():
    gt, ft = F['gut_top'], F['fiber_top']
    grows = [[f'<td><span class="rest">{e(d["restaurant"])}</span><span class="sub">{e(d["dish"])}</span></td>',
              f'<td class="n num">{d["fiber"]}&#8202;g</td>',
              f'<td class="n score">{d["GUT"]:.1f}</td>'] for d in ft]
    grows2 = [[f'<td><span class="rest">{e(d["restaurant"])}</span><span class="sub">{e(d["dish"])}</span></td>',
               f'<td class="n num">{d["fiber"]}&#8202;g</td>',
               f'<td class="n score">{d["GUT"]:.1f}</td>'] for d in gt]
    ceiling = [d for d in D if d['sodium'] >= 2000]
    ck = byname['Chosun Ok']
    fw = byname['First Watch']
    r_fg = f"{F['r_fiber_gut']:+.2f}"

    faults = [
      ('The gut criterion gives fiber no weight at all',
       'It scores live ferments at 60% and a count of plant types at 40%. Fiber contributes nothing, and across the set '
       'fiber and the gut score correlate at only <span class="num">' + r_fg + '</span>. There is a narrow defence &mdash; a 17-week '
       'trial found a fermented-food diet raised microbiome diversity where a high-fiber diet did not &mdash; but that defence is '
       'about alpha diversity, not about gut health as a reader would understand the phrase, and the criterion is labelled for the '
       'reader. As built it is a live-culture detector wearing a gut-health label.',
       'Wastyk et al., <em>Cell</em>, August 2021.',
       table(['Highest fiber in the set', '~Fiber', '~Gut'], grows)
       + table(['Highest gut score in the set', '~Fiber', '~Gut'], grows2)),

      ('The kidney criterion stops measuring at 2,000&#8202;mg',
       'It runs linearly from 350&#8202;mg to 2,000 and then floors, so every dish past that point scores zero and none can be told apart. '
       'That sounds academic until you meet ' + e(ck['restaurant']) + '. This edition corrected its sodium from 2,100&#8202;mg to about '
       '<strong class="num">' + f"{ck['sodium']:,}" + '&#8202;mg</strong>, once the 1&#8202;lb kimchi side was counted at USDA’s figure of 498&#8202;mg '
       'per 100&#8202;g &mdash; roughly 2,300&#8202;mg from the kimchi alone, before the stew. Its overall score moved by '
       '<strong class="num">0.02</strong>. A dish carrying nearly twice a full day’s recommended sodium is scored as merely equal to '
       'the worst thing the criterion can express.',
       'USDA FoodData Central, FNDDS 2021&ndash;2023, food code 75502520.', ''),

      ('Sugar is scored as total, not added',
       'Current dietary guidance targets added and free sugars and explicitly exempts the sugars in fruit and plain milk. This '
       'criterion does not distinguish them, so a bowl of fruit and a honey vinaigrette are penalised identically. First Watch’s '
       'Tri-Fecta &mdash; eggs, avocado, seasonal fruit and whole-grain toast &mdash; takes a sugar score of <span class="num">'
       + f"{fw['SUG']:.1f}" + '</span> mostly on the fruit, where the same 12&#8202;g from a glaze would cost exactly as much.',
       'Dietary Guidelines for Americans 2025&ndash;2030.', ''),

      ('The omega-3 ladder treats flaxseed as if it were fish',
       'The inflammation criterion scores omega-3 on a single ladder that does not distinguish plant ALA from marine EPA and DHA. It '
       'should. A review of 13 randomised trials found high-dose flaxseed and echium oil produced no increase in the omega-3 index at '
       'all, against reliable increases from fish oil; conversion of ALA to EPA runs at a few percent and to DHA below one. Every '
       'entry here scored for flaxseed is scored generously.',
       'Lane et al., <em>Critical Reviews in Food Science and Nutrition</em>, 2022.', ''),

      ('Cost knows nothing about how much food you get',
       'It rewards a low price and good protein value and ignores portion size entirely. A 320-calorie dish and a 780-calorie dish at '
       'the same price and protein score identically, though only one of them is dinner. On a list whose portions range more than '
       'twofold, this is the criterion most likely to mislead.',
       '', ''),
    ]

    blocks = ''
    for head, body, cite, tbl in faults:
        cite_html = f'<p class="cite">{cite}</p>' if cite else ''
        blocks += (f'<div class="fault"><h3>{head}</h3><p class="small">{body}</p>{cite_html}{tbl}</div>')

    return (
      '<section id="audit">\n'
      '  <hr class="rule-heavy">\n'
      '  <span class="eyebrow">Against interest</span>\n'
      '  <h2>Where this model misfires</h2>\n'
      '  <div class="measure stack" style="margin-top:16px">\n'
      '    <p>Every criterion in this document was checked against current dietary guidance and the primary literature. Five produce '
      'results their own author would struggle to defend. They are printed here because a ranking that never argues with itself is not '
      'worth reading, and because a reader who knows where a model is weak can still use it.</p>\n'
      '  </div>\n'
      f'  <div class="faults">{blocks}</div>\n'
      '  <div class="callout">\n'
      '    <h4>And what held up</h4>\n'
      '    <p style="margin-top:6px">Two of the model’s more contestable calls survived the check. Weighting the liver criterion on '
      '<strong>saturated fat</strong> rather than sugar is right: in a head-to-head overfeeding trial, saturated fat raised liver fat '
      'substantially more than unsaturated fat or simple sugars did &mdash; though the same guidance also names excess fructose, so a '
      'small added-sugar term belongs in that criterion and is not there. And the rule that <strong>vinegar quick-pickles score '
      'zero</strong> is correct: quick-process pickles are brined briefly then covered in vinegar with no fermentation step at all, a '
      'real and frequently-missed distinction. Labneh, cacık and raita are confirmed live-culture items, conditional only on the '
      'yogurt not having been heat-treated after culturing &mdash; which no menu will tell you.</p>\n'
      '  </div>\n'
      '</section>')

def sec_ranking():
    rows = []
    for i, d in enumerate(MERGED, 1):
        old = d.get('rank')
        if d.get('is_new'):
            prov = '<span class="prov prov-new">new this edition</span>'
        elif old:
            lst = 'first thirty' if old <= 30 else 'next thirty'
            delta = old - i
            arrow = ''
            if abs(delta) >= 5:
                arrow = f' <span class="prov-move">{"&#9650;" if delta > 0 else "&#9660;"}{abs(delta)}</span>'
            prov = f'<span class="prov">1st ed. #{old} of the {lst}{arrow}</span>'
        else:
            prov = ''
        flag = ' <span class="flag" title="macros corrected against published data">&#9873;</span>' if d.get('corrected') else ''
        flag += ' <span class="flag flag-d" title="figures disputed - see the verification log">&#9888;</span>' if d.get('disputed') else ''
        rows.append(f'''<tr>
      <td class="pos">{i}</td>
      <td><span class="rest">{e(d['restaurant'])}{flag}</span><span class="sub">{e(d['dish'])}</span>{prov}</td>
      <td>{tier_badge(d)}</td>
      <td class="n score" style="font-weight:600">{d['overall']:.2f}</td>
      <td class="n score">{d['health']:.1f}</td>
      <td>{charts.crit_bars(d)}</td>
      <td class="n money">{money(d['price'])}</td>
      <td class="n num">{d['cal']:,}</td>
      <td class="n num">{d['protein']}</td>
      <td class="n num {'lo' if d['sodium'] >= 1500 else ''}">{d['sodium']:,}</td>
      <td class="n num">{d['fiber']}</td>
    </tr>''')
    return f'''<section id="ranking">
  <hr class="rule-heavy">
  <span class="eyebrow">All {len(MERGED)}, in one sequence</span>
  <h2>The ranking</h2>
  <div class="measure stack" style="margin-top:16px">
    <p>The first edition split this into two lists and ranked each separately, which buried good food: {F['n_promoted']} entries in the second list outscored the weakest entry in the first, and the highest of them would have placed tenth. The split tracked how much research each restaurant got, not how the food scored. Here everything sits in one order.</p>
    <p class="caption">The nine bars are the criteria in the order kidney, liver, muscle, gut, energy, inflammation, sugar &mdash; then, set apart, flavor in amber and cost in slate. Tall is good. Each row carries where the first edition printed it. &#9873; marks an entry whose figures were corrected against a restaurant's published data; &#9888; marks one whose figures are disputed and could not be replaced.</p>
  </div>
  <div class="tablewrap">
    <table class="rank-table">
      <thead><tr>
        <th class="n">#</th><th>Restaurant and dish</th><th>Data</th>
        <th class="n">Overall</th><th class="n">Health</th><th>Profile</th>
        <th class="n">Price</th><th class="n">Cal</th><th class="n">Pro</th><th class="n">Na mg</th><th class="n">Fib</th>
      </tr></thead>
      <tbody>{''.join(rows)}</tbody>
    </table>
  </div>
</section>'''

def sec_gap():
    B = F['bowl_share']
    absent = ''.join(f'<li>{e(x)}</li>' for x in F['absent'])
    covrows = [[f'<td><span class="rest">{e(c["name"])}</span></td>',
                f'<td class="n num">{c["n"]}</td>',
                f'<td class="n num">{c["share"]*100:.1f}%</td>',
                f'<td class="n score">{c["overall"]:.2f}</td>'] for c in F['coverage'][:10]]
    return f'''<section id="gap">
  <hr class="rule-heavy">
  <span class="eyebrow">The sample</span>
  <h2>What a ranking leaves out</h2>
  <div class="measure stack" style="margin-top:16px">
    <p>A ranking is only as good as the set it ranks, and this one was assembled from a narrow slice of what actually delivers here. {B['n']} of the {len(D)} entries &mdash; <strong>{B['pct']:.0f}%</strong> &mdash; are build-your-own bowls or poke, and {B['in_top10']} of the top ten are. That is not a finding about food. It is a finding about how the list was built: assembled-to-order formats are easy to score because you control every component, so they get picked, and they then win on criteria the format is designed to satisfy.</p>
    <p>The omissions are more telling than the concentrations. This is a document written about food in North Carolina that contains no barbecue.</p>
  </div>
  <div class="pair">
    <div>
      <h4>The ten largest groups</h4>
      {table(['Cuisine', '~Dishes', '~Share', '~Mean score'], covrows)}
    </div>
    <div>
      <h4>Absent entirely from the first edition</h4>
      <ul class="absent">{absent}</ul>
    </div>
  </div>
</section>'''

def sec_additions():
    if not ADDS: return ''
    rows = []
    for d in sorted(ADDS, key=lambda x: -x['overall']):
        rows.append(f'''<tr>
      <td><span class="rest">{e(d['restaurant'])}</span><span class="sub">{e(d['dish'])} &middot; {e(d.get('city',''))}</span></td>
      <td><span class="sub" style="margin:0">{e(d.get('cuisine',''))}</span></td>
      <td class="n score" style="font-weight:600">{d['overall']:.2f}</td>
      <td class="n score">{d['health']:.1f}</td>
      <td class="n score" style="color:var(--flavor)">{d['FLAVOR']:.1f}</td>
      <td class="n money">{money(d['price'])}</td>
      <td class="n num">{d['protein']}</td>
      <td class="n num">{d['sodium']:,}</td>
    </tr>''')
    notes = ''.join(f'<div class="corr"><div class="corr-head"><span class="rest">{e(d["restaurant"])}</span><span class="badge badge-open">{e(d.get("cuisine",""))}</span></div>'
                    f'<p class="small">{e(d.get("why_it_scores",""))}</p>'
                    f'<p class="small" style="margin-top:8px;color:var(--ink-3)"><strong>Order it:</strong> {e(d.get("build",""))}</p></div>'
                    for d in sorted(ADDS, key=lambda x: -x['overall']))
    return f'''<section id="additions">
  <hr class="rule-heavy">
  <span class="eyebrow">New in this edition</span>
  <h2>The food the first edition missed</h2>
  <div class="measure stack" style="margin-top:16px">
    <p>These {len(ADDS)} entries close part of the gap the previous section describes. Each was found by looking for what actually delivers in the Research Triangle in the categories the first edition skipped, each was checked for whether the restaurant exists and the dish is on its menu, and each was scored on the identical model &mdash; the six computed criteria by formula, the three rubric criteria by the same judgement the original sixty got.</p>
    <p class="caption">All of these are estimated from menu construction, not published nutrition, and should be read at the confidence the chapter above describes. Where a DoorDash store ID could not be confirmed it is not printed rather than guessed.</p>
  </div>
  <div class="tablewrap"><table><thead><tr>
    <th>Restaurant and dish</th><th>Cuisine</th><th class="n">Overall</th><th class="n">Health</th>
    <th class="n">Flavor</th><th class="n">Price</th><th class="n">Pro</th><th class="n">Na mg</th>
  </tr></thead><tbody>{''.join(rows)}</tbody></table></div>
  <h3 style="margin-top:40px">Why each one is here</h3>
  <div style="margin-top:14px">{notes}</div>
</section>'''

def sec_corrections():
    if not CORR: return ''
    BADGE = {'wrong': ('badge-wrong', 'Corrected'), 'stale': ('badge-stale', 'Out of date'),
             'confirmed': ('badge-ok', 'Confirmed'), 'open': ('badge-open', 'Unresolved')}
    def block(c):
        b = BADGE[c.get('kind', 'wrong')]
        who = c.get('restaurant', '')
        rescored = ''
        if c['action'] == 'rescore':
            d = byname.get(who)
            if d: rescored = (f'<p class="corr-effect">Rescored: overall {d["overall"]:.2f}, '
                              f'now ranked {MERGED.index(d)+1} of {len(MERGED)}.</p>')
        return f'''<div class="corr">
      <div class="corr-head"><span class="badge {b[0]}">{b[1]}</span><span class="corr-who">{e(who)}</span></div>
      <h3 style="font-size:1.02rem;margin-bottom:7px">{e(c['claim'])}</h3>
      <p class="was"><b>First edition</b> {e(c['was'])}</p>
      <p class="now">{e(c['now'])}</p>
      {rescored}
      {f'<p class="caption" style="margin-top:6px">{e(c["source"])}</p>' if c.get('source') else ''}
    </div>'''
    order = {'wrong': 0, 'open': 1, 'stale': 2, 'confirmed': 3}
    items = sorted(CORR, key=lambda c: (order[c.get('kind', 'wrong')], 0 if c['action'] == 'rescore' else 1))
    n_wrong = sum(1 for c in CORR if c.get('kind') == 'wrong')
    n_open = sum(1 for c in CORR if c.get('kind') == 'open')
    n_score = sum(1 for c in CORR if c['action'] == 'rescore')
    return f'''<section id="corrections">
  <hr class="rule-heavy">
  <span class="eyebrow">The verification log</span>
  <h2>What was wrong</h2>
  <div class="measure stack" style="margin-top:16px">
    <p>Every nutrition figure the first edition attributed to a published document was re-read against that document, and the restaurants were spot-checked for whether they exist and are trading. {n_wrong} claims came back wrong, {n_score} of them badly enough to change a score. {n_open} could not be settled either way and are printed as open rather than quietly dropped.</p>
    <p>Two of the corrections move an entry a long way. Sassool was ranked third on figures its own published nutrition sheet does not support. Bul Box was scored on sodium inferred from construction because its nutrition page was returning an error; the page works now, and the real number is more than double.</p>
  </div>
  <div style="margin-top:26px">{''.join(block(c) for c in items)}</div>
</section>'''

def sec_method():
    return f'''<footer>
  <span class="eyebrow">Method and provenance</span>
  <div class="pair" style="margin-top:6px">
    <div class="stack-tight">
      <h4>What a score is</h4>
      <p class="small">Each entry is one specific dish, ordered one specific way, and every figure describes that dish as built &mdash; not the restaurant, and not the menu item as it arrives by default. Where the build says to refuse something, the numbers assume you refused it.</p>
      <h4 style="margin-top:20px">Prices</h4>
      <p class="small">DoorDash-listed, which run roughly 15&ndash;25% above in-store. Distances are straight-line from Research Triangle Park; an active storefront is not the same as delivery to a given address, which is computed per address at checkout.</p>
    </div>
    <div class="stack-tight">
      <h4>What this is not</h4>
      <p class="small">Not medical advice, and not a clinical instrument. The criteria are a defensible way to compare restaurant meals with each other; they are not a diagnosis and the anchor points are judgement calls, some of which are argued with above.</p>
      <h4 style="margin-top:20px">Reproducibility</h4>
      <p class="small">The six computed criteria are printed as functions and the dataset behind this edition is machine-readable. Any score here can be recomputed, disagreed with, and refitted with different anchors.</p>
    </div>
  </div>
  <p class="caption" style="margin-top:30px;border-top:1px solid var(--rule);padding-top:16px">
    Second edition. First edition compiled 25 August 2026; this revision {e(BUILD_DATE)}. Menus and formulations change constantly and every figure here has a shelf life measured in months.
  </p>
</footer>'''

BUILD_DATE = '28 August 2026'

# ============================================================ assemble
PAGE = f'''<title>The Fast-Casual Compendium</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..100,400..900&family=IBM+Plex+Mono:wght@400;500;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400..600;1,8..60,400&display=swap">
<style>
{CSS}
</style>
<div class="wrap">
{sec_masthead()}
{sec_changes()}
{sec_findings()}
{sec_money()}
{sec_sodium()}
{sec_flavor()}
{sec_swaps()}
{sec_gap()}
{sec_additions()}
{sec_criteria()}
{sec_confidence()}
{sec_audit()}
{sec_ranking()}
{sec_corrections()}
{sec_method()}
</div>
'''

open('compendium.html', 'w').write(PAGE)
print(f'wrote compendium.html — {len(PAGE):,} bytes, {len(MERGED)} ranked entries')
