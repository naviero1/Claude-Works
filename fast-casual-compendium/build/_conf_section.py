def sec_confidence():
    T = F['tiers']; rt = F['round_tell']; V = F['verified_by_prep']; TC = F['tier_controlled']
    n_retier = sum(1 for c in CORR if c.get('retier') == 'PUBLISHED') if CORR else 0
    _pc = sorted(d['cal'] for d in D if d['data'] == 'PUBLISHED')
    pub_cals = ', '.join(str(c) for c in _pc[:-1]) + ' and ' + str(_pc[-1])
    rows = [[f'<td><span class="rest">{e(k.title())}</span></td>',
             f'<td class="n num">{v["n"]}</td>',
             f'<td class="n score">{v["health"]:.2f}</td>',
             f'<td class="n num">{v["sodium"]:,.0f}</td>',
             f'<td class="n score">{v["flavor"]:.2f}</td>',
             f'<td class="n money">{money(v["price"])}</td>'] for k, v in T.items()]
    return (
      '<section id="confidence">\n'
      '  <hr class="rule-heavy">\n'
      '  <span class="eyebrow">Before you trust a number</span>\n'
      '  <h2>How much of this is measured</h2>\n'
      '  <div class="measure stack" style="margin-top:16px">\n'
      f'    <p>{T["PUBLISHED"]["n"]} of the {len(D)} entries are built from a chain&rsquo;s own published nutrition documents &mdash; '
      f'{n_retier} more than the first edition claimed, because Chopt and Sweetgreen both publish figures it never consulted. '
      f'{T["PARTIAL"]["n"]} are partial. The other {T["ESTIMATED"]["n"]} are reasoned from how the dish is put together, and that '
      f'reasoning leaves fingerprints: {rt["sodium"]} of them land on a round multiple of 50&#8202;mg of sodium and {rt["cal"]} on a '
      f'multiple of 20 calories. Real nutrition panels do not do that. The published entries here read {pub_cals} calories.</p>\n'
      '  </div>\n'
      f'  {table(["Confidence tier", "~Entries", "~Mean health", "~Mean sodium mg", "~Mean flavor", "~Mean price"], rows)}\n'
      '  <div class="callout warn">\n'
      '    <h4>The gap in that table is not what it looks like</h4>\n'
      f'    <p style="margin-top:6px">Read naively, published entries carry <span class="num">{abs(TC["raw_sodium_gap"]):,.0f}&#8202;mg</span> '
      f'less sodium than estimated ones and score <span class="num">{abs(TC["raw_flavor_gap"]):.2f}</span> lower on flavor. That reads '
      f'like an estimator who reaches for a high, dull number when they do not know one. It is not. '
      f'<strong>Every one of the {V["n_assembled_verified"]} entries with published or partial data is an assembled bowl or a plate '
      f'of raw fish. Not one of the {V["n_cooked"]} dishes here that meets heat &mdash; grilled, stewed or steamed &mdash; rests on a '
      f'published number.</strong> Nobody publishes nutrition for food cooked to order over fire, so the published tier and the '
      f'bowl-chain tier are the same tier.</p>\n'
      f'    <p style="margin-top:10px">Control for that and the apparent bias mostly disappears. Compare only the assembled and raw '
      f'dishes with each other &mdash; {TC["n_pub"]} verified against {TC["n_est"]} estimated, same format &mdash; and the flavor gap '
      f'collapses to <span class="num">{TC["flavor_gap"]:+.2f}</span> and the sodium gap actually reverses to '
      f'<span class="num">{TC["sodium_gap"]:+,.0f}&#8202;mg</span>. The estimator was not systematically pessimistic. '
      f'<strong>The sample was systematically narrow.</strong></p>\n'
      '    <p style="margin-top:10px">Which leaves the caveat in a more useful place. Trust the ranking&rsquo;s treatment of bowls, '
      'salads and raw fish, because that is where the real numbers are. Treat every grilled, stewed and steamed entry as a '
      'construction estimate that no restaurant has confirmed &mdash; and note that this edition&rsquo;s largest corrections, '
      'Sassool and El Cuscatleco, both came from exactly that group.</p>\n'
      '  </div>\n'
      '</section>')

