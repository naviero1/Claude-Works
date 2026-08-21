# G8 · Summarize & Compare Documents

**Type:** Generative · **Version:** 1.0 · **Use when:** condensing long material (reports, procedures, meeting transcripts) or diffing versions/documents (what changed, what conflicts).
**Works in:** any chat assistant with file upload; prefer long-context models for 100+ pages.

---

## Template A — Summary that serves a decision

```text
Summarize the attached {{document}} for {{audience}} who must {{decide/do X}}.

<format>
1. The 3 things they must know (one line each, with the number/date where relevant).
2. What's new or changed vs. what we already knew: {{baseline, if any}}.
3. Risks/asks buried in the text (page/section reference each).
4. What the document does NOT cover that {{audience}} will assume it does.
Length cap: {{half a page}}. Quote exact wording (with location) for anything contractual,
regulatory, or numeric — no paraphrase there.
</format>

Placement tip: attach/paste the long document FIRST, instructions after — long-context
models follow instructions at the end more reliably.
```

## Template B — Compare versions / documents

```text
Compare the attached documents: {{A = v1 / supplier X}}, {{B = v2 / supplier Y}}.

<task>
1. Table of substantive differences: section | A says | B says | why it matters.
   Ignore formatting/typo changes unless they change meaning.
2. Conflicts: where they can't both be true/complied with.
3. What A has that B lacks, and vice versa.
4. For contracts/procedures: every changed obligation, deadline, threshold, or
   responsibility — quoted verbatim, both versions, with location.
</task>

<rules>
If the documents are versions, do not assume newer = correct; flag regressions too.
If a section is unreadable (scan/table mangling), say so rather than guessing.
</rules>
```

## Template C — Meeting notes → actions

```text
From the attached transcript/notes: 
1. Action table: owner | action | due date | the sentence it comes from (verbatim).
   Unassigned actions get owner "UNASSIGNED" — don't guess names.
2. Decisions made (verbatim where wording matters).
3. Open disagreements — where the group did NOT converge.
Nothing else. If a name is ambiguous ({{two Alexes}}), flag it.
```

---

## What makes this work
- **Audience + decision framing** — a summary is a filter; without knowing what it's for, the model keeps the wrong 10%.
- **"What it does NOT cover"** kills the completeness illusion, the most dangerous property of fluent summaries.
- **Verbatim-quote rule for load-bearing text**: paraphrase is where obligations quietly change meaning.
- **Attribution with source sentences** in the actions table makes verification instant.

## Pitfalls
- Summarizing the summary: chains of condensation compound loss; go back to the original.
- Trusting extraction of tables from bad scans — check the numbers that matter.
- Comparing 5 documents in one pass: do pairwise, then merge; wholesale N-way comparison drops details.
- The middle of very long documents gets less attention ("lost in the middle") — for critical sections, ask directly: "what does section 7 say about X?"
