# Six Thinking Hats — Analysis

**Topic:** Should our 12-person startup adopt a four-day work week (32 hours, same pay)?

**Modality:** `decisions`  ·  **Sequence:** blue → white → green → yellow → black → red → blue

*Illustrative sample of the format the framework produces. Hand-written for the repo; a live run via `cli/six_hats.py` will vary.*

---

## 🔵 Blue — Framing

We're deciding whether to move the whole company from a standard five-day week to
a four-day, 32-hour week at unchanged pay. A good outcome is a clear go / no-go /
pilot call with the two or three factors that actually drive it named explicitly,
plus what would change our minds. This is a reversible operational decision, so
the bar is "worth trying," not "certain to work." Agenda: facts → options →
upside → downside → gut → synthesis.

---

## ⚪ White — Facts & Information

**Known (verified):** We're 12 people — 7 engineering, 2 sales, 3 ops/founders.
Current week is Mon–Fri, ~45 hrs typical. We have no shift or on-call coverage
obligation except a business-hours support SLA (verified: contract says 9–5 ET,
Mon–Fri).

**Known (probable):** Recruiting is our current bottleneck — two roles open ~90
days. A shorter week is a strong differentiator for small firms (probable, from
widely reported pilots).

**Claimed but unverified:** That output holds constant at 32 hours. Public
four-day-week trials report maintained or improved productivity, but they skew
toward self-selected firms and short horizons — not verified for us.

**Unknown:** Our own utilization (how many of the 45 hours are focused vs.
reactive); whether the support SLA can be met in four days; customers' reaction.

**Would most change the picture:** a 6–8 week time-tracked pilot; a read on
whether Friday coverage can be handled async or on a light rotation.

---

## 🟢 Green — Creativity

- **Full switch:** everyone off Fridays.
- **Staggered:** half the team off Friday, half off Monday — preserves five-day
  coverage while each person works four.
- **Seasonal:** four-day weeks only in the two slow quarters.
- **"Earn it" version:** hit the sprint goal, take Friday; miss it, Friday is a
  catch-up day.
- **Meeting-bankruptcy first:** cut meetings hard and see if 32 productive hours
  already exist inside the current 45 before changing the calendar at all.
- **Provocation (po):** abolish the fixed week entirely — output-only, no hour
  count. (Almost certainly too far for a 12-person team, but it points at the
  real lever: measure output, not chairs.)
- **Reframe:** the question might not be "four days?" but "why does our work
  need 45 hours?" — attack that first.

---

## 🟡 Yellow — Optimism & Value

- **Recruiting edge is real and immediate** — a four-day week is a rare perk a
  tiny startup can offer that even big-pay competitors won't, directly attacking
  our 90-day open roles.
- **Forcing function on waste** — because the constraint is hard, it pressures
  us to kill low-value meetings and process, which compounds beyond the day off.
- **Retention & burnout** — a genuine schedule change (not fruit-in-the-office)
  is the kind of thing that keeps a stretched early team from leaving, because
  it changes their actual week.
- **Cheap to test** — reversible in a sprint, so the expected value of a pilot is
  high: small downside, information-rich either way.

---

## ⚫ Black — Caution & Critique

- **The support SLA breaks** if Friday goes dark, because the contract commits us
  to Mon–Fri 9–5 — this is the single hard blocker and it's contractual, not
  cultural. Any plan must solve Friday coverage first.
- **Sales cadence mismatch** — customers and prospects work five days, so a
  fully-dark Friday risks slower deal response, because buying momentum decays
  over a weekend-plus-Friday gap.
- **32 hours may be fiction** — if real focused output today is ~35 hrs, not 45,
  then cutting to 32 is a real capacity cut, not slack removal, and delivery
  slips.
- **Reversal has a morale cost** — taking the day *back* if it fails reads as a
  takeaway and can hurt worse than never trying, because people re-plan their
  lives around it.
- **Small-team fragility** — with 12 people, one person out on their day plus one
  sick can drop a function to zero, because there's no bench.

---

## 🔴 Red — Emotion & Intuition

- Strong excitement about the recruiting angle — this *feels* like an edge.
- Moderate unease about the support SLA — a nagging "this is the thing that bites
  us."
- Mild skepticism that output really holds at 32 hours — gut says it dips at
  first.
- Quiet pull toward the staggered/pilot version rather than the full switch —
  feels safer without feeling timid.

---

## 🔵 Blue — Synthesis

**Bottom line: run a time-boxed pilot of the *staggered* four-day week, not a
full immediate switch.** The upside (recruiting, focus, retention) is real and
the decision is cheap and reversible, which clears the "worth trying" bar — but
two Black-hat points are load-bearing and must be handled *before* day one.

**Key tensions.** Yellow's recruiting/retention case is strong and Green offers a
clean way to capture most of it, but Black's SLA point is a hard contractual
blocker that Yellow can't wish away — that's the sharpest tension, and Black
wins on it as a *precondition*, not a veto. Red's pull toward staggered-over-full
matches the logic, which is a good sign.

**What tipped it.** (1) The decision is reversible and information-rich, so a
pilot dominates both "do nothing" and "full switch." (2) The staggered variant
neutralizes the two worst risks (Friday coverage, sales cadence) while keeping
the individual four-day benefit. (3) Our real utilization is unknown, and a pilot
is the cheapest way to learn it.

**Open questions / what would flip it.** If time-tracking in the pilot shows
output falling materially below the five-day baseline (not just noise), or if the
customer covering the SLA objects, downgrade to "meeting-bankruptcy only" and
shelve the day off.

**Next actions.**
1. Confirm the support SLA can be met with a light Friday rotation or async
   coverage — this gates everything.
2. Design a 6-week staggered pilot (half off Fri, half off Mon) with simple
   time-tracking and one success metric per function.
3. Do the meeting cull *now*, independent of the pilot — it's upside with no
   downside.
4. Pre-commit to the decision rule (what result = adopt / extend / stop) before
   starting, so the reversal isn't read as a takeaway.
