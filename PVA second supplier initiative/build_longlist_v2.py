#!/usr/bin/env python3
"""PVA_Supplier_Longlist.xlsx v2 — audited longlist + action plan + RFQ templates."""
import json, re
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

AUDIT="/tmp/claude-0/-home-user-Claude-Works/56a7748e-f0f6-5e4c-b4c2-718e974c8765/scratchpad/audit.json"
d=json.load(open(AUDIT))
verified=d["verified"]; newc=d["newCandidates"]; rfq=d["finalRFQ"]

ARIAL="Arial"
def F(bold=False,size=10,color="000000",italic=False):
    return Font(name=ARIAL,bold=bold,size=size,color=color,italic=italic)
HDR=PatternFill("solid",fgColor="1F3864")
SUB=PatternFill("solid",fgColor="D6DCE5")
A_F=PatternFill("solid",fgColor="C6EFCE")
B_F=PatternFill("solid",fgColor="FFF2CC")
C_F=PatternFill("solid",fgColor="F2F2F2")
D_F=PatternFill("solid",fgColor="FFC7CE")
GOLD=PatternFill("solid",fgColor="FFE699")
thin=Side(style="thin",color="D9D9D9")
BORD=Border(left=thin,right=thin,top=thin,bottom=thin)
LINKF=Font(name=ARIAL,size=9,color="0563C1",underline="single")

def clip(s,n=300):
    s=(s or "").strip()
    return s if len(s)<=n else s[:n-1]+"…"

wb=openpyxl.Workbook()

# ================= TAB 1: READ ME =================
c=wb.active; c.title="Read Me — What Changed"
c.sheet_view.showGridLines=False
c.column_dimensions['A'].width=2; c.column_dimensions['B'].width=32; c.column_dimensions['C'].width=104
c['B2']="PVA Second Source — Audited Supplier List & Action Plan"; c['B2'].font=F(bold=True,size=15,color="1F3864")
c['B3']="v2. Every company on v1 was re-verified against its live website. Corrections below. Nothing here is assumed — where a site is silent, it says silent."
c['B3'].font=F(italic=True,size=9,color="595959")
r=5
def sec(t):
    global r
    cell=c.cell(row=r,column=2,value=t); cell.font=F(bold=True,color="FFFFFF")
    for col in (2,3): c.cell(row=r,column=col).fill=HDR
    r+=1
def kv(k,v,fill=None):
    global r
    c.cell(row=r,column=2,value=k).font=F(bold=True); c.cell(row=r,column=2).alignment=Alignment(vertical="top",wrap_text=True)
    cell=c.cell(row=r,column=3,value=v); cell.font=F(); cell.alignment=Alignment(wrap_text=True,vertical="top")
    if fill:
        c.cell(row=r,column=2).fill=fill; cell.fill=fill
    r+=1

sec("THREE FINDINGS THAT CHANGE THE STRATEGY")
kv("1. SNP is a PVA specialist — that's why $0.75/lb is hard to beat","SNP's own site says they make aqueous PVA solutions for customers who 'don't have the equipment to cook the dry product into an aqueous solution.' Cooking PVA IS their product line. A generic toll blender is doing a one-off; SNP does it daily. That structural difference — not a bad quote — is why outside prices come in high. Judge every quote against that reality.",GOLD)
kv("2. Sekisui already sells cooked PVOH solution in 450-lb drums","Sekisui (the Selvol resin producer) markets ready-to-use PVOH SOLUTIONS packaged in 450-lb drums and 2,250-lb totes — our exact drum size — on the pitch that 'no cooking required.' Our old roster had them as 'advisor only.' That looks wrong. This is a potential ALTERNATE PATH: buy the solution instead of tolling it. Open risk: their minimum order may be far above 1 drum/week.",GOLD)
kv("3. Piedmont has 5–100 gallon pilot reactors","Already on our roster but under-prioritized. Steam AND hot-oil reactors with reflux (routinely run above 100 C), plus a dedicated 5–100 gal pilot fleet. Our ~50-gal batch fits a 100-gal reactor almost perfectly — rare, since most tollers start at 500–1,000 gal.",GOLD)

sec("SPEC NOW CONFIRMED — both open blockers closed")
kv("Viscosity target — CONFIRMED","< 2,500 cps, Brookfield spindle #3, 10 RPM, 25 C. This was the longest-standing open item on the project and it gated every firm quote. Two consequences: (1) suppliers can now quote firmly and a qualification batch can be judged pass/fail against a real number; (2) commercially it is good news — under 2,500 cps is an easily pumped and easily filtered fluid, so no blender can price this as a 'difficult, high-viscosity' job. Put the number in every RFQ and require it on every CoA.",A_F)
kv("ISO 13485 — NOT required","Confirmed: no ISO 13485 supplier needed. Still require ISO 9001, lot traceability, and a CoA with lot #, production date, %TS, pH, and viscosity.",A_F)

sec("MAJOR CORRECTIONS TO v1 (why the tiers moved)")
kv("PhilChem — was Tier A, now B","MIS-TARGETED. PhilChem (Greer, SC) is a DRY blending / repackaging house — 'specialty formulated dry blends,' 250 MM lb/yr dry capacity. The jacketed heated-vessel language that earned it Tier A lives on the PARENT site (Mount Vernon Chemicals) and describes other plants. Contact the group and ask which plant runs jacketed liquid batches.")
kv("Chemjet — was Tier A, now C","TWO ERRORS. Houston is a sales office; the plants are in Conroe and Odessa, TX. And it's an oilfield / drilling-fluids house — a poor fit for a medical-device component. A 'heat room' is also not a jacketed vessel.")
kv("MFG Chemical — was Tier A, now C","SCALE MISMATCH. Heat is a slam dunk (hot oil to 290 C) but the smallest production reactor is 2,000 gal against our ~50 gal. This is exactly the profile that produced the $8/lb quote you just declined. Also now PE-owned (Windjammer, Jan 2026).")
kv("Tiarco / TRCC — was Tier A, now B","No published basis for Tier A — the site publishes zero equipment, temperature, batch-size or certification data. Real company, right geography, but everything must be established by phone. (Their 'verify before proceeding with POs' banner is an anti-fraud notice, not financial distress.)")
kv("REXCO-USA — was Tier A, now C","Makes pigmented aqueous PVA solutions, but publishes nothing supporting toll manufacturing, heat capability, or a quality system. Keep as a technical resource / long shot.")
kv("5 companies DROPPED","Peach State Labs (dead URL — the Rome GA business is now Polyventive), Aicello (no US manufacturing), Troy Chemical (listing conflated two companies; intended one acquired 2022), CHT USA (Richmond VA is a SILICONE plant — silicone contamination is close to worst-case for a waterborne coating), South Coast Terminals (self-documented disqualification: 10 MT minimum batches).",D_F)

sec("WHAT'S NEW IN v2")
kv("ISO 13485 NOT required — RESOLVED","Confirmed by Oscar: we do not need an ISO 13485 supplier. That closes an open blocker and simplifies the search. The medical-grade candidates found in research (Polysciences, Hydromer, HR Pharmaceuticals, Strukmyer, GeminiBio, Kingchem, Alpha Teknova, Biocoat, NEXT Medical) are therefore DEPRIORITIZED to Tier C — they would price well above the incumbent for a certification we do not need. They stay listed only as a fallback if Quality later asks for a stricter supply chain. What we DO still want from any supplier: ISO 9001, a QC lab, lot traceability, and a CoA carrying %TS, pH and Brookfield viscosity.",A_F)
kv("Best small-batch find","Avion Manufacturing (Medina, OH) publishes batch sizes of 1–55 gallons and 60–275 gallons — the best cadence fit found anywhere. ISO 9001. Heat capability is the one unknown; ask it first.")
kv("Regional coverage filled","West: Sunland Chemical (LA — jacketed from 50 gal). Northeast: Shamrock Technologies (Newark NJ — 50-gal jacketed oil-heated kettles, ISO 9001). Midwest: Applied Material Solutions (WI — steam and hot-oil reactors from 140 gal).")
kv("Non-obvious category worth a look","Mallard Creek Polymers (Charlotte, NC) — emulsion polymer plants DISSOLVE PVOH IN HOT WATER as a routine step in vinyl acetate emulsion production. That capability is real but never advertised as 'PVA tolling.'")
kv("One diligence warning","Medical Products Laboratories (Philadelphia) looks like a strong process match on paper but has an FDA warning letter. Do not advance without confirming it is closed out. Listed so it's on your radar, not as a recommendation.",D_F)

sec("HOW TO READ THE TIERS")
kv("Tier A","Published evidence supports the heat gate AND a toll model AND a workable batch size. Call these first.")
kv("Tier B","Real, capable shops where one or both gates are unpublished. One phone call moves them to A or out.")
kv("Tier C","Special role — resin supplier, distributor, technical resource — or a scale/focus mismatch. Not primary toll targets.")
kv("Two questions decide everything","(1) Can you reach AND HOLD 90–95 C for 30–45 min? (2) What is your minimum batch size? Most candidates die on one of these, and both are cheap to ask.")

# ================= TAB 2: LONGLIST =================
L=wb.create_sheet("Longlist (audited)")
L.sheet_view.showGridLines=False
heads=["Tier","Company","Location","Website","Heat 90-95 C (evidence)","Min batch / MOQ","Quality certs","Contact route","Assessment / what to ask","Conf."]
widths=[6,30,30,30,42,28,26,34,52,7]
for i,w in enumerate(widths): L.column_dimensions[chr(65+i)].width=w
for i,h in enumerate(heads):
    cell=L.cell(row=1,column=1+i,value=h); cell.font=F(bold=True,color="FFFFFF"); cell.fill=HDR
    cell.alignment=Alignment(horizontal="center",wrap_text=True,vertical="center"); cell.border=BORD
L.freeze_panes="C2"; L.row_dimensions[1].height=30

rows=[]
seen=set()
def key(n): return re.sub(r'[^a-z]','',(n or '').lower())[:14]

# curated priority entries first (incumbent-adjacent + roster)
curated=[
 ("A","Sekisui Specialty Chemicals (Selvol)","Dallas TX; plants Calvert City KY, Pasadena TX","https://www.sekisui-sc.com/products/polyvinyl-alcohol/",
  "Implied — sells cooked PVOH solutions; a super-hydrolyzed cook cannot happen below ~90 C. Get it in writing for OUR formula.",
  "UNKNOWN — the main risk. Likely geared to mill-scale volumes.","Resin producer; formal CoA practice on resin","sekisui-sc.com contact form / technical service",
  "ALTERNATE PATH — they already package PVOH solutions in 450-lb drums, our exact size, 'no cooking required.' Ask: can you supply our formulation (adds NaCl, pigment, hot biocide) in 450-lb drums weekly, and what is the minimum order?","H"),
 ("A","Piedmont Chemical Industries","High Point NC (multi-site NC/SC/TN/TX)","https://www.piedmontchemical.com/custom-toll-manufacturing/",
  "STRONGEST published: SS reactors 250-5,000 gal with steam AND hot oil, reflux + distillation — designed to run above 100 C.",
  "STRONG — dedicated 5-100 GAL pilot reactor fleet. Our ~50-gal batch fits a 100-gal reactor.","Not published — ask ISO 9001 + lot traceability","+1 336-885-5131 — ask for toll/custom manufacturing",
  "ON OUR ROSTER ALREADY but under-prioritized. Best documented heat + small batch anywhere. Pitch the 100-gal pilot reactor as the production vessel.","H"),
 ("A","APV Engineered Coatings","Akron OH","https://www.apvcoatings.com",
  "Verbal yes earlier — RE-CONFIRM the 90-95 C hold explicitly.","Excellent — from ~5 gal","ISO 9001 / EPA-reg","already engaged — resume with prior contact",
  "WARMEST LEAD — you were mid-interview. Pigment-dispersion specialty fits our pigmented product. Close the heat gate and get a per-drum number.","H"),
 ("B","Columbus Chemical (CCI)","Columbus WI / Phoenix AZ","https://www.columbuschemical.com",
  "Yes — heating/cooling capability","Excellent — 20 L to 20,000 L (~5 gal floor); widest range = least shelf-life waste","ISO 9001, in-house lab","on roster — resume",
  "ON OUR ROSTER. Lowest batch floor of the roster group; can scale if demand grows.","M"),
 ("C","CORECHEM","Knoxville TN","https://www.corechemtn.com",
  "Confirm","CAUTION — smallest tank ~250 gal (~4.5 drums) may overshoot the 18-day shelf life","Not published","on roster",
  "ON OUR ROSTER. Ask specifically about PARTIAL batches — a full 250-gal batch is ~4.5 drums but only ~2 are usable in 18 days.","M"),
 ("C","Northstar Chemical","Charlotte NC","https://www.northstarchemical.com",
  "Confirm","Unknown (small custom/toll)","Not published","(800) 570-0204",
  "ON OUR ROSTER as backup. Smaller dry-to-liquid custom/toll blender — verify.","M"),
]
for row in curated:
    rows.append(row); seen.add(key(row[1]))


LOC={'philchemmountv': 'Greer, SC (parent: Mount Vernon Chemicals)', 'tiarcotrcctiar': 'Dalton, GA', 'mfgchemical': 'Chattanooga TN; plants Dalton GA', 'chemjet': 'CORRECTED: plants Conroe & Odessa TX (Houston = sales office)', 'rexcousapartal': 'Conyers, GA', 'colonialchemic': 'Savannah GA (+Atlanta, Charlotte, Richmond)', 'tollsolutionsl': 'Duncan, SC', 'keypolymer': 'Lawrence, MA', 'valpacinc': 'Federalsburg & Hurlock, MD', 'hydritechemica': 'Brookfield WI (multi-site)', 'aexcelcorporat': 'Mentor, OH', 'apollochemical': 'Burlington, NC', 'nationfordchem': 'Fort Mill, SC', 'ethoxchemicals': 'Greenville, SC', 'peachstatelabs': 'Rome, GA (URL dead — now Polyventive)', 'polyventivefor': 'Calhoun / Dalton / Rome, GA', 'sandstromcoati': 'Port Byron, IL', 'sierraperforma': 'Minnetonka, MN', 'americandisper': 'Louisville, KY', 'alphachemicals': 'Stoughton, MA', 'capitalresinco': 'Columbus, OH', 'seacoleseacole': 'CORRECTED: Plymouth, MN', 'customchemical': 'Santa Fe Springs, CA', 'camcochemicalf': 'Florence, KY', 'hubbardhallwat': 'Waterbury CT + Inman SC', 'hansonchemical': 'Friendship, NY', 'tbkonetbkmanuf': 'Carrollton, TX', 'spectrachemlod': 'Lodi, NJ', 'spectracoloran': 'Union, SC', 'kurarayamerica': 'Houston / Pasadena / La Porte, TX', 'monosolkuraray': 'Merrillville, IN', 'mitsubishichem': 'US sales office only (no US plant)', 'changchunpetro': 'Taiwan (US = distribution only)', 'aicelloamerica': 'Japan (no US manufacturing)', 'thechemicalcom': 'Jamestown, RI', 'stonermoldings': 'Quarryville, PA', 'troychemicaltr': 'Florham Park, NJ', 'chemicalsolven': 'Cleveland, OH', 'chtusa': 'Richmond, VA (silicone plant)', 'southernchemic': 'Dalton, GA', 'southcoastterm': 'Houston, TX', 'formulacorp': 'Auburn, WA'}

TIER_ORDER={"A":0,"B":1,"C":2,"DROP":3}
def add_verified():
    out=[]
    for v in verified:
        n=v.get("name","")
        if key(n) in seen: continue
        seen.add(key(n))
        t=v.get("tier_recommended","C")
        assess=v.get("tier_change_reason") or ""
        corr=v.get("corrections") or ""
        if corr and corr.strip().lower() not in ("none","none.",""):
            assess=f"CORRECTION: {clip(corr,220)}  |  {clip(assess,200)}"
        loc=LOC.get(key(n),"")
        url=v.get("correct_url","") or ""
        m=re.search(r"https?://[^\s()|]+",url)
        url=m.group(0) if m else url
        out.append((t,n,loc,url,
                    clip(v.get("heat_gate_evidence"),260),clip(v.get("small_batch_evidence"),160),
                    clip(v.get("medical_quality_signals"),140),clip(v.get("contact_route"),160),
                    clip(assess,420),v.get("confidence","")))
    return out
MEDICAL_TOKENS=("polysciences","hydromer","hr pharmaceutical","strukmyer","geminibio","gemini bio",
                "kingchem","alpha teknova","biocoat","next medical","medical products laboratories")
def is_medical(n): return any(t in (n or "").lower() for t in MEDICAL_TOKENS)
MED_NOTE=("ISO 13485 NOT REQUIRED (confirmed by Oscar) — deprioritized. Medical-grade pricing would run well above "
          "the incumbent for a certification we do not need. Keep only as a fallback if Quality later asks for a "
          "stricter supply chain. | ")
def add_new():
    out=[]
    for v in newc:
        n=v.get("name","")
        # collapse near-duplicates that differ only by suffix (e.g. "Hydromer, Inc." vs "Hydromer, Inc. (OTC: HYDI)")
        base=re.sub(r'[^a-z]','',(n or '').lower().split("(")[0])[:10]
        if key(n) in seen or base in seen: continue
        seen.add(key(n)); seen.add(base)
        heat=(v.get("heat_gate_evidence") or "")
        strong = any(w in heat.upper() for w in ("STRONG","GOOD","CONFIRM","PUBLISHED:","STRONGEST"))
        silent = heat.strip().upper().startswith(("SILENT","NOT PUBLISHED","UNVERIFIED","UNKNOWN"))
        t = "B" if strong else ("C" if silent else "B")
        why=clip(v.get("why_relevant"),420)
        if is_medical(n):
            t="C"; why=MED_NOTE+clip(v.get("why_relevant"),240)
        out.append((t,n+"  [NEW]",v.get("location",""),v.get("url",""),
                    clip(heat,260),clip(v.get("small_batch_evidence"),160),
                    clip(v.get("quality_certs"),140),clip(v.get("contact_route"),160),
                    why,clip(v.get("confidence"),24)))
    return out

allrows = rows + add_verified() + add_new()
allrows.sort(key=lambda x:(TIER_ORDER.get(x[0],9), x[1]))

r=2
for row in allrows:
    t=row[0]
    fill = A_F if t=="A" else B_F if t=="B" else D_F if t=="DROP" else C_F
    for j,val in enumerate(row):
        cell=L.cell(row=r,column=1+j,value=val)
        cell.alignment=Alignment(wrap_text=True,vertical="top",horizontal="center" if j in(0,9) else "left")
        cell.border=BORD; cell.font=F(size=9); cell.fill=fill
        if j==0: cell.font=F(bold=True,size=11)
        if j==3 and isinstance(val,str) and val.startswith("http"):
            try:
                cell.hyperlink=val; cell.font=LINKF
            except Exception: pass
    r+=1
total=len(allrows)

# ================= TAB 3: ACTION PLAN =================
A=wb.create_sheet("Action Plan")
A.sheet_view.showGridLines=False
ah=["#","Priority","Who to contact","How","Ask specifically","Why this one","Owner","Status"]
aw=[5,15,30,30,66,44,10,12]
for i,w in enumerate(aw): A.column_dimensions[chr(65+i)].width=w
A['A1']="ACTION PLAN — PVA Second Source"; A['A1'].font=F(bold=True,size=14,color="1F3864")
A['A2']="Sequenced so the cheapest, highest-information calls happen first. Every 'ask' is written so you can read it straight off the sheet."
A['A2'].font=F(italic=True,size=9,color="595959")
for i,h in enumerate(ah):
    cell=A.cell(row=4,column=1+i,value=h); cell.font=F(bold=True,color="FFFFFF"); cell.fill=HDR
    cell.alignment=Alignment(horizontal="center",wrap_text=True,vertical="center"); cell.border=BORD
A.freeze_panes="A5"; A.row_dimensions[4].height=28

acts=[
 ("WAVE 0 — unblock (do first, internal)","","","","","",""),
 ("RESOLVED","Viscosity specification","Closed","SPEC CONFIRMED: Brookfield viscosity < 2,500 cps, spindle #3, 10 RPM, 25 C. Put this in every RFQ and on every CoA, and use it as the pass/fail criterion for any qualification batch.","Was the longest-standing blocker on this project. With it, suppliers can quote firmly and a trial batch can actually be judged pass/fail. Also good news commercially: under 2,500 cps is an easily pumpable, easily filterable fluid — no special high-viscosity equipment needed, so no blender can charge a premium for 'difficult' handling.","Oscar","DONE"),
 ("RESOLVED","Quality / Regulatory — ISO 13485","Closed","No ISO 13485 required (confirmed by Oscar). Medical-grade candidates deprioritized to Tier C. Still specify on every RFQ: ISO 9001, lot traceability, and a CoA with lot #, production date, %TS, pH, Brookfield viscosity (spindle #3, 10 RPM, 25 C).","Removes a whole cost tier from the search — generic ISO 9001 tollers are now fully in scope.","Oscar","DONE"),
 ("BLOCKER","Internal — McC","Internal","Get the NDA template ready to execute before sharing the full spec/formula with any new supplier.","Every candidate will ask for the formula before quoting firmly.","Oscar",""),
 ("WAVE 1 — highest-information calls (this week)","","","","","",""),
 ("1","Sekisui Specialty Chemicals — technical service","Web form + ask for tech service","Do you sell a made-to-spec PVOH SOLUTION in 450-lb drums for our formula (~10-12% solids, super-hydrolyzed, plus NaCl, pigment, and a hot biocide addition)? What is the minimum order, and can you support ~1 drum/week? If not made-to-spec, which catalog solution is closest?","POTENTIAL GAME-CHANGER: they already package cooked PVOH solutions in 450-lb drums and market 'no cooking required.' If they can do our formula, we skip tolling entirely. Also free grade/cook expertise either way.","Oscar",""),
 ("2","Piedmont Chemical — toll/custom manufacturing group","Phone 336-885-5131","Can you run our batch in one of your 5-100 gallon PILOT reactors as recurring production, ~1 drum/week? Confirm you can hold 90-95 C for 30-45 min. Indicative conversion price per 55-gal drum (~450 lb net). ISO 9001? Lot traceability + CoA with %TS, pH, Brookfield viscosity?","Best documented heat + small-batch fit found anywhere, and already on our roster. The 100-gal pilot reactor is an almost perfect match for our ~50-gal batch.","Oscar",""),
 ("3","APV Engineered Coatings — prior contact","Resume existing thread","Re-confirm explicitly: can you reach AND HOLD 90-95 C for 30-45 min? Then: minimum batch, and an indicative conversion price per 55-gal drum.","Warmest lead — you were mid-interview. Pigment-dispersion specialty fits our pigmented product.","Oscar",""),
 ("4","SNP (incumbent) — leverage check","Existing relationship","Without signalling we're leaving: confirm current lead time, whether they'd hold $0.75/lb under a term agreement, and whether they can flex a second production line/site for continuity.","Their site shows cooking PVA IS their specialty — which is why the price is hard to beat. A second SNP site may deliver more redundancy per dollar than a weak second vendor.","Oscar",""),
 ("WAVE 2 — Tier A toll blenders (RFQ email)","","","","","",""),
 ("5","Valpac Inc (Federalsburg/Hurlock MD)","RFQ email","Use the RFQ template. Plus: confirm maximum vessel temperature, and smallest vessel (published smallest is 100 gal).","Pure-play toll manufacturer of WATER-BASED adhesives/coatings since 1983; steam AND hot-oil jacketed SS; ISO 9001 + AS9100. Structurally the closest business model.","Oscar",""),
 ("6","Key Polymer (Lawrence MA)","RFQ email","Use the RFQ template. Plus: confirm max temperature on the jacketed vessels; you list vessels from 5 gal — confirm the small end is available for recurring production.","Only candidate combining jacketed heat-and-cool, a vessel range starting at 5 gal, ISO 9001, and 316 SS.","Oscar",""),
 ("7","Apollo Chemical (Burlington NC)","RFQ email","Use the RFQ template. Plus: what is the numeric maximum temperature on your jacketed vessels? Confirm the 3-drum minimum batch.","Only candidate with all three legs documented: jacketed heat AND cool, a 3-drum minimum, explicit toll model, ISO 9001 since 1998.","Oscar",""),
 ("8","Toll Solutions (Duncan SC)","RFQ email","Use the RFQ template. Plus: confirm 316L availability (published vessels are 304 SS) — ask whether any 316L vessel is available for a medical-device component.","Pure toll business model (no competing product line), jacketed reactors to 150 C, ISO 9001, 50-gal batches.","Oscar",""),
 ("9","Polyventive (Calhoun/Dalton GA)","RFQ email","Use the RFQ template. Plus: confirm batch minimum and that 'aqueous solution polymerization' equipment can be used for a simple dissolution.","Publishes 'Polymerizations (Aqueous Solution)' plus a hot-oil thermal system — closest published capability match to our cook. Georgia freight.","Oscar",""),
 ("10","Alpha Chemical Services (Stoughton MA)","RFQ email","Use the RFQ template. Plus: confirm maximum steam-jacket temperature.","Publishes BOTH steam-jacketed vessels AND a 50-gal smallest vessel (= one drum), markets 'small minimums,' ISO 9001.","Oscar",""),
 ("11","Capital Resin (Columbus OH)","RFQ email","Use the RFQ template. Plus: confirm they will run a simple dissolution (not just synthesis), and ask about cross-contamination controls from resin production.","Heat gate is unambiguously trivial for their equipment; ISO 9001; explicit toll model; pilot-scale vessels.","Oscar",""),
 ("12","Colonial Chemical Solutions (Savannah GA)","RFQ email","Use the RFQ template. Plus: their heated tank is large (6,000 gal) — ask which vessel would run a 50-gal batch and what its max temperature is.","Published 50-gallon minimum is the single best cadence fit on the list; Georgia freight.","Oscar",""),
 ("13","Avion Manufacturing (Medina OH)  [NEW]","RFQ email","LEAD WITH THE HEAT QUESTION — their site never mentions heated or jacketed vessels. If yes, use the full RFQ.","Best small-batch fit found anywhere: publishes 1-55 gallon and 60-275 gallon batch ranges, ISO 9001. Heat is the single unknown.","Oscar",""),
 ("WAVE 3 — conditional / specialist","","","","","",""),
 ("14","Aexcel Corporation (Mentor OH)","RFQ email","LEAD WITH THE HEAT QUESTION — their site is silent on temperature. If yes, send the full RFQ.","Best batch-size fit in Tier B and an explicit toll model that already assumes customer-supplied raw materials — exactly our arrangement. Packages to 55-gal drums and IBCs.","Oscar",""),
 ("15","Sandstrom Coating Technologies (Port Byron IL)","RFQ email","Use the RFQ template. Plus: confirm maximum vessel temperature.","Their published toll model describes ours almost word for word: customer provides the formula and the raw materials, they process and package. ISO 9001, vessels from 1 gal.","Oscar",""),
 ("16","Mallard Creek Polymers (Charlotte NC)  [NEW]","RFQ email","Use the RFQ template, but frame it their way: 'you already dissolve PVOH in hot water as the protective colloid step in vinyl acetate emulsions — we want that step alone, as a toll.'","Non-obvious but real: emulsion polymer plants dissolve PVOH in hot water routinely. Never advertised as PVA tolling.","Oscar",""),
 ("17","Sunland Chemical (Los Angeles CA)  [NEW]","RFQ email","Use the RFQ template. Plus: confirm max temperature on the jacketed tanks.","Best WEST-coast fit: 18 blending tanks 5-6,000 gal, jacketed heating available from 50 gal up.","Oscar",""),
 ("18","Shamrock Technologies (Newark NJ)  [NEW]","RFQ email","Use the RFQ template. Plus: confirm max oil-jacket temperature on the 50-gal unit.","Best NORTHEAST fit: 50-gal jacketed high-shear (= one drum) and 500/1,200-gal oil-heated jacketed kettles; ISO 9001 + a cGMP clean room.","Oscar",""),
 ("19","Applied Material Solutions (Elkhorn WI)  [NEW]","RFQ email","Use the RFQ template. Plus: smallest published vessel is 140 gal — ask if a ~50-gal batch is workable in it.","Publishes 'steam and hot oil reactors, 140-13,000 gallon capacities' — best heat evidence outside the Southeast; ISO 9001.","Oscar",""),
 ("20","Aqua Based Technologies (Northvale NJ)  [NEW]","RFQ email","LEAD WITH THE HEAT QUESTION — no heating capability is stated anywhere on their site.","A water-based-ONLY house offering custom formulating + toll manufacturing + drum/tote quantities — the right three services bundled.","Oscar",""),
 ("21","Kuraray America — technical service","Email/phone","Not a toller. Ask: (a) confirm the right super-hydrolyzed high-MW grade (Exceval family) and the recommended dissolution profile; (b) can you refer toll blenders who already cook your resin?","Free expert validation of the 90-95 C profile, plus resin supply. Resin producers know who cooks their product — the best referral source available.","Oscar",""),
 ("WAVE 4 — housekeeping","","","","","",""),
 ("22","CJB Applied Technologies","Email","Send the cancellation note (already drafted). Close it out cleanly and keep the door open.","Quote was ~10x the incumbent's all-in delivered price. Declined.","Oscar",""),
 ("23","Track every response","Spreadsheet","Log for each: max temp + hold (Y/N), min batch, price per 55-gal drum, lead time, ISO status, MOQ. Kill any that fails the heat gate immediately.","The two gate answers kill most candidates fast — capture them consistently so the comparison is apples-to-apples.","Oscar",""),
]
r=5
for a in acts:
    if len(a)==7 and a[1]=="" and a[2]=="":
        cell=A.cell(row=r,column=1,value=a[0]); cell.font=F(bold=True,size=11,color="FFFFFF")
        for col in range(1,9): A.cell(row=r,column=col).fill=SUB; A.cell(row=r,column=col).border=BORD
        cell.font=F(bold=True,size=11,color="1F3864")
        r+=1; continue
    pri=a[0]
    vals=[r-4,pri,a[1],a[2],a[3],a[4],a[5],a[6]]
    fill = D_F if pri=="BLOCKER" else A_F if str(pri).isdigit() and int(pri)<=4 else B_F
    for j,val in enumerate(vals):
        cell=A.cell(row=r,column=1+j,value=val)
        cell.alignment=Alignment(wrap_text=True,vertical="top",horizontal="center" if j in(0,1,6,7) else "left")
        cell.border=BORD; cell.font=F(size=9); cell.fill=fill
        if j==1: cell.font=F(bold=True,size=9)
    r+=1

# ================= TAB 4: RFQ TEMPLATES =================
T=wb.create_sheet("RFQ Templates")
T.sheet_view.showGridLines=False
T.column_dimensions['A'].width=2; T.column_dimensions['B'].width=26; T.column_dimensions['C'].width=104
T['B2']="Outreach Templates"; T['B2'].font=F(bold=True,size=14,color="1F3864")
T['B3']="Built on your existing email. Two changes that matter: the heat gate is stated as pass/fail up front so unqualified shops self-select out, and the price question forces an unambiguous basis so nobody can repeat the '$8/lb of what?' problem."
T['B3'].font=F(italic=True,size=9,color="595959")
r=5
def block(title,body,fill=None,height=None):
    global r
    cell=T.cell(row=r,column=2,value=title); cell.font=F(bold=True,color="FFFFFF")
    for col in (2,3): T.cell(row=r,column=col).fill=HDR
    r+=1
    T.cell(row=r,column=2,value="").font=F()
    b=T.cell(row=r,column=3,value=body); b.font=F(size=10); b.alignment=Alignment(wrap_text=True,vertical="top")
    if fill: b.fill=fill
    if height: T.row_dimensions[r].height=height
    r+=2

VISC="finished viscosity under 2,500 cps (Brookfield, spindle #3, 10 RPM, 25 C)"
email_body=rfq["email_body"].replace(
  "The product is an aqueous PVA solution, roughly 10-12% solids.",
  "The product is an aqueous PVA solution, roughly 10-12% solids, "+VISC+".")
web_body=rfq["web_form_body"].replace(
  "Product is an aqueous PVA solution, ~10-12% solids, that has to reach",
  "Product is an aqueous PVA solution, ~10-12% solids, under 2,500 cps, that has to reach")

block("EMAIL — subject line", rfq["email_subject"], A_F, 22)
block("EMAIL — body (send as-is)", email_body, A_F, 300)
block("WEBSITE CONTACT FORM (shorter — for small text boxes)", web_body, B_F, 180)
block("PHONE — opening lines", rfq["phone_opener"], C_F, 90)
block("IF THEY ASK FOR SPEC DETAIL (send after they confirm they can do it)",
 "Aqueous polyvinyl alcohol solution, made to order.\n\n"
 "• Total solids: 10-12%, in water\n"
 "• Viscosity: UNDER 2,500 cps — Brookfield, spindle #3, 10 RPM, 25 C\n"
 "• Process: heat to 90-95 C and hold 30-45 min under agitation to fully dissolve; cool to <=40 C; filter to 200 micron; fill 55-gal drums (~450 lb net)\n"
 "• Materials: we supply the resin and all other raw materials\n"
 "• Shelf life: 18 days — made fresh to order, no stockpiling\n"
 "• Cadence: ~1 drum/week, ~50 drums/year\n"
 "• CoA required every shipment: lot #, production date, % total solids, final pH, Brookfield viscosity (spindle #3, 10 RPM, 25 C)\n"
 "• Quality: ISO 9001 and lot traceability preferred. ISO 13485 not required.\n"
 "• Handling: protect from freezing in transit and storage\n\n"
 "Full formula released under NDA.", None, 210)
block("WHAT CHANGED vs your original, and why",
 "Your original was good and short — these keep that. What was added, and the reason for each:\n\n"
 "• THE HOLD, not just the temperature. Your version said 'heat up to 95 C.' The real gate is holding 90-95 C for 30-45 minutes — that is what separates a real heating system from one that can briefly touch temperature. It also states the failure mode plainly ('if your equipment tops out below 90 C') so a shop running 85 C cannot talk itself into a yes.\n\n"
 "• THE TOLL MODEL, stated up front. 'We supply the raw materials and the formula; you charge a conversion fee' tells them immediately there is no raw-material risk on their side, and it prevents a quote that silently includes materials.\n\n"
 "• THE PRICE BASIS, forced. Asking for a price PER 55-GALLON DRUM — and, if they quote per pound, per pound of WHAT — is the direct fix for the $8.00-8.50/lb ambiguity that cost weeks.\n\n"
 "• THE VOLUME, up front. One drum a week, ~50 a year, recurring. This is what gets a cold email forwarded to someone who can actually answer.\n\n"
 "• MINIMUM BATCH SIZE. The second-most-common killer after heat, and free to ask.\n\n"
 "What was deliberately LEFT OUT: the incumbent's name, our current price, and the formula. None of that helps a first contact, and all of it weakens the negotiating position.", None, 300)

# ================= TAB 5: STAKEHOLDER MAP =================
S=wb.create_sheet("Stakeholder Map")
S.sheet_view.showGridLines=False
S.column_dimensions['A'].width=2; S.column_dimensions['B'].width=26; S.column_dimensions['C'].width=34; S.column_dimensions['D'].width=76
S['B2']="Who to Reach — beyond just toll blenders"; S['B2'].font=F(bold=True,size=14,color="1F3864")
S['B3']="A second source is not only a blender search. These are the other parties that move this forward."
S['B3'].font=F(italic=True,size=9,color="595959")
for i,h in enumerate(["Category","Who","Role / what they give you"]):
    cell=S.cell(row=5,column=2+i,value=h); cell.font=F(bold=True,color="FFFFFF"); cell.fill=HDR; cell.border=BORD; cell.alignment=Alignment(horizontal="center")
sh=[
 ("Incumbent","SNP Inc. (Durham, NC)","The benchmark and the fallback. Their site shows cooking PVA IS their specialty — that's why $0.75/lb is hard to beat. Explore a second SNP site/line for continuity before assuming a new vendor is cheaper redundancy.",A_F),
 ("Alternate path","Sekisui (Selvol producer)","May sell the FINISHED solution in 450-lb drums — potentially removing the need for a toll blender at all. Also free technical service on grade + cook.",GOLD),
 ("Resin supply","Kuraray America; Mitsubishi Chemical America; Chang Chun (import)","Resin source if we consign materials, plus free technical validation of the dissolution profile — and referrals to blenders who already cook their resin.",C_F),
 ("Resin distribution","Brenntag; Tilley; Palmer Holland; The Chemical Company","Drum-quantity resin if we supply materials to a toller. TCC and Tilley can also refer blenders. (Tilley runs its own blending plant but has a 220-gal minimum.)",C_F),
 ("Toll blenders","Tier A/B on the Longlist tab","The core search. Two questions decide most of them: hold 90-95 C, and minimum batch size.",B_F),
 ("Medical-grade CMs","Polysciences; Hydromer; HR Pharmaceuticals; Strukmyer; GeminiBio; Kingchem; Alpha Teknova; Biocoat; NEXT Medical","NOT NEEDED — ISO 13485 is not required (confirmed by Oscar). Parked as a fallback only; do not spend time here.",C_F),
 ("Internal — Quality/Reg","Intuitive Quality / Regulatory","RESOLVED — ISO 13485 not required. Still specify on every RFQ: ISO 9001, lot traceability, and a CoA with lot #, production date, %TS, pH, Brookfield viscosity (spindle #3, 10 RPM, 25 C).",A_F),
 ("Internal — spec owner","Viscosity specification","RESOLVED — < 2,500 cps, Brookfield spindle #3, 10 RPM, 25 C. Now the pass/fail criterion for any qualification batch, and a required CoA field.",A_F),
 ("Internal — legal","McC","NDA execution before sharing the formula with any new supplier.",D_F),
 ("Closed out","CJB Applied Technologies","Quote was ~10x the incumbent all-in. Cancellation note drafted; keep the relationship cordial.",C_F),
]
r=6
for cat,who,role,fill in sh:
    for j,val in enumerate([cat,who,role]):
        cell=S.cell(row=r,column=2+j,value=val); cell.font=F(size=9,bold=(j==0))
        cell.alignment=Alignment(wrap_text=True,vertical="top"); cell.border=BORD; cell.fill=fill
    r+=1

out="/home/user/Claude-Works/PVA second supplier initiative/PVA_Supplier_Longlist.xlsx"
wb.save(out)
print("saved",out)
print("longlist rows:",total)
from collections import Counter
print("tiers:",dict(Counter(x[0] for x in allrows)))
