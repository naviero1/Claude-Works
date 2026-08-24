# G1 · Writing & Editing

**Type:** Generative · **Version:** 1.0 · **Use when:** drafting or improving emails, summaries, reports, announcements — any prose a human will send or publish.
**Works in:** any chat assistant.

> Most workplace writing requests are **edits of text you supply**, not blank-page drafting.
> Give the model your raw material and your voice; keep the judgment call — what the message
> must accomplish — for yourself.

---

## Template A — Draft from raw material

```text
<role>
You are an experienced {{business|technical}} writer. You write plainly, front-load the point,
and never pad. You match the voice of the samples I give you.
</role>

<task>
Draft a {{email | one-page summary | status update | announcement}} for {{audience — role and
what they already know}}. Its job: the reader should {{know | decide | do}} {{X}} after reading.
</task>

<context>
Raw material (everything relevant; do not invent beyond it):
"""
{{notes, bullet points, data, prior thread}}
"""
Key point that must survive: {{the one thing that cannot be lost or buried}}
Sensitivities: {{what not to promise / mention / speculate about}}
</context>

<format>
- Length: at most {{120}} words (hard cap — cut content before quality).
- Structure: {{point first, then support | subject line + 3 short paragraphs | bullets}}.
- Tone: {{plain and direct | warm but professional | formal}}.
- Do not add facts, numbers, or commitments that are not in the raw material.
- End with: {{the specific ask and deadline | next step | nothing}}.
</format>
```

## Template B — Edit / rewrite what I wrote

```text
Rewrite the text below. Keep every fact and commitment exactly as written — change only
clarity, order, and tone.

Goals, in priority order:
1. {{cut it to half the length | make the ask impossible to miss | neutral tone}}
2. {{plain language — a busy reader gets it in one pass}}

Audience: {{who}}. Tone: {{...}}. Hard cap: {{N}} words.
Then list in 2-3 bullets what you changed and why, so I can accept or reject each change.

"""
{{your draft}}
"""
```

## Template C — Voice matching (do once, reuse forever)

```text
Below are {{2-3}} samples of my writing (~500-1,000 words total). Describe my voice as a
reusable style guide: sentence length, formality, vocabulary, greeting/sign-off habits,
things I never do. Output it as a compact "STYLE CARD" I can paste into future prompts.

"""
{{samples}}
"""
```
Store the STYLE CARD in your prompt library / project instructions; paste it into `<role>` afterwards.

---

## What makes this work
- **Job-of-the-message framing** ("reader should know/decide/do X") beats "write an email about Y" — it gives the model a success criterion, not a topic.
- **Hard length caps.** Uncapped AI drafts run 2-3× too long. State a word cap and say it wins over completeness.
- **"Do not add facts"** is the highest-value line: fabricated details in routine email is the most common AI writing failure.
- **Delimiters** (`"""`) around raw material keep instructions and content from bleeding together.
- **Edit mode with a change list** keeps you the author: accept/reject per change instead of adopting a rewrite wholesale.

## Pitfalls
- Burying difficult news: state the core message by the second sentence; never let the model cushion it into paragraph three.
- Sending unread. The model writes fluently, so errors read fluently too. Read as the recipient once before sending.
- Voice drift on long threads: re-paste the STYLE CARD in a fresh chat rather than trusting a 40-message-old instruction.
