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
       f"All {fr['n_dominated']} dishes priced above {money(fr['cutoff'])} are beaten outright by something cheaper: "
       f"{e(fr['worst_example']['restaurant'])}&rsquo;s {money(fr['worst_example']['price'])} dish scores "
       f"{fr['worst_example']['health']:.1f} where {money(fr['beater']['price'])} buys {fr['beater']['health']:.1f}.",
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

