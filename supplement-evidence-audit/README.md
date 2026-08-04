# Supplement Evidence Audit

An open-ended, decision-grade field guide to **244 popular supplements, herbs, mushrooms, nootropics and beverages** — each graded **1–5 on the strength of industry-independent human-trial evidence** (not popularity), and written up as **The Noise → The Science → The Verdict**, with the best form to buy and whether you can get it on Amazon or direct from a website.

Built from a multi-workflow adversarial research pass — **~150 AI research agents, ~5.7M tokens, 0 errors** — across four stages: grade every compound from primary trials against seven bias checks, hand the high-stakes and compromised grades to independent reviewers instructed to *refute* them, add best-form bioavailability guidance, and cover teas/coffee/cocoa as their own family.

> **Not medical advice.** Grades measure the *quality and independence of the evidence*, not whether something will work for you specifically or is safe with your medications. Availability reflects typical US retail status and moves over time. Confirm the active/elemental dose and third-party testing before buying anything.

## Files

| File | What it is |
|---|---|
| **`Popular-Supplements-Noise-Science-Verdict.pdf`** | The full field guide (137 pp): master ranked table + a Noise/Science/Verdict entry for all 244 items, with best-form and availability. **Start here.** |
| **`index.html`** | Interactive version — filter by section/score/availability, sort, click any row for the full reasoning. Self-contained, open in any browser. |
| **`data-full.json`** | The complete 244-item dataset (every field), for re-deriving the decision when new trials land. |
| `full-audit.md` · `data.json` | Deep-dive companion: the original **outcome-focused** pass on 121 compounds with trial-level dossiers (effect sizes + CIs, doses, funding splits, primary-source citations) and the four decision lists (placebo / compromised / conditional). |

## How every entry reads

- **The Noise** — what the marketing, influencers and label claim (the hype).
- **The Science** — what independent human trials actually show: effect size with CI, whether it clears the minimum clinically important difference (MCID), the population, RCT vs cohort.
- **The Verdict** — buy / skip / conditional, and for whom.
- **Best form** — the most bioavailable / best-tolerated form (e.g. magnesium **glycinate/citrate** over oxide; **ubiquinol** vs ubiquinone; **methylfolate** vs folic acid; curcumin **phytosome**; fish-oil **triglyceride** vs ethyl-ester; mushroom **fruiting-body + β-glucan %** vs mycelium-on-grain).
- **Watch** — absorption blockers/enhancers, timing, upper limits, interactions, safety.
- **Amazon ✓/✗ · Website ✓/✗** — where you can actually buy it.

The 1–5 scale: **5** large independent RCTs, would bet on it · **4** real but modest, or narrower than marketed · **3** real signal but small/conditional · **2** mechanism outruns outcome (industry-funded/low-quality) · **1** marketing, no credible human outcome. Confidence in the grade is reported separately. A few compounds appear under more than one outcome because the evidence differs by use (creatine is a **5 for muscle, 4 for memory**).

## The headline

Of 244 items, only **15 score ≥4** and **134 sit at 2–2.5** — the market's resting state is a real mechanism, a plausible meta-analysis, and an effect that doesn't clear the MCID, leans on industry funding or one outlier trial, or vanishes outside a deficient/diseased population. **83 grades rest on a funding or outlier artifact.**

**Distribution:** ≥4: **15** · 3–3.5: **44** · 2–2.5: **134** · below 2: **51**.

### What actually earns a place (score ≥4)

Creatine (5, muscle) · Caffeine (4.5) · Whey/protein (4.5) · **Coffee, paper-filtered (4)** · Iron (4, *if ferritin low*) · Psyllium (4) · Cranberry (4, *recurrent UTIs*) · Red yeast rice (4, *but it's just a low-dose statin — take the actual statin*) · Folate (4, *pre-conception*) · Beetroot/dietary nitrate (4) · Sodium bicarbonate (4) · Modafinil (4, *prescription only*). Then a **3.5 tier**: caffeine+L-theanine, nicotinamide, collagen+vitC pre-load, melatonin (circadian, not insomnia), *S. boulardii*, EAAs, beta-alanine, ginger, soy isoflavones, plant sterols, hibiscus tea. **Everything else — the 2s — skip.**

### Where the ✗ shows up (not on Amazon)

13 items can't be bought on US Amazon: prescription drugs (**modafinil, metformin, rapamycin**), the racetam/nootropic gray market (**piracetam, aniracetam, oxiracetam, phenylpiracetam, noopept, phenibut** — not DSHEA-compliant, so specialist vendor sites only), research chemicals (**7,8-DHF, centrophenoxine**), **NMN** (FDA moved to exclude it from supplements), and **CBD** (Amazon policy — vendor sites only).

### A few honest surprises

- **Coffee (filtered) outscores every tea** on hard endpoints — but **espresso and unfiltered/French-press coffee raise LDL** via diterpenes (a causal RCT finding, unlike the confounded cohort benefits).
- The **green-tea liver-tox signal is specific to concentrated extract capsules**, not the brewed cup.
- **Chaga** carries a real oxalate-nephropathy (kidney) risk; **agaricus** and **reishi** have hepatotoxicity reports — "natural" is not "safe."
- Most **functional-mushroom** products are **mycelium-grown-on-grain**, whose "polysaccharide %" is inflated by starch — insist on fruiting-body extract with a stated β-glucan number.
- The entire **longevity aisle** (NAD boosters, senolytics) tops out at 2.5: biomarkers move, human *outcomes* don't.

## Method & caveats

Four adversarial workflows: (1) 121 compounds across 12 outcome categories, re-derived from primary trials + adversarially verified; (2) 98 more popular supplements by type (mushrooms, herbs, nootropics, mood, metabolic, weight-loss, vitamins/minerals, wellness); (3) 25 beverages (teas, coffee, cocoa, functional drinks), distinguishing the brewed drink from the extract/capsule form; (4) best-form bioavailability for all 244. Seven checks applied to every grade: funding-source subgroup, outlier leverage, effect-size vs MCID, trial vs retail dose, population transfer, dose–response direction, regulatory advisories.

Grades measure evidence quality, not personal fit — several are conditional on a deficiency (iron, B12, vitamin D, omega-3 status) or a specific complaint. Supplement potency and purity are loosely regulated. Talk to a clinician about your labs, conditions and medications before starting anything, especially where the **Watch** line flags an interaction (e.g. St John's Wort induces CYP3A4; ginkgo/ginger/fish-oil and bleeding; yohimbine and cardiovascular risk).
