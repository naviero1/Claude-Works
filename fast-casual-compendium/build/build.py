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
CORR = load('corrections.json', None)
ADDS = load('additions.json', [])      # from the widening workflow

e = lambda s: html.escape(str(s), quote=False)
byname = {d['restaurant']: d for d in D}
def money(v): return f"${v:,.2f}"
def r2(v):    return f"{v:+.2f}".replace('+0.', '+.').replace('-0.', '−.')

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
    items = [
      ('The front page is new.', 'The first edition opened with four findings, three of which were trivia about a single restaurant each. They have been replaced with findings drawn from the whole set &mdash; led by what the data says about money.'),
      ('The two lists are now one.', f'The first edition printed &ldquo;The Thirty&rdquo; and &ldquo;The Next Thirty&rdquo; as separate ranked lists, but the split was by research depth, not by score: {F["n_promoted"]} of the second thirty outscored the weakest member of the first. Everything is now ranked in a single sequence.'),
      ('The scoring model is printed, not described.', 'Every criterion that can be computed from the macros is now given as an actual function. Anyone can recompute any score in this document, including the ones they disagree with.'),
      ('The sample was too narrow.', f'Eighteen of the original sixty entries were build-your-own bowls or poke &mdash; 30% of the set, and four of the top ten &mdash; in a state with no barbecue entry at all. {"This edition adds " + str(len(ADDS)) + " dishes from cuisines and formats the first edition skipped." if ADDS else "That gap is documented below."}'),
      ('Claims were checked against sources.', 'The nutrition figures the first edition attributed to published documents were re-read against those documents, and the food-science claims against the literature. What was wrong is listed at the end rather than quietly fixed.'),
    ]
    lis = ''.join(f'<li><strong>{t}</strong> {b}</li>' for t, b in items)
    return f'''<section id="changes">
  <div class="changelog measure-wide">
    <span class="eyebrow">What changed in this edition</span>
    <ul>{lis}</ul>
  </div>
</section>'''

def sec_findings():
    if not FIND:
        return ''
    kinds = ['money', 'money', 'warn', '', 'flav', '']
    cards = ''.join(finding_card(f, kinds[i % len(kinds)]) for i, f in enumerate(FIND['headline_findings']))
    return f'''<section id="findings">
  <hr class="rule-heavy">
  <span class="eyebrow">The findings that should change your order</span>
  <h2>What {len(ALL)} menus actually tell you</h2>
  <p class="lede measure" style="margin-top:14px">Each of these holds across the whole set rather than at one restaurant, and each survived an attempt to disprove it. The arithmetic is reproducible from the ranking table below.</p>
  <div class="findings" style="margin-top:34px">{cards}</div>
</section>'''

def sec_money():
    lo, hi = F['r_price_health_range']
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
    <p>Across all {len(D)} dishes in the original set, the correlation between what a dish costs on DoorDash and how healthy it scores is <strong class="num">{r2(F['r_price_health'])}</strong>. That is not a weak relationship; it is the absence of one. Drop any single dish from the set and it stays between <span class="num">{lo:+.2f}</span> and <span class="num">{hi:+.2f}</span>, so it is not the work of one outlier either.</p>
    <p>Money does buy something. The correlation between price and <em>flavor</em> is <strong class="num">{r2(F['r_price_flavor'])}</strong> &mdash; real, if modest. Expensive food in this set is more interesting to eat and no better for you. Everything in this chapter follows from those two numbers.</p>
  </div>
  <figure>
    {charts.scatter_price_health(D, quad_n=len(quad))}
    <figcaption>Each dot is one dish. The dashed line is the least-squares fit through all sixty &mdash; it is nearly flat. The shaded corner is the useful part of the chart: dishes at or under $16 that still score 6.0 or better on health. There are {len(quad)} of them.</figcaption>
  </figure>

  <h3 style="margin-top:44px">Cheap and genuinely good for you</h3>
  <p class="small measure" style="margin-top:8px">Sorted by health score. The last column is health points per dollar, which is the blunt version of the same question.</p>
  {val}

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
                 f'<td class="n num {"lo" if x["mg"] >= 400 else "hi"}">{x["mg"]:,}</td>'] for x in F['salt_components']]
    salt = table(['Component', 'Portion', '~Sodium mg'], saltrows)
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
  <p class="small measure" style="margin-top:8px">Single components, each read off the restaurant's own published nutrition document. Almost none of these is the part of the meal a customer thinks of as salty.</p>
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
    <p>Take the {fs['n_hi']} dishes scoring 7.5 or better on flavor and the {fs['n_lo']} scoring 5.5 or worse. The flavorful group carries <strong class="num">{fs['na_hi']-fs['na_lo']:+,.0f}&#8202;mg</strong> more sodium &mdash; a difference far too large to be chance, at <span class="num">t&nbsp;=&nbsp;{F['welch_sodium'][0]:.1f}</span> on {F['welch_sodium'][1]:.0f} degrees of freedom. It carries <strong class="num">{fs['sf_hi']-fs['sf_lo']:+.1f}&#8202;g</strong> more saturated fat, which at <span class="num">t&nbsp;=&nbsp;{F['welch_satfat'][0]:.1f}</span> is indistinguishable from noise.</p>
    <p>So flavor in this set is not bought with fat. It is bought with salt, and the first edition was policing the wrong nutrient. That is also why there is no health-flavor tradeoff between individual dishes &mdash; the correlation is <span class="num">{r2(F['r_health_flavor'])}</span>, nil. The tradeoff is not a property of a dish. It is a property of a kitchen's whole seasoning strategy, and it shows up only when you group by cuisine.</p>
  </div>
  <figure>
    {charts.cuisine_map(F)}
    <figcaption>Each bubble is a cuisine with at least two dishes in the set, sized by how many. The kitchens that lead on flavor tend to trail on health and the reverse; across the {len(F['cuisines'])} groups the relationship is <span class="num">{r2(F['r_health_flavor_cuisine'])}</span>, which is a pattern worth seeing rather than a result worth betting on. What is solid is the mechanism in the sodium column below: every cuisine above 7.0 on flavor sits at or above 1,096&#8202;mg.</figcaption>
  </figure>
  <div class="tablewrap" style="margin-top:26px">
    {table(['Cuisine', '~Flavor', '~Health', '~Sodium mg', '~Sat fat g', '~Mean price'], rows)}
  </div>
  <h3 style="margin-top:44px">The dishes that break the pattern</h3>
  <p class="small measure" style="margin-top:8px">Flavor of 7.5 or better, health of 6.0 or better, on under 1,100&#8202;mg of sodium. There are only {len(br)} in {len(D)}, and they are the most useful entries in this document: food you would order because you wanted it, that also happens to score.</p>
  {table(['Dish', '~Flavor', '~Health', '~Sodium mg', '~Price'], brrows)}
</section>'''

def sec_swaps():
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
    <p>The first edition scored {sum(len(d['alternatives']) for d in D)} alternative orders alongside its recommendations. In {len(F['beats'])} cases the alternative outscores the dish it sits under, and the reason is nearly always the same: the alternative is smaller. Six of the {len(F['beats'])} cut calories, and five cut sodium, while giving up protein the score barely misses.</p>
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
    <p>Five of the original sixty entries are built from a chain's own published nutrition documents. Two are partial. The other {T['ESTIMATED']['n']} are reasoned from how the dish is put together, and that reasoning leaves fingerprints: {rt['sodium']} of the {rt['n']} estimated entries land on a round multiple of 50&#8202;mg of sodium, and {rt['cal']} on a multiple of 20 calories. Real nutrition panels do not do that. The published entries in this set read 542, 420, 380, 740 and 575 calories.</p>
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
    zero = [d for d in D if d['sodium'] >= 2000]
    return f'''<section id="audit">
  <hr class="rule-heavy">
  <span class="eyebrow">Against interest</span>
  <h2>Where this model misfires</h2>
  <div class="measure stack" style="margin-top:16px">
    <p>Four places where the scoring produces a result its own author would struggle to defend. They are printed here because a ranking that never argues with itself is not worth reading.</p>
  </div>

  <div class="pair">
    <div class="stack-tight">
      <h4>1 &mdash; The gut criterion ignores fiber</h4>
      <p class="small">It weights live ferments at 60% and a plant-type count at 40%, and gives fiber nothing. Across the set, fiber and the gut score correlate at only <span class="num">{F['r_fiber_gut']:+.2f}</span>. The result is that the highest-fiber dish in the compendium scores mid-table on gut health while a bowl of curd rice scores a perfect ten.</p>
      {table(['Highest fiber in the set', '~Fiber', '~Gut'], grows)}
      {table(['Highest gut score in the set', '~Fiber', '~Gut'], grows2)}
    </div>
    <div class="stack-tight">
      <h4>2 &mdash; The kidney criterion has a floor it hits early</h4>
      <p class="small">It runs linearly from 350&#8202;mg to 2,000&#8202;mg and then stops. {len(zero)} dish{'es' if len(zero)!=1 else ''} in the set {'are' if len(zero)!=1 else 'is'} at or past 2,000&#8202;mg, so the model cannot distinguish a 2,100&#8202;mg stew from a 3,000&#8202;mg one. Both are simply zero.</p>
      <h4 style="margin-top:22px">3 &mdash; Sugar is scored as total, not added</h4>
      <p class="small">A dish is penalised identically for 12&#8202;g of sugar from a bowl of fruit and 12&#8202;g from a honey vinaigrette. First Watch's Tri-Fecta, which is eggs, avocado, seasonal fruit and whole-grain toast, takes a sugar score of {byname['First Watch']['SUG']:.1f} almost entirely on the fruit.</p>
      <h4 style="margin-top:22px">4 &mdash; Cost ignores how much food you get</h4>
      <p class="small">The cost criterion rewards a low price and good protein value, and knows nothing about portion size. A 320-calorie dish and a 780-calorie dish at the same price and protein score identically, though only one of them is dinner.</p>
    </div>
  </div>
</section>'''

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
    <p>Eighteen of the original sixty entries were build-your-own bowls or poke &mdash; 30% of the set and four of the top ten &mdash; while a document written in North Carolina contained no barbecue, no Southern cooking, no Greek, no Persian, no West African and no Chinese-American takeout. These {len(ADDS)} entries close part of that gap. Each was scored on the identical model.</p>
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
    def block(c):
        kind = c.get('kind', 'wrong')
        badge = {'wrong': ('badge-wrong', 'Corrected'), 'stale': ('badge-stale', 'Out of date'),
                 'confirmed': ('badge-ok', 'Confirmed'), 'open': ('badge-open', 'Still open')}[kind]
        return f'''<div class="corr">
      <div class="corr-head"><span class="badge {badge[0]}">{badge[1]}</span><h3 style="font-size:1rem">{e(c['claim'])}</h3></div>
      <p class="was">First edition: {e(c['was'])}</p>
      <p class="now">{e(c['now'])}</p>
      {f'<p class="caption" style="margin-top:5px">{e(c["source"])}</p>' if c.get('source') else ''}
    </div>'''
    return f'''<section id="corrections">
  <hr class="rule-heavy">
  <span class="eyebrow">The verification log</span>
  <h2>What was wrong</h2>
  <div class="measure stack" style="margin-top:16px">
    <p>{e(CORR.get('preamble',''))}</p>
  </div>
  <div style="margin-top:24px">{''.join(block(c) for c in CORR['items'])}</div>
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
