import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# ---------- styling helpers ----------
TITLE = Font(bold=True, size=14, color="FFFFFF")
HDR   = Font(bold=True, size=10, color="FFFFFF")
BOLD  = Font(bold=True)
input_fill = PatternFill("solid", fgColor="FFF2CC")   # yellow = editable input
hdr_fill   = PatternFill("solid", fgColor="1F4E78")    # dark blue
title_fill = PatternFill("solid", fgColor="2E75B6")
you_fill   = PatternFill("solid", fgColor="FCE4D6")    # light orange = your payment
her_fill   = PatternFill("solid", fgColor="E2EFDA")    # light green
grp_fill   = PatternFill("solid", fgColor="DDEBF7")
money = '#,##0'
pct   = '0.0%'
thin = Side(style="thin", color="BFBFBF")
border = Border(left=thin, right=thin, top=thin, bottom=thin)

def cell(ws, coord, val, font=None, fill=None, fmt=None, align=None, bd=False):
    c = ws[coord]; c.value = val
    if font: c.font = font
    if fill: c.fill = fill
    if fmt: c.number_format = fmt
    if align: c.alignment = Alignment(horizontal=align, vertical="center", wrap_text=True)
    if bd: c.border = border
    return c

# ================= SCENARIOS SHEET =================
ws = wb.active
ws.title = "Scenarios"

cell(ws, "A1", "House Sale Scenarios — 537 Duchart Ln, Fuquay-Varina NC", TITLE, title_fill)
ws.merge_cells("A1:L1"); ws.row_dimensions[1].height = 24

# ---- INPUTS ----
cell(ws, "A3", "INPUTS (edit yellow cells — everything recalculates)", BOLD)
inputs = [
    ("A4","Purchase price (sold Mar 18, 2024)","B4",405700,money),
    ("A5","Down payment (her contribution)","B5",48000,money),
    ("A6","Current mortgage balance / payoff","B6",356149.76,money),
    ("A7","Excise/transfer tax rate (NC = $1 per $500)","B7",0.002,pct),
    ("A8","Other closing costs - attorney/title/misc (flat $)","B8",2000,money),
    ("A9","HER recovery share — Option A","B9",0.80,pct),
    ("A10","HER recovery share — Option B","B10",0.70,pct),
]
for lab_c, lab, val_c, val, fmt in inputs:
    cell(ws, lab_c, lab)
    cell(ws, val_c, val, BOLD, input_fill, fmt, bd=True)

# ---- TABLE ----
hdr_row = 13
headers = ["Sale price","Selling option","Commission %","Commission $",
           "Other closing $","Total selling costs","NET proceeds\n(money back to her)",
           "Shortfall\nvs $48k","YOUR payment\n@ 80%","YOUR payment\n@ 70%",
           "Her total\nrecovery @80%","Her total\nrecovery @70%"]
for i,h in enumerate(headers):
    cell(ws, f"{get_column_letter(i+1)}{hdr_row}", h, HDR, hdr_fill, align="center", bd=True)
ws.row_dimensions[hdr_row].height = 42

sale_prices = [390000, 395000, 399000, 405000, 409900]
options = [
    ("Full-service agent (6%)", 0.06),
    ("Typical agent (5.5%)", 0.055),
    ("FSBO + buyer agent only (2.5%)", 0.025),
    ("Full FSBO — no agents (0%)", 0.00),
]

r = hdr_row + 1
for sp in sale_prices:
    block_start = r
    for name, comm in options:
        A=f"A{r}"; B=f"B{r}"; C=f"C{r}"; D=f"D{r}"; E=f"E{r}"; F=f"F{r}"
        G=f"G{r}"; H=f"H{r}"; I=f"I{r}"; J=f"J{r}"; K=f"K{r}"; L=f"L{r}"
        cell(ws, A, sp, None, grp_fill, money, bd=True)
        cell(ws, B, name, None, None, None, "left", bd=True)
        cell(ws, C, comm, None, None, pct, bd=True)
        cell(ws, D, f"={A}*{C}", None, None, money, bd=True)
        cell(ws, E, f"={A}*$B$7+$B$8", None, None, money, bd=True)
        cell(ws, F, f"={D}+{E}", None, None, money, bd=True)
        cell(ws, G, f"={A}-$B$6-{F}", BOLD, None, money, bd=True)
        cell(ws, H, f"=MAX(0,$B$5-{G})", None, None, money, bd=True)
        cell(ws, I, f"={H}*$B$9", BOLD, you_fill, money, bd=True)
        cell(ws, J, f"={H}*$B$10", BOLD, you_fill, money, bd=True)
        cell(ws, K, f"={G}+{I}", None, her_fill, money, bd=True)
        cell(ws, L, f"={G}+{J}", None, her_fill, money, bd=True)
        r += 1

# column widths
widths = [12,30,11,12,12,12,14,11,12,12,12,12]
for i,w in enumerate(widths):
    ws.column_dimensions[get_column_letter(i+1)].width = w
ws.freeze_panes = "A14"

# ================= NOTES SHEET =================
ns = wb.create_sheet("Notes & Assumptions")
ns.column_dimensions["A"].width = 100
notes = [
    ("House Sale Scenarios — Notes & Assumptions", TITLE, title_fill),
    ("", None, None),
    ("PROPERTY (verified online)", BOLD, None),
    ("• 537 Duchart Ln, Fuquay-Varina, NC 27526 — 3 bd / 2.5 ba, 2,216 sq ft, Lakestone Village.", None, None),
    ("• Recorded sale: March 18, 2024 for $405,700 (you recalled ~April 2024 / ~$407,500 — very close).", None, None),
    ("• Currently listed on Zillow at $409,900.", None, None),
    ("", None, None),
    ("MORTGAGE (from your screenshot, loan *5990)", BOLD, None),
    ("• Current balance / payoff used: $356,149.76.", None, None),
    ("• Monthly payment: $3,050.77 (with a recurring -$712.80 escrow advance refund line).", None, None),
    ("• Original loan was ~$357,700 (405,700 - 48,000). After ~26 months you've paid down only ~$1,550 of", None, None),
    ("  principal — normal this early in a loan (almost all of each payment is interest + escrow).", None, None),
    ("• NOTE: the true payoff figure is usually a bit higher than the screen balance (per-day interest +", None, None),
    ("  any fees). Get an official 'payoff quote' from the servicer before relying on exact net numbers.", None, None),
    ("", None, None),
    ("HOW THE NUMBERS WORK", BOLD, None),
    ("• NET proceeds = Sale price − Mortgage payoff − Total selling costs. This is the cash left at closing", None, None),
    ("  = the 'money back from the house sale' that goes toward recovering her $48,000.", None, None),
    ("• Shortfall = $48,000 − NET proceeds (the part of her down payment the sale did NOT return).", None, None),
    ("• YOUR payment to her = Shortfall × 80% (Option A) or × 70% (Option B), per her proposed deal.", None, None),
    ("• Her total recovery = NET proceeds + YOUR payment.", None, None),
    ("", None, None),
    ("SELLING-COST ASSUMPTIONS (NC averages)", BOLD, None),
    ("• Agent commission: full-service ≈ 5.5%–6% total (split listing + buyer agent). Modeled at 6%, 5.5%,", None, None),
    ("  a FSBO case where you still offer the buyer's agent 2.5%, and a pure FSBO at 0%.", None, None),
    ("• Other closing costs: NC excise/transfer tax = $1 per $500 (0.2%) + ~$2,000 flat for attorney,", None, None),
    ("  title, recording & misc. (NC non-commission seller costs average ~2.5%, but much of that is", None, None),
    ("  optional concessions/prorations — adjust the flat $ and rate cells to taste.)", None, None),
    ("• NOT included: any seller concessions to the buyer, home-warranty, repairs, or staging. Add them to", None, None),
    ("  the 'Other closing costs' input if you expect them.", None, None),
    ("", None, None),
    ("BIG PICTURE", BOLD, None),
    ("• At a sale price below ~$406k you are essentially selling near/under what you owe once costs are", None, None),
    ("  added, so net proceeds are small — meaning a large shortfall against the $48k, and a larger payment", None, None),
    ("  from you. The lower the price AND the higher the commission, the more YOU pay her.", None, None),
    ("• Going FSBO (no/low commission) is the single biggest lever to shrink your payment — see the table.", None, None),
    ("", None, None),
    ("SOURCES", BOLD, None),
    ("• Coldwell Banker / Apartments.com listing for 537 Duchart Ln (sale history & current list price).", None, None),
    ("• ListWithClever, Houzeo, Bankrate, Redfin — NC seller closing costs & transfer tax (2024–2026).", None, None),
    ("", None, None),
    ("This is an estimate to compare scenarios, not legal/financial/tax advice. Confirm payoff and closing", None, None),
    ("costs with your mortgage servicer and a NC closing attorney before finalizing any agreement.", None, None),
]
for i,(txt,font,fill) in enumerate(notes, start=1):
    c = cell(ns, f"A{i}", txt, font, fill)
    if i==1:
        ns.merge_cells("A1:A1"); ns.row_dimensions[1].height=24

wb.save("/home/user/Claude-Works/House_Sale_Scenarios_537_Duchart.xlsx")
print("saved")
