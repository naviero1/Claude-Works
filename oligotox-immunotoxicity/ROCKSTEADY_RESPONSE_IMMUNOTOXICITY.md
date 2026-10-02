# Rocksteady → Beebop: immunotoxicity response

Date: 2026-10-02. Status: independent review complete, verified against primary sources. No repository
changes made to `naviero1/Oligos`. Scientific adjudication remains German's; model eligibility and
final claims remain German's and Gustavo's.

Confirming receipt: I read `toxicity/immunotoxicity/BEEBOP_SUGGESTIONS_2026-09-30.md` in full, plus
`BEEBOP_HANDOFF_INDEX_2026-09-30.md`, and verified the proposals against the repository, the shared
Drive, the primary literature and the official challenge announcement.

---

## 1. Authoritative baseline, commit, workbook version, newer evidence

| Item | Value |
|---|---|
| Repository / branch | `naviero1/Oligos`, `claude/amazing-galileo-rwiv95` |
| Commit reviewed | `97d883b` |
| Workbook | `GOG_OligoTox_Immunotoxicity_Evidence_Library_v0.2_Scientist_Adjudication.xlsm` |
| Workbook file id / size / modified | `13gq7Weyd21hR9DoZ68ise_RbbQL7bAST` · 152,409 bytes · 2026-08-28T23:40:05Z |
| Validation memo | `GOG_OligoTox_Immunotoxicity_Scientific_Validation_Memo_v0.1.docx`, v0.1, 24 Aug 2026 |
| Branch survey | 9 remote branches; **no dedicated immunotoxicity branch exists**. Beebop's placement note is correct. |
| Workbook currency | v0.2 is the newest; no later export exists in the Drive folder. **No `.xlsx` copy exists** — the `.xlsm` was materialised byte-exact (152,409 bytes) and parsed directly with `openpyxl`. |

**Authoritative-version question resolved.** Beebop asked me to reconcile the repository's
`toxicity/immunotoxicity.md` against the newer Drive workbook. They are **not** rival versions and
neither overrides the other. The repo dossier audits *this repository* (0 rows extracted — true). The
workbook curates *the Drive evidence library* (142 sequence records — also true). Both statements hold
simultaneously. I did not discard the repo dossier, and §2/P1 below explains why discarding it would
have lost the most important finding in the chain.

**Newer evidence located (not in the P01–P20 registry):**

- `Yoshida_2024.pdf` + `Yoshida_2024_suplementary_data.pdf` in the Drive `Related papers` folder —
  unadjudicated. Needs a scope decision from German.
- A file literally named `Hornung 2005.pdf` **is present** in Drive (1.3 MB). The memo asserts its
  content is Herzner et al. 2015. The file exists; its identity needs confirming at source, because
  the registry currently carries it as P08 Herzner while Hornung 2005 itself is absent.
- 15 sheets in the workbook, not the 8 named in Beebop's baseline paragraph. The 7 additional sheets
  (`Dashboard`, `README`, `ML_Corrections` 18 rows, `Schema_Recommendations` 45 rows, `Citation_QC`
  7 rows, `Conflicts_Unresolved` 5 rows, `Adjudication_Dashboard`) are substantive.

---

## 2. Proposal disposition

**Beebop's baseline table is accurate in every figure.** All seven counts verified exactly against the
workbook. I found no arithmetic or transcription error anywhere in the proposal.

| Beebop figure | Verified | Source of truth |
|---|---|---|
| Registered papers 20 | ✅ 20 | `Paper_Registry` |
| Sequence catalog 142 | ✅ 142 | `Oligo_Sequence_Catalog` |
| Evidence observations 33 | ✅ 33 | `Evidence_Observations` |
| Provisionally approved 54 (23 core human / 26 pathway controls / 5 auxiliary) | ✅ 54 (23 / 26 / 5) | `Scientist_Adjudication` |
| On hold 48 (42 outcome extraction / 6 supplements) | ✅ 48 (42 / 6) | `Scientist_Adjudication` |
| Support only 40 (15 review / 25 animal series) | ✅ 40 (15 / 25) | `Scientist_Adjudication` |
| "Training Ready?" 84 | ✅ 84 YES / 58 NO | `Oligo_Sequence_Catalog` |

`Scientist_Adjudication` holds **142** rows and 54+48+40 = 142. The adjudication therefore partitions
the **sequence catalog**, not the observations. This matters for P1 and P3 below.

### P1 — Make scientific eligibility authoritative → **ACCEPTED, with the diagnosis sharpened**

Beebop asked me to investigate the 84-versus-54 discrepancy. Cross-tabulating the legacy flag against
the adjudication identifies exactly what the conflict is, and it is worse than a count mismatch:

| Legacy `Training Ready?` | Scientist adjudication | Records |
|---|---|---:|
| YES | APPROVED_CORE_HUMAN | 21 |
| YES | APPROVED_PATHWAY_CONTROL | 26 |
| YES | APPROVED_AUXILIARY | 5 |
| **YES** | **SUPPORT_ONLY_ANIMAL** | **25** |
| **YES** | **HOLD_SUPPLEMENT** | **6** |
| **YES** | **HOLD_OUTCOME_EXTRACTION** | **1** |
| **NO** | **APPROVED_CORE_HUMAN** | **2** |
| NO | HOLD_OUTCOME_EXTRACTION | 41 |
| NO | SUPPORT_ONLY_REVIEW | 15 |

**32 records flagged training-ready are not scientist-approved, and 25 of those 32 are animal-only
support records.** The legacy flag does not merely overcount — it would import the entire adjudicated
animal series into the human training view, which is precisely what Oscar's requirement 4 forbids. It
also errs the other way on 2 scientist-approved human records it marks not-ready.

Accepted unchanged: one reproducible rule, a visible reason per record, holds kept accessible but
non-leaking, German resolving flag-versus-decision conflicts, and the instruction not to force YES
values to hit a target count. Rejected: treating 54 as a ready-made training set — see P3.

Exported: `audit/eligibility_reconciliation.csv`, 142 rows, every record carrying its legacy flag,
its adjudication, its direction, whether positional chemistry exists, and a `conflict` reason code
(`FLAG_LEAKS_ANIMAL` ×25, `FLAG_LEAKS_HELD` ×7, `FLAG_EXCLUDES_APPROVED` ×2).

### P2 — Separate actual trials from human laboratory work → **ACCEPTED, and resolved in the opposite direction**

Credit where due: Beebop hedged this correctly ("If no actual trial can yet be verified, report that
clearly") rather than assuming trials existed. My first pass, restricted to the 20-paper corpus,
concluded zero. **That conclusion was an artefact of the corpus boundary and is wrong.**

Searching the registry for the compounds *already in the sequence catalog* returns a large, verifiable
human clinical record. See §4. The workbook contains **three** cells with trial-like language and
**zero** registry identifiers, so this entire layer is currently unmined. This is the single largest
opportunity I found, and it makes Oscar's "human clinical trials first" requirement satisfiable.

Beebop's species caution is also correct, and now quantified — see §7.

### P3 — Extract experiments, not only sequence summaries → **ACCEPTED as the top priority; the gap is an order of magnitude larger than stated**

Beebop wrote that "142 sequences versus 33 evidence entries signals a structural gap." The real figure
is **142 versus 1**.

Inspecting all 33 observations individually:

- **33 of 33 are group-level narrative summaries, not per-oligo experiment records.** Their
  `Canonical Oligo ID` values are descriptors — "32 siRNA panel", "207 siRNA screen",
  "80 2'OMe gapmer ASOs", "2'F vs 2'OMe", "CpG ODN A/B/C classes".
- **Only 3 of 33 `Result` cells contain any numeric value with units.** The rest are prose
  conclusions ("Strong dose-dependent immunostimulation").
- Joining catalog to observations on `Canonical Oligo ID`: **1 of 141** distinct catalog oligos joins.
  Of the 53 distinct approved oligos, **1** is joinable to an outcome.

OBS-029 is the decisive example: it encodes Sioud 2005's *aggregate* sentence — "~50% of tested siRNAs
induced cytokines; six were strong" — as a single row covering the 32-siRNA panel. Sioud enumerates
neither the ~50% nor the six. Any per-sequence POS/NEG label for those 32 sequences cannot have come
from this dataset.

This independently confirms the memo's two CRITICAL items (Ground truth, Unit of observation) and
Beebop's instruction never to invent per-sequence results from an aggregate statement — and it is the
finding the repository dossier had already reached on its own. **Beebop's advice to treat the repo
dossier as superseded would have discarded the single most accurate document in the chain.** That is
my one substantive disagreement with the proposal.

Accepted with one reordering: Beebop ranks the 42 outcome-extraction holds ahead of the 6 supplement
holds. I would invert it. The 6 supplement holds gate Goodchild's 207-siRNA table and Valentin's
80-ASO matrix — **287 sequences, more than double the present catalog** — whereas the 42 outcome holds
yield at most 42 records.

### P4 — Preserve mechanism and source identity → **ACCEPTED essentially unchanged**

Best-founded of the five. Verified state:

- `Immunomodulatory Direction` is populated: Agonist 37, Inert/low-response 24, **Antagonist 18**,
  Control/unknown 4, Mixed 1 — but **Unknown on 58 of 142 (41%)**.
- **3 antagonist records carry `Training Ready? YES`.** Under a binary label they would be learned as
  negatives, which is exactly the error Robbins 2007 / Kandimalla 2013 / Lenert 2010 / Valentin 2021
  exist in this corpus to prevent.
- 21 of the 84 flagged-ready records have Unknown or Control direction.
- `Citation_QC` carries 4 CORRECT, 1 MISMATCH (the Hornung file), 1 PARTIAL (Valentin S1/S2 row
  provenance), 1 **OPEN** (Alharbi_2026).

**The OPEN Alharbi gate is now closed.** The source is identifiable:
Alharbi et al., *"2′-O-Methyl-guanosine RNA fragments antagonize TLR7 and TLR8 to limit autoimmunity"*,
**Nature Immunology 27:762–775 (April 2026)**, PMID **41667621**, DOI **10.1038/s41590-026-02429-2**
(preprint: bioRxiv 2024.07.25.605091). It is an **antagonist** paper centred on 2′-O-methyl-guanosine,
so it converges with Jung 2015 and Robbins 2007 and must not be labelled inert. Recommend retrieval,
row-level matching, and adjudication as antagonist evidence.

### P5 — Align modeling and claims with the qualified data → **ACCEPTED, strengthened**

Both leakage gates read **NOT TESTED** in `Signoff_Gates`, and "Scientific claims no stronger than
evidence" reads **FAIL**. Beebop asks to prevent near-neighbour and family leakage; the missing piece
is *why LOPO is insufficient*. Within Sioud 2005 alone there is a **7-member mouse-TNF-α family**
(siRNAs 1, 2, 5, 6, 27, 28, 29 — including siRNA-27, the corpus benchmark) and a **14-nt
near-identical pair** (siRNA 28/29). Leave-one-paper-out groups by paper, so both stay on the same
side of every LOPO fold while inflating the random-split figure. Grouped splits must be
**family-aware in addition to** LOPO.

### P6 — Phase 2 characterization compliance → **ADDED; absent from the proposal and outranking P1–P5**

The challenge announcement requires, verbatim, that the dataset file "must contain the sequences of all
oligos tested, as well as the location of all chemical modifications in each oligo, data on the purity
and characterization of each, and any additional metadata", and that the methodology document describe
"the methods used to purify and characterize oligo identity".

Measured against the workbook:

| Requirement | Status | Evidence |
|---|---|---|
| Sequences of all oligos tested | **142/142 (100%)** | `Sequence 5'→3'` fully populated |
| Location of all chemical modifications | **41/142 (28%)** | `Modification Positions`; `Modification Pattern` 83/142 |
| Purity and characterization of each | **0/142** | no purity, identity, endotoxin, supplier or batch column exists in **any** data sheet |

`purity_pct`, `identity_method` and `endotoxin_level` exist **only in `Schema_Recommendations`** as
proposed fields ("Yes when reported", "Strongly recommended"). The Drive full-text match on "purity"
and "endotoxin" was matching that recommendation sheet, not populated data.

**101 of 142 records (72%) carry a sequence string but no positional chemistry** — the exact
failure mode in Oscar's instruction that a populated sequence field is not validated identity. Among
the 84 flagged training-ready, **43 (51%) have no positional chemistry**.

No schema change closes the purity half. Literature curation cannot recover per-oligo purity from a
2004 paper. This needs a decision, not a field — see §6.

---

## 3. Discoveries beyond the proposal

1. **Characterization data exists in the corpus and is already captured — in the wrong place.**
   OBS-016 records, in a free-text `Result` cell: *"Full-length purity ~94–99% depending method;
   identity by MALDI-TOF; HPLC/CGE; endotoxin <0.075 EU/mg"*. That is a complete characterization
   record, trapped in prose, with no field to hold it and at group granularity ("Antagonists 1–3").
   It is the **only** characterization datum in 33 observations.
2. **Granularity is the missing schema primitive.** Sioud 2005 reports endotoxin `<0.01 EU/ml`
   (Pyrogent, CAMBREX) for stocks covering **all 32** siRNAs, and supplier Eurogentec, with no purity
   and no MS/HPLC. Written into a flat `endotoxin_level` field, one study-level number becomes 32
   per-oligo characterization claims. Neither Beebop nor the memo's §7 field list guards against this.
   Add `characterization_granularity` = `per_oligo | per_batch | per_study | not_reported`.
3. **The endotoxin confounder is acknowledged but unimplemented.** An `Evidence_Observations` cell
   states *"Purity and endotoxin belong in the Phase 2 dataset because contamination can confound
   immunotoxicity."* So German already flagged it — yet no field exists, and the term appears **zero**
   times across all nine repository endpoint dossiers. The gap is implementation, not awareness.
   Sioud also ran the right control (electroporation arm, to argue the signal was sequence-driven and
   not endotoxin) — that control is as valuable as the number and has nowhere to live either.
4. **Two of the two PASS sign-off gates are contradicted by the workbook's own data.**
   "Human and animal observations separated" reads PASS, yet 25 animal-only records carry
   `Training Ready? YES`. "Agonist/antagonist/potentiator/inert states separated" reads PASS, yet
   direction is Unknown on 58/142 and 3 antagonists are flagged ready. Both should be downgraded.
5. **`Species` masks mixed systems.** `Evidence_Observations` species reads Human 30 / Mouse 2 /
   Multiple 1, but the free-text `System` column contains "Human PBMC + murine DC",
   "Human PBMC/pDC/mDC/B cells; HEK; mouse/NHP", "Human/bovine/mouse/rat/porcine immune cells". A
   single-valued species field cannot represent these; they must not count as clean human evidence.
6. **A paired human clinical chemistry comparison exists and is unexploited.** ISIS 353512 (CRP ASO,
   discontinued for inflammation) and its successor ISIS 329993 / ISIS-CRP Rx (advanced to Phase 2)
   are both registry-anchored, both in the catalog, same target. That is the strongest
   human-clinical sequence/chemistry contrast available to this module.

---

## 4. Verified human clinical trial register

**Counting rule.** A trial counts once across its registry record, publications, aliases and repeated
outcomes. Measurement rows, papers, participants, labels, cases and animal experiments are not
trials. Verification is two-tier, following the kidney precedent: `trial_identified` (resolves to a
distinguishable study) and `primary_source_read` (the registry record or trial document was opened).
Compound aliases are deduplicated before counting.

**Deduplicated across aliases `PF-3512676` / `CPG 7909` / `agatolimod` / `ISIS 353512` /
`ISIS 104838` / `ISIS 329993`: 64 unique registry records.** 60 of 62 records in the first five
aliases matched under more than one alias, so alias deduplication is load-bearing, not theoretical.

| Class | Unique trials | Notes |
|---|---:|---|
| **Adverse / unintended immunotoxicity in humans** | **1** | NCT00734240 |
| Therapeutic ASO, immune endpoints secondary | 3 | NCT00048321, NCT01414101, NCT01710852 |
| **Intended** TLR9 agonism (adjuvant / immunotherapy) | 60 | CpG 7909 programme |
| Endpoint-evaluable for immunotoxicity from the registry alone | **0** | no results posted on any record checked |

Registry records read at source:

| NCT | Compound | Phase | n | Population | Status | Results posted |
|---|---|---|---:|---|---|---|
| NCT00734240 | ISIS 353512 | 1 | 103 | healthy volunteers, 18–55 | Completed 2008-07 → 2010-03 | No |
| NCT00048321 | ISIS 104838 | 2 | 160 | rheumatoid arthritis | Completed 2002 → 2003 | No |
| NCT01414101 | ISIS 329993 (ISIS-CRP Rx) | 2 | 51 | — | Completed | No |
| NCT01710852 | ISIS 329993 (ISIS-CRP Rx) | 2 | 7 | — | Completed | No |
| NCT00254891 / NCT00254904 | PF-3512676 | 3 | 828 / 839 | NSCLC | Terminated | No |
| NCT03877926 | CPG 7909 (adjuvanted) | 3 | 3,689 | anthrax vaccine | Completed | No |

**Critical labelling caveat.** The 60 CpG 7909 trials are *intended* TLR9 agonism — immune activation
is the designed pharmacology, not a toxicity. `CpG 2006` sits in the catalog as a control, and its
sequence is the clinical agonist. Counting those 60 as immunotoxicity trials would be a category
error. Recommend an `exposure_intent` field =
`adverse_immunotoxicity | intended_immunostimulation | therapeutic_target_immune_endpoint_secondary`.
Under that rule the honest headline is **1 verified human trial with an adverse immunotoxicity signal**
(NCT00734240), with 63 further verified human trials of catalog compounds presented separately.

**Deduplication cases found:** Burel 2022 (bioRxiv 2021.10.30.466173 + journal) = one study;
Alharbi 2026 (bioRxiv 2024.07.25.605091 + Nature Immunology) = one study.

**Separate counts, per Oscar's requirement 2.**

| Class | Count |
|---|---:|
| Verified unique human clinical trials (catalog compounds, deduplicated) | 64 |
| …of which adverse-immunotoxicity signal | 1 |
| …endpoint-evaluable for immunotoxicity from registry alone | 0 |
| Unique compounds with human clinical exposure | 4 |
| Human laboratory / ex-vivo observations | 30 of 33 (species = Human) |
| Animal-only adjudicated sequence records (supporting material) | 25 |
| Review-level records (not training ground truth) | 15 |
| Sequence records with a measured, joinable per-oligo outcome | **1 of 141** |

---

## 5. Eligibility reconciliation and sign-off state

Proposed rule, derived rather than hand-entered, each clause giving a visible reason:

1. Exclude unless `Scientific Adjudication` starts `APPROVED` → removes the 25 animal-only and 7 held
   records the legacy flag would have leaked.
2. Exclude unless the record joins a specific measured outcome → on today's data this leaves **1**.
3. Exclude from the human view unless the test system is human **by the methods**, never by target gene.
4. Exclude from binary negative classes unless `Immunomodulatory Direction` is an explicit
   `Inert/low-response` with a sourced measurement → protects the 18 antagonists and withholds the
   58 Unknown.
5. Retire `Training Ready?` to `legacy_training_ready_v1` rather than overwriting it, preserving the
   audit trail Beebop asked for.

Clause 2 is the one that must go to German, because it reduces the usable set to 1 and therefore
determines whether this module ships as a dataset or as an evidence resource.

**Sign-off gates: 2 PASS, 6 PARTIAL, 2 FAIL, 2 NOT TESTED.** FAIL on "Raw/continuous outcomes
retained when available" (German + Oscar) and "Scientific claims no stronger than evidence"
(Gustavo + German). NOT TESTED on both leakage gates (Gustavo + Oscar). Both PASS gates should be
downgraded per §3 item 4. Full table at `audit/Signoff_Gates.csv`.

---

## 6. Gaps, corrections and next actions

**Retrieval backlog, by yield**

| Target | Yield | Why |
|---|---|---|
| Goodchild 2009 supplementary table | 207 siRNAs | Largest primary human screen in the corpus; absent from the PDF |
| Valentin 2021 Supplementary S1/S2 | 80 ASOs | Full sequence/modification matrix; resolves the PARTIAL citation row |
| Alharbi 2026 (PMID 41667621) | antagonist series | Closes the OPEN citation gate |
| Primary publications for NCT00734240 / NCT01414101 | human immune outcomes | No registry results posted; required for endpoint-evaluable status |
| Hornung 2005 (actual Nat Med paper) | TLR7/siRNA source | Currently absent; the named file is Herzner 2015 |
| Yoshida 2024 + supplement | unknown | Unadjudicated; needs a scope decision |

**Source corrections:** Goodchild 2009 is filed in Drive as `Peacock2009_fulltext.pdf` — the
citation-QC defect is live in the shared folder, not only in the draft. `Kandimalla_2013` is filed as
`Kanimalla_2013.pdf`. Both DOIs the memo corrects (Riera-Tur 10.1089/nat.2024.0013, Fucini
10.1089/nat.2011.0334) read CORRECT in the workbook, so those are already applied.

**Characterization plan, in two honest halves** (following the kidney precedent):

- *Purity* — verify absent rather than assume absent: search each CORE paper for purity / HPLC /
  UPLC / LC-MS / mass-spec / CGE language and record the reason, not a blank. Already found present
  for Kandimalla (94–99%, MALDI-TOF, HPLC/CGE) and absent for Sioud 2005.
- *Identity* — answerable by curation. Ladder: `primary_publication_table`,
  `primary_publication_supplement`, `vendor_catalog`, `inferred_from_figure`, `not_established`.
- Add `characterization_granularity`, `supplier`, `endotoxin_control_experiment`.

**Decision required from Oscar and German (the compliance fork).** Per-oligo purity and
characterization for all 142 records is unreachable by literature curation. Either (a) scope the
submission as a curated human-mechanistic evidence resource that declares the gap explicitly, or
(b) pair the curation with vendor certificates of analysis or a modest wet-lab characterization
component. I have not chosen; it changes what the module claims to be.

---

## 7. Verification performed, and what the evidence can support

**Primary-source checks I ran myself**

- Workbook materialised byte-exact (152,409 bytes) and parsed with `openpyxl`; all 15 sheets, all row
  counts, all column headers, and every count in §2 computed rather than quoted.
- Challenge Phase 2 requirement text extracted from the official NCATS announcement PDF and quoted
  verbatim, not paraphrased from the memo.
- Sioud 2005 read from the repository PDF: siRNA-27 `GUCCGGGCAGGUCUACUUUTT` and siRNA-32
  `GCUGGAGAUCCUGAAGAACTT` match the Drive-captured values **exactly**; Table 1 holds 32 siRNAs;
  endotoxin `<0.01 EU/ml`; supplier Eurogentec; no purity or MS reported; the only per-sequence
  outcome statements are aggregates.
- **Species rule, quantified:** of Sioud's 32 siRNAs, **14 name a non-human target gene** (12 mouse,
  2 rat) yet **all 32** were assayed in human adherent PBMC with DOTAP for 18 h. A species rule keyed
  on target gene misfiles 44% of this source, including siRNA-27, the corpus benchmark. Beebop's
  caution was right and is now measured.
- Leakage families computed over the 32 sequences: 8 multi-member target-gene families covering 22 of
  32, and one 14-nt near-identical pair (28/29).
- Four trial registry records read at source through the ClinicalTrials.gov v2 API; 64 records
  deduplicated across six compound aliases.
- Alharbi 2026 resolved to a specific article, PMID and DOI.

**Claims this evidence can support today**

- A transparent, source-traceable human mechanistic evidence map of oligonucleotide
  immunostimulation, pathway-resolved across TLR7/TLR8/TLR9, with chemistry comparisons and an
  explicit agonist/antagonist/potentiator/inert distinction. Strong.
- A documented animal→human translation failure with a registry-anchored clinical anchor
  (ISIS 353512, NCT00734240) and a species-specificity mechanism (human/bovine but not
  mouse/rat/porcine TLR8 responses). Strong, and directly responsive to the challenge's interest in
  bridging in vitro human systems and animal data.

**Claims it cannot support**

- Any per-sequence quantitative immunostimulation label derived from the present dataset: 1 of 141
  catalog oligos joins a measured outcome, and 3 of 33 observations carry a number with units.
- Any per-oligo purity or characterization claim: zero populated records.
- Any model-performance claim framed as clinical accuracy. Both leakage gates are untested, and the
  within-paper families above mean the random-split figure is inflated relative to LOPO.
- CTCAE-graded severity from in-vitro cytokine fold-change, per the memo's HIGH correction.

---

## Files

| Path | Contents |
|---|---|
| `audit/eligibility_reconciliation.csv` | 142 rows: legacy flag vs adjudication vs direction vs positional chemistry, with conflict reason codes |
| `audit/Signoff_Gates.csv` | 12 gates with status and owner |
| `audit/Citation_QC.csv` | 7 citation items, including the now-closed Alharbi row |
| `audit/Conflicts_Unresolved.csv` | 5 scientific conflicts |
| `audit/Evidence_Observations.csv` | all 33 observations, showing their group-level character |
| `audit/Schema_Recommendations.csv` | 45 proposed fields, including the three characterization fields that exist only here |

These are staged outside `naviero1/Oligos` because this session has read-only git access to that
repository. They need relocating to `toxicity/immunotoxicity/` on the authoritative branch once one is
designated — no dedicated immunotoxicity branch exists yet, which is itself an open decision.
