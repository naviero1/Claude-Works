# Sprint 02 — Sep 28 to Oct 11, 2026

Full content in `sprint-02.html` / the published artifact. Adaptive design: tracker showed week 1 weekdays checked, nothing after Sep 18 (no B1, no floor, empty notes — a notes-box bug fixed this sprint may have eaten notes), so this sprint **carries forward instead of piling on**.

## Structure
- **Week 1 (Sep 28–Oct 4): finish Sprint 01** — L6–L10 lessons (linked into the archive) + ML Module 1 completion (B1 due Oct 3). Sunday: original application work + tracker true-up.
- **Week 2 (Oct 5–11): advance** — six NEW lessons chaining from Sprint 01, + ML Module 2 (B2 due Oct 10).

## New lessons (full template: figure → bullets → case → task → glossary → chapter)
| # | Lesson | Domain | Chains from |
|---|---|---|---|
| N1 | Supplier qualification & the quality agreement (stage-gate flow) | Supplier Eng | L1 |
| N2 | SPC on supplier CoAs (computed I-chart, drift-before-spec case) | IE | L8 |
| N3 | Should-cost modeling ($180 quote vs $138 build-up) | Finance | L7 |
| N4 | Risk register & KRIs (worked 3-row register + leading/lagging timeline) | Risk | L5 |
| N5 | SQL 2: window functions & CTEs (partition-lanes diagram) | Data & AI | L11 |
| N6 | Auditing a price increase: pass-through & indexation (+12% vs +4.2%) | Economics | L10/N3 |

## ML re-base (honest slip, stated plainly)
B1 = Module 1 by Oct 3; B2 = Module 2 by Oct 10; Course 1 certificate → Sprint 03 (Oct 25); Course 2 by Nov 22; Specialization ~Dec 27.

## Tracker changes
- Dual-doc storage: Sprint 01 boxes keep writing to `progress/sprint-01`; new boxes → `progress/sprint-02` (JS routes by `data-sp`).
- **Bug fix:** notes textarea shared `id="notes"` with its section — `getElementById` grabbed the section, so saved notes could read back empty. Textarea now `id="notes-text"`. This may explain Sprint 01's empty notes.
- Sprint 01 archived intact at the bottom (checkboxes live; ML benchmark boxes deduplicated to the active section); in-page links auto-open the archive.

## Compliance floor (carried, still open)
IATA shipper course · OSHA BBP/BSL-2 · WES/ECE transcript evaluation.
