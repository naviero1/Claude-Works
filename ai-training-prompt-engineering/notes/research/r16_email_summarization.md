# r16 — Email-thread summarization: methods, prompts, Copilot mechanics (researched 2026-09-09)

Powers the v1.5 Part 4 inbox walkthrough (two slides) and its notes. Owner asked for
popular practitioner sources (Reddit, YouTube, prompt libraries) — popularity signals are
reported where verifiable. Caveat: reddit.com blocks the crawler; Reddit evidence is
secondhand and flagged.

## The five summary shapes (each verified against ≥2 sources)

1. **TL;DR triage** — one sentence, ~30 words, current state or decision needed first;
   end with what's needed from me. (AIEmaily Jun 2026; the bare "TLDR:" trick per
   Herklotz/Medium.)
2. **Structured brief** — OVERVIEW / DECISIONS / ACTION ITEMS (task—owner—due) / OPEN
   QUESTIONS, "None" when empty, facts-only, no invented owners or dates. The default.
   (AIEmaily; Mailbird 2026 teaches the same headers.)
3. **Action-items table** — Task | Owner | Due | Priority | Blocked by; blank beats
   guessed; sort by due date. (AIEmaily; Copilot equivalents from van der Schyff MVP
   Jan 2026 and Missive Mar 2026.)
4. **Decisions log** — Decision | Decided by | Reasoning (if stated) | Date; settled only;
   flag "agreed but never confirmed." (AIEmaily; Mailbird one-liner variant.)
5. **"Who owes what" reply-prep** — unanswered questions + "X owes Y: [thing]", latest
   state only. (AIEmaily; Copilot: "Who owes the next reply and by when?" — Bowdoin KB;
   "Highlight who owes a response" — m365.fm Apr 2026.)
Also in use: chronological "what changed" catch-up (van der Schyff; AI Academy Aug 2026),
per-person disagreement map, risk/urgency triage (Jace template Jan 2026; CloudCapsule
ranked-triage Nov 2025), stakeholder handoff summary (Missive; Mailbird).

## Copilot mechanics (verified on Microsoft pages, Sep 2026)

- "Summary by Copilot" scans the thread and may add **numbered citations that jump to the
  source email** — the built-in verification tool (MS Support: "Summarize an email thread
  with Copilot in Outlook").
- Refinement in the pane works: "List the action items" · "What does the sender need from
  me?" · "Who owes the next reply and by when?" · "What did you base that on?" (Bowdoin
  College KB).
- Copilot Chat can search the mailbox: "Summarize my emails from the last week related to
  [project]" (MS Support: "Chat with Copilot in Outlook").
- **Limits:** attachments NOT read by default ("Summarize a file" explicitly; added Jun
  2025; not in classic Outlook) · primary mailbox only — no shared/delegate/archive
  mailboxes · no S/MIME / IRM / some MIP-labeled mail · ~1,000-character minimum
  (verbatim in the Copilot-for-Sales FAQ; widely reported for Outlook).
- Microsoft's prompt anatomy: **Goal · Context · Source · Expectations** ("Get started
  writing prompts in Microsoft 365 Copilot"); example: "Write a summary based on all
  emails from Sam in the past two weeks."
- Prompt Gallery (adoption.microsoft.com) carries five email-summarization entries
  (texts truncated on page — partially verified).
- Scheduled/recurring prompts enable daily triage digests (CloudCapsule Nov 2025).

## Sequences practitioners teach

- **Brief → open questions → draft reply** (one conversation; reply prompt rules: answer
  the opens, confirm decisions, no invented commitments, [bracket] where I must decide,
  <120 words, one next step). (AIEmaily; Copilot "Summarize and reply" gallery entry.)
- **Chunk → running state → merge** for 30+ message threads: strip quoted history; split
  chronologically; per-chunk carry RUNNING DECISIONS / RUNNING OPEN QUESTIONS forward;
  merge rule: "if an early question was answered later, log it as a decision; resolve
  conflicting dates/numbers to the latest value, and say so"; spot-check names/dates.
  (AIEmaily; Mailbird independently teaches dedup-first.)
- **Triage ladder**: 1-2 paragraph summary → detailed shape only if action needed →
  interrogate → verify via citations (Mailbird 2026).
- **Cross-channel reconcile table**: Mail/Teams/Channel | Topic | Summary | Action |
  Follow-up (Ragnar Heil MVP, Substack Jun 2024 — widely recirculated).

## Pitfalls (the walkthrough's red card)

- Reports the FIRST date/position, missing mid-thread reversals → fix: oldest-first +
  "flag anywhere a decision or date CHANGED — show both, mark the latest" (The Human Co.
  Jun 2026; AIEmaily).
- Drops qualifiers ("agreed to proceed, subject to board sign-off" → "agreed to proceed")
  → fix: caveat-preservation QA pass (The Human Co.).
- Invents owners/dates/action items from vague "I'll look into it" lines → fix: "None"
  slots, blank-beats-guessed, firm-commitments-only rules (AIEmaily; Mailbird/Missive).
- Wrong who-said-what attribution → fix: verify names via Copilot citations / "what did
  you base that on?".
- Incomplete input (collapsed quoted history; newest-first pastes) → expand, paste
  oldest-first, say so.
- Privacy: thread summarization belongs in the tenant (green tier, r11), not personal
  chatbots. ⚠ A "10–15% of summaries hallucinate names/dates" figure circulates
  UNVERIFIED — do not use.

## Standout popular sources

1. Microsoft Copilot Prompt Gallery — the canonical corporate source
   (adoption.microsoft.com/en-us/copilot/prompt-gallery/).
2. Kevin Stratvert (YouTube, 4.4M subscribers; ranked #1 of 53 tracked Copilot educator
   channels, developereducators.com Sep 2026) — Copilot in Outlook & Teams tutorial.
   Runner-up: Mike Tholfsen (Microsoft PM), "Outlook AI Chief," Jun 1, 2026.
3. AIEmaily, "AI Prompts to Summarize an Email Thread" (Jun 2026) — richest verbatim
   prompt library found; popularity unverified.
4. Tracy van der Schyff (Microsoft MVP), "Master Your Inbox with AI" (Jan 15, 2026).
Reddit: blocked to the crawler; secondhand — a ~400+-upvote r/ChatGPT meta-prompt ("ask
me clarifying questions until you are 95% confident") is the community's most-recommended
reliability fix (via aitooldiscovery.com; upvote count unconfirmed).

Full URLs for every claim are preserved in the v1.5 research transcript; key ones:
support.microsoft.com articles (thread summarize · Outlook Copilot FAQ · prompt-writing ·
Copilot Chat) · aiemaily.com/blog/ai-prompts-to-summarize-an-email-thread ·
getmailbird.com/summarize-long-email-threads · missiveapp.com/blog/summarize-email-thread-ai ·
thehumanco.org/ai-resources · jace.ai/blog · tracyvanderschyff.com (2026/01/15) ·
m365.fm/blog/mastering-copilot-prompts-for-email-summarization ·
blog.cloudcapsule.io (Outlook executive assistant) · ragnarheil.substack.com.
