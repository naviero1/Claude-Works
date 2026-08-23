# Tool Blueprint — Capture in Excel, Report in HTML

**Step 2 of the redesign.** How the redefined model (see MODEL_DICTIONARY.md)
becomes a tool a first-time analyst can use without knowing the architecture —
answering: Excel or HTML? how does capture stay correct all the way to the
dashboard? and what do the tabs say?

---

## 1 · The architecture call: Excel captures, HTML reports

One spine, two surfaces:

| Surface | Format | Why |
|---|---|---|
| **Capture + compute** | One Excel workbook | Capture happens in rooms, on corporate laptops, offline, with no IT approval, by people who all know Excel. The verdict formulas live in the same file, so status appears as you type — no pipeline needed during a pilot. |
| **Share + readout** | One self-contained HTML dashboard file | Generated from the workbook (the pipeline already does this). Email it, drop it on SharePoint — read-only, interactive, filterable, and nobody can break a formula in it. This is what B sees. |

**Why not HTML for capture:** a shareable HTML file cannot durably store what
users type (browser storage is per-person, per-browser, unmergeable) — real
HTML capture means a hosted app with a backend, which is a v3 investment to
make *after* the pilot proves the method, not before. The v2 stored model
(six entities) is deliberately the schema such an app would use, so nothing
done now is throwaway.

**The bridge ritual:** finish capture → the Start tab's Data Health panel is
green → run one command (`python3 analysis/run_analysis.py`) → send
`dashboard.html`. For Excel-only users, the Results tabs *are* the dashboard.

## 2 · The structural principle: organize by journey, not by schema

The current workbook's tabs mirror the database (Goals, Topics, Flows,
Carriers, Rituals…) — that is exactly why it needs the architecture in your
head. The v2 workbook's tabs mirror **the method's phases, in order, numbered**
— the numbers are honest structure (it genuinely is a sequence), and the tab
color keeps the three-kind code (green = start, yellow = you type,
blue = computed, gray = reference).

### The tab map

| Tab | Color | What the user does there | Replaces |
|---|---|---|---|
| `▶ Start` | green | Reads what this is (5 lines), sees the cell legend, follows a 6-step checklist with **live progress counts** and jump links, watches the **Data Health panel** (§3). | README |
| `1 · Goals` | yellow | Goal, owner, class (core / aspirational). Rarely more than 5 rows. | Goals |
| `2 · People` | yellow | Everyone who produces or consumes information: name, function, person/team. | Stakeholders |
| `3 · Venues` | yellow | The inventory: meetings (cadence, duration, attendees, claims, compliance) and channels (synchrony, persistence, real cadence) — two blocks, one tab. | Rituals + Channels |
| `4 · Topics` | yellow | Per goal: the named subjects people must hear about — the controlled vocabulary. | Topics |
| `5 · Needs` | yellow | "What should flow": one row per need — topic, from, to, criticality (critical/important/routine), how fast, conversation-or-any — plus a goal-owner **sign-off column** (catchball made visible). | Flows (required) |
| `6 · Reality` | yellow | "What actually flows": one row per observed flow — topic, from, to, corroboration, evidence, and up to 3 inline carrier slots (venue + push/pull). **The status verdict appears right on the row as you type.** | Flows (actual) + Carriers |
| `7 · Meeting Audit` | yellow | CR1–CR6 pass/fail, each with its evidence cell beside it; cost computes automatically. | Rituals CR block |
| `8 · Decisions` | yellow | Name, topic, who owns it on paper, where it actually got decided. | Decisions |
| `Findings` | blue | The whole readout: stats, BY GOAL banded core-first, top defects, theater, decision flags, risks. | Findings |
| `Goal Lens` | blue | Pick a goal, see everything that serves it. | GoalLens |
| `White Space` | blue | The function-to-function hand-off matrix. | WhiteSpace |
| `Sources` | gray | The frameworks library (reference appendix). | Frameworks |
| *(hidden)* `Engine`, `Lists` | — | ALL helper/intermediate columns move here — data tabs show only human columns plus the verdict. | ~40 scattered helper columns |

Two rules make this teachable:

1. **Data tabs show inputs + the verdict, nothing else.** Today the Flows tab
   shows 15 gray intermediate columns beside 11 input columns; every
   intermediate moves to the hidden Engine sheet. What remains reads as a
   sentence: *this topic, from her, to him, this critical, this fast → status.*
2. **Schema nouns disappear from tab names into column headers.** "Flows,"
   "Carriers," "Rituals" are the model's vocabulary; "Needs," "Reality,"
   "Venues," "Meeting Audit" are the analyst's. The dictionary keeps the formal
   names; the tool speaks the user's.

## 3 · Capture correctness — how data stays dashboard-ready

The question "how do we capture the outputs correctly in a dashboard" is
answered by making *wrongness visible at type-time* and *readiness explicit
before export*:

1. **Dropdowns everywhere, by name.** Every reference field (topic, person,
   venue, goal) is a dropdown showing names — IDs resolve behind the scenes.
   A typo becomes impossible, which kills the three documented
   "afternoon-costing" entry mistakes at the source.
2. **The Data Health panel** on `▶ Start` — a live pre-flight check:
   - needs with no topic / latency / criticality (status can't compute)
   - observed flows with no carrier ("reads as latency gap — add where it travels")
   - disputed flows awaiting follow-up interviews
   - meetings claiming goals nobody defined; unscored meetings
   - goals with zero needs ("no nervous system")
   Every line shows a count and a jump link; **all-green = dashboard-ready.**
   This is the gate that guarantees the export is right.
3. **Verdicts appear as you type** — status conditional colors over every
   pre-wired row (per the polish punch list), not just the seed.
4. **One-line "how to read this" header** on each Results tab.
5. **The export ritual is one command**, documented on `▶ Start`; the
   dashboard file is regenerated whole, never edited.

## 4 · What stays true from the current tool

The cell legend (pale yellow = type here, gray = computed), the ID-keyed
renames-never-break rule, both workbooks' verdict vocabulary, the pipeline as
ground truth with the three verifier suites, and the single-file dashboard.
This blueprint rearranges the furniture; the engine and the method are the
dictionary's job and they carry over intact.

## 5 · Build order

1. Generator restructure (`make_workbook.py`): journey tabs, hidden Engine
   sheet, name-keyed dropdowns, Data Health panel, goal_class banding.
2. Punch-list fixes ride along (POLISH_REVIEW.md): delimiter-guarded claim
   matching, CF coverage, internal hyperlinks, GoalIds range.
3. Verifiers updated to the new sheet map; all three suites green.
4. Dashboard adds the core/aspirational band and the class badge.
5. (v3, post-pilot) The same six-entity model becomes a hosted capture app;
   Excel remains the offline capture path.
