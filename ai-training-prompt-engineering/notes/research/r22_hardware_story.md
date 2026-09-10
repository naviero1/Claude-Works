# r22 — The hardware story: Moore's law, Nvidia, data centers (researched 2026-09-10)

Powers the NEW Part-1 hardware slide held in PENDING_CHANGES Round 6 (owner: "chip
theory… moores or something law… the role of nvidia… why do we need so many data
centers — introduction only, one slide"). Every fact carries source + as-of date;
UNVERIFIED items quarantined at the end. Deck coordination: Part 1 already cites
AlexNet's 15.3%-vs-26.2% (don't duplicate); Part 2 owns the DeepSeek $589B day (this
slide SETS UP that moment, doesn't repeat it).

## 1. Moore's law, plainly

- Gordon Moore (Fairchild R&D director), Electronics magazine, Apr 19 1965: component
  count on a chip doubles every year; revised 1975 (by then Intel co-founder, at IEEE
  IEDM) to doubling ~every TWO years. Held ~50 years.
  (Original paper: cs.utexas.edu/~fussell/courses/cs352h/papers/moore.pdf ·
  computerhistory.org/siliconengine/moores-law-predicts-the-future-of-integrated-circuits ·
  intel.com virtual-vault Moore's-law page.)
- What it bought: Intel 4004 (1971) = 2,300 transistors → Nvidia Blackwell (announced
  Mar 18 2024) = 208 billion — ~90 million× more on one chip in 53 years.
  (Intel history; nvidianews.nvidia.com Blackwell launch, Mar 2024.)
- Status 2026: SLOWING, NOT DEAD. Intel CEO: slowed to ~a three-year cadence "but it's
  not dead yet" (emsnow.com, 2025/26); imec + MIT CSAIL: physics/cost walls at 2–3nm;
  industry pivots to chiplets, 3D stacking, specialized AI silicon
  (imec-int.com moores-law-dead page; cap.csail.mit.edu death-moores-law).
- Jensen Huang (CES, Jan 7 2025, TechCrunch interview): "Our systems are progressing
  way faster than Moore's Law… we can innovate across the entire stack"; claims AI
  chips 1,000× better than 10 years ago (ATTRIBUTE AS QUOTE — see UNVERIFIED). Huang
  had called Moore's law "dead" in 2022.
- "Huang's law": coined by IEEE Spectrum after Huang's 2018 GTC keynote; popularized
  by WSJ 2020. CONTESTED/part marketing: Epoch AI measured GPU price-performance
  (FLOP/s per $) doubling only ~every 2.5 years 2006–2021
  (epoch.ai/blog/trends-in-gpu-price-performance; ExtremeTech 2020 "an illusion").
  Honest phrasing: "Nvidia claims whole-SYSTEM AI performance outruns Moore's law;
  independent analysts say per-dollar chip gains are slower than the marketing."

## 2. Why GPUs

- One breath: a CPU is a few very smart cores working one task after another; a GPU is
  thousands of simple cores doing the SAME arithmetic simultaneously. Games need
  millions of pixels at once — neural networks need exactly the same thing: giant
  grids of multiply-and-add (matrix math). (Nvidia CUDA programming guide intro.)
- The 2012 moment: AlexNet trained 5–6 days on just TWO consumer gaming cards (Nvidia
  GTX 580, 3GB) and won ImageNet (Krizhevsky/Sutskever/Hinton paper, NeurIPS 2012:
  proceedings.neurips.cc/paper/4824). Two gaming cards beat decades of hand-built AI —
  the hardware punchline behind the error-rate stat already on the era slide.
- CUDA = the moat: introduced 2006 (first public release 2007) — lets anyone program a
  graphics chip for ANY computation. Five-year head start of tools/libraries/trained
  developers before AI needed it; ~20 years on, the software ecosystem more than the
  chips is why competitors struggle. (Nvidia docs; en.wikipedia.org/wiki/CUDA;
  modular.com/blog/democratizing-compute-part-2.)

## 3. Nvidia milestones (all checkable)

- Data center overtakes gaming: quarter ended May 1 2022 ($3.75B vs $3.62B)
  (datacenterdynamics.com; counterpointresearch.com, May 2022).
- Now IS the business: Q2 FY2027 (ended Jul 26 2026, reported Aug 26 2026): revenue
  $96.2B, data center $89.0B ≈ 92% (nvidianews Q2-FY2027 release; SEC 8-K).
- Market-cap strip ("first reached"): $1T May 30 2023 · $2T Feb 23 2024 · $3T Jun 5
  2024 · $4T Jul 9 2025 (first company ever — CNBC) · $5T Oct 29 2025 (first close
  above, $5.03T — TechCrunch/CNBC) · ~$5.56T as of Sep 4 2026, world's most valuable
  company (Apple ~$4.7T) (stockanalysis.com/stocks/nvda/market-cap; fool.com research).
  Honesty note: $1T/$2T/$4T are intraday touches, $5T a close — "first reached" covers
  all consistently.
- Cadence: Hopper/H100 (2022) → Blackwell (GTC Mar 18 2024) → Blackwell Ultra (2025) →
  Vera Rubin (GTC Mar 16 2026; full production per Nvidia May 31 2026; systems H2
  2026). Two-year → ANNUAL architecture cadence; Huang cites ~$1T Blackwell+Rubin
  orders through 2027 (CNBC GTC-2026; nvidianews vera-rubin-full-production).
- DeepSeek day CONFIRMED still the record: Jan 27 2025, $589B — largest single-day
  market-cap loss as of Sep 2026 (biggest since: ~$279B, Jun 5 2026). Deck line safe.
- Export controls, one line: US restricted advanced AI-chip sales to China since Oct
  2022; Apr 2025 license rule on the China-market H20 forced a $5.5B write-down
  (Nvidia 8-K Apr 9 2025; CNBC Apr 15 2025), partially reversed that summer.

## 4. The feedback loop (three beats)

- Scaling laws (Kaplan 2020, already on deck) made "more compute = better AI"
  forecastable → training compute for notable models grew 4–5×/year since 2010 —
  doubling ~every SIX months vs Moore's every two years
  (epoch.ai/data-insights/compute-trend-post-2010, Jun 19 2024).
- AI designs chips now: Google DeepMind AlphaChip (RL; Nature 2021) laid out parts of
  the last three TPU generations (deepmind.google blog, Sep 2024); Nvidia ChipNeMo
  (2023) + chief scientist Bill Dally: one RL tool turned a 10-month, 8-engineer task
  into an overnight run — while conceding they're "a long way" from AI designing chips
  unaided (Tom's Hardware; VENDOR CLAIMS — label when spoken).
- Bigger models → bigger clusters → next chip: 2012 AlexNet 2 gaming GPUs ~6 days →
  2024 Llama 3.1 405B 16,000+ H100s for months (ai.meta.com/blog/meta-llama-3-1, Jul
  2024) → 2025–26 gigawatt campuses (Stargate Abilene 1.2 GW). Each jump sells out the
  next generation before it ships.

## 5. Why so many data centers

- Training = a months-long factory shift: tens of thousands of GPUs for months
  (Llama 3.1 anchor above).
- Inference never sleeps: ~a billion people served around the clock (Gemini 1B monthly
  Aug 2026; ChatGPT 900M+ weekly Feb 2026 — citations live in r1_history §3, reuse).
- Electricity (IEA "Energy and AI," Apr 2025): data centres ~415 TWh in 2024 (~1.5% of
  world electricity) → projected ~945 TWh by 2030 (~3%) — growing 4× faster than all
  other demand (iea.org/reports/energy-and-ai/executive-summary).
- The striking comparison (same IEA report): a typical AI-focused data centre consumes
  as much electricity as 100,000 households; the largest under construction will
  consume 20× that (~2M households — a large city).
- The money: Microsoft+Google+Meta+Amazon ~$410B capex 2025, guiding "roughly $700B+"
  for 2026 (CNBC Feb 6 2026; Tom's Hardware analyst tally $725B — say "roughly $700B
  planned"; fiscal years differ).
- Stargate — ANNOUNCED vs BUILT (keep on slide): announced Jan 2025 "up to $500B over
  four years"; first campus (Abilene, TX) opened Sep 2025 (CNBC Sep 23 2025); by May
  2026 ~7 GW of PLANNED capacity across 7 US sites, ~$400B committed, only 4 of 8
  Abilene buildings live (epoch.ai/publications/openai-stargate-where-the-us-sites-stand).

## Chartable dataset (draw natively, log scale)

Primary — training compute vs Moore's-law pace (Epoch AI database, insight Jun 19 2024):
AlexNet 2012 = 4.7e17 FLOP · GPT-2 2019 = 1.9e21 · GPT-3 2020 = 3.1e23 · GPT-4 2023 =
2.1e25 (Epoch ESTIMATE — label "est."). Dashed Moore-pace reference from the AlexNet
point: 2012→2023 at 2-year doubling = ~45× (endpoint ≈2.1e19). Punchline (arithmetic
checks): Moore pace = ~45×; actual = ~45,000,000×. Caption: "Epoch AI database; GPT-4
is an estimate."
Backup (fully verified, no estimates): the Nvidia market-cap milestone strip above.

## Speaker-note stories

- The two gaming cards (2012): couldn't afford a supercomputer → two store-tier gaming
  cards, six days, beat 30 years of hand-built AI. Every AI company is still scaling
  that trick.
- The shovel-seller: the most valuable company on Earth (~$5.6T, Sep 2026) makes no
  chatbot, phone, or search engine — it sells the shovels; 92% of revenue from AI data
  centers; ten years ago it was "the video-game graphics company." (Sets up Part 2's
  DeepSeek day: when one cheap model made investors doubt how many shovels are needed,
  it lost $589B in a day.)
- The city-sized computer: IEA — one large AI data center ≈ 100,000 homes; biggest
  under construction ≈ 2M; ~$700B of build-out planned for 2026 alone. Caveat aloud:
  much of what you read is ANNOUNCED, not built.

## UNVERIFIED — never present as fact

- Rubin specs (336B transistors, 5× Blackwell inference, 10× cost/token) — vendor
  marketing via secondary coverage; "Nvidia claims" only.
- Huang's "1,000× in 10 years" — verified as a QUOTE, not a measurement; pair with
  Epoch's ~2.5-year price-performance doubling.
- GPT-4 2.1e25 FLOP — Epoch estimate (label on chart).
- 2026 capex "$725B / up 77%" — analyst aggregation; present as "roughly $700B+."
- IEA's late-2025 news update (403 on fetch) — use the Apr 2025 report numbers.
- Exact date of the Dally "overnight" claim — 2025, corroborated across outlets;
  attribute "Nvidia's chief scientist, 2025 (company claim)."
- H100 "shipped 2022" — standard history via secondaries; fine at primer level as
  "Hopper generation, 2022."
- Stargate "$400B committed" — Epoch tracker, not a party to the deals; always pair
  with announced-vs-built.
