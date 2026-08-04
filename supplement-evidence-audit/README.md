# Supplement Evidence Audit

*A decision-grade map of the consumer supplement market, organized by the outcome you care about and graded on how well each claim survives **high-quality, industry-independent human trials**. Compiled 2026-08-04.*

**121 compounds · 12 outcome categories · graded 1–5 on evidence quality, not popularity.** Built by a 67-agent adversarial research workflow: one skeptical researcher per category re-derived every grade from primary trials, then an independent reviewer was told to *refute* every grade that scored ≥4, looked statistically compromised, or moved ≥1 point from the prior pass. Seven mandatory bias checks were applied to every compound — funding-source subgroup, outlier leverage, effect-size vs MCID, trial dose vs retail dose, population transfer, dose–response direction, and regulatory advisories.

**Companion files:** [`full-audit.md`](full-audit.md) — the complete per-compound dossiers with trial counts, effect sizes + CIs, doses, populations, funding splits and primary-source citations (the *reasoning attached*). [`data.json`](data.json) — the machine-readable dataset, so the decision can be re-derived when new trials land.

> **Not medical advice.** Grades measure the *quality and independence of the evidence*, not whether a compound will work for you specifically. Product links are Amazon **search** URLs chosen for ingredient form and dose, not endorsements — verify the per-serving active dose before buying.

---

## The finding, in one paragraph

Of 121 compounds, **8 score ≥4 and only five are distinct molecules** — creatine, caffeine, whey/protein, psyllium fibre, and iron (the last only if you're deficient). **75 sit at 2–2.5**: a real mechanism, a plausible-looking meta-analysis, and an effect that either doesn't clear the minimum clinically important difference, depends on industry funding or a single outlier trial, or evaporates the moment you leave the deficient/diseased population it was studied in. That 2–2.5 band is exactly where most supplement money is spent. The pattern from the first pass held under deeper scrutiny and got sharper: **the only unconditional 5 is creatine for muscle/strength; every other high grade is either conditional on correcting a deficiency or bounded to one narrow, specific job.** The whole longevity aisle (NAD boosters, senolytics) tops out at 2.5 — not one compound has a human *outcome*, only biomarkers.

Score distribution: **≥4:** 8 · **3–3.5:** 21 · **2–2.5:** 75 · **<2:** 17.

## What actually earns a place (the short list)

**Tier A — worth buying, evidence is real (score ≥4):**
- **Creatine monohydrate** (5) — Buy. The single best-evidenced sports supplement. Large, mostly independent RCT base shows a real, clinically meaningful add-on to resistance training. Cheap,…
- **Caffeine** (4.5) — This is the one 'energy' agent that actually works. Large independent literature: reliable, dose-related reduction in fatigue and improvement in alertness, vig… — acute alertness/performance; you already get this from matcha
- **Whey / protein powder** (4.5) — Buy only if you are not already hitting your protein target from food. It is a convenient food, not a magic compound - the benefit vanishes once total intake r…
- **Iron (oral ferrous salts, for fatigue/energy)** (4) — Buy ONLY if serum ferritin is low. In iron-deficient menstruating women (ferritin <50 ug/L, no anemia) oral iron produces a real, modest reduction in fatigue.… — *only if ferritin is low*
- **Psyllium husk (ispaghula)** (4) — Buy — the strongest evidence in the category. Cheap, independent, guideline-endorsed soluble/gel-forming fiber for IBS global symptoms and for chronic constipa…

**Tier B — worth it only for a specific, named problem (score 3–3.5):** melatonin *for circadian problems, not insomnia*; *S. boulardii* and PHGG/psyllium for specific gut complaints; zinc **acetate/gluconate lozenges** at cold onset; nicotinamide 500 mg BID *for high skin-cancer risk*; Polypodium (Fernblock) as a sunscreen adjunct; beta-alanine for 1–4 min high-intensity efforts; collagen+vitamin C **pre-load** *layered on a tendon-loading program*; curcumin (Meriva/BCM-95) for knee OA pain; bacopa (12 weeks) for attention; vitamin D **for strength only if deficient**; calcium+D together for fracture risk. See the ranked table for the exact conditions.

**Everything else (the 2s and below) — don't buy.** A short shopping list is the successful outcome here.

---

## For you specifically

Section 5 of the brief (age/sex, training, diet, labs, medications) was left blank, so most personal grades stay conditional — the [conditional list](#deliverable-4--needs-a-blood-test-before-it-applies-to-you) below names exactly which numbers would resolve them. Three things I *can* say from what you gave me:

- **Your matcha already supplies caffeine + L-theanine together** — the best-in-class acute-focus intervention (graded 3.5 after adversarial trimming). Be honest about the ratio, though: a serving of matcha delivers roughly 40–70 mg caffeine but only ~10–20 mg L-theanine — a *lower* theanine:caffeine ratio than the ~2:1 (≈200 mg theanine : 100 mg caffeine) used in the positive trials. So matcha is a gentler, partial version of the stack, not a full substitute for the dosed ratio — but you're already getting both ingredients (plus EGCG), so don't bolt a separate caffeine product on top; watch total daily caffeine instead.
- **Your creatine (capsules): check the serving count.** Creatine is your single best-evidenced supplement — **5/5 for muscle/strength**, 4/5 for memory, and higher still if you're vegetarian or sleep-deprived. But the effect needs **3–5 g/day**, and capsules are typically ~0.75–1 g each, so a '2-capsule' serving can leave you at half the trial dose. Count the grams; powder (Creapure, NSF-certified) is far more dose- and cost-efficient.
- **Patellar / knee health is the cleanest "not a supplement" case in this whole audit.** For patellar tendinopathy the treatment with actual evidence is **heavy-slow resistance loading** (or an eccentric-decline protocol) — progressive, months-long. Collagen + vitamin C taken 30–60 min pre-load is at best a *marginal adjunct on top of the loading program* (trials used 15 g collagen; retail is usually 5–10 g), and does approximately nothing without the training. If the issue is knee **joint/cartilage** (OA) rather than tendon, glucosamine/chondroitin/MSM are 2–2.5 and mostly fail to clear the pain-scale MCID; curcumin (Meriva/BCM-95, 3/5) is the one with a real signal. Load first, supplement a distant second.

---

## Three structural traps (why the market clusters at 2)

The seven checks kept flagging the same three failure modes. They map directly onto the three lists below.

1. **The dose gap** — the compound may work at the trial dose, but the product on the shelf is dosed below it. This is the difference between an effect and a placebo, and it caught **41 compounds**. (Deliverable 2.)
2. **Compromised literature** — the grade rests on industry-funded trials or one outlier study; split by funding or drop the outlier and the effect thins or vanishes. **40 compounds**. (Deliverable 3.)
3. **Population transfer** — the benefit is real in a deficient, older, or diseased population and does not transfer to a healthy adult. This is why so many grades are *conditional on a blood test*. (Deliverable 4.)

---

## Deliverable 1 — the single ranked table (all 121)

Sorted by score, then category. **Flags:** `dose-gap` = typical retail active dose is below the trial dose · `compromised` = grade depends on a funding-source or outlier artifact · `moved≥1` = re-derived score moved ≥1 point from the prior pass. Doses are trimmed here; full figures and CIs are in [`full-audit.md`](full-audit.md). Buy links shown for scores ≥3 only.

| # | Compound | Cat | Score | Conf | Trial dose | Retail (active) | Flags | Buy (search) |
|---|---|---|:--:|:--:|---|---|---|---|
| 1 | Creatine monohydrate | Muscle | **5** | H | 3-5 g/day maintenance (optional 20 g/day… | 5 g monohydrate per serving - matches tri… | — | [Thorne Thorne Creatine](https://www.amazon.com/s?k=Thorne+Creatine+NSF+Certified+for+Sport) |
| 2 | Caffeine | Energy | **4.5** | H | ~40-300 mg (single dose); ~3-6 mg/kg for… | 100-200 mg per coffee/tablet/energy produ… | — | [Nutricost Nutricost Caffeine Pills 200 mg](https://www.amazon.com/s?k=Nutricost+Caffeine+200mg+tablets) |
| 3 | Whey / protein powder | Muscle | **4.5** | H | Supplemental protein such that total inta… | 20-40 g protein per scoop - adequate; not… | — | [Klean Athlete Klean Athlete Klean Isolate Whe…](https://www.amazon.com/s?k=Klean+Athlete+Klean+Isolate+whey+protein) |
| 4 | Creatine monohydrate | Mind | **4** | H | Chronic cognition trials 5-20 g/day; acut… | 3-5 g/day creatine monohydrate (fully act… | moved≥1 | [Thorne Thorne Creatine](https://www.amazon.com/s?k=Thorne+Creatine+NSF+Certified+for+Sport) |
| 5 | Caffeine (alone) | Focus | **4** | H | Typically 40-300 mg (commonly 75-200 mg)… | Retail caffeine/energy products 50-200 mg… | — | [Nutricost Nutricost Caffeine Pills 200 mg](https://www.amazon.com/s?k=Nutricost+Caffeine+200mg+tablets) |
| 6 | Iron (oral ferrous salts, for fatigue/e… | Energy | **4** | H | 80 mg elemental iron/day (ferrous sulfate… | Ferrous sulfate 325 mg = ~65 mg elemental… | — | [Nature Made Nature Made Iron 65 mg (from Ferr…](https://www.amazon.com/s?k=Nature+Made+Iron+65+mg+ferrous+sulfate+tablets) ⚠under-dosed |
| 7 | Psyllium husk (ispaghula) | Gut | **4** | H | ≥10 g/day psyllium for ≥4 weeks (optimal)… | ~3.4-5 g psyllium per single serving (e.g… | dose-gap | [NOW Foods NOW Foods Psyllium Husk Powder](https://www.amazon.com/s?k=NOW+Foods+psyllium+husk+powder) ⚠under-dosed |
| 8 | Caffeine | Muscle | **4** | H | 3-6 mg/kg ~60 min pre-exercise (jump bene… | Pre-workouts/tablets 150-300 mg (~2-4 mg/… | — | [Nutricost Nutricost Caffeine Pills 200 mg](https://www.amazon.com/s?k=Nutricost+Caffeine+200mg+tablets) |
| 9 | Caffeine + L-theanine | Focus | **3.5** | H | Meta-analysed combos: median L-theanine 8… | Typical retail focus stacks deliver ~100-… | — | [Nutricost Nutricost Caffeine Pills 200 mg](https://www.amazon.com/s?k=Nutricost+Caffeine+200mg+tablets) |
| 10 | Creatine monohydrate (for 'energy'/anti… | Energy | **3.5** | H | 3-5 g/day maintenance (20 g/day loading);… | 5 g/day (standard scoop) - matches muscle… | dose-gap | [Thorne Thorne Creatine](https://www.amazon.com/s?k=Thorne+Creatine+NSF+Certified+for+Sport) |
| 11 | Nicotinamide (niacinamide, oral vitamin… | Skin | **3.5** | H | 500 mg twice daily = 1000 mg/day for 12 m… | Nicotinamide/niacinamide capsules commonl… | dose-gap | [NOW Foods NOW Foods Niacinamide (Vitamin B-3)…](https://www.amazon.com/s?k=NOW+Foods+Niacinamide+500+mg+capsules) ⚠under-dosed |
| 12 | Collagen / gelatin + vitamin C, dosed 3… | Tendon | **3.5** | M | 15-30 g/day hydrolyzed collagen peptides… | Typically 2.5-10 g collagen peptides per… | dose-gap | [Momentous Momentous Collagen Peptides (Tendon…](https://www.amazon.com/s?k=Momentous+Collagen+Peptides+vitamin+C) |
| 13 | Melatonin (dose & timing) | Sleep | **3.5** | H | 0.5-5 mg; phase-shift work uses 0.5 mg; i… | 3-10 mg immediate-release (typically ABOV… | — | [Life Extension Life Extension Melatonin 500 m…](https://www.amazon.com/s?k=Life+Extension+Melatonin+500+mcg) |
| 14 | Saccharomyces boulardii (CNCM I-745) | Gut | **3.5** | H | 250-500 mg BID (5-10 billion CFU/day) | 250-500 mg (~5-10 billion CFU) per capsul… | — | [Florastor (Biocodex) Florastor Daily Probioti…](https://www.amazon.com/s?k=Florastor+daily+probiotic+250mg+Saccharomyces+boulardii) |
| 15 | Beta-alanine | Muscle | **3.5** | H | 4-6 g/day for 2-4+ weeks (cumulative load… | 3.2-6.4 g/day standalone is adequate, but… | dose-gap | [NOW Sports (NOW Foods) NOW Sports Beta-Alanin…](https://www.amazon.com/s?k=NOW+Sports+Beta-Alanine+CarnoSyn+powder) ⚠under-dosed |
| 16 | Essential amino acids (EAA) | Muscle | **3.5** | M | ~10-15 g EAA with ~2-3 g leucine per dose. | ~5-10 g EAA per serving - often at or sli… | — | [Thorne Thorne Amino Complex](https://www.amazon.com/s?k=Thorne+Amino+Complex) ⚠under-dosed |
| 17 | B-vitamins (B12/folate/B6, homocysteine… | Mind | **3** | M | Folic acid 0.8 mg + B12 0.5 mg + B6 20 mg… | Comparable B-complex doses widely availab… | — | [Jarrow Formulas Jarrow Formulas B-Right](https://www.amazon.com/s?k=Jarrow+Formulas+B-Right) ⚠under-dosed |
| 18 | Bacopa monnieri | Mind | **3** | M | 300-450 mg/day standardized extract (~55%… | 300-320 mg standardized extract (matches… | — | [Toniiq Toniiq Bacopa Monnieri (45% Bacosides)](https://www.amazon.com/s?k=Toniiq+Bacopa+Monnieri+45%25+bacosides) |
| 19 | Omega-3 DHA (fish/algal oil) | Mind | **3** | H | VITAL 1 g/day fish oil (840 mg EPA+DHA);… | ~200-400 mg DHA per softgel (algal DHA ~4… | dose-gap | [Nordic Naturals Nordic Naturals Ultimate Omega](https://www.amazon.com/s?k=Nordic+Naturals+Ultimate+Omega+1280mg) |
| 20 | Polypodium leucotomos extract (Fernbloc… | Skin | **3** | M | 240 mg once or twice daily (240-480 mg/da… | Heliocare and equivalents are 240 mg caps… | — | [Heliocare (Cantabria Labs/Ferndale) Heliocare…](https://www.amazon.com/s?k=Heliocare+Fernblock+240+mg+60+capsules) |
| 21 | Calcium + vitamin D (combined) | Bones | **3** | M | 1000-1200 mg elemental calcium + 400-800… | 500-600 mg elemental calcium per pill (of… | — | [Nature Made Nature Made Calcium 600 mg with V…](https://www.amazon.com/s?k=Nature+Made+Calcium+600+mg+with+Vitamin+D3+tablets) ⚠under-dosed |
| 22 | Curcumin / Curcuma longa (turmeric) ext… | Joint | **3** | M | Standardized curcuminoids ~1000-1500 mg/d… | Generic turmeric capsules/powder deliver… | dose-gap | [Thorne Thorne Curcumin Phytosome (Meriva)](https://www.amazon.com/s?k=Thorne+Curcumin+Phytosome+Meriva) |
| 23 | L-tryptophan | Sleep | **3** | M | >=1 g at bedtime (older SOL work used 1-4… | 500 mg per capsule typical; many users ta… | dose-gap | [NOW Foods NOW Foods L-Tryptophan 1000 mg (dou…](https://www.amazon.com/s?k=NOW+Foods+L-Tryptophan+1000+mg+tablets) |
| 24 | Probiotics for URTI prevention | Immune | **3** | M | Strain-specific, typically 1e9-1e10 CFU/d… | CFU and strain vary enormously; many prod… | — | [Culturelle Culturelle Daily Probiotic (Digest…](https://www.amazon.com/s?k=Culturelle+Daily+Probiotic+Lactobacillus+rhamnosus+GG) |
| 25 | Zinc (acute cold lozenges vs prophylaxi… | Immune | **3** | M | 80-207 mg/day ELEMENTAL zinc as acetate/g… | Lozenges commonly 5-23 mg elemental per l… | dose-gap | [Life Extension Life Extension Zinc Lozenges (…](https://www.amazon.com/s?k=Life+Extension+Zinc+Acetate+Lozenges) ⚠under-dosed |
| 26 | L-glutamine (post-infectious IBS-D) | Gut | **3** | L | 5 g three times daily = 15 g/day for 8 we… | ~5 g per serving (typical retail dosing i… | dose-gap, compromised | [Thorne Thorne L-Glutamine Powder](https://www.amazon.com/s?k=Thorne+L-Glutamine+powder+NSF+Certified+for+Sport) ⚠under-dosed |
| 27 | Partially hydrolyzed guar gum (PHGG) | Gut | **3** | L | 5-10 g/day | ~5-6 g per serving (e.g. Sunfiber); often… | dose-gap | [Tomorrow's Nutrition (Sunfiber, Taiyo) Tomorr…](https://www.amazon.com/s?k=Tomorrow%27s+Nutrition+Sunfiber+PHGG+prebiotic+fiber+powder) |
| 28 | Peppermint oil (enteric/gastro-resistan… | Gut | **3** | M | 180-225 mg enteric/gastro-resistant peppe… | ~180-225 mg peppermint oil per enteric-co… | compromised | [Nature's Way Nature's Way Pepogest, Peppermin…](https://www.amazon.com/s?k=Nature%27s+Way+Pepogest+peppermint+oil+enteric+coated) |
| 29 | Vitamin D (strength in deficiency) | Muscle | **3** | H | Repletion dosing ~1000-2000 IU/day (or eq… | 1000-2000 IU adequate; 5000-10000 IU prod… | — | [Klean Athlete Klean Athlete Klean D3](https://www.amazon.com/s?k=Klean+Athlete+Klean+D3+2000) |
| 30 | L-Tyrosine | Focus | **2.5** | M | 100-150 mg/kg single dose (~7-12 g for a… | 500 mg-1 g per serving of L-tyrosine - ro… | dose-gap | — |
| 31 | L-theanine (alone) | Focus | **2.5** | M | 50-500 mg acute; the one significant atte… | Typical retail 100-200 mg - below the 400… | dose-gap | — |
| 32 | Rhodiola rosea | Focus | **2.5** | L | Commonly 200-576 mg/day of standardized e… | 200-500 mg standardized extract - broadly… | compromised | — |
| 33 | Astaxanthin (oral, Haematococcus pluvia… | Skin | **2.5** | L | 2-12 mg/day (most 4-9 mg/day) | Retail astaxanthin 4-12 mg/day — matches… | — | — |
| 34 | Oral hyaluronic acid (sodium hyaluronat… | Skin | **2.5** | L | 120 mg/day (range 120-240 mg/day), variou… | Retail oral HA commonly 100-200 mg/day —… | compromised | — |
| 35 | Vitamin K2 (MK-7) | Bones | **2.5** | M | MK-7 180 mcg/day (Knapen); fracture-signa… | MK-7 ~90-180 mcg/day | dose-gap | — |
| 36 | Avocado-soybean unsaponifiables (ASU) | Joint | **2.5** | L | 300 mg/day Piascledine (pharmaceutical AS… | US retail ASU products are uncommon and o… | dose-gap, compromised | — |
| 37 | Boswellia serrata extract (AKBA-standar… | Joint | **2.5** | L | 5-Loxin 100-250 mg/day (30% AKBA) or Afla… | Generic Boswellia 300-500 mg capsules are… | dose-gap, compromised | — |
| 38 | MSM (methylsulfonylmethane) | Joint | **2.5** | L | 3-6 g/day (Kim 1.125 g x3; Debbi 3 g x2 =… | Retail commonly 1-2 g/day (often bundled… | dose-gap | — |
| 39 | UC-II (undenatured type II collagen) | Joint | **2.5** | M | 40 mg/day UC-II (delivering ~10 mg undena… | 40 mg/day UC-II (matches trial dose); dos… | compromised | — |
| 40 | Ashwagandha (KSM-66, Withania somnifera) | Sleep | **2.5** | M | 300-600 mg/day root extract (KSM-66), 6-1… | 300-600 mg KSM-66 - retail matches trial… | compromised | — |
| 41 | Glycine | Sleep | **2.5** | L | 3 g before bedtime | 3 g (bulk glycine or sleep blends) - reta… | compromised | — |
| 42 | L-theanine | Sleep | **2.5** | M | 200-450 mg/day | 100-200 mg (Suntheanine) - broadly matche… | — | — |
| 43 | Lavender oil - Silexan (Lavandula angus… | Sleep | **2.5** | M | 80 mg/day Silexan (single standardized ca… | 80 mg Silexan (CalmAid/Lasea) - retail ma… | compromised | — |
| 44 | Magnesium glycinate (bisglycinate) | Sleep | **2.5** | M | 500 mg elemental Mg/day (Abbasi 2012, as… | ~90-100 mg elemental Mg (a '500 mg magnes… | dose-gap | — |
| 45 | Montmorency tart cherry (Prunus cerasus) | Sleep | **2.5** | L | 2 x 30 mL Montmorency concentrate/day (~… | Gummies/capsules and single small juice s… | dose-gap, compromised | — |
| 46 | Andrographis paniculata | Immune | **2.5** | M | ~60-200 mg/day andrographolides (standard… | Extracts standardized to andrographolides… | — | — |
| 47 | Beta-glucans (yeast 1,3/1,6, Wellmune) | Immune | **2.5** | M | 250 mg/day Wellmune (yeast beta-1,3/1,6-g… | 250-500 mg/day — matches or exceeds trial… | compromised | — |
| 48 | Bovine colostrum | Immune | **2.5** | L | 20-60 g/day bovine colostrum (commonly 20… | Typically 2-10 g/day capsules or scoops —… | dose-gap | — |
| 49 | N-acetylcysteine (NAC) | Immune | **2.5** | M | 600 mg twice daily (1200 mg/day) for 6 mo… | 600-1200 mg/day capsules — matches trial | — | — |
| 50 | Vitamin C (regular prophylaxis and cold… | Immune | **2.5** | H | >=200 mg/day regular supplementation (man… | 500-1000 mg/day ascorbic acid — meets or… | — | — |
| 51 | Vitamin D (respiratory infection preven… | Immune | **2.5** | H | Daily 400-4000 IU (10-100 mcg); daily/wee… | 1000-2000 IU (25-50 mcg) cholecalciferol… | — | — |
| 52 | Lactobacillus rhamnosus GG (LGG) | Gut | **2.5** | M | 1×10^10 CFU BID (2×10^10 CFU/day) | 10-20 billion CFU/day (matches trial dose) | compromised | — |
| 53 | Multi-strain probiotics (IBS / general… | Gut | **2.5** | L | Highly variable (1×10^9 to 5×10^10+ CFU/d… | 1-50 billion CFU/day, product-dependent;… | compromised | — |
| 54 | Zinc-carnosine (polaprezinc) | Gut | **2.5** | L | 75 mg/day polaprezinc (37.5 mg BID; deliv… | ~75 mg zinc-carnosine chelate (~16 mg ele… | — | — |
| 55 | Betaine anhydrous | Muscle | **2.5** | L | 2.5 g/day for 1+ weeks. | ~2.5 g/day - matches trial dose. | compromised | — |
| 56 | Citrulline malate | Muscle | **2.5** | M | 6-8 g citrulline malate (~3.5-4.5 g L-cit… | 6-8 g standalone is on-dose, but many pre… | dose-gap | — |
| 57 | GlyNAC (glycine + N-acetylcysteine) | Longevity | **2.5** | M | Glycine + NAC dosed to body weight (glyci… | Retail GlyNAC blends commonly deliver wel… | dose-gap, compromised | — |
| 58 | NMN (nicotinamide mononucleotide) | Longevity | **2.5** | M | 150-1200 mg/day (most 250-900 mg) | 250-1000 mg/day (retail matches trial ran… | — | — |
| 59 | NR (nicotinamide riboside) | Longevity | **2.5** | M | 500-1000 mg/day (safety up to 3000 mg/day) | 250-500 mg/day (typically below the 1000… | dose-gap | — |
| 60 | Rapamycin / sirolimus (drug - noted) | Longevity | **2.5** | M | 5 or 10 mg compounded weekly (intermitten… | n/a (prescription drug; 'longevity' dosin… | dose-gap | — |
| 61 | Urolithin A (Mitopure) | Longevity | **2.5** | M | 500-1000 mg/day x4 months | 500-1000 mg/day (Mitopure matches trial d… | compromised | — |
| 62 | Alpha-GPC (choline alphoscerate) | Mind | **2** | M | 1200 mg/day (400 mg three times daily) in… | 300-600 mg/day (below the 1200 mg trial d… | dose-gap | — |
| 63 | Citicoline (CDP-choline / Cognizin) | Mind | **2** | M | 500 mg/day (Nakazaki, positive) vs 1 g/da… | Cognizin 250-500 mg/day (250 mg products… | compromised | — |
| 64 | Ginkgo biloba (EGb761) | Mind | **2** | H | EGb761 120-240 mg/day (prevention trials… | Commonly 120 mg/day standardized extract… | dose-gap | — |
| 65 | Lion's mane (Hericium erinaceus) | Mind | **2** | M | Mori 3 g/day powder (16 wk); Docherty 1.8… | 500-1000 mg/day, frequently non-standardi… | dose-gap | — |
| 66 | Phosphatidylserine (soy-derived) | Mind | **2** | M | 300-600 mg/day; historical bovine trials… | 100-300 mg/day soy-derived PS (often 100… | dose-gap, compromised | — |
| 67 | Citicoline (CDP-choline) | Focus | **2** | M | 250-500 mg/day for 6-12 weeks. | 250-500 mg (often as Cognizin) - matches… | compromised, moved≥1 | — |
| 68 | Panax ginseng | Focus | **2** | L | 200 mg or 400 mg G115 for 8 days. | Standardized ginseng products commonly 20… | compromised | — |
| 69 | Ashwagandha (Withania somnifera) for en… | Energy | **2** | M | 300 mg twice daily (KSM-66) or 600 mg/day… | 300-600 mg/day standardized extract - mat… | compromised | — |
| 70 | CoQ10 / Ubiquinol | Energy | **2** | M | 100-600 mg/day (fatigue and statin trials) | 100-200 mg/day (ubiquinone); ubiquinol 10… | dose-gap, compromised | — |
| 71 | Cordyceps (Cs-4 / C. sinensis / C. mili… | Energy | **2** | L | Cs-4 fermentation product 3-4.5 g/day for… | ~1 g/day mushroom/mycelium (often low act… | dose-gap | — |
| 72 | Rhodiola rosea (added - common in 'ener… | Energy | **2** | L | ~200-600 mg/day standardized extract (SHR… | 200-500 mg/day, standardization highly va… | — | — |
| 73 | Collagen peptides (hydrolyzed collagen) | Skin | **2** | H | Skin RCTs used ~2.5-10 g/day hydrolyzed c… | Retail skin collagen 2.5-10 g/day — match… | compromised | — |
| 74 | Calcium alone | Bones | **2** | M | 1000-1200 mg elemental calcium/day | 500-600 mg elemental calcium per pill (ca… | — | — |
| 75 | Collagen peptides (specific bioactive c… | Bones | **2** | L | 5 g specific collagen peptides (FORTIBONE… | Generic collagen powders 5-10 g/day, usua… | compromised | — |
| 76 | Magnesium | Bones | **2** | M | ~300-600 mg elemental Mg/day in the small… | Magnesium glycinate/citrate labelled '400… | dose-gap | — |
| 77 | Curcumin (turmeric extract) | Tendon | **2** | H | Human combination studies ~500-2000 mg/da… | 500-1500 mg turmeric extract per serving,… | — | — |
| 78 | Omega-3 (EPA/DHA) | Tendon | **2** | M | ~1.5-2.5 g/day combined EPA+DHA (Sandford… | Standard fish-oil softgel delivers ~300 m… | dose-gap | — |
| 79 | Chondroitin sulfate | Joint | **2** | H | 800-1200 mg/day pharmaceutical-grade chon… | US OTC typically 400-1200 mg/day but puri… | dose-gap, compromised | — |
| 80 | Glucosamine (sulfate or HCl) | Joint | **2** | H | 1500 mg/day glucosamine sulfate (Rotta cr… | 1500 mg/day glucosamine (HCl or sulfate);… | compromised | — |
| 81 | Glucosamine + chondroitin combination | Joint | **2** | H | 1500 mg glucosamine + 1200 mg chondroitin… | 1500 mg + 1200 mg/day, matching trial dos… | compromised | — |
| 82 | 5-HTP (5-hydroxytryptophan) | Sleep | **2** | L | 100-300 mg/day (older-adult trial ~100 mg) | 50-100 mg - often at/below the lower tria… | dose-gap | — |
| 83 | Apigenin / Chamomile (Matricaria chamom… | Sleep | **2** | M | 270-540 mg standardized extract/day, or ~… | 'Apigenin 50 mg' pills or chamomile tea (… | compromised | — |
| 84 | GABA (gamma-aminobutyric acid, oral) | Sleep | **2** | M | 100-300 mg (PharmaGABA) | 100-750 mg - retail meets or exceeds tria… | compromised | — |
| 85 | Kava (Piper methysticum) | Sleep | **2** | H | Standardized to ~70-210 mg kavalactones/d… | Variable kavalactone content; often poorl… | — | — |
| 86 | Magnesium L-threonate (Magtein) | Sleep | **2** | M | 2 g magnesium L-threonate/day (~144 mg el… | ~2 g L-threonate (~144 mg elemental) - re… | compromised | — |
| 87 | Passionflower (Passiflora incarnata) | Sleep | **2** | L | 2 g passionflower as tea | Capsule extracts of variable strength; of… | — | — |
| 88 | Valerian (Valeriana officinalis) | Sleep | **2** | M | 300-900 mg extract at night | 300-600 mg extract (variable valerenic-ac… | compromised | — |
| 89 | Echinacea | Immune | **2** | H | Highly variable — different species (purp… | Wildly variable and often not matched to… | — | — |
| 90 | Elderberry (Sambucus nigra) | Immune | **2** | M | Standardized extract (BerryPharma) ~600-1… | Gummies/syrups frequently deliver far les… | dose-gap, compromised | — |
| 91 | Ginseng (Panax quinquefolius, COLD-fX/C… | Immune | **2** | L | CVT-E002 (COLD-fX) 400 mg/day standardize… | Proprietary product at 400 mg/day; generi… | compromised | — |
| 92 | Pelargonium sidoides (EPs 7630, Umckalo… | Immune | **2** | L | EPs 7630 root extract, ~30 drops 3x/day o… | Standardized EPs 7630 products at label d… | compromised | — |
| 93 | Butyrate / tributyrin (oral) | Gut | **2** | M | Oral sodium butyrate 300-1800 mg/day (som… | Sodium/calcium butyrate ~500-600 mg/day —… | — | — |
| 94 | Digestive enzymes (lactase, alpha-galac… | Gut | **2** | M | Enzyme-specific (e.g. alpha-galactosidase… | Highly variable proprietary blends; units… | — | — |
| 95 | Prebiotics (inulin, GOS/FOS, inulin-typ… | Gut | **2** | M | Varies; ≤6 g/day better tolerated, >6 g i… | Inulin/FOS ~3-5 g per serving (users ofte… | — | — |
| 96 | Synbiotics (probiotic + prebiotic combi… | Gut | **2** | M | Product-specific probiotic CFU + prebioti… | Variable proprietary blends; CFU and preb… | — | — |
| 97 | Ashwagandha (Withania somnifera) | Muscle | **2** | M | 300 mg root extract twice daily (KSM-66),… | 600 mg KSM-66 - matches trial dose (dose… | compromised | — |
| 98 | HMB (beta-hydroxy-beta-methylbutyrate) | Muscle | **2** | M | 3 g/day (as Ca-HMB or HMB-free acid). | 3 g/day - matches trial dose; underdosing… | compromised | — |
| 99 | Fisetin (senolytic) | Longevity | **2** | M | 20 mg/kg/day x2 days, intermittent pulsed… | 100-500 mg/day taken continuously (differ… | dose-gap | — |
| 100 | Metformin (drug - noted) | Longevity | **2** | M | 1500-2000 mg/day | n/a (prescription drug) | — | — |
| 101 | Resveratrol | Longevity | **2** | H | 150 mg - 1000+ mg/day (some to 5 g) | 250-500 mg/day (trans-resveratrol) | — | — |
| 102 | Spermidine | Longevity | **2** | H | 0.9 mg spermidine/day (wheat-germ extract) | 1-10 mg/day (retail often higher than the… | — | — |
| 103 | Sulforaphane (broccoli sprout extract) | Longevity | **2** | M | ~50-150 umol sulforaphane/day (broccoli s… | Variable and often poorly standardised (g… | — | — |
| 104 | Taurine | Longevity | **2** | M | Mouse: ~1 g/kg/day; human aging trials pe… | 500-2000 mg/day (below the allometric mou… | dose-gap | — |
| 105 | Huperzine A | Mind | **1.5** | M | 300-500 mcg/day for 8-24 weeks | 50-200 mcg/day (typically below the 300-5… | dose-gap, compromised | — |
| 106 | NR / NMN (nicotinamide riboside / monon… | Mind | **1.5** | H | NMN 250-1000 mg/day; NR 250-1000 mg/day | NMN 250-500 mg/day; NR ~300 mg/day (doses… | — | — |
| 107 | Boron | Bones | **1.5** | M | ~3 mg/day in balance studies | 3-6 mg/day | — | — |
| 108 | Vitamin D alone | Bones | **1.5** | H | VITAL 2000 IU/day; D-Health 60,000 IU/mon… | 1000-5000 IU/day common; many products 50… | — | — |
| 109 | Vitamin C (alone, as a standalone tendo… | Tendon | **1.5** | M | Rotator cuff preliminary study used supra… | 500-1000 mg ascorbic acid per tablet - ro… | — | — |
| 110 | Garlic / allicin | Immune | **1.5** | M | Allicin-standardized supplement ~180 mg a… | Aged garlic/garlic powder capsules with h… | dose-gap, compromised | — |
| 111 | Quercetin | Immune | **1.5** | M | 1000 mg/day (the dose with the subgroup s… | Typically 500 mg/day — below the 1000 mg… | dose-gap | — |
| 112 | BCAAs (branched-chain amino acids) | Muscle | **1.5** | H | ~5-10 g BCAA in acute trials. | 5-7 g per serving (2:1:1) - dose is not t… | — | — |
| 113 | Calcium alpha-ketoglutarate (CaAKG / Re… | Longevity | **1.5** | H | 2 g/day CaAKG (2x1 g timed-release) + vit… | 1-2 g/day CaAKG (matches the reported dos… | compromised | — |
| 114 | Pterostilbene | Longevity | **1.5** | M | 125-250 mg/day (monotherapy trial); ~100-… | 50-250 mg/day (often paired with NMN/NR) | — | — |
| 115 | Quercetin (senolytic) | Longevity | **1.5** | H | Senolytic: 1000 mg quercetin x3 days WITH… | 500-1000 mg/day quercetin (matches BP-tri… | — | — |
| 116 | Adaptogen blends (proprietary multi-her… | Energy | **1** | H | n/a - the finished multi-herb products ar… | Proprietary blend totals often 300-1000 m… | dose-gap | — |
| 117 | Vitamin B12 (cyanocobalamin/methylcobal… | Energy | **1** | H | Deficiency correction: 1000 ug oral/day o… | 1000 ug cyanocobalamin typical (~40,000%… | — | — |
| 118 | Biotin (vitamin B7) | Skin | **1** | H | Case/series doses vary (e.g., 2.5 mg/day… | Retail biotin 5,000-10,000 mcg (5-10 mg)… | — | — |
| 119 | Strontium (retail strontium citrate) | Bones | **1** | H | Ranelate 2 g/day (SOTI/TROPOS). Retail ci… | ~340-680 mg elemental strontium/day (citr… | — | — |
| 120 | Slippery elm / marshmallow root / demul… | Gut | **1** | H | Not established | Variable powders/capsules; no defined act… | — | — |
| 121 | Testosterone boosters (Tribulus, D-aspa… | Muscle | **1** | H | Varies (e.g. D-aspartic acid 3-6 g/day; T… | Proprietary blends, frequently underdosed… | — | — |

---

## Deliverable 2 — "you'd be buying a placebo"

Compounds scoring ≥2.5 where the **typical retail active dose is below the dose used in the trials that justify the claim** — so the shelf product can fail even though the compound has a real signal. (41 compounds in total carry the dose-gap flag; these 24 are the ones where it changes the decision. Full dose-gap list is in `data.json`.)

| Compound | Cat | Score | Trial dose | Typical retail (active) | The gap |
|---|:--:|:--:|---|---|---|
| Psyllium husk (ispaghula) | Gut | 4 | ≥10 g/day psyllium for ≥4 weeks (optima… | ~3.4-5 g psyllium per single serving (e… | Metamucil-type single serving ~3.4 g; the IBS/constipation trials need ≥10 g/day (2–3 servings). |
| Beta-alanine | Muscle | 3.5 | 4-6 g/day for 2-4+ weeks (cumulative lo… | 3.2-6.4 g/day standalone is adequate, b… | Needs 3.2–6.4 g/day; pre-workout blends split ~1.6–3.2 g, below the loading dose. |
| Collagen / gelatin + vitamin C, dosed 3… | Tendon | 3.5 | 15-30 g/day hydrolyzed collagen peptide… | Typically 2.5-10 g collagen peptides pe… | Trials 15 g; retail collagen 5–10 g — and only works layered on tendon loading. |
| Creatine monohydrate (for 'energy'/anti… | Energy | 3.5 | 3-5 g/day maintenance (20 g/day loading… | 5 g/day (standard scoop) - matches musc… | 5 g/day scoop is on-dose for muscle; flagged only because some cognition/'energy' work used higher acute load… |
| Nicotinamide (niacinamide, oral vitamin… | Skin | 3.5 | 500 mg twice daily = 1000 mg/day for 12… | Nicotinamide/niacinamide capsules commo… | Common 500 mg once-daily products are HALF the 500 mg twice-daily (1000 mg/day) skin-cancer dose. |
| Curcumin / Curcuma longa (turmeric) ext… | Joint | 3 | Standardized curcuminoids ~1000-1500 mg… | Generic turmeric capsules/powder delive… | Needs a phytosome/bioavailable form (Meriva/BCM-95); plain turmeric is negligibly absorbed. |
| L-glutamine (post-infectious IBS-D) | Gut | 3 | 5 g three times daily = 15 g/day for 8… | ~5 g per serving (typical retail dosing… | 5 g/day products are one-third of the 15 g/day (5 g × 3) post-infectious IBS-D trial dose. |
| L-tryptophan | Sleep | 3 | >=1 g at bedtime (older SOL work used 1… | 500 mg per capsule typical; many users… | Sleep trials ~1–4 g; many products under-dose. |
| Omega-3 DHA (fish/algal oil) | Mind | 3 | VITAL 1 g/day fish oil (840 mg EPA+DHA)… | ~200-400 mg DHA per softgel (algal DHA… | '1000 mg fish oil' caps deliver only ~200–300 mg DHA; the (null-ish) memory trials used ~1 g EPA+DHA. |
| Partially hydrolyzed guar gum (PHGG) | Gut | 3 | 5-10 g/day | ~5-6 g per serving (e.g. Sunfiber); oft… | A single 5–6 g serving sits at/below the 5–10 g/day effective range. |
| Zinc (acute cold lozenges vs prophylaxi… | Immune | 3 | 80-207 mg/day ELEMENTAL zinc as acetate… | Lozenges commonly 5-23 mg elemental per… | Trials 75–100 mg/day elemental as acetate/gluconate; most lozenges are 5–23 mg and/or chelated by flavour aci… |
| Avocado-soybean unsaponifiables (ASU) | Joint | 2.5 | 300 mg/day Piascledine (pharmaceutical… | US retail ASU products are uncommon and… | US retail ASU products are uncommon and of variable standardization; typically below the pharmaceutical 300 m… |
| Boswellia serrata extract (AKBA-standar… | Joint | 2.5 | 5-Loxin 100-250 mg/day (30% AKBA) or Af… | Generic Boswellia 300-500 mg capsules a… | Needs standardized AKBA fraction at trial dose. |
| Bovine colostrum | Immune | 2.5 | 20-60 g/day bovine colostrum (commonly… | Typically 2-10 g/day capsules or scoops… | Typically 2-10 g/day capsules or scoops — well below trial doses |
| Citrulline malate | Muscle | 2.5 | 6-8 g citrulline malate (~3.5-4.5 g L-c… | 6-8 g standalone is on-dose, but many p… | 6-8 g standalone is on-dose, but many pre-workout blends contain only 1-3 g - below trial dose. |
| GlyNAC (glycine + N-acetylcysteine) | Longevity | 2.5 | Glycine + NAC dosed to body weight (gly… | Retail GlyNAC blends commonly deliver w… | Retail GlyNAC blends commonly deliver well below the weight-based grams used by Sekhar (typical products unde… |
| L-Tyrosine | Focus | 2.5 | 100-150 mg/kg single dose (~7-12 g for… | 500 mg-1 g per serving of L-tyrosine -… | 500 mg-1 g per serving of L-tyrosine - roughly 7-20x below the effective per-kg trial dose. |
| L-theanine (alone) | Focus | 2.5 | 50-500 mg acute; the one significant at… | Typical retail 100-200 mg - below the 4… | Typical retail 100-200 mg - below the 400 mg needed for the only positive attention endpoint. |
| MSM (methylsulfonylmethane) | Joint | 2.5 | 3-6 g/day (Kim 1.125 g x3; Debbi 3 g x2… | Retail commonly 1-2 g/day (often bundle… | Trials ~3–6 g/day; many products under 1.5 g. |
| Magnesium glycinate (bisglycinate) | Sleep | 2.5 | 500 mg elemental Mg/day (Abbasi 2012, a… | ~90-100 mg elemental Mg (a '500 mg magn… | '500 mg' label = ~90–100 mg elemental Mg; trials use 300+ mg elemental. |
| Montmorency tart cherry (Prunus cerasus) | Sleep | 2.5 | 2 x 30 mL Montmorency concentrate/day (… | Gummies/capsules and single small juice… | Gummies/capsules and single small juice servings delivering a fraction of the trial anthocyanin/phytomelatoni… |
| NR (nicotinamide riboside) | Longevity | 2.5 | 500-1000 mg/day (safety up to 3000 mg/d… | 250-500 mg/day (typically below the 100… | 250-500 mg/day (typically below the 1000 mg trial dose) |
| Rapamycin / sirolimus (drug - noted) | Longevity | 2.5 | 5 or 10 mg compounded weekly (intermitt… | n/a (prescription drug; 'longevity' dos… | n/a (prescription drug; 'longevity' dosing 5-6 mg/wk is off-label and below immunosuppressive daily dosing) |
| Vitamin K2 (MK-7) | Bones | 2.5 | MK-7 180 mcg/day (Knapen); fracture-sig… | MK-7 ~90-180 mcg/day | MK-7 ~90-180 mcg/day |

**Standout dose traps:** *collagen for tendon* (15 g in trials vs 5–10 g retail, and useless without a loading program), *zinc cold lozenges* (the mg is fine on paper but flavour acids and chelators neutralise the ionic zinc that actually shortens colds), *beta-alanine* buried in split pre-workout servings, and *magnesium glycinate* where a '500 mg' label is ~90 mg of actual magnesium.

---

## Deliverable 3 — "the literature is compromised here"

Compounds scoring ≥2.5 where the grade **depends on a funding-source or outlier artifact** — the effect is carried by industry-funded trials or by a single leveraged study, and an independent-only or outlier-removed reanalysis thins or erases it. (40 compounds carry the flag overall; these 17 are where it materially props up a non-trivial score.)

| Compound | Cat | Score | What's compromised |
|---|:--:|:--:|---|
| L-glutamine (post-infectious IBS-D) | Gut | 3 | Not industry-funded per se, but single-center, single-investigator-group (Verne/Zhou), unreplicated — the grade hinges on one study. · Outlier: Yes — the entire evidence base is one trial with an implausibly large effect; awaits independen… |
| Peppermint oil (enteric/gastro-resistan… | Gut | 3 | Not cleanly split in the meta-analysis, but many older positive trials were small/industry-linked; the independent, government/academic-funded Weerts 2020 trial (4 Dutch hospitals) was null on both co-primary endpoints (abdominal pain resp… |
| Ashwagandha (KSM-66, Withania somnifera) | Sleep | 2.5 | No independent-only pooled estimate exists - the SMD -0.59 is effectively an industry-funded pooled result (Ixoreal supplied material in the key trials). That is the compromise. |
| Avocado-soybean unsaponifiables (ASU) | Joint | 2.5 | Positive symptomatic trials largely manufacturer-sponsored; no clean independent replication of structure modification. · Outlier: Structure-modification claim hinges on secondary subgroup outcomes of one trial. |
| Beta-glucans (yeast 1,3/1,6, Wellmune) | Immune | 2.5 | Effect concentrated in Kerry/Biothera (Wellmune manufacturer)-funded trials; independent replication absent · Outlier: Small trials, sponsor-linked; no single outlier but the whole base is sponsor-driven |
| Betaine anhydrous | Muscle | 2.5 | Not formally split, but betaine is manufactured by ingredient suppliers (e.g. DuPont/Danisco) and several trials are industry-adjacent - contributes to the low confidence. · Outlier: Yes - with CI lower bounds at 0.01-0.04, removing one sm… |
| Boswellia serrata extract (AKBA-standar… | Joint | 2.5 | No funding-split meta-analysis exists because independent trials are nearly absent; virtually all positive data are sponsor-generated. · Outlier: The headline NMA pain effect (-22.4) rests on ONE 38-patient sponsor trial; extreme leverage. |
| GlyNAC (glycine + N-acetylcysteine) | Longevity | 2.5 | Single-lab, conflict-of-interest concern; no independent replication - the favourable grade depends on this unreplicated body of work. |
| Glycine | Sleep | 2.5 | No formal split; the foundational trials are linked to Ajinomoto (glycine manufacturer) - an industry-concentration flag. · Outlier: Whole case rests on 2 small same-group studies. |
| Lactobacillus rhamnosus GG (LGG) | Gut | 2.5 | Positive pooled estimates lean on small, older, often industry-linked/low-quality trials; the two definitive nulls were NIH/independently funded. |
| Lavender oil - Silexan (Lavandula angus… | Sleep | 2.5 | No independent-only pooled estimate; the Silexan program is overwhelmingly Dr. Willmar Schwabe-funded - the main caveat. · Outlier: Consistent across several trials, not one-study-driven, but all from one sponsor.  → adversarial re-check C… |
| Montmorency tart cherry (Prunus cerasus) | Sleep | 2.5 | No formal split; Cherry Marketing Institute / grower funding present in several studies. · Outlier: Losso n=8 +84 min is a classic single-tiny-study outlier that dominates the popular claim. |
| Multi-strain probiotics (IBS / general… | Gut | 2.5 | Substantial manufacturer funding across the positive literature; independent replication is inconsistent. |
| Oral hyaluronic acid (sodium hyaluronat… | Skin | 2.5 | No formal meta subgroup, but the core hydration/wrinkle evidence comes largely from authors employed by Kewpie Corporation (Hyabest ingredient); a 2025 trial was manufacturer-funded (Ritual) with Kewpie supplying HA. Independent confirmati… |
| Rhodiola rosea | Focus | 2.5 | Positive fatigue findings concentrate in SHR-5 (Swedish Herbal Institute) manufacturer-linked trials; independent replication is sparse and inconsistent. |
| UC-II (undenatured type II collagen) | Joint | 2.5 | No independent trial exists to split against. The entire efficacy claim is manufacturer-funded; the one independent pooled reanalysis (2025 NMA) is null-to-worst. |
| Urolithin A (Mitopure) | Longevity | 2.5 | No independent replication exists; every positive result is manufacturer-run. The grade's upside depends entirely on industry-funded data - hence compromised. · Outlier: The favourable functional read-out rests on the single middle-aged tr… |

**The clearest cases:** *citicoline* (the one supportive healthy-adult RCT is industry-funded; EFSA rejected the memory claim — this is a ≥1-point drop, 3→2); *nicotinamide* skin-cancer benefit that leans heavily on the single ONTRAC trial; *lavender/Silexan*, *UC-II*, *elderberry*, *Urolithin A/Mitopure* (every pivotal trial is manufacturer-run, and the older-adult primary endpoints were null); and the *glucosamine/chondroitin* commercial-vs-independent effect-size split.

---

## Deliverable 4 — needs a blood test before it applies to you

These grades are **gated on a measurable personal value** — the score is high only if a specific deficiency or condition is present. With Section 5 blank, these can't be finalised for you until the number exists. This is also the honest answer to "what should *I* actually take": test first.

| To resolve | Test / condition | Compounds it gates | If the answer is… |
|---|---|---|---|
| Iron / energy & fatigue | **Ferritin** (+ CBC, transferrin sat) | Iron | low → iron is a **4–5**; normal → **1**, and iron is pro-oxidant to over-supplement |
| B12 / energy & cognition | **Serum B12** (± MMA, homocysteine) | Vitamin B12; B-complex (homocysteine) | low/elevated Hcy → real benefit; replete → **1** |
| Vitamin D status | **25(OH)D** | Vitamin D (bones, strength, immunity) | deficient → strength/immunity benefit is plausible; replete → mega-trials are **null** for falls/fractures, and 4000–10 000 IU can *lower* BMD |
| Omega-3 status | **Omega-3 index** (± APOE genotype) | Omega-3 DHA (memory) | low status/APOE4 → possible signal; replete → large trials are null |
| Statin use | **On a statin?** | CoQ10 | yes → the only population with a signal; no → **2** |
| Diet pattern | **Vegetarian/vegan?** | Creatine (cognition) | yes → largest cognitive effect (depleted state); omnivore → smaller |
| Menopausal status / sex | **Peri-/post-menopausal?** | Vitamin K2, calcium+D | the bone signals concentrate in women and are near-absent in mixed-sex studies |

Everything else that the workflow tagged 'conditional' is conditional on *how you use it* (timing, an actual cold, a diagnosed IBS subtype, taking fibre with water), not on a lab value — those conditions are in each dossier's **Conditional on** line.

---

## Where the real fix is not a supplement

The brief asked for this to be said plainly. In these cases the effective intervention is named; the supplement is at best an adjunct.

- **Patellar / other tendinopathy →** heavy-slow resistance loading (or eccentric protocol). Collagen+vitamin C pre-load is an adjunct *on top of* loading, nothing without it.
- **Chronic primary insomnia →** CBT-I (the AASM/ACP first-line; the AASM recommends *against* melatonin for it). Melatonin is for **circadian** problems — jet lag, delayed sleep-wake phase, shift work — at a **low** 0.5–1 mg dose timed hours before sleep, not the 5–10 mg hypnotic dose most products sell.
- **Knee osteoarthritis →** exercise therapy and weight management move pain and function more than any joint supplement in this table.
- **Constipation / IBS →** soluble/gel-forming fibre (psyllium, PHGG) and diet — which *is* the top-graded 'supplement' here, so this one's aligned.
- **General low energy without a deficiency →** sleep, training and calories. Adaptogen 'energy' blends are a **1**.
- **Longevity / healthspan →** nothing in the NAD-booster or senolytic aisle has a human outcome; the interventions with outcome data are exercise, not over-nutrition, and sleep. NAD precursors reliably raise NAD — a biomarker, not a result.

---

## The interesting cases: grades that moved ≥1 point

The brief flagged these as the ones worth surfacing rather than silently correcting. Reading the primary trials (not review summaries) moved three grades by a full point — all **downward**, all for the same reason: an industry-funded or population-mismatched base that the summary literature had smoothed over.

- **Creatine (memory) 5 → 4.** The 16-RCT memory meta is real but rests on only ~492 subjects with a modest SMD, and the headline acute effect (sleep-deprivation rescue) used a single ~0.35 g/kg dose (~25 g), not the 3–5 g/day people take. Still a 4, still the best in the category — and still an unconditional **5 for muscle/strength**, where the adversarial reviewer (correctly, for *that* outcome) pushed back to 5.
- **Citicoline (memory) 3 → 2** and **Citicoline (focus) 3 → 2.** The one supportive healthy-adult RCT is industry-funded, wasn't replicated at higher dose, and **EFSA (2024) rejected the memory health claim**. The cholinergic mechanism is real; the independent human outcome isn't there.

Several more moved half a point on the same logic and are worth knowing: **nicotinamide (skin) 4 → 3.5** (single-trial leverage), **caffeine + L-theanine 4 → 3.5** (effect real but small vs MCID), **calcium+D 3.5 → 3**, **vitamin D alone 2 → 1.5**, and **peppermint oil 3.5 → 3** and **lavender/Silexan 3 → 2.5** (the last two failed the adversarial pass outright on outlier/funding grounds). The adversarial reviewer also *raised* two it judged underrated — **UC-II** and **beta-glucans**, both 2 → 2.5.

---

## How this was built, and how to re-derive it

- **Rubric.** 5 = large independent RCTs, consistent, clinically meaningful (would bet on it). 4 = multiple good RCTs, real but modest or narrower than marketed. 3 = real signal but small/short trials or condition-dependent. 2 = positive results concentrated in industry-funded/low-quality studies; mechanism outruns outcome. 1 = marketing, no credible human outcome.
- **Confidence** is reported *separately* from the score — it's how firmly the evidence pins the grade, not how good the compound is. A confident 2 (the evidence clearly shows little) is different from a low-confidence 2.5 (thin data).
- **The adversarial pass** is the point of the method: 50 grades that scored ≥4, looked compromised, or moved ≥1 point were handed to an independent reviewer told to *refute* them. It confirmed most, trimmed six downward — four of them judged to fail scrutiny (citicoline, nicotinamide, lavender, peppermint) and two upheld but shaved half a point (caffeine+L-theanine, caffeine-for-energy) — and nudged two upward that it judged underrated (UC-II, beta-glucans). Where it disagreed with the researcher (notably creatine-for-memory, which it pushed back to 5 by scoring whole-body evidence), both numbers and the reasoning are in the dossier.
- **To re-derive when new trials land:** `data.json` carries every field per compound (effect+CI, doses, funding split, sources). Re-run the seven checks against the new trial and update the score; the dossier tells you which check the grade is currently balanced on.

**Hard caveats.** Product links are Amazon *search* URLs (product pages/ASINs change); confirm the per-serving **active/elemental** dose against the trial dose before buying — several 'adequate' products still need 2+ servings/day to reach it. Supplement potency is loosely regulated (melatonin content has been measured from 83% below to 478% above label). Regulatory advisories were checked (TGA/EMA/FDA/MHRA) but move; the ashwagandha liver signal and the intranasal-zinc anosmia warning are the notable ones here. None of this is medical advice or a substitute for talking to a clinician about your labs and medications.

*Full per-compound reasoning: [`full-audit.md`](full-audit.md). Structured data: [`data.json`](data.json).*
