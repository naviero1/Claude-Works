# The Biweekly Sprint Program

A standing contract, started 2026-09-13.

## Cadence

- **Every second Sunday** (next: 2026-09-27, then 10-11, 10-25, …) Claude prepares the next sprint and republishes the **Ops Learning Sprints** artifact (same URL every time). A scheduled trigger fires into the session at ~7:00 AM ET each prep Sunday; each firing also arms the next one.
- Each sprint = **14 days × ~1 hour/day**: weekdays ≈ 30 min ML course + 30 min domain micro-lesson; Saturdays = ML lab time; Sundays = application + review.

## What every sprint contains

1. **At least one taught topic from each of the 11 curriculum domains** — plain-language micro-lessons with acronyms defined, a case from Oscar's world (ex-vivo materials, his resume projects), a 10-minute task, and references split into *owned* (Google Drive library) vs. *worth buying* (Amazon links).
   **Lesson template (standard from Sprint 01 v2 onward, per Oscar's request): visual first.** Each lesson opens with an original diagram or chart (hand-authored inline SVG: `currentColor` theming, one accent hue, real computed numbers for charts, `figure`/`figcaption` with aria-labels), then 4–5 "read the picture" bullets, then case → task, with the full prose collapsed in a "Depth" block. Multi-series charts use the validated `--s1/--s2/--s3` palette slots. Never paste figures from copyrighted books — redraw the standard concept with his own case data, and cite the owned book for depth.
2. **ML track benchmarks** for the Andrew Ng Machine Learning Specialization — dated checkpoints plus guiding questions to self-test on Sundays.
3. **Certification radar** — path-tagged, updated as targets approach.
4. **A progress tracker** — the artifact stores checkboxes and a "notes to Claude" box in its database (`progress/sprint-NN`); Claude reads both before building the next sprint.

## Topic sequencing rule

Micro-lessons walk `DOMAIN-MAP.md` in priority order (NOW → NEXT → LATER), preferring topics that (a) feed a Stage 1–2 curriculum deliverable, (b) chain with each other (e.g., Kraljic → market power → BATNA), and (c) lean on books already in the Drive library. Oscar's Sunday notes can reorder anything.

## ML master plan (assumed start: 2026-09-14, Course 1 from zero)

| Sprint | Target | By |
|---|---|---|
| 1 | Course 1 (Supervised ML: Regression & Classification) Modules 1–2 | Sep 27 |
| 2 | Course 1 Module 3 → **Course 1 certificate** | Oct 11 |
| 3–4 | Course 2 (Advanced Learning Algorithms, 4 modules) | Nov 8 |
| 5–6 | Course 3 (Unsupervised, Recommenders, RL) → **Specialization certificate** | ~Dec 13 |
| 7+ | Capstone on his own data: supplier risk scoring or lead-time regression | — |

## Operational notes

- Artifact: "Ops Learning Sprints" — one stable URL, Sprint N on top, prior sprints archived below over time. Progress docs are per-sprint (`progress/sprint-01`, `progress/sprint-02`, …) so history is kept.
- Coursera connector currently needs re-authorization on Oscar's side; until then benchmarks rely on his check-offs rather than live course data.
- Each sprint's sources are committed here as `sprint-NN.md` (+ the published HTML) on branch `claude/determined-cannon-xrn001`.
