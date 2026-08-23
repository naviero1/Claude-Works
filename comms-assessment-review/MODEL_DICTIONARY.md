# The Model, Defined — Variable Dictionary & Redundancy Audit

**Step 1 of the redesign.** Every element of the Communication Process Assessment
framework defined to a T, rated for whether it belongs in the final model, and
audited for redundancy — grounded in the *actual formulas* of the delivered
workbook (not just the documentation), cross-examined by independent review
passes (data-model normalization, semantic hygiene, newcomer capture burden),
with every proposed cut or merge adversarially verified against what would break.

Sources: Concept Cheat Sheet + Full Workbook Manual + Framework Course v1.1,
plus a full formula-level extraction of `comms_assessment_workbook.xlsx` and
`comms_assessment_lite.xlsx`. Date: 2026-08-23.

---

## 0 · The spine (the model in one breath)

**Goal** → decomposed into **Topics** (the controlled vocabulary) → which
**required Flows** (who must hear what from whom, how fast) are derived from and
**actual Flows** (what interviews observed) are coded to → actual flows ride
venues via **Carriers** (a **Meeting/Ritual** or a **Channel**) → and the engine
diffs the two states into **FlowStatus**, crosses meeting *claims* against
observed *carries* into **AlignmentClaim**, audits **Decisions** (paper rights
vs. real venue), scores meetings (**RitualHealth**), and surfaces everything
worth fixing as **Findings**, each stamped with its goal.

Everything in the framework is one of three kinds — and the current workbook's
biggest teachability failure is that it does not visually distinguish them:

1. **Identity & structure** (IDs, names, links) — the skeleton.
2. **Captured facts** (what the analyst types, with evidence) — the muscle.
3. **Computed verdicts** (what formulas produce) — the readout. Never typed.

---

## 1 · The headline numbers

- The full workbook presents **71 input fields** across 10 sheets.
- The verdict engine actually consumes **~30** of them.
- **12 input fields are read by no formula and no view** — they are process
  documentation living inside the data model (§4.3).
- **5 enum values are computationally dead** — legal to enter, but produce the
  same result as a sibling value (§4.4).
- The verified **day-one capture core is ~27 fields** (§5) — a newcomer can
  produce all three headline verdicts (the diff, the theater test, the decision
  defects) without touching anything else.
- The audit found **2 latent bugs** and **6 doc-vs-implementation divergences**
  the redesign should settle regardless of schema choices (§6).

---

## 2 · Data dictionary — input objects

Conventions: **Tier 1** = day-one capture (feeds a headline verdict) ·
**Tier 2** = audit layer (feeds meeting hygiene/cost) · **Tier 3** =
process-only (read by humans during the engagement, never computed on).
*Consumed by* traces the delivered formulas, not the docs.

### 2.1 Goal — the anchor

> One measurable business outcome, entered with the sponsor at framing.
> Every other object must trace back to exactly one goal — a flow serving no
> goal is not modeled; a goal with no flows "has no nervous system."

| Field | Tier | Definition (to a T) | Consumed by | Verdict |
|---|---|---|---|---|
| `goal_id` | 1 | Immutable key (G1…), assigned at creation; the only way anything refers to this goal, so renames never break links. | The busiest key in the model: topic→goal attribution, GoalLens picker, claims matching, alignment matrix, involvement flags. | **Core.** |
| `name` | 1 | The outcome statement — a result with a number ("Reduce supplier defect rate 30%"), never an activity — confirmed by the goal owner at sign-off. | No formula (display label). ⚠ In the **lite** workbook names ARE the join keys — a rename there breaks references. v2: one key (`goal_id`), one label, both editions. | **Keep.** |
| `owner_actor_id` | 1 | The single person accountable for the outcome, who signs off the goal's required-flow set in conversation (catchball) and receives its findings first. | Nothing computes on it — consumption is procedural (sign-off, findings routing). Cheap v2 win: check "owner absent from the goal's own stakeholder set." | **Keep.** |
| `priority` | 3 | The sponsor's ranking of goals for scoping order. **Not** part of defect ranking. | **Nothing.** No formula, no view sorts by it. | **Demote + rename** to `rank` — it name-collides with the computed Flow `priority`, the model's worst vocabulary trap. |

### 2.2 Topic — the controlled vocabulary

> One named subject of information, decomposed from exactly one goal via that
> goal's operations. Topics exist so required and actual flows can be
> *compared at all* — the diff matches on `(topic_id, to_actor)`.

| Field | Tier | Definition | Consumed by | Verdict |
|---|---|---|---|---|
| `topic_id` | 1 | Immutable key (T1…) minted during required-state derivation; the token every flow and decision is coded to at write-up — never live. | The match key of the entire diff; the hinge of goal attribution (flows and carriers deliberately carry no goal — they inherit it through Topic). | **Core.** |
| `name` | 1 | Short snake_case label (`design_change_notice`) interviewers recognize and code against. | Display only — matching runs on the ID. | **Keep.** |
| `goal_id` | 1 | The one goal this topic decomposes from. Deliberately single-parent: a subject serving two goals becomes two topics. | The single busiest edge: stamps the goal on every flow (Flows!L) and carrier (Carriers!O) — feeding involvement flags, alignment carries, GoalLens. ⚠ Unvalidated FK today; a typo propagates silently. | **Core.** |
| `operation` | 3 | The goal activity this topic serves — the middle link of goal → operation → topic, used as the enumeration checklist ("walk each activity, ask what information it needs"). | GoalLens "Operations block" grouping label only. Free text; two rows share an operation only by exact spelling. | **Keep (demote to grouping label).** Its real value is the *method step*, not the stored field. |
| `description` | 3 | One-two sentences drawing the topic's semantic boundary — what counts as this subject vs. a neighbor — tightened whenever an interview-coding call is close. | Humans at write-up. | **Keep.** Distinct job from `name` (label vs. boundary) and from Flow `rationale` (what the subject is vs. why a movement is needed). |

### 2.3 Actor (Stakeholder) — the nodes

> One row per person, team-modeled-as-one, or external party that produces or
> consumes information. Every flow endpoint, meeting seat, decision letter, and
> goal owner is a foreign key into this table.

| Field | Tier | Definition | Consumed by | Verdict |
|---|---|---|---|---|
| `actor_id` | 1 | Immutable key (A1…) assigned at inventory; all references use it, so renaming a person breaks nothing. | Flow endpoints, WhiteSpace lanes, involvement flags, roster matching, RACI. | **Core.** |
| `name` | 1 | Display name from the org chart. | Display only. | **Keep.** |
| `role` | 3 | Free-text job title, so readers know who "A2" is. | **Nothing.** | **Demote.** Narrative context. |
| `group` | 1 | The organizational function / swim-lane (Quality, Operations, …) — the actor's coordinate on the WhiteSpace matrix and both maps. | Flows from_group/to_group → WhiteSpace matrix, map lanes. | **Core. Rename to `function`** — ends the collision with `kind`'s enum value "group"; the lite workbook already calls it `FuncL`. |
| `kind` | 3 | `{person \| group \| external}` — what sort of node this row models. | **Nothing.** And `kind='external'` double-encodes `group='External'`. | **Restructure:** `{person \| team}` only; externality lives in `function='External'`. One fact, one home. |
| `power`, `interest` | 3 | Two 1–5 judgments (ability to block/advance; degree of caring) recorded from sponsor scoping — the Mendelow grid axes. | **Nothing** — the grid view was never built. | **Demote** to a post-interview "pilot scoping" analyst block. Keep only if the Mendelow view ships; a newcomer cannot calibrate these at capture time. |

### 2.4 Channel — the standing media

> One row per standing non-meeting medium a flow can ride. Channels are the
> only carriers that can be asynchronous or persistent — the engine hardcodes
> every meeting to sync + ephemeral — so these attributes are what decide
> `latency_gap`, `channel_mismatch`, and SPOF mitigation.

| Field | Tier | Definition | Consumed by | Verdict |
|---|---|---|---|---|
| `channel_id` | 1 | Immutable key (C1…). | Carrier lookups. | **Core.** |
| `name` | 1 | Precise enough that interviewee and analyst mean the same artifact ("Supplier quality dashboard", not "the dashboard"). | Carrier display lookup. | **Keep.** |
| `type` | 3 | Category label `{email \| chat \| doc \| dashboard \| ticket \| in_person}` — what *kind* of thing it is, vs. how it behaves (next three fields). | **Nothing.** | **Demote** to descriptive label that *defaults* the functional trio; v2 adds consistency rules (`in_person ⇒ sync`). |
| `synchrony` | 1 | `{sync \| async}` — does use require both parties present in real time? | The `channel_mismatch` check (only the value `sync` is ever tested). | **Core.** |
| `persistence` | 1 | `{ephemeral \| searchable \| system_of_record}` — how durably content survives, judged by inspecting the medium. `system_of_record` = survives any individual, readable by non-participants. | The SPOF-mitigation test (only `system_of_record` is ever tested; `searchable` is computationally dead — flag for Oscar: keep for capture nuance or collapse). | **Core.** |
| `effective_cadence` | 1 | How often it ACTUALLY moves fresh information — from observed usage, not nominal capability. | The `latency_gap` check (fastest usable carrier vs. required max latency). | **Core.** |

### 2.5 Meeting (Ritual) — the recurring venues

> One recurring gathering per row, every claim backed by an artifact seen over
> the last three occurrences. **v2 naming decision: standardize on "Meeting"**
> (the lite workbook and the manual's prose already do); keep R-prefixed IDs.

| Field | Tier | Definition | Consumed by | Verdict |
|---|---|---|---|---|
| `ritual_id` | 1 | Immutable key (R1…). | Carriers, Decisions venue, Alignment. | **Core.** |
| `name` | 1 | The calendar name. | Display lookups. | **Keep.** |
| `owner_actor_id` | 1 | The single actor accountable for the meeting existing and being run; receives its findings first. | Only via the computed roster: counts as "in the room" for `a_absent` and stakeholder presence. Not costed unless also listed in attendees. | **Keep.** |
| `attendee_ids` | 1 | Every regular attendee, from invite lists cross-checked against who actually shows. Chronic spectators stay listed — CR5 judges whether they should be. | Headcount → cost; roster → `a_absent`, stakeholder %. ⚠ Semicolon-list format is an engine concession — v2 uses a proper attendees link table or multi-select. | **Core.** |
| `cadence` | 1 | Actual occurrence frequency from the calendar record, not the charter's aspiration. | Cost per week AND the latency rank of every flow this meeting carries. ⚠ Shared CadenceList lets you enter `continuous` (cost 0) — v2 sub-enums per field. | **Core.** |
| `duration_min` | 1 | Scheduled length of one occurrence. | Cost. | **Core.** |
| `inputs` | 3 | What material the meeting consumes — context for judging CR6. | **Nothing.** | **Demote:** this is CR6's unstructured evidence; in v2 it becomes exactly that (per-criterion evidence field). |
| `outputs` | 3 | What the meeting is *said* to produce. | **Nothing** — `output_evidence` is the load-bearing twin. | **Merge/demote:** keep at most as the descriptive home of Grove's "name the output" exercise; the proof lives in `output_evidence`. |
| `goal_ids` | 1 | The goals this meeting **CLAIMS** to serve — transcribed from the meeting's own charter/agenda *as stated, never inferred from what it carries*. That independence from Carriers is the deliberate design behind the theater verdict. | The claims half of AlignmentClaim; the classification's goal test. ⚠ Latent bug: matched by bare substring `SEARCH` — G1 false-matches inside G10 (§6.1). | **Core.** Not redundant with Carriers — the duality is the crown jewel. |
| `compliance_required` | 1 | Whether an external obligation (regulation, contract, mandate) forces this meeting to exist — from the obligation source, not the owner's assertion. | The `necessary_NVA` branch of classification. | **Core.** |
| `written_purpose_evidence` | 2 | Pointer to the artifact proving a written purpose exists — entered only after personally seeing it; empty = none exists. | The classification's t1 test. | **Merge** with CR1 (§4.1-R1): same fact captured twice, uncoordinated. |
| `output_evidence` | 2 | Pointer to the artifact proving real output. ⚠ Sentinel: text starting `"no "` counts as absence — invisible to a newcomer. | The classification's t2 test. | **Keep**; v2 makes the sentinel an explicit field or dropdown, not a string prefix convention. |
| `CR1–CR6` | 2 | Six pass/fail hygiene judgments (written purpose · action items logged · decisions findable by a non-attendee · output traces to a goal · right people, no chronic spectators · pre-read not live retelling), each entered **only after seeing the evidence artifact** over the last three occurrences. | criteria score → GoalLens/Alignment displays. | **Core** (schema locked — changes need Oscar). ⚠ The designed per-criterion *evidence* cells don't exist in the delivered workbook (§4.1-R1). |

### 2.6 Criterion — the rubric definitions

> One row per binary hygiene test. No formula reads this sheet — it operates
> **on the human**: `question` is what the scorer must ask, `evidence_expected`
> is what they must see before entering TRUE. Keep all four fields; they are the
> anti-opinion guardrail, and the documented extension point. ⚠ Criterion
> identity is currently encoded three times (Criteria rows, Rituals column
> headers, failed-criteria display tokens) with nothing enforcing agreement —
> v2 derives the latter two.

### 2.7 Flow — the atom (two states in one table)

> One unit of "consumer must/does hear topic X from producer Y." **The
> verified structural finding: Flow is a discriminated union** — two entities
> sharing an identity block, wearing one table. Six of eleven input columns are
> meaningful in only one state, which is the single biggest newcomer trap in
> the workbook. v2 presents two capture forms (Required need / Observed flow)
> over one logical store.

**Shared identity (both states):**

| Field | Tier | Definition | Verdict |
|---|---|---|---|
| `flow_id` | 1 | Immutable key. FR/FA prefix convention informally re-encodes `state` — harmless, but v2 treats `state` as authoritative and never parses ID spelling. | **Core.** |
| `state` | 1 | `{required \| actual}` — which half of the diff. Required rows are derived from goals and owner-signed *before* interviews; actual rows are written up from two-ended interviews. | **Core.** |
| `topic_id` | 1 | The controlled-vocabulary subject — half of the cross-state match key. | **Core.** |
| `from_actor` | 1 | Producer: the source the goal demands (required) / who interviews say actually sends it (actual). Drives `wrong_producer`. | **Core.** |
| `to_actor` | 1 | Consumer — the other half of the match key. The match rule deliberately pairs on `(topic, to_actor)`: the consumer's need is the unit of satisfaction. | **Core.** |

**Required-state extension:**

| Field | Tier | Definition | Verdict |
|---|---|---|---|
| `criticality` | 1 | 1–5 goal damage if this flow fails, set with the goal owner at sign-off. The engine consumes exactly three facts: `=5` arms the pull-only rule, `≥4` arms SPOF, and the number multiplies status weight into priority. | **Core**, but v2 captures it as an anchored enum — `critical(5) · important(4) · routine(2)` — with the 1–5 number as an advanced override. Verified: no formula changes needed. |
| `required_max_latency` | 1 | The slowest delivery cadence the goal tolerates, compared against the fastest usable carrier. | **Core.** ⚠ v2 sub-enum: `ad_hoc` (rank 99) can never fail and doesn't belong here. |
| `channel_class_required` | 1 | `{sync \| async \| any}` — "sync means a conversation, not a message." | **Keep** — but `async` is computationally identical to `any` today (§4.4). Oscar's call: implement the async check or collapse to `{sync, any}`. |
| `rationale` | 2 | One line on why the goal needs this flow — the artifact each goal owner signs in conversation. The catchball anchor. | **Keep** (process-load-bearing, formula-inert). |

**Actual-state extension:**

| Field | Tier | Definition | Verdict |
|---|---|---|---|
| `confidence` | 1 | `{confirmed \| claimed \| disputed}`: both ends said it · one end only · the ends contradict — and `disputed` **automatically quarantines** the row from every status, verdict, and count, surfacing it as its own follow-up list. | **Core.** ⚠ Only the `disputed`/not-disputed boundary is load-bearing today; the manual's promised "covered but only one side confirmed it" flag is unimplemented — v2 should implement it (cheap, honest) rather than collapse the enum. Consider renaming the field `corroboration` (it is not a confidence scale). |
| `evidence` | 2 | The artifact proving the flow exists (agenda item, recurring email, dashboard URL) — the anti-hearsay discipline. | **Keep** (human trail; dashboard hover text). |

### 2.8 Carrier — the humble binding

> One row per (actual flow, venue) pair: "through what does this travel?"
> Four typed cells feed the latency, sync, and pull-only checks, the SPOF
> mitigation test, and the entire *carries* half of AlignmentClaim. A flow with
> no carrier is hearsay — and currently reads as `latency_gap` (a documented
> but surprising rule worth a friendlier surface in v2).

| Field | Tier | Definition | Verdict |
|---|---|---|---|
| `flow_id` | 1 | Which actual flow this venue moves. ⚠ Pointing at a required row is a *silent no-op* — v2 validates. | **Core.** |
| `carrier_type` | 1 | `{ritual \| channel}` — selects the inventory and hardcodes venue semantics: meetings are always sync + ephemeral; channels bring their own attributes. | **Core.** v2 models one **Venue** interface (`cadence, synchrony, persistence`) with Meeting and Channel implementing it — the engine already treats them that way. |
| `carrier_id` | 1 | The specific meeting or channel. This is precisely the independent *carries* evidence AlignmentClaim crosses against `goal_ids`. | **Core.** |
| `mode` | 1 | `{push \| pull}` per link — delivered to the consumer, or must the consumer remember to check? Only consumed by the crit-5 pull-only rule. | **Keep.** |

### 2.9 Decision — the RACI-vs-reality probe

> One recurring, named decision: paper rights vs. the evidenced venue of its
> most recent instance.

| Field | Tier | Definition | Consumed by | Verdict |
|---|---|---|---|---|
| `decision_id` | 1 | Immutable key. | Row identity/links only. | **Core.** |
| `name` | 1 | Plain-language label a non-attendee recognizes. | Display. | **Keep.** |
| `topic_id` | 1 | The vocabulary topic the decision is about. | **Nothing today** — see the adjudication below. | **Core in v2** (becomes the goal anchor). |
| `goal_id` | — | The goal, typed independently — the value the engine actually trusts today. | Alignment `decisions_decided`; BY GOAL rollup. | **Merge → computed.** See adjudication. |
| `accountable` | 1 | The ONE person who owns it on paper (loader-enforced). Deliberately blank when nobody owns it — that blank IS the `no_accountable` finding. | The decision-defect verdict. | **Core.** |
| `responsible`, `consulted` | 3 | The R and C letters, recorded for the rights picture; never checked against anything. | **Nothing.** | **Demote** to the redesign layer (used when charting RAPID/DARE fixes, per the model's own scoping rule: chart high-value/high-frequency decisions only). |
| `informed` | 3 | The I letter. | **Nothing.** | **Cut from capture** — an "informed" entry *is* a required flow on the decision's topic; model it as one and the diff engine can actually check it. The one RACI letter the framework makes literally redundant. |
| `actual_venue_type` | 1 | Where the LAST instance actually got decided: `{ritual \| channel \| ad_hoc \| none_observed}` (ground truth; cheat sheet documents only two of these). | Defect branch + alignment counting. ⚠ `channel` and `ad_hoc` currently fall through to unconditional `aligned` — a verdict hole (§6.2). | **Core**, with all four values given explicit verdicts in v2. |
| `actual_venue_id` | 1 | The specific venue of the last instance. | Roster fetch → `a_absent`; alignment. | **Core.** |

**Adjudication — the goal_id / topic_id split.** The three review passes
disagreed here (one says derive goal from topic; one says keep goal and demote
topic). Resolution, consistent with the model's own spine: **v2 anchors
Decision to `topic_id` (required, validated) and computes goal exactly as Flows
already does.** Two facts that can disagree — the typed goal vs. the topic's
goal — currently make a decision count under a goal its topic doesn't serve,
silently. The lite workbook's goal-only capture stays legal as a *provisional*
state flagged "needs topic coding" during migration, mirroring how interview
answers are coded to the vocabulary at write-up.

---

## 3 · Data dictionary — computed verdicts (never typed)

These are the model's outputs. None are redundant *with each other* — each
answers a distinct question — but the current workbook surfaces ~40 helper
columns around them that are pure engine plumbing (§4.2).

| Verdict | Question it answers | Computed from | Status |
|---|---|---|---|
| **FlowStatus** | "Is this required flow served — and if not, what exactly is broken?" Strict cascade: `missing → wrong_producer → latency_gap → channel_mismatch → covered`; first failed check names the defect *and its fix family*. | Both flow states + carriers, quarantine-filtered. | **Core — crown jewel.** Note: as delivered it is a **5-value** enum; `disputed` is not a status but a quarantine property of *actual* rows (the docs' "six-way" framing should be corrected, or an explicit sixth branch added — Oscar's call, it touches the locked cascade). |
| **priority** | "Fix what first?" `criticality × status-weight` (3 / 2 / 2 / 1.5 / 0), max 15. | criticality + FlowStatus. | **Core.** The name stays; Goal's field gets renamed (§4.1-R5). |
| **AlignmentClaim verdict** | "Does this meeting claim this goal, and does it actually carry it?" `aligned / claims_no_contribution ("theater") / unclaimed_contributor / —`. | claims: `goal_ids` alone · carries: usable+required carrier links landing in the meeting + decisions actually decided there. | **Core — crown jewel.** The two sources are independent BY DESIGN; their disagreement is the signal. Quarantined and unrequired ("extra") traffic earns no contribution credit — both rules verified in the formulas. |
| **RitualHealth** (criteria %, cost, VA class) | "Is this meeting run well, what does it cost weekly, and has it any right to that cost?" | CR scores; cadence × duration × headcount; three tests t1/t2/t3. | **Core** — with one verified correction: **the delivered "feeds a goal" test reads the claims side** (`goal_ids` non-empty), not carries — so a theater meeting with paperwork can score VA. v2 recomputes t3 from the carry side (carriers + decisions), making classification consume the alignment engine instead of running a weaker parallel test. |
| **DecisionDefect** | "Do paper rights and reality diverge?" `aligned / a_absent / none_observed / no_accountable`. | accountable + venue + venue roster. | **Core.** Extend to cover `channel`/`ad_hoc` venues explicitly (§6.2). |
| **SPOF risk** | "Which delivered critical flows survive only as long as one person shows up?" | criticality ≥4, single delivery path, zero `system_of_record` carriers. | **Core.** ⚠ Workbook predicate (single-path) and pipeline predicate (sole-producer) differ — unify in v2 (§6.4). |
| **Findings taxonomy** | The output contract: defects, disputed follow-ups, extra flows, theater, unclaimed, decision flags, SPOF, orphan meetings, overload, isolation — each stamped with its goal. | All of the above. | **Core.** Overload and isolation exist only in the pipeline, not the workbook — v2 should compute them in one place. |

---

## 4 · The redundancy audit

### 4.1 Confirmed redundancies (each adversarially verified)

- **R1 — Meeting purpose is captured twice, uncoordinated.**
  `written_purpose_evidence` (feeds VA classification) and `CR1 written_purpose`
  (feeds criteria score) are independent entries of the same fact and can
  contradict. Verified fix, needs Oscar (locked schema): instantiate the cheat
  sheet's own designed-but-never-built `ritual_scores` shape — per-criterion
  **pass + evidence** — and derive the classification's t1 from CR1. The
  evidence guard must follow `output_evidence`'s pattern (a value like "no
  charter found" must not auto-pass). Zero-break v1 step: make t1 read CR1.
- **R2 — `outputs` shadows `output_evidence`; `inputs` is CR6's evidence.**
  Neither free-text field is read by anything. Merge/demote (§2.5). Verified
  caveat: don't concatenate into `output_evidence` — the `"no "` sentinel would
  corrupt the t2 test.
- **R3 — Decision stores its goal twice** (typed `goal_id` + derivable via
  `topic_id`). Resolution in §2.9.
- **R4 — Externality is encoded twice on Actor** (`kind='external'` and
  `group='External'`), and `kind`'s value "group" collides with the *field*
  `group`. Fix: `function` (swim-lane, incl. External) + `kind {person|team}`.
- **R5 — Two unrelated "priorities."** Goal's inert input vs. Flow's computed
  defect score. Verified resolution: rename the **Goal** side (`rank`) — the
  published method vocabulary already owns "priority" for the defect score.
- **R6 — `state` is informally duplicated by the FR/FA id prefix.** Keep IDs
  opaque; `state` is authoritative.
- **R7 — Engine plumbing masquerading as model.** The MAX+1 rank idiom exists
  in ~6 copies (defect_rank, risk_rank, lens/theater/unclaimed ranks…), the
  delimiter-wrapped roster in 3 copies, the GoalLens lens_rank helper in 4
  copies, and Carriers denormalizes six Flow/venue fields (topic, to, state,
  confidence, cadence, sync, persistence, goal) purely because COUNTIFS can't
  join. **None of this is the model** — in any v2 engine (SQL, Python, app)
  every one of these ~40 columns disappears into queries. The dictionary's
  rule: *if it exists only so a spreadsheet formula can see it, it is not a
  variable of the framework.*
- **R8 — `Channel.type` soft-determines `synchrony`/`persistence`.** Keep as a
  defaulting label, explicitly non-load-bearing.
- **R9 — Criterion identity triple-encoded** (Criteria rows / CR column
  headers / display tokens). Derive from one source in v2.

### 4.2 Verified false positives — deliberate dualities to protect

- **`goal_ids` (claims) vs. Carriers (carries).** Not redundancy. The two
  independent sources ARE the theater verdict. Locked.
- **CR4 `goal_traceable` vs. t3 vs. AlignmentClaim.** Three goal-linkage
  encodings, but distinct questions: CR4 = evidence-judged output traceability
  (human), t3 = claims (should become carries, §3), verdict = the cross. After
  the t3 fix, each has a distinct job.
- **`confidence` vs. `evidence`.** Structured strength vs. human-readable
  artifact trail. Keep both.
- **Topic `name` vs. `description`.** Label vs. boundary definition.
- **`matched` (actual flows) vs. `carrier_cnt` (carrier links).** A real
  distinction — a matched flow with no carriers is hearsay — but it belongs in
  the engine, not the schema surface.

### 4.3 Fields no formula and no view reads (process-only by fact)

`Goal.priority` · `Actor.role` · `Actor.kind` · `Actor.power` ·
`Actor.interest` · `Channel.type` · `Ritual.inputs` · `Ritual.outputs` ·
`Decision.topic_id`* · `Decision.responsible` · `Decision.consulted` ·
`Decision.informed` — (*promoted to the anchor in v2, §2.9.)

None of these is *worthless* — most are process instruments (scoping,
feedback ethics, redesign grammar). The redesign decision is to **label them
honestly as a distinct class** ("inputs to the engagement, not to the model")
and move them off the day-one capture path.

### 4.4 Computationally dead enum values (decisions for Oscar)

| Value | Reality | Options |
|---|---|---|
| `confidence = claimed` (vs `confirmed`) | Only `disputed`/not-disputed branches anywhere; the manual's "covered, one side only" flag is unimplemented. | Implement the flag (recommended) or document as metadata. |
| `channel_class_required = async` | Behaves exactly like `any`. | Implement the async-required check (symmetric to sync) or collapse to `{sync, any}`. |
| `persistence = searchable` | Only `system_of_record` is ever tested. | Keep for capture nuance (recommended) or collapse. |
| `actual_venue_type = channel`, `ad_hoc` | Fall through to unconditional `aligned`. | Give each an explicit verdict (§6.2). |
| `required_max_latency = ad_hoc` (rank 99) | Can never produce a latency gap. | Exclude from the latency sub-enum. |

---

## 5 · The day-one capture core (~27 fields)

Verified: these produce the diff, the theater verdict, and the decision
defects. Everything else is Tier 2 (meeting audit) or Tier 3 (process).

- **Goal**: id, name, owner
- **Topic**: id, name, goal
- **Actor**: id, name, function
- **Channel**: id, name, synchrony, persistence, effective_cadence
- **Meeting**: id, name, owner, attendees, cadence, duration, goal_ids
  (claims), compliance_required
- **Required need**: topic, from, to, criticality (3-level), max_latency
  (+ channel_class where sync matters)
- **Observed flow**: topic, from, to, corroboration, carriers (venue + mode)
- **Decision**: name, topic, accountable, venue_type, venue_id

The three-tier presentation is itself the answer to "hard to understand for
someone who doesn't know the architecture": the current workbook presents all
71 fields at once with equal visual weight; the redesigned tool presents ~27,
and the analyst discovers Tiers 2–3 when they need them.

---

## 6 · Latent bugs & divergences found during this audit
*(independent of any redesign choice — worth fixing in the current generators)*

1. **Goal-claim matching is un-delimited substring SEARCH** (Alignment
   `claimed`): `G1` false-matches inside `G10` the day a tenth goal exists.
   Fix with the `";"&id&";"` guard the decision-defect formula already uses.
   Same pattern audit for `Alignment.flows_carried`, which matches ritual IDs
   without checking `carrier_type`.
2. **Decisions in `channel`/`ad_hoc` venues score `aligned` unconditionally** —
   no accountable-presence check, no distinct flag. An ownerless drift pattern
   (`ad_hoc`) currently passes.
3. **VA classification's goal test reads claims, not carries** — contradicts
   the cheat sheet's own definition ("feeds a goal's flows/decisions"), and a
   theater meeting with paperwork scores VA.
4. **Two SPOF definitions**: the workbook ranks single-delivery-path flows;
   the pipeline tests sole-producer; the docs say sole-producer. Unify.
5. **Stakeholder involvement flags implement "flows only"** while the cheat
   sheet defines the goal's stakeholder set as the union over flows, rituals,
   and decisions.
6. **Doc drift**: "six-way status" vs. the implemented 5+quarantine;
   `decisions_hosted` (cheat sheet) vs. `decisions_decided` (workbook);
   Ritual cadence enum documented as 4 values, delivered as 7; the cheat
   sheet's 4-value latency list vs. the delivered 7.

---

## 7 · What v2's stored model looks like (the target of the next step)

Six stored entities — everything else computed:

```
Goal(id, name, owner→Actor, rank°)                       ° = process-only tier
Actor(id, name, function, kind{person|team}, role°, power°, interest°)
Topic(id, name, goal→Goal, operation°, description°)
Venue = Meeting(id, name, owner→Actor, attendees[→Actor], cadence,
                duration_min, claims[→Goal], compliance_required,
                criteria_scores[CR×{pass, evidence}]², inputs°, outputs°)
      | Channel(id, name, synchrony, persistence, effective_cadence, type°)
Flow  = Need(id, topic→Topic, from→Actor, to→Actor,          ² = audit tier
             criticality{critical|important|routine}, max_latency,
             channel_class, rationale²)
      | Observation(id, topic→Topic, from→Actor, to→Actor,
             corroboration{confirmed|claimed|disputed}, evidence²,
             carriers[{venue→Venue, mode{push|pull}}])
Decision(id, name, topic→Topic, accountable→Actor, venue_type,
         venue→Venue?, responsible°, consulted°)   [informed° → model as Need]
```

Verdicts (FlowStatus, priority, AlignmentClaim, RitualHealth, DecisionDefect,
SPOF, Findings) are pure functions over these — no helper columns, no
denormalized copies, no hand-maintained cross joins (the goal×meeting matrix
is generated). The claims/carries duality, the quarantine rule, the
(topic, consumer) match key, and the strict status cascade carry over intact —
they are the framework; everything removed above was scaffolding.
