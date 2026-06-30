import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

TITLE = Font(bold=True, size=14, color="FFFFFF")
HDR   = Font(bold=True, size=10, color="FFFFFF")
BOLD  = Font(bold=True)
input_fill = PatternFill("solid", fgColor="FFF2CC")
hdr_fill   = PatternFill("solid", fgColor="1F4E78")
prob_hdr   = PatternFill("solid", fgColor="375623")
title_fill = PatternFill("solid", fgColor="2E75B6")
you_fill   = PatternFill("solid", fgColor="FCE4D6")
her_fill   = PatternFill("solid", fgColor="E2EFDA")
prob_fill  = PatternFill("solid", fgColor="EDF7E9")
grp_fill   = PatternFill("solid", fgColor="DDEBF7")
param_fill = PatternFill("solid", fgColor="FFF2CC")
money='#,##0'; pct='0.0%'; pct0='0%'
thin=Side(style="thin",color="BFBFBF")
border=Border(left=thin,right=thin,top=thin,bottom=thin)

def cell(ws,coord,val,font=None,fill=None,fmt=None,align=None,bd=False):
    c=ws[coord]; c.value=val
    if font:c.font=font
    if fill:c.fill=fill
    if fmt:c.number_format=fmt
    if align:c.alignment=Alignment(horizontal=align,vertical="center",wrap_text=True)
    if bd:c.border=border
    return c

ws=wb.active; ws.title="Scenarios"
cell(ws,"A1","House Sale Scenarios + Probability of Sale — 537 Duchart Ln, Fuquay-Varina NC",TITLE,title_fill)
ws.merge_cells("A1:R1"); ws.row_dimensions[1].height=24

# ---- DEAL INPUTS (left) ----
cell(ws,"A3","DEAL INPUTS (edit yellow)",BOLD)
inputs=[("A4","Purchase price (sold Mar 18 2024)","B4",405700,money),
        ("A5","Down payment (her contribution)","B5",48000,money),
        ("A6","Current mortgage balance / payoff","B6",356149.76,money),
        ("A7","Excise/transfer tax rate (NC)","B7",0.002,pct),
        ("A8","Other closing costs (flat $)","B8",2000,money),
        ("A9","HER recovery share — Option A","B9",0.80,pct),
        ("A10","HER recovery share — Option B","B10",0.70,pct)]
for lc,lab,vc,val,fmt in inputs:
    cell(ws,lc,lab); cell(ws,vc,val,BOLD,input_fill,fmt,bd=True)

# ---- PROBABILITY MODEL PARAMETERS (right, above table) ----
cell(ws,"N3","PROBABILITY MODEL (edit yellow)",BOLD)
params=[("N4","Est. current market value","O4",410000,money),
        ("N5","Base monthly sale chance (h0)","O5",0.25,pct),
        ("N6","Price sensitivity (k)","O6",7,'0.0'),
        ("N7","Exposure: full-service agent","O7",1.10,'0.00'),
        ("N8","Exposure: typical agent","O8",1.05,'0.00'),
        ("N9","Exposure: FSBO + buyer agent 3%","O9",0.90,'0.00'),
        ("N10","Exposure: FSBO + buyer agent 2.5%","O10",0.85,'0.00'),
        ("N11","Season — Jul 2026","O11",1.05,'0.00'),
        ("N12","Season — Aug 2026","O12",0.95,'0.00'),
        ("N13","Season — Sep 2026","O13",0.85,'0.00'),
        ("N14","Season — Oct 2026","O14",0.75,'0.00')]
for lc,lab,vc,val,fmt in params:
    cell(ws,lc,lab); cell(ws,vc,val,BOLD,param_fill,fmt,bd=True)

# ---- TABLE ----
H=18
headers=["Sale price","Selling option","Comm %","Comm $","Other\nclosing $",
         "Total\nsell costs","NET proceeds\n(money back)","Shortfall\nvs $48k",
         "YOUR pay\n@80%","YOUR pay\n@70%","Her total\n@80%","Her total\n@70%",
         "Price\nfactor","Exposure\nfactor","P(sold by\nend Jul)","P(sold by\nend Aug)",
         "P(sold by\nend Sep)","P(sold by\nend Oct)"]
for i,h in enumerate(headers):
    fill = prob_hdr if i>=12 else hdr_fill
    cell(ws,f"{get_column_letter(i+1)}{H}",h,HDR,fill,align="center",bd=True)
ws.row_dimensions[H].height=42

sale_prices=[390000,395000,399000,405000,409900]
# option: (label, commission, exposure-param-cell)
options=[("Full-service agent (6%)",0.06,"$O$7"),
         ("Typical agent (5.5%)",0.055,"$O$8"),
         ("FSBO + buyer agent (3%)",0.03,"$O$9"),
         ("FSBO + buyer agent (2.5%)",0.025,"$O$10")]

r=H+1
for sp in sale_prices:
    for name,comm,exp_cell in options:
        a=f"A{r}";c=f"C{r}";d=f"D{r}";e=f"E{r}";f=f"F{r}";g=f"G{r}";h=f"H{r}"
        i=f"I{r}";j=f"J{r}";k=f"K{r}";l=f"L{r}";m=f"M{r}";n=f"N{r}"
        o=f"O{r}";p=f"P{r}";q=f"Q{r}";rr=f"R{r}"
        cell(ws,a,sp,None,grp_fill,money,bd=True)
        cell(ws,f"B{r}",name,None,None,None,"left",bd=True)
        cell(ws,c,comm,None,None,pct,bd=True)
        cell(ws,d,f"={a}*{c}",None,None,money,bd=True)
        cell(ws,e,f"={a}*$B$7+$B$8",None,None,money,bd=True)
        cell(ws,f,f"={d}+{e}",None,None,money,bd=True)
        cell(ws,g,f"={a}-$B$6-{f}",BOLD,None,money,bd=True)
        cell(ws,h,f"=MAX(0,$B$5-{g})",None,None,money,bd=True)
        cell(ws,i,f"={h}*$B$9",BOLD,you_fill,money,bd=True)
        cell(ws,j,f"={h}*$B$10",BOLD,you_fill,money,bd=True)
        cell(ws,k,f"={g}+{i}",None,her_fill,money,bd=True)
        cell(ws,l,f"={g}+{j}",None,her_fill,money,bd=True)
        # probability model
        cell(ws,m,f"=EXP(-$O$6*({a}-$O$4)/$O$4)",None,None,'0.00',bd=True)
        cell(ws,n,f"={exp_cell}",None,None,'0.00',bd=True)
        cell(ws,o,f"=MIN(0.95,$O$5*{m}*{n}*$O$11)",BOLD,prob_fill,pct0,bd=True)
        cell(ws,p,f"=1-(1-{o})*(1-MIN(0.95,$O$5*{m}*{n}*$O$12))",None,prob_fill,pct0,bd=True)
        cell(ws,q,f"=1-(1-{p})*(1-MIN(0.95,$O$5*{m}*{n}*$O$13))",None,prob_fill,pct0,bd=True)
        cell(ws,rr,f"=1-(1-{q})*(1-MIN(0.95,$O$5*{m}*{n}*$O$14))",BOLD,prob_fill,pct0,bd=True)
        r+=1

widths=[12,28,8,11,10,11,13,11,11,11,11,11,9,9,10,10,10,10]
for i,w in enumerate(widths):
    ws.column_dimensions[get_column_letter(i+1)].width=w
ws.freeze_panes=f"A{H+1}"

# ================= NOTES =================
ns=wb.create_sheet("Notes & Assumptions"); ns.column_dimensions["A"].width=104
notes=[
 ("House Sale Scenarios + Probability of Sale — Notes",TITLE,title_fill),
 ("",None,None),
 ("PROPERTY (verified online)",BOLD,None),
 ("• 537 Duchart Ln, Fuquay-Varina, NC 27526 — 3bd/2.5ba, 2,216 sqft, Lakestone Village.",None,None),
 ("• Recorded sale: Mar 18, 2024 for $405,700.  Currently listed $409,900.",None,None),
 ("",None,None),
 ("MORTGAGE (from your screenshot, loan *5990)",BOLD,None),
 ("• Payoff used: $356,149.76. Payment $3,050.77/mo. Get an official payoff quote — true payoff",None,None),
 ("  runs a bit higher (per-day interest). Only ~$1,550 principal paid since 2024 (normal this early).",None,None),
 ("",None,None),
 ("DEAL MATH (unchanged from v1)",BOLD,None),
 ("• NET proceeds = Sale price − payoff − selling costs = 'money back' toward her $48,000.",None,None),
 ("• Shortfall = $48,000 − NET proceeds.  YOUR payment = Shortfall × 80% (or 70%).",None,None),
 ("",None,None),
 ("CURRENT MARKET — Fuquay-Varina (June 2026)",BOLD,None),
 ("• Median days on market ≈ 85 days (flat vs a year ago) — a slow, normalizing market.",None,None),
 ("• Inventory elevated: ~700+ active listings. Prices down ~3–4% year-over-year.",None,None),
 ("• Net read: this is a BUYER-leaning market. Overpricing sits; competitive pricing moves.",None,None),
 ("• Your home has already sat ~2 weeks at $409,900 with no contract — consistent with the model's",None,None),
 ("  low near-term odds at the top price.",None,None),
 ("",None,None),
 ("SEASONALITY (Triangle / Raleigh area) — answers 'when do odds rise?'",BOLD,None),
 ("• Peak selling season is APRIL–JUNE (fastest sales, best prices). July still strong.",None,None),
 ("• Aug → Oct demand TAPERS; Nov–Jan is the slowest window; odds rebound Feb–Apr.",None,None),
 ("• So over your next 4 months (Jul→Oct 2026) the seasonal trend works AGAINST you — the monthly",None,None),
 ("  chance of selling DECLINES each month. The next natural uptick is ~Feb–Apr 2027.",None,None),
 ("• Bottom line: in the near term, PRICE and EXPOSURE (using an agent) are the levers that raise",None,None),
 ("  your odds — not waiting. Waiting into fall lowers them.",None,None),
 ("",None,None),
 ("HOW THE PROBABILITY COLUMNS ARE BUILT (all factors editable on the Scenarios tab)",BOLD,None),
 ("• Monthly chance of going UNDER CONTRACT = h0 × Price factor × Exposure factor × Season factor.",None,None),
 ("• h0 = 0.25/month: the baseline ~ derived from an ~85-day median time-to-contract.",None,None),
 ("• Price factor = EXP(−k × (price − market value)/market value), k=7. Pricing BELOW the ~$410k",None,None),
 ("  market value raises odds; pricing at/above lowers them. Adjust 'market value' and k to taste.",None,None),
 ("• Exposure factor: full-service 1.10, typical agent 1.05, FSBO+3% buyer agent 0.90, FSBO+2.5% 0.85.",None,None),
 ("  ASSUMPTION: the buyer always has a realtor, so you ALWAYS pay a buyer's-agent commission. 'FSBO'",None,None),
 ("  means you skip the LISTING agent only (saving ~3%) and still pay the buyer's agent — there is no",None,None),
 ("  0% / no-commission case. FSBO is penalized a little (amateur photos/marketing/negotiation), not a",None,None),
 ("  lot, because a competitive buyer-agent commission still gets the home shown.",None,None),
 ("• Season factor: Jul 1.05, Aug 0.95, Sep 0.85, Oct 0.75 (declining into fall, per above).",None,None),
 ("• The four 'P(sold by end of month)' columns are CUMULATIVE — the chance you're under contract",None,None),
 ("  by the end of that month. They rise across months because each month adds another chance,",None,None),
 ("  even though the per-month odds shrink seasonally.",None,None),
 ("• 'Sold' here = under contract / offer accepted, not the closing date (closing is ~30–45 days later).",None,None),
 ("",None,None),
 ("THE CORE TENSION",BOLD,None),
 ("• Lower price / using an agent = HIGHER chance of selling soon, but LOWER net proceeds = you pay",None,None),
 ("  her MORE. Higher price / FSBO = you pay her less IF it sells, but lower odds it sells at all.",None,None),
 ("• Read the table as a trade-off: cross-reference 'YOUR pay' against 'P(sold by end Oct)' per row.",None,None),
 ("",None,None),
 ("These are estimates to compare scenarios, not a guarantee, appraisal, or legal/financial advice.",None,None),
 ("Probabilities are modeled, not market-quoted. Confirm payoff & costs with your servicer/attorney.",None,None),
 ("",None,None),
 ("SOURCES",BOLD,None),
 ("• Listing/sale history: Coldwell Banker & Apartments.com (537 Duchart Ln).",None,None),
 ("• Market: Redfin & Long&Foster Market Minute (Fuquay-Varina DOM/inventory/prices, 2026).",None,None),
 ("• Seasonality: Houzeo, HomeLight, ListWithClever (best time to sell Raleigh/NC, 2025–2026).",None,None),
 ("• Closing costs: ListWithClever, Houzeo, Bankrate, Redfin (NC seller costs & transfer tax).",None,None),
]
for idx,(txt,font,fill) in enumerate(notes,start=1):
    cell(ns,f"A{idx}",txt,font,fill)
ns.row_dimensions[1].height=24

wb.save("/home/user/Claude-Works/House_Sale_Scenarios_537_Duchart.xlsx")
print("saved")
