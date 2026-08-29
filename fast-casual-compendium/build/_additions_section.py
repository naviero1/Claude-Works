def sec_additions():
    if not ADDS: return ''
    A = F['added']
    NOTES = load('addnotes.json', {})
    entries = sorted(ADDS, key=lambda x: -x['overall'])
    best = entries[0]
    place = ordinal(sum(1 for x in MERGED if x['overall'] > best['overall']) + 1)

    def block(d):
        pos = sum(1 for x in MERGED if x['overall'] > d['overall']) + 1
        sid = (d.get('store') or '').strip()
        prov = (f'DoorDash store {e(sid)}, reported but not independently confirmed'
                if sid else 'no DoorDash store id established')
        if d.get('price_note'): prov += f' &middot; {e(d["price_note"])}'
        return f'''<article class="entry">
      <div class="entry-head">
        <div>
          <h3>{e(d['restaurant'])}</h3>
          <p class="entry-dish">{e(d['dish'])}</p>
          <p class="entry-meta">{e(d['cuisine'])} &middot; {e(d.get('city',''))} &middot; {ordinal(pos)} of {len(MERGED)}</p>
        </div>
        <div class="entry-score">
          <span class="entry-ovr num">{d['overall']:.2f}</span>
          <span class="entry-ovr-l">overall</span>
        </div>
      </div>
      <div class="tablewrap">
        <table class="entry-tbl"><thead><tr>{charts.score_headers()}
          <th class="n">Price</th><th class="n">Cal</th><th class="n">Pro</th>
          <th class="n">Na mg</th><th class="n">Sat</th><th class="n">Fib</th></tr></thead>
        <tbody><tr>{charts.score_cells(d)}
          <td class="n money">{money(d['price'])}</td>
          <td class="n num">{d['cal']:,}</td><td class="n num">{d['protein']}</td>
          <td class="n num {'lo' if d['sodium'] >= 1500 else ''}">{d['sodium']:,}</td>
          <td class="n num">{d['satfat']:g}</td><td class="n num">{d['fiber']:g}</td>
        </tr></tbody></table>
      </div>
      <p class="entry-note">{e(NOTES.get(d['restaurant'], ''))}</p>
      <p class="entry-build"><b>Order it</b>{e(d.get('build',''))}</p>
      <p class="entry-prov">{prov}</p>
    </article>'''

    return (
      '<section id="additions">\n'
      '  <hr class="rule-heavy">\n'
      '  <span class="eyebrow">New in this edition</span>\n'
      '  <h2>The food the first edition missed</h2>\n'
      '  <div class="measure stack" style="margin-top:16px">\n'
      f'    <p>These {len(ADDS)} entries close part of the gap the previous section describes. Each was found by asking '
      f'what actually delivers in the Research Triangle in a category the first edition skipped, each was independently '
      f'checked for whether the restaurant exists and the dish is really on its menu, and each was scored on the '
      f'identical model. The best of them, {e(best["restaurant"])}&rsquo;s {e(best["dish"]).lower()} at '
      f'{money(best["price"])}, would place {place} of {len(MERGED)}.</p>\n'
      '  </div>\n'
      '  <div class="callout">\n'
      '    <h4>How they score against the same measures</h4>\n'
      f'    <p style="margin-top:6px">Worse food, on this model, and predictably so: mean health {A["health"]:.2f} '
      f'against {A["orig_health"]:.2f} for the original sixty, on {A["sodium"]-A["orig_sodium"]:+,.0f}&#8202;mg more '
      f'sodium at almost exactly the same price. That is what filling the gaps costs &mdash; {A["n_grilled"]} of the '
      f'{A["n"]} are grilled, smoked or fried, and this document&rsquo;s whole argument is that those formats buy their '
      f'flavor with salt. The exceptions are the point: {e(A["cheapest_good"]["restaurant"])} clears health 6.0 at '
      f'{money(A["cheapest_good"]["price"])}, cheaper than anything in the original set that does.</p>\n'
      '  </div>\n'
      f'  <div class="entries">{"".join(block(d) for d in entries)}</div>\n'
      '</section>')

