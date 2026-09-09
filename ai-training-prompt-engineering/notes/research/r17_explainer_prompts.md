# r17 — Succinct explainer prompts & token explanations (researched 2026-09-09)

Owner request (round-2 audit, slide 7): "explain this in a more succinct and engaging
way, do some research for best examples on this." Powers the R10 prompt-template shape
and P3's final wording.

## The reusable 4-part shape for ALL short "explain" prompts (research-backed)

Maps onto Google's Persona-Task-Context-Format guide (Oct 2024 PDF), ATLAS principles 2
& 5 (arXiv:2312.16171), and promptingguide.ai's specific-beats-vague contrast:
1. **Concept** — name it precisely ("what an LLM token is", not "how AI reads").
2. **Audience anchor** — a person ("to a busy office worker", "like I'm a 5th grader").
3. **Hard cap** — a number, never "briefly" ("under 80 words", "3 sentences").
4. **Analogy + application** — one everyday analogy, end with "why it matters for my
   work".
Evidence strength: audience anchoring reliably reshapes style (strong practitioner
consensus; a 2024 Springer study found simplify-requests cut reading level ~3 grades
without accuracy loss); ATLAS's 57.7%/67.3% improvement figures are the authors' own
benchmark across 26 principles — cite the shape, not those numbers.

## Token explanations — what the best sources say

- OpenAI Help Center (canonical): "Tokens can be thought of as pieces of words…";
  1 token ≈ 4 chars ≈ ¾ word; 1,000 tokens ≈ 750 words. (Exact current wording via
  consistent third-party reproductions — direct fetch 403.)
- Anthropic glossary: "the smallest individual units of a language model… words,
  subwords, characters, or even bytes"; Claude ≈ 3.5 chars/token.
- 3Blue1Brown (8.49M subscribers): "little chunks of the initial input text, typically
  words or little pieces of words."
- Karpathy: tokens are "the fundamental unit — the atom — of large language models."
- NVIDIA (Mar 2025): "the language and currency of AI" — good for the billing angle.
- **Most popular vivid analogy: LEGO bricks** (multiple popular explainers), then puzzle
  pieces. The deck's "bricks, not letters" framing sits on the dominant analogy —
  validated.

## Best live demo that is NOT letter-counting

Paste attendees' own names / company jargon / an email into a live tokenizer
(platform.openai.com/tokenizer or tiktokenizer.vercel.app): common words stay whole,
rare words shatter into colored chunks — interactive, personal, reliable (Karpathy does
exactly this in his lectures). Secondary hooks: the same email in Spanish/German costs
more tokens; "billed in bricks, not pages."

## P3 final wording (R10 format, adopted into the ledger)

TYPE → "Explain AI tokens to a busy office worker in under 80 words: use a LEGO-brick
analogy, show one word splitting into tokens, and end with why tokens set my AI's cost
and limits."
WHY → the definition lands in your course log — and the brick analogy is the one the
best explainers on the internet use.

Sources (key): help.openai.com article 4936856 · docs.anthropic.com glossary ·
3blue1brown.com/lessons/gpt + /mini-llm · Karpathy tokenizer lecture (Feb 2024) ·
blogs.nvidia.com/blog/ai-tokens-explained (Mar 2025) · Google "Prompting Guide 101"
(Oct 2024) · promptingguide.ai/introduction/tips · arXiv:2312.16171 (ATLAS) · Springer
s00464-024-10720-2. UNVERIFIED: per-video view counts; exact verbatim of 403-blocked
OpenAI pages; Anthropic prompt-library exact wording.
