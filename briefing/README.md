# Daily Briefing

`PROMPT.md` is the master prompt for the daily catch-up briefing. It replaces the old 7-point prompt with a pipeline that (a) reconciles every place to-dos get written — BOOX notebook photos → Notion → Google Calendar — and (b) delivers a world brief ranked by significance rather than coverage volume, with cross-run memory so stories never repeat.

## What changed vs. v1

| v1 section | v2 |
|---|---|
| 1 Schedule | Kept, now merged with Notion due dates and BOOX capture (Step 2–4) |
| 2 Emails, 3 Messages, 4 Action items | Kept as-is (Inbox / Waiting on your reply / Open loops, split Intuitive vs Personal) |
| 5 News | Rebuilt: `<news_doctrine>` — consequence / irreversibility / proximity / divergence ranking, Δ-deltas on developing stories, "Your angle" edge bullets, memory-backed anti-repetition |
| 6 BOOX photos | Kept, plus write-back: new items created in Notion, dated items on Calendar, ambiguous ones become numbered questions |
| 7 Notion→Calendar sync | Folded into Step 4 (it was redundant as a separate step) |

## How to run it

**Scheduled (recommended):** claude.ai → Scheduled tasks → new task, weekday mornings. Paste the contents of `PROMPT.md` (below the divider). Enable connectors: Gmail, Google Calendar, Google Drive, Notion (+ GitHub if you want the Claude Code check). Model: Fable 5 (else Opus), extended thinking ON.

**On demand:** run `/briefing` in any Claude Code session on this repo, or paste the prompt into a chat with the same connectors.

## One-time setup

1. **BOOX Inbox folder** — create a folder named `BOOX Inbox` in Google Drive. Photos replied in the chat also work, but Drive is the reliable path when each scheduled run is a fresh conversation.
2. **Apple Calendar** — no write connector exists for it, and none is needed: add your Google account on iPhone/Mac (Settings → Apps → Calendar → Accounts) and everything the briefing puts on Google Calendar appears there automatically. That's why the old step 7 is gone.
3. **Briefing Memory** — a Notion page the prompt reads first and updates last (news log, watchlist, open questions, last run). Created already; the prompt re-creates it if it ever goes missing.

## Feeding it

- Reply to the "Needs from you" block in one message: photos + numbered answers ("2: close, 3: Sep 5").
- Undated or ambiguous items keep getting re-asked until you answer — that's intentional.
