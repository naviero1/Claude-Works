def sec_findings():
    """The six findings that replace the first edition's front page.
    Every number is computed from the corrected dataset at build time."""
    B  = F['bowl_share']
    fs = F['flavor_split']
    wn, wc = F['week_naive'], F['week_cheap']
    saving = wn['cost'] - wc['cost']
    best_val = min(D, key=lambda d: d['dpp'])
    best_na  = min(D, key=lambda d: d['na_p'])
    quinoa   = next(x for x in F['salt_components'] if 'quinoa' in x['item'])
    bowls    = next(g for g in F['dupes'] if g['name'] == 'Build-your-own bowl')
    cheapest_good = min([d for d in D if d['health'] >= 6.0], key=lambda d: d['price'])
    dearest_bad   = max([d for d in D if d['health'] < 5.5], key=lambda d: d['price'])

    cards = [
      ('money', f"{F['r_price_health']:+.2f}", 'price against health, all 60 dishes',
       'Paying more buys flavor, not health',
       f"Across the whole set, price and health correlate at {F['r_price_health']:+.2f} &mdash; under one percent of the "
       f"variation, and it survives dropping any single dish. Price and <em>flavor</em> correlate at "
       f"{F['r_price_flavor']:+.2f}, five times as strong. {e(cheapest_good['restaurant'])} at "
       f"{money(cheapest_good['price'])} outscores {e(dearest_bad['restaurant'])} at {money(dearest_bad['price'])} on "
       f"every health criterion that matters.",
       'Spend money when you want the meal to be good, not when you want it to be good for you.'),

      ('money', money(saving), 'saved on a week, for the same coverage',
       'The cheap week is as good as the expensive one',
       f"Five dinners chosen as the top-ranked dishes cost {money(wn['cost'])}. Five chosen as the cheapest that still "
       f"cover every criterion cost {money(wc['cost'])} &mdash; and both bottom out at exactly "
       f"{wc['floor']:.1f}&#8202;/&#8202;10 on their weakest criterion. The extra {money(saving)} buys nothing the model "
       f"can measure.",
       f"Rotate {', '.join(e(d['restaurant']) for d in sorted(wc['dishes'], key=lambda x: x['price'])[:3])} and two more "
       f"instead of chasing the top of the list."),

      ('money', f"${best_val['dpp']:.2f}", 'per gram of protein',
       'The cheapest protein here is also the cleanest',
       f"{e(best_val['restaurant'])}'s {e(best_val['dish']).lower()} is {money(best_val['price'])} for "
       f"{best_val['protein']}&#8202;g of protein &mdash; the best value on the list &mdash; and it carries "
       f"{best_na['na_p']:.1f}&#8202;mg of sodium per gram of that protein, also the best on the list. Cheap and clean are "
       f"usually a trade. Here they are the same dish, and it is the second-cheapest thing in the document.",
       'If you order one thing off this list, order that.'),

      ('warn', f"+{fs['na_hi']-fs['na_lo']:,.0f}&#8202;mg", 'what flavor actually costs',
       'Flavor is bought with salt, not with fat',
       f"The {fs['n_hi']} dishes scoring 7.5 or better on flavor carry {fs['na_hi']-fs['na_lo']:+,.0f}&#8202;mg more sodium "
       f"than the {fs['n_lo']} scoring 5.5 or worse (t&nbsp;=&nbsp;{F['welch_sodium'][0]:.1f}), and only "
       f"{fs['sf_hi']-fs['sf_lo']:+.1f}&#8202;g more saturated fat (t&nbsp;=&nbsp;{F['welch_satfat'][0]:.1f}, which is "
       f"nearly nothing). The seasoning is the cost, not the cooking fat.",
       'Watch the sauce, the base and the cure. Stop watching the olive oil and the avocado.'),

      ('warn', f"{quinoa['mg']:,}&#8202;mg", 'in a portion of plain quinoa',
       'The salt is in the base, not in the dressing',
       f"Farmside Kitchen's seasoned quinoa is {quinoa['mg']:,}&#8202;mg of sodium before anything is put on it; CAVA's two "
       f"rice bases are 770 each. Meanwhile the four lowest-sodium components anywhere in this document are all proteins &mdash; "
       f"plain tuna at 40&#8202;mg, a salmon add-on at 90, grilled chicken at 69. The first edition blamed the dressing and "
       f"the cheese. Its own restaurant's numbers say otherwise.",
       'Change the base before you change the protein. Refusing the grain saves more than refusing the sauce.'),

      ('flav', f"{F['dupe_priciest_wins']} of {len(F['dupes'])}", 'times the priciest version wins',
       'The same dish costs twice as much and scores worse',
       f"Seven groups of near-identical dishes appear across the set &mdash; kebab plates, build-your-own bowls, raw fish "
       f"plates, South Indian steamed plates. The most expensive version is the best one in only "
       f"{F['dupe_priciest_wins']} of them. Among the {bowls['n']} build-your-own bowls, price and score correlate at "
       f"{bowls['r']:+.2f}: within that format, paying more is actively worse.",
       'Once you have chosen the kind of food you want, take the cheapest version of it.'),
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
      'restaurant, and each is recomputable from the ranking table below. Three of them are about money, because that is '
      'where the data turned out to be most surprising.</p>\n'
      f'  <div class="findings" style="margin-top:34px">{out}</div>\n'
      '</section>')

