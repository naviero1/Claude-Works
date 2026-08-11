# Part–Supplier Risk Model

`Part_Supplier_Risk_Model.xlsx` — one consolidated, simplified tool to decompose each
model into its parts (tissue and non-tissue) and assess the risk of every
**part–supplier combination**.

It replaces two earlier attempts:

| Prior tool | What it had | What held it back |
|---|---|---|
| `Part_Supplier_RiskAssessmentTool_v2` | The right structure — part rows linked to candidate suppliers, grouped criteria | ~60 columns, no working scoring, broken formulas |
| `supplier_risk_tool_v12_WIP` | A developed scoring engine — 7 weighted pillars, overrides, dependency multipliers | Supplier-level only (no part view), ~120 columns, Z-scores/PPM/Cpk inputs our small suppliers can't provide |

## How it works

- **MODELS** — one row per model/project (with or without tissue parts) plus its
  production volume per quarter. Rolls up counts and band automatically.
- **SUPPLIERS** — each supplier scored **once**: two **base** 1–5 scores (Stability, External Factors) plus flags (2 red + 3 yellow slots). Flags are supplier-level only. Each yellow flag automatically bumps the score it affects — routed by an editable "Affects" tag on LISTS — into **adjusted** Stability/External columns (+1 per flag, capped at 5), which is what part rows inherit through the normal 20%/10% weights. Any red flag (bankruptcy, permitting issues, recall, stop-ship, site loss…) makes **every part row of that supplier** CRITICAL.
- **PART_RISK** — one row per part–supplier combo. Enter: model, part, type (Tissue APHIS / Tissue Non-APHIS / Non-Tissue Custom / Non-Tissue COTS), quantity per model, supplier, three part-level 1–5 scores (Sourcing & Backup, Quality & Compliance, Capacity), and Impact (1–5). Part-specific emergencies are scored, not flagged: EOL → Sourcing 5, stop-ship on one part → Quality 5, noted in Mitigation/Notes. Inherited supplier flags display in an auto column. Quarterly consumption (qty × model volume) computes automatically.
- **DASHBOARD** — portfolio KPIs, risk by model, a model selector that lists the selected model's parts ranked by risk (red flags always on top), and the Top 10 risks across all models.
- **SCORING_GUIDE** — plain-language 1/3/5 anchors for every criterion, editable weights and thresholds, red- and yellow-flag definitions, method sources, and design notes.

**Score:** Likelihood (weighted average of the five 1–5 criteria: 25/25/20/20/10,
using each supplier's adjusted Stability/External scores) × Impact (1–5) =
Risk 1–25. Bands: ≥15 CRITICAL, 7–14.9 MONITOR, <7 LOW.
Any **red flag** on a supplier (permitting issues, stop-ship, recall, cert
lapse, exiting, insolvency, import block, site loss) forces all its rows
CRITICAL regardless of the numbers. **Yellow flags** are early warnings
(welfare violations, poor communication, financial warning signs, weather
exposure, logistics disruption…) that raise the supplier score they're
evidence for. Base = steady state, flags = current events — never both for the
same thing. Flag lists and their routing are editable on the LISTS sheet.

## Why this design (sources)

- Two-axis logic (supply risk × business impact per purchased item): [Kraljic's purchasing portfolio matrix, HBR 1983](https://en.wikipedia.org/wiki/Kraljic_matrix).
- Likelihood × Impact on a 5×5 matrix with 15/7 cutoffs: standard [ISO 31000 / IEC 31010 risk-matrix convention](https://safetyculture.com/topics/risk-assessment/5x5-risk-matrix); same probability × severity logic as ISO 14971 medical-device risk files.
- "Stock-out before recovery" red flag: [Simchi-Levi's Time-to-Recover / Time-to-Survive framework](https://news.mit.edu/2022/companies-use-mit-research-identify-respond-supply-chain-risks-0615) (HBR 2014; used by Ford, Cisco, the UN) — a node where TTS < TTR exposes you in *any* disruption.
- Part-level assessment + `Last_Reviewed` column: [ISO 13485 §7.4 / FDA QMSR](https://www.neotas.com/21-cfr-820-fda-qmsr-supplier-control-guide-2026/) require supplier controls proportionate to the effect of the purchased product on device quality, plus a dated ongoing monitoring record.
- Z-score, PPM and Cpk thresholds were deliberately dropped as *inputs*: most of our suppliers are small private businesses where those numbers don't exist or aren't reliable. They survive as considerations inside the 1–5 anchors.

Example data (2 models, 6 suppliers, 6 part rows, all marked EXAMPLE) shows the
format — replace it with real data.

## Companion: Supplier_Scorecard.xlsx

`Supplier_Scorecard.xlsx` logs per-project supplier performance (Cost, Quality,
Lead time, Responsiveness → weighted Overall). Its **Risk Suggestions tab**
translates those averages into suggested 1–5 entries for the master model's
PART_RISK columns, one row per **part–supplier combo**: label the part, pick
the Supplier and the Process/part type that makes it, and the averages filter
to that supplier's projects of that process (Process blank = all their
projects) — so the two tools aren't islands:

- **Quality_Compliance** ← 6 − avg Quality *of the combo*
- **Capacity** ← 6 − avg Lead time *of the combo*
- **Supplier_Stability** ← 6 − average(Responsiveness, Cost) across **all**
  the supplier's projects — stability is about the supplier as a business, and
  cost (no part-level column in the register) feeds it as evidence
- Sourcing_Backup, External_Factors and Impact have no scorecard equivalent —
  scored by judgment in the master model.

Suggestions are rounded, clamped to 1–5, and meant as starting points; the
Projects column shows how much evidence sits behind each.
