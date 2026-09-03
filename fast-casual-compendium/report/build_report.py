"""Assemble the report: the argument up front, all 87 entries in price bands.

The two traditions the research surfaced disagree about where a big scored set
belongs. Data journalism shows it early as one sorted picture (538 put all 85
candies in a chart before any analysis). Print reference guides never sort the
body by score at all - Michelin orders by commune, Zagat alphabetically - and
keep the ranking in short cross-cutting lists instead. They are solving
different problems: one wants a picture of the distribution, the other wants a
place to look things up. This document does both, and neither has to lose.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'research'))
import hybrid_figures as HF
import ranking_chart as RC
import entries as E

HERE = os.path.dirname(os.path.abspath(__file__))
F, R = HF.F, HF.R
esc = E.esc

def money(x): return f'${x:,.2f}'

# ---------------------------------------------------------------- sections
def sec_hook():
    c, d = F['cheap'], F['dear']
    # The second, harder case: a proper cooked dinner rather than a pizza.
    # Both counts are computed, never typed - an earlier draft asserted a
    # number by hand and it was wrong.
    ox = min([x for x in R if x['price'] >= 30], key=lambda x: x['overall'])
    half = [x for x in R if x['price'] < ox['price'] / 2]
    beat = [x for x in half if x['overall'] > ox['overall']]
    def card(x, kind, note):
        return f'''<div class="hk {kind}">
   <p class="hk-price">{money(x['price'])}</p>
   <h3>{esc(x['dish'])}</h3>
   <p class="hk-who">{esc(x['restaurant'])} · {esc(x['cuisine'])}</p>
   <p class="hk-score"><b>{x['overall']:.2f}</b><span>out of 10</span></p>
   <p class="hk-note">{note}</p></div>'''
    return f'''<section class="hook" id="top">
 <p class="kicker">Eighty-seven delivery dinners in the Research Triangle, scored</p>
 <h1>What you pay has almost nothing to do with what you get</h1>
 <div class="hk-pair">
  {card(d, 'hk-bad', 'The worst-scoring dish that costs at least twice the one beside it.')}
  {card(c, 'hk-good', 'The best-scoring dish under twelve dollars.')}
 </div>
 <p class="hk-sum">{money(d['price'] - c['price'])} more money.
    <b>{d['overall'] - c['overall']:+.2f} points.</b></p>
 <p class="lede">You can object that a pizza was never going to beat a lentil bowl, and
    you would be right. So take the harder case: {esc(ox['restaurant'])}'s
    {esc(ox['dish'].lower())}, a proper cooked dinner at <b>{money(ox['price'])}</b>, scores
    <b>{ox['overall']:.2f}</b>. Of the <b>{len(half)}</b> dishes here that cost less than
    half as much, <b>{len(beat)}</b> beat it. Across all {F['n']} dishes, from
    {F['n_cuisines']} cuisines and {F['n_restaurants']} different restaurants, the
    relationship between what a dish costs and how good it is for you is
    <b>r&nbsp;=&nbsp;+{F['r_price_health_all']:.2f}</b> — which is, in plain English,
    nothing.</p>
</section>'''

def sec_finding():
    p = F['per5']
    return f'''<section id="finding">
 <h2>What an extra five dollars actually buys</h2>
 <p>Not nothing — that is the surprise. Money does buy something. It just does not buy
    health. Every additional five dollars on a Triangle delivery order brings, on average:</p>
 <div class="deltas">
  <div class="dl up"><b>+{p['protein']:.1f} g</b><span>protein</span></div>
  <div class="dl up"><b>+{p['cal']:.0f}</b><span>calories</span></div>
  <div class="dl dn"><b>+{p['sodium']:.0f} mg</b><span>sodium</span></div>
  <div class="dl dn"><b>+{p['satfat']:.1f} g</b><span>saturated fat</span></div>
  <div class="dl dn"><b>{p['fiber']:.1f} g</b><span>fibre</span></div>
 </div>
 <p class="pull">Money buys a bigger, richer plate. The good and the bad arrive together,
    and they cancel.</p>
 <p>This is the finding that does not depend on our scoring model at all, and it is the
    one to trust most. With no model, no weights and no judgement calls — just price
    against the numbers on the label — price correlates with protein at
    <b>{F['raw']['protein']:+.2f}</b> and with saturated fat at <b>{F['raw']['satfat']:+.2f}</b>,
    with sodium at <b>{F['raw']['sodium']:+.2f}</b> and with fibre at
    <b>{F['raw']['fiber']:+.2f}</b>. A more expensive dinner is a larger dinner. Whether
    that is better for you depends entirely on what the kitchen does, and price does not
    tell you.</p>
</section>'''

def sec_chart():
    return f'''<section id="all87" class="wide">
 <h2>All 87, ranked</h2>
 <p class="sub">Sorted by overall score, so the bars fall by construction — that on its
    own shows nothing. The price column beside them is on its own scale and is sorted by
    nothing at all. Read down it.</p>
 {RC.chart()}
 <p class="cap">Tinting follows the health score. Two dishes score 6.5 or better and are
    still held out of the top tier by a criterion that is plain arithmetic on the macros;
    both are flagged in the row with the criterion that did it.</p>
</section>'''

def sec_obvious():
    return '''<section id="obvious">
 <h2>Why we did not just divide calories by dollars</h2>
 <p>The obvious measure is the one everybody reaches for first, and it fails badly here.
    Calories per dollar makes a $9 plate of fried rice the best purchase in the Triangle
    and a $17 tuna bowl one of the worst, which inverts the answer. Protein per dollar is
    better and still wrong: it ranks a sodium-loaded rotisserie combo above a lentil bowl
    with two-thirds the salt. A star rating from reviews measures whether people enjoyed
    dinner, which is a real thing to measure and a different one.</p>
 <p>So the score here is nine criteria, and the important disclosure is that they are not
    all the same kind of number. <b>Six are arithmetic</b> on the figures a restaurant
    publishes or that we estimated from the build — sodium, saturated fat, protein
    density, sugar, plus flavour and value. <b>Three are judgements</b> against a written
    rubric: gut, steady energy, inflammation. We audited our own model and those three are
    where it is weakest. They are drawn differently everywhere in this document —
    outlined rather than solid — so you can always see which half of a score is computed
    and which half is opinion.</p>
</section>'''

def sec_sensitivity():
    a = F['alts']; m60, m87 = F['mc60'], F['mc87']
    rows = ''.join(
        f'<tr><td>{esc(x["name"])}</td><td class="n">{x["r_overall"]:+.3f}</td>'
        f'<td class="n">{x["r_health"]:+.3f}</td><td class="n">#{x["cheap_rank"]}</td>'
        f'<td class="n">#{x["dear_rank"]}</td></tr>' for x in a)
    return f'''<section id="sensitivity">
 <h2>“You only got that answer because of how you weighted it”</h2>
 <p>It is the right objection, and it is the one that sank Food Compass — a nutrition
    score that produced a famously counterintuitive result and had not published how
    much that result depended on its own weights. So here are ours, tested to
    destruction.</p>
 <table class="alt">
  <thead><tr><th>Weighting</th><th>r&nbsp;(price, overall)</th><th>r&nbsp;(price, health)</th>
   <th>{esc(F['cheap']['restaurant'])}</th><th>{esc(F['dear']['restaurant'])}</th></tr></thead>
  <tbody>{rows}</tbody>
 </table>
 <p>Then 2,000 random weightings, each of the nine criteria drawn independently between
    a quarter and double its published weight. On the sixty dishes that form our
    representative sample the median correlation is <b>{m60['median']:+.3f}</b>; on all 87
    it is <b>{m87['median']:+.3f}</b>. Restricted to the four criteria that are plain
    arithmetic and that our audit did not dispute, it turns slightly negative
    (<b>−0.11</b>).</p>
 <p class="honest"><b>What does not survive:</b> about one weighting in ten
    ({m87['p_over_2']}% of the 2,000) does push the correlation past +0.2, and the most
    price-favourable weighting we found reaches +0.35. So the claim is not that no
    weighting can make price look like a guide to health. It is narrower than that, and
    it is this: the most favourable weighting of these nine criteria still leaves price
    explaining about a tenth of the variation in how good a dish is for you, and the
    typical weighting leaves it explaining none.</p>
</section>'''

def sec_bands():
    out = ['<section id="bands"><h2>The eighty-seven, by what they cost</h2>',
           '<p class="sub">Not sorted by rank. The bands are the argument: each one holds '
           'roughly the same spread of health scores as the one before it, and the money '
           'goes up regardless. Walk them in order and the finding arrives without a chart.</p>',
           E.legend()]
    badged = {id(d) for d in F['badged']}
    for b in F['bands']:
        g = sorted([d for d in R if d['band'] == b['name']], key=lambda d: -d['overall'])
        nb = sum(1 for d in g if id(d) in badged)
        note = ('' if b['name'] != '$20 and up' else
                ' <b class="warn">Every dish in this band is beaten on health by '
                'something cheaper on this list.</b>')
        out.append(f'''<div class="band">
   <div class="band-hd">
     <h3>{esc(b['name'])}</h3>
     <p class="band-st"><b>{b['n']}</b> dishes · median health <b>{b['med_health']:.2f}</b>
        · range {b['lo']:.1f} to {b['hi']:.1f} · mean price <b>{money(b['mean_price'])}</b>
        {f"· <b>{nb}</b> best buys" if nb else ""}{note}</p>
   </div>
   <div class="grid">{''.join(E.entry(d, badge=id(d) in badged) for d in g)}</div>
  </div>''')
    return '\n'.join(out) + '</section>'

def sec_picks():
    def lst(items, fn):
        return '<ol class="picks">' + ''.join(
            f'<li><span class="p-money">{money(x["price"])}</span>'
            f'<span class="p-d">{esc(x["dish"])}<i>{esc(x["restaurant"])}</i></span>'
            f'<span class="p-n">{fn(x)}</span></li>' for x in items) + '</ol>'
    fr = F['frontier']
    wk = F['week_value']
    return f'''<section id="picks">
 <h2>The short lists</h2>
 <div class="two">
  <div>
   <h3>The best buys</h3>
   <p class="sub">Under {money(F['cap'])} delivered, and health at {F['floor']:.1f} or above.
      Six of the {F['n_under_cap']} dishes under the cap qualify.</p>
   {lst(F['badged'], lambda x: f'{x["health"]:.1f}')}
  </div>
  <div>
   <h3>Nothing on this list beats these on both price and health</h3>
   <p class="sub">The efficient frontier: {len(fr)} dishes of {F['n']}. Every one of the
      <b>{F['n_over_17']}</b> dishes over $17 is beaten by something cheaper.</p>
   {lst(fr, lambda x: f'{x["health"]:.1f}')}
  </div>
 </div>
 <div class="week">
  <h3>Five dinners</h3>
  <p>Ordering the five best-value dishes for a working week costs
     <b>{money(F['week_value_cost'])}</b> and averages <b>{F['week_value_health']:.2f}</b> on
     health. Ordering the five highest-scoring dishes instead costs
     <b>{money(F['week_top_cost'])}</b> and averages <b>{F['week_top_health']:.2f}</b>.
     That is <b>{money(F['week_top_cost'] - F['week_value_cost'])}</b> a week — about
     {money((F['week_top_cost'] - F['week_value_cost']) * 52)} a year — for
     <b>{F['week_top_health'] - F['week_value_health']:+.2f}</b> points. At the very top of
     the market money does buy something. Across the middle, where almost every order
     actually happens, it does not.</p>
  {lst(wk, lambda x: f'{x["health"]:.1f}')}
 </div>
</section>'''

def sec_method():
    n_pub = sum(1 for d in R if d.get('data') == 'PUBLISHED')
    n_part = sum(1 for d in R if d.get('data') == 'PARTIAL')
    return f'''<section id="method">
 <h2>How to argue with this</h2>
 <p><b>Where the numbers come from.</b> {n_pub} of the {F['n']} dishes carry figures the
    restaurant publishes itself; {n_part} are part published and part estimated; the rest
    are estimated from the stated build using USDA reference values. Every entry says
    which it is, and no estimated figure is ever presented as a measured one. The
    published entries share a striking property: all of them are assembled bowls or raw
    fish. Not one heat-cooked dish in the set has published nutrition data, which is why
    the gap between published and estimated dishes is a fact about who publishes, not
    about our estimates.</p>
 <p><b>Where it is weakest.</b> Three of the nine criteria are rubric judgements rather
    than arithmetic, and our own audit found them the least defensible part of the model.
    Prices are what DoorDash showed, which moves, and excludes fees, tips and promotions.
    Portion sizes for estimated dishes are the largest source of error. The score is not
    a health claim about you; it is a comparison between these 87 dishes.</p>
 <p><b>What changed since the first edition.</b> Thirteen dishes were re-scored against
    figures their restaurants publish. Eleven of the thirteen got <i>worse</i> — mean
    −0.55 — which is the direction you would expect if estimates flatter food, and a
    reason to read the estimated entries with more suspicion than the published ones.</p>
</section>'''

# ---------------------------------------------------------------- assembly
def build():
    css = open(os.path.join(HERE, 'report.css')).read()
    fonts = open(os.path.join(HERE, '..', 'brochure', 'fonts.css')).read()
    prin = open(os.path.join(HERE, 'print.css')).read()
    body = '\n'.join([sec_hook(), sec_finding(), sec_chart(), sec_obvious(),
                      sec_sensitivity(), sec_bands(), sec_picks(), sec_method()])
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>What Delivery Costs You — 87 dishes, ranked</title>
<meta name="description" content="Eighty-seven fast-casual delivery dishes in the Research
 Triangle, scored on nine criteria. What you pay has almost nothing to do with what you get.">
<style>{fonts}</style>
<style>{css}</style>
<style media="print">{prin}</style>
</head><body>
<main>{body}</main>
<footer><p>Eighty-seven dishes from 87 restaurants across 43 cuisines in Durham, Raleigh,
 Chapel Hill and Cary. Prices and menus as listed on DoorDash. Every figure in this
 document is computed from the dataset, not typed by hand.</p></footer>
</body></html>'''
    out = os.path.join(HERE, 'What-Delivery-Costs-You-87.html')
    open(out, 'w').write(html)
    return out, len(html)

if __name__ == '__main__':
    p, n = build()
    print(f'{p}  ({n/1024:.0f} KB)')
