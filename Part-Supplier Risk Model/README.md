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

- **MODELS** — one row per model/project (with or without tissue parts). Rolls up counts and band automatically.
- **SUPPLIERS** — each supplier scored **once** on two 1–5 criteria (Supplier Stability, External & Location). Every part row inherits them.
- **PART_RISK** — one row per part–supplier combo. Enter: model, part, type (Tissue APHIS / Tissue Non-APHIS / Non-Tissue Custom / Non-Tissue COTS), supplier, three part-level 1–5 scores (Sourcing & Backup, Quality & Compliance, Capacity & Delivery), Impact (1–5), and an optional Red Flag.
- **DASHBOARD** — portfolio KPIs, risk by model, a model selector that lists the selected model's parts ranked by risk (red flags always on top), and the Top 10 risks across all models.
- **SCORING_GUIDE** — plain-language 1/3/5 anchors for every criterion, editable weights and thresholds, red-flag definitions, method sources, and design notes.

**Score:** Likelihood (weighted average of the five 1–5 criteria: 25/25/20/20/10)
× Impact (1–5) = Risk 1–25. Bands: ≥15 CRITICAL, 7–14.9 MONITOR, <7 LOW.
Any red flag (permit lapse, EOL, stop-ship, supplier exiting, stock-out before
recovery, capacity exceeded) forces CRITICAL regardless of the numbers.

## Why this design (sources)

- Two-axis logic (supply risk × business impact per purchased item): [Kraljic's purchasing portfolio matrix, HBR 1983](https://en.wikipedia.org/wiki/Kraljic_matrix).
- Likelihood × Impact on a 5×5 matrix with 15/7 cutoffs: standard [ISO 31000 / IEC 31010 risk-matrix convention](https://safetyculture.com/topics/risk-assessment/5x5-risk-matrix); same probability × severity logic as ISO 14971 medical-device risk files.
- "Stock-out before recovery" red flag: [Simchi-Levi's Time-to-Recover / Time-to-Survive framework](https://news.mit.edu/2022/companies-use-mit-research-identify-respond-supply-chain-risks-0615) (HBR 2014; used by Ford, Cisco, the UN) — a node where TTS < TTR exposes you in *any* disruption.
- Part-level assessment + `Last_Reviewed` column: [ISO 13485 §7.4 / FDA QMSR](https://www.neotas.com/21-cfr-820-fda-qmsr-supplier-control-guide-2026/) require supplier controls proportionate to the effect of the purchased product on device quality, plus a dated ongoing monitoring record.
- Z-score, PPM and Cpk thresholds were deliberately dropped as *inputs*: most of our suppliers are small private businesses where those numbers don't exist or aren't reliable. They survive as considerations inside the 1–5 anchors.

Example data (2 models, 6 suppliers, 6 part rows, all marked EXAMPLE) shows the
format — replace it with real data.
