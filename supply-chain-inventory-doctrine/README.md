# The Inventory Doctrine

How supply chain and manufacturing theory treated inventory **before 2019**, what
COVID broke, and why the KPIs and risk models changed.

## Files

- **`index.html`** — the full report. Open it in any browser. Charts and diagrams
  are inline SVG/CSS with no libraries; the only network request is the Google
  Fonts stylesheet, and the page degrades cleanly to system fallbacks offline.
- **`data.json`** — every figure used in the report with its source, date and type
  (measured / reported / forecast / survey), plus the full monthly raw series.
- **`artifact.html`** — the same page as a body fragment, for publishing.
- **`src/`** — the sources the two HTML files are built from. Run
  `python3 src/build.py` to regenerate both.
- **`notes/design-plan.md`** — the design brief and the chart-palette validation.

## The argument

1. **§01 The doctrine.** A century of inventory theory — EOQ, the newsvendor,
   statistical safety stock, JIT/TPS, the bullwhip, risk pooling, Theory of
   Constraints, Lean, Fisher's matrix, Triple-A, the cash conversion cycle — all
   pointing one way: hold less. Every model gives *demand* a distribution and
   *supply* a constant. That unwritten assumption is the whole story.
2. **§02 What broke.** The 2020–22 record with figures: the NY Fed pressure index
   peaking at **+4.44σ** in December 2021, the highest since the series began in
   1998; the bullwhip in the chip market; 109 ships at anchor off Los Angeles.
   Four modelling failures — and a fifth failure that was not modelling at all,
   but the scorecard.
3. **§03 The correction.** The measured finding at the centre of this report:
   US manufacturing and retail inventory-to-sales **diverged**. Retail is below
   its pre-COVID level on every baseline (1.25 against a 2015–19 average of
   1.47); the aggregate is **0.10 below**; manufacturing is **0.08 above**. The
   section reports all three pre-COVID baselines, including the one that
   weakens the manufacturing claim.
4. **§04 The new doctrine.** Nine things that replaced "minimise inventory,"
   including the steel-man for just-in-time — which did not cause this.
5. **§05 The KPI ledger.** The centrepiece: 16 metric pairs, filterable by domain.
   Old metric → what it optimised for → the failure mode COVID exposed → the new
   metric → why that replacement follows.
6. **§06 Risk assessment.** The seven conceptual shifts underneath all of it.
7. **§07 Did it stick?** What leaders *say* against what the data *shows*, and an
   evidence-weighted verdict on what retreated and what held.
8. **§08 Sources & method**, including four things a careful reader should hold
   against the document.

## The finding, in one line

"Just-in-case replaced just-in-time" is **false in aggregate**. What replaced lean
was not *hold more* but **hold according to consequence** — heavier buffers on the
small number of parts that can stop a line, thinner buffers than ever on
everything else. That is a change in the *composition* of inventory, which is
exactly why it needed a new set of metrics: the old ones could only measure the
*level*.

**On baselines.** Manufacturing inventories were already climbing through 2019
under the trade war (1.40 in January to 1.52 in December), so the manufacturing
result moves with the baseline: **+0.08** against the 2015–19 average, **+0.03**
against the 2019 average, **−0.04** against December 2019 alone. The report shows
all three. What is robust under every baseline is the **divergence** between
manufacturing and retail — the gap widened by 0.14 to 0.29 months — and the fact
that retail, wholesale and the total all sit below any pre-COVID level. That is
the claim the argument rests on.

## Method & caveats

Built from eight parallel research passes across doctrine, evidence, KPIs and
modelling, each put through an adversarial fact-checking pass, plus direct
retrieval of the primary time series.

Read the numbers carefully. Measured public series (Census MTIS, NY Fed GSCPI)
carry the argument. Consultant forecasts and survey responses are labelled as
such and are *not* treated as data — notably the AlixPartners chip-shortage
figure, which is a forecast issued in September 2021, and the McKinsey pulse
survey percentages, which come from unmatched waves with shifting question
wording. Full caveats are in §08 of the report and in `data.json`.
