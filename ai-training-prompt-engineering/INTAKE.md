# Intake checklist — what to collect to refine the taxonomy & tools

Drop anything collected into `notes/intake/`. **Scope rule: no company data** — no part numbers,
supplier or site names, internal codes, or personal data. What we want is *how prompts are used*:
structure, habits, and generic patterns. Redact anything specific before dropping it in.

## Tier 1 — how you actually use prompts

- [ ] **Real prompts, redacted** — 15–30 prompts you've actually used (from any tool), with any
      company-specific values swapped for `{{placeholders}}` before sharing.
      → gap analysis vs. the taxonomy; new options mined from real phrasing patterns.
      *Path A:* claude.ai → Settings → Privacy → Export data → redact → drop in.
      *Path B (often better):* copy your 15–30 favorites into one doc, genericized as you paste.
- [ ] **Job-shape inventory** — the *kinds* of recurring jobs (e.g., "monthly metric review deck",
      "document-folder → tracker", "compare N options and recommend"), cadence, and deliverable
      shapes — described generically, no project names needed.
      → real presets: one saved instance per job shape.

## Tier 2 — usage feedback

- [ ] **Builder pilot (3–5 people, 1 week):** which attribute confused you? which options did you
      pick? what did you type in custom boxes (redacted)?
      → wording fixes; custom text promoted to options.
- [ ] **Failure stories, genericized** — 2–3 cases where AI output caused rework ("it invented a
      figure", "wrong tone to a customer") with the identifying details stripped.
      → mapped to missing elements/options.

## Tier 3 — gated product content (screenshots suffice)

- [ ] Copilot Prompt Gallery: full **Task** and **Job type** filter lists.
- [ ] Anthropic Console **prompt improver** output for any one generic prompt.
- [ ] ChatGPT Canvas **reading-level** and **length** slider labels.

## Tier 4 — the books' missing chapters (notes/photos of frameworks are enough)

- [x] Phoenix & Taylor — full book received as DOCX (Aug 2026 upload).
- [ ] Berryman & Ziegler — **Ch. 4–11** (assembling the prompt, few-shot, RAG, agents, evals).
      The Drive PDF (12.6MB) exceeds the 10MB API download limit — upload an EPUB or split the
      PDF into <9MB parts.
- [ ] Huyen, *AI Engineering* — **Ch. 4–7** (evaluation, prompt engineering, RAG & agents).
      Same limit (32MB) — EPUB or split parts.

**Skip:** anything on the public web / arXiv / vendor docs — already captured with sources in
`notes/research/`. **Not wanted:** internal policies, glossaries, templates, or any company data.
