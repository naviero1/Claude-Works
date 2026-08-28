#!/usr/bin/env python3
"""Generate the KPI ledger markup from a single table of metric pairs."""
import html, pathlib

# domain, old metric, old formula, optimised for, failure COVID exposed, new metric, new definition, why it follows
ROWS = [
("Inventory",
 "Inventory turns", "COGS ÷ average inventory",
 "Capital efficiency, as one number covering the whole book. Higher was always better, and the board could read it without context.",
 "A high turn rate and a stockout look identical in the metric. It also prices a $3 line-stopping connector and a pallet of finished goods identically, because it can only see dollars — so the cheapest cut was always the most dangerous one.",
 "Inventory composition &amp; health", "Cycle · safety · strategic · excess &amp; obsolete, each with its own target",
 "Once you buffer by consequence rather than uniformly, the aggregate <em>must</em> move in confusing directions. The useful question stopped being how much inventory there is and became which inventory grew, and whether it is the inventory you chose."),

("Inventory",
 "Days inventory outstanding", "365 × average inventory ÷ COGS — one target for the enterprise",
 "A single, comparable, benchmarkable number that finance could set as a target and cascade down.",
 "A company-wide DIO target is a blunt instrument applied to a portfolio with hugely varying consequence. It was the mechanism by which planners were instructed to cut exactly the cheap, long-lead, sole-sourced parts that later stopped the line.",
 "Critical-component days of supply", "Tracked separately per risk-designated part, with a floor, exempt from the aggregate target",
 "You cannot let one target govern both a commodity fastener and a custom ASIC with a 52-week lead time. Carving critical parts out of the aggregate is what makes a deliberate buffer survive the next cost programme."),

("Sourcing",
 "Supplier count reduction", "Number of active suppliers, tracked downward",
 "Leverage, administrative cost, quality consistency. Consolidation was a stated strategic goal with a number attached.",
 "Supplier rationalisation and supply concentration are the same act, reported with opposite signs. Firms hit their consolidation targets and reported it as progress right up until the single remaining source went offline.",
 "Single-source exposure &amp; concentration", "% of spend and % of critical BOM on one source; supplier concentration index",
 "The identical underlying fact — few suppliers — now carries the sign it always deserved. What was an achievement metric became an exposure metric."),

("Sourcing",
 "Purchase price variance", "Actual purchase price − standard cost",
 "Unit cost, measured per buyer, per quarter. The single most powerful individual incentive in procurement.",
 "PPV rewards awarding volume to the cheapest single source and actively penalises paying to qualify a second one. The cost of resilience lands in this metric; the benefit never does. This is the incentive that built the fragility.",
 "Total cost of ownership incl. risk", "Landed cost + qualification + carrying + expected disruption cost",
 "If the second source's cost is charged to the buyer and its benefit is charged to nobody, no buyer will ever qualify one. Making the disruption term explicit is the only way the trade-off gets made at the level where it is decided."),

("Sourcing",
 "Tier-1 audit &amp; scorecard coverage", "% of direct suppliers audited and scored",
 "Quality, delivery and compliance assurance across the suppliers you actually contract with.",
 "Dual-sourcing tier one is worthless if both tier ones buy from the same tier two, who buys from the same tier three. Firms with perfect tier-1 coverage discovered their true dependency only when it stopped.",
 "<em>n</em>-tier visibility coverage", "% of critical BOM mapped to tier 2 / 3, with site-level geolocation",
 "Correlated failure lives below tier one. A map that stops at your contractual boundary cannot show you the shared node that makes your two suppliers one supplier."),

("Planning",
 "Forecast accuracy — MAPE", "mean(|actual − forecast| ÷ actual)",
 "A single-number report card on the demand plan, comparable across periods and planners.",
 "MAPE scores a point forecast, but an inventory decision is a statement about a <em>tail</em>. It also penalises volatile, high-consequence items hardest, so the planner's rational move is to focus on the SKUs that matter least.",
 "Quantile forecasts, pinball loss &amp; FVA", "Score the quantile you stock to (CRPS / pinball); score each process step against a naive benchmark",
 "Safety stock has always been a quantile — the <span class=\"num\">z</span> in the formula is a service level. Forecasting the mean and bolting a normal assumption onto it was always a workaround. Forecast Value Added answers the separate question MAPE never could — <em>is this step worth doing?</em> — and its characteristic finding is politically explosive: planner and executive overrides frequently make the statistical forecast <b>worse</b> while consuming most of the process cost."),

("Planning",
 "Schedule attainment", "% of the production plan executed as planned",
 "Stability and discipline on the shop floor: build what was scheduled.",
 "In a volatile regime, a plan produced on Monday is wrong by Wednesday. Attainment measures fidelity to a stale instruction, and rewards a planner who refuses to re-plan.",
 "Plan stability &amp; time-to-detect", "Re-plan frequency and nervousness; latency from demand or supply signal to plan response",
 "When the environment moves faster than the planning cycle, the speed and quality of re-planning matters more than adherence to the original plan."),

("Service",
 "Fill rate / OTIF", "Units or lines shipped complete and on time ÷ demanded, in aggregate",
 "Customer service, measured as one enterprise-level percentage.",
 "A 98% aggregate fill rate can hide that the missing 2% was 40% of gross margin, or the one customer with a contractual penalty. Aggregation destroys precisely the information you need in a shortage.",
 "Segmented, revenue-weighted service", "Service level by customer and product criticality; margin- or revenue-weighted OTIF",
 "During an allocation event the only useful question is which demand you protect. A metric that cannot distinguish between customers cannot inform that decision."),

("Service",
 "Asset / capacity utilisation", "Output ÷ theoretical capacity",
 "Sweating capital. Every idle hour of a machine reads as waste.",
 "Queueing theory has always said that as utilisation approaches 1, queue length and lead time go to infinity. A plant run at 100% has no ability to catch up after any disruption at all — it is the definition of no recovery capacity.",
 "Surge capacity &amp; time-to-scale", "Sustainable headroom above plan; time to reach a defined uplift",
 "Slack stopped being a defect and became an asset with a price. If you want to recover from a shock, someone has to have somewhere to recover into."),

("Network",
 "Landed cost per unit", "Ex-works price + freight + duty + handling",
 "The lowest delivered cost per unit, which for two decades meant the longest supply line to the lowest-wage geography.",
 "Landed cost is a point estimate on a stable route. It has no term for the route closing, the port queueing, the freight rate going up twelvefold, or the tariff being changed by legislation.",
 "Cost-to-serve under scenarios", "Landed cost evaluated across defined disruption and policy scenarios, not just base case",
 "The comparison that matters is not which source is cheapest today but which is cheapest across the range of futures you are actually exposed to."),

("Network",
 "DC count &amp; pooling savings", "Safety stock reduction from consolidation, ≈ √n",
 "Risk pooling. Eppen's square-root law is correct and the savings are real.",
 "Pooling assumes independent demand and an always-available supply line into the pooled node. Consolidation converts many partial failures into one total failure, and 2020–22 was a decade's worth of correlated events.",
 "Geographic &amp; chokepoint concentration", "% of critical volume through one country, one port, one strait, one plant",
 "Pooling and single-point-of-failure are the same structure. The saving is real and so is the exposure; both now have a number so the trade is made deliberately."),

("Finance",
 "Cash conversion cycle", "CCC = DIO + DSO − DPO",
 "Free cash flow, the fastest lever available to a CFO and the one most visible to investors.",
 "CCC improves when you extend payment terms — which finances your inventory on a small supplier's balance sheet at their cost of capital, not yours. The network's total financing cost rises while your metric improves. Then the supplier fails and it is your disruption.",
 "Network working capital &amp; supplier health", "Chain-level working capital cost; supplier financial-distress scoring",
 "A metric you can improve by moving a cost onto someone whose failure would stop your line is not measuring what it claims to measure."),

("Finance",
 "Supply-chain value-at-risk", "VaR = P(risk event) × monetised impact — SCOR AG.1.4, in the standard since 2012",
 "Monetising risk for the CFO. Note that the ambition was right and the metric already existed: it adapts J.P. Morgan's RiskMetrics VaR to the five SCOR processes.",
 "It needs <em>P</em> — and P for a specific plant in a specific year does not exist. The standard's own documentation concedes the metric is derived from historical event frequencies that are unavailable precisely for rare, high-impact events. So SCOR relegated it to a Level-2/3 diagnostic because it could not be rolled into cost, and in practice almost nobody produced it. The pre-2019 system did not fail to think of this. It thought of it and could not make it work.",
 "Revenue-at-risk per node", "exposure × (TTR − TTS), aggregated across the network — no probability term",
 "The same ambition, achieved by deleting the impossible input. This is the change that made all the others fundable: once exposure is denominated in revenue <em>without</em> requiring a probability nobody can estimate, a buffer stops being an operational preference and becomes a capital allocation decision on the same terms as any other."),

("Risk",
 "Likelihood × impact heat map", "Probability score 1–5 × impact score 1–5, on a risk register",
 "An auditable-looking register that satisfied governance requirements.",
 "Nobody can estimate the annual probability of a fire at a named plant, so the probability column was invented. Worse, genuine low-probability / catastrophic-impact events score mid-range on a 5×5 grid and receive no budget — the arithmetic actively hides the risks that matter.",
 "Time-to-recover / time-to-survive", "TTR: days to restore a node. TTS: days you can serve without it. Exposure = the gap.",
 "It deletes the unknowable input. You stop guessing how likely a failure is and instead measure two quantities you can actually establish, then price the difference. Auditable, comparable, and arguable in front of a CFO."),

("Risk",
 "Business continuity plan exists", "A document, reviewed annually, filed",
 "Compliance. The plan's existence was the metric.",
 "Plans that had never been exercised failed on contact. Nobody knew how long it actually took to re-qualify an alternate part, because nobody had ever done it under time pressure.",
 "Recovery time objective, rehearsed", "Measured RTO per critical node; stress-test and playbook rehearsal cadence",
 "Stress testing moved across from banking wholesale. An untested recovery time is an assumption, and this decade's lesson is that untested assumptions are where the exposure lives."),

("Governance",
 "Supplier code of conduct signed", "% of suppliers who have signed the code",
 "Documented compliance at the tier-1 contractual boundary.",
 "Forced-labour import bans, origin rules and emissions accounting all attach to the <em>source</em>, not to your direct supplier. A signature from tier one says nothing about tier three, and unmappable inputs became seizable at the border.",
 "Traceability to source", "% of restricted or high-risk inputs traced to origin; Scope 3 coverage",
 "The same <em>n</em>-tier map that supports resilience is now also a legal and regulatory requirement. Two separate arguments now fund the same capability, which is a large part of why this one stuck."),
]

def cell(kind, lab, metric, formula, body):
    return f'''      <div class="lcell {kind}">
        <div class="reg lab">{lab}</div>
        <div class="m">{metric}</div>
        <div class="f">{formula}</div>
        <div class="d">{body}</div>
      </div>'''

ARROW = ('      <div class="larrow" aria-hidden="true"><svg viewBox="0 0 16 16" fill="none" '
         'stroke="currentColor" stroke-width="1.6"><path d="M1 8h13M9 3l5 5-5 5"/></svg></div>')

out = []
for i, (dom, om, of_, opt, fail, nm, nf, why) in enumerate(ROWS, 1):
    slug = dom.split()[0].lower()
    out.append(f'''    <div class="lrow" data-domain="{slug}">
      <div class="lhead"><span class="reg dom">{dom}</span><span class="reg idx">{i:02d} / {len(ROWS)}</span></div>
{cell("old", "Before 2019", om, of_, "<b>Optimised for:</b> " + opt)}
{ARROW}
{cell("new", "After 2022", nm, nf, "<b>Why it follows:</b> " + why)}
      <div class="lfail">
        <div class="reg lab">Exposed</div>
        <div>{fail}</div>
      </div>
    </div>''')

pathlib.Path("src/partials/ledger.html").write_text("\n".join(out) + "\n")
print(f"{len(ROWS)} rows written")
doms = sorted({r[0] for r in ROWS})
print("domains:", doms)
