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
       'It runs linearly from 350&#8202;mg to 2,000 and then floors. ' + str(len(ceiling)) + ' dishes sit at or past that floor, so the '
       'model cannot separate them. The clearest case is ' + e(ck['restaurant']) + ': this edition corrected its sodium from 2,100&#8202;mg to '
       'roughly <strong class="num">' + f"{ck['sodium']:,}" + '&#8202;mg</strong> once the kimchi side was counted at USDA’s figure of '
       '498&#8202;mg per 100&#8202;g. Its overall score moved by <strong class="num">0.02</strong>. Nearly doubling the sodium in the '
       'saltiest dish here is invisible to the criterion built to catch it.',
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

