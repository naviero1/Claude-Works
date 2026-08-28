def sec_additions():
    if not ADDS: return ''
    entries = sorted(ADDS, key=lambda x: -x['overall'])

    rows = ''
    for d in entries:
        sid = d.get('store') or ''
        sid_html = (f'<span class="sub dimtd">DoorDash store {e(sid)}, reported but not independently confirmed</span>'
                    if sid else '<span class="sub dimtd">no DoorDash store id established</span>')
        na_cls = 'lo' if d['sodium'] >= 1500 else ''
        rows += (
            '<tr>'
            f'<td><span class="rest">{e(d["restaurant"])}</span>'
            f'<span class="sub">{e(d["dish"])} &middot; {e(d.get("city", ""))}</span>{sid_html}</td>'
            f'<td class="dimtd">{e(d.get("cuisine", ""))}</td>'
            f'<td class="n score" style="font-weight:600">{d["overall"]:.2f}</td>'
            f'<td class="n score">{d["health"]:.1f}</td>'
            f'<td class="n score" style="color:var(--flavor)">{d["FLAVOR"]:.1f}</td>'
            f'<td class="n money">{money(d["price"])}</td>'
            f'<td class="n num">{d["protein"]}</td>'
            f'<td class="n num {na_cls}">{d["sodium"]:,}</td>'
            '</tr>')

    notes = ''
    for d in entries:
        flav = f'<p class="small" style="margin-top:7px">{e(d.get("on_flavor", ""))}</p>' if d.get('on_flavor') else ''
        notes += (
            '<div class="corr">'
            f'<div class="corr-head"><span class="corr-who">{e(d.get("cuisine", ""))}</span></div>'
            f'<h3 style="font-size:1.02rem;margin-bottom:7px">{e(d["restaurant"])} &mdash; {e(d["dish"])}</h3>'
            f'<p class="small">{e(d.get("why_it_scores", ""))}</p>'
            f'{flav}'
            f'<p class="small" style="margin-top:9px;color:var(--ink-3)">'
            f'<strong>Order it:</strong> {e(d.get("build", ""))}</p>'
            '</div>')

    absent = ''
    if ABSENT:
        absent = ('<div class="callout"><h4>Categories that really are empty here</h4>'
                  f'<p style="margin-top:6px">Searched, and not padded to fill a row. {e(ABSENT)}</p></div>')

    best = entries[0]
    place = ordinal(sum(1 for x in MERGED if x['overall'] > best['overall']) + 1)

    return (
      '<section id="additions">\n'
      '  <hr class="rule-heavy">\n'
      '  <span class="eyebrow">New in this edition</span>\n'
      '  <h2>The food the first edition missed</h2>\n'
      '  <div class="measure stack" style="margin-top:16px">\n'
      f'    <p>These {len(entries)} entries close part of the gap the previous section describes. Each was found by asking what '
      'actually delivers in the Research Triangle in a category the first edition skipped, each was independently checked for '
      'whether the restaurant exists and the dish is really on its menu, and each was scored on the identical model &mdash; the '
      'six computed criteria by formula, the three rubric criteria by the same judgement the original sixty got.</p>\n'
      f'    <p>The best of them, {e(best["restaurant"])}&rsquo;s {e(best["dish"]).lower()} at {money(best["price"])}, scores '
      f'{best["overall"]:.2f} &mdash; which would place it {place} in the main ranking.</p>\n'
      '    <p class="caption">Every one of these is estimated from menu construction rather than published nutrition, and should '
      'be read at the confidence the measurement chapter describes. Existence was established against county restaurant-inspection '
      'registries and the restaurants&rsquo; own sites; <strong>no DoorDash store id in this group could be independently checked</strong>, '
      'because DoorDash refuses automated requests, so the ids below are reported rather than verified and several entries carry '
      'none at all.</p>\n'
      '  </div>\n'
      '  <div class="tablewrap"><table><thead><tr>'
      '<th>Restaurant and dish</th><th>Cuisine</th><th class="n">Overall</th><th class="n">Health</th>'
      '<th class="n">Flavor</th><th class="n">Price</th><th class="n">Pro</th><th class="n">Na mg</th>'
      f'</tr></thead><tbody>{rows}</tbody></table></div>\n'
      f'  {absent}\n'
      '  <h3 style="margin-top:40px">Why each one is here</h3>\n'
      f'  <div style="margin-top:14px">{notes}</div>\n'
      '</section>')


