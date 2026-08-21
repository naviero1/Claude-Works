# G7 · Research Brief (cited web/document research)

**Type:** Generative · **Version:** 1.0 · **Use when:** you need a sourced answer — market/supplier/regulatory/technical research — not the model's from-memory recollection.
**Works in:** Perplexity, ChatGPT / Claude / Gemini deep-research modes, Copilot Researcher. Use tools that **search and cite**; never trust from-memory citations.

---

## The template

```text
<mission>
Research question (one sentence): {{precise question — not a topic}}
Decision it feeds: {{what I'll do differently based on the answer}}
Scope: {{time range — e.g., "developments since 2024"}} · {{geography}} · {{in/out of scope}}
</mission>

<sources>
Prefer: {{primary sources — regulator sites, standards bodies, vendor documentation,
peer-reviewed work, major outlets}}. 
Avoid: {{content farms, forums, undated pages}}.
If sources conflict, present both sides with dates — do not silently pick one.
</sources>

<format>
1. Answer in 3 sentences (even if uncertain — say what's known vs. contested).
2. Key findings as bullets — every bullet ends with its source link and publication date.
3. What the sources DON'T establish (gaps, open questions).
4. Confidence: high / medium / low, and what would raise it.
Length cap: {{1 page}}.
</format>

<rules>
- Every factual claim needs a working link. No link = label it "unsourced — verify".
- Note the as-of date of each key fact; this field moves fast.
- Distinguish vendor marketing from independent evidence.
</rules>
```

## Quick variant — verify one claim

```text
Verify this claim and nothing else: "{{claim}}".
Search for primary sources. Verdict: TRUE / FALSE / PARTLY TRUE / CAN'T VERIFY, then the
evidence with links and dates, then what nuance the one-line version loses.
```

---

## What makes this work
- **Question, not topic** — "What changed in {{regulation}} since 2024 that affects {{X}}?" returns an answer; "{{regulation}} update" returns a landfill.
- **Decision-it-feeds** tells the model which details matter.
- **Gaps section** is where honesty lives; without it every brief reads complete.
- **Links + dates on every bullet** make spot-checking a 2-minute job — and spot-check you must: 2-3 links per brief, especially the ones your conclusion leans on.

## Pitfalls
- Citation laundering: a fluent brief with dead or misquoted links. Click before you forward.
- Recency illusion: models answer from training memory unless search actually ran — check that sources are dated after your scope starts.
- One-engine research for big calls: run the same question in a second tool; disagreements are the interesting part.
