# Ongoing logs — how this works

This folder is the durable, append-only record. The conversation thread is
disposable; **these files are the memory.** Any Claude session can read them and
pick up exactly where the last one left off.

## How Oscar logs (no formatting required)

Just say it in plain language, in any session:
- "Chipotle chicken bowl + chips for lunch, felt heavy after."
- "Skipped breakfast, McDonald's on the way home ~8pm."
- "Home-cooked salmon and rice for dinner."

Claude appends a structured row to `meal-log.csv` and commits it. You never touch
the CSV yourself unless you want to.

## meal-log.csv columns

| column | meaning |
|---|---|
| date | YYYY-MM-DD |
| meal | breakfast / lunch / dinner / snack |
| source | doordash / home / restaurant / grocery |
| description | what was actually eaten |
| rating | solid / ok / junk — Claude's rough call, editable |
| notes | how you felt, timing vs. bedtime, anything relevant |

## Tags (VNSt / VNSn and any others)

Oura day-tags don't export in the trends CSV. To fold them in, either drop an
Oura tag export here, or list the tagged dates in a session and Claude records
them in `oura-tags.csv` (created on first use). Once tags accumulate, Claude can
group any metric by tag.

## What Claude does with it

- Appends meals/tags here and commits.
- Periodically re-runs the solid-vs-junk correlation against Oura (in
  `../data/oura/`) as the sample grows — the current blocker is too few logged
  dinners/weekends and no item detail, both of which this log fixes over time.
- When you paste new DoorDash options, cross-references this log + recent Oura
  readiness/sleep to recommend.

## Starting a fresh session later

Say: "load my health folder." Claude reads `health/README.md`, `profile.md`,
the data files, and this log — full context restored, no thread history needed.
