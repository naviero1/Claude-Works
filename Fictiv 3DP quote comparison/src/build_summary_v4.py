import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

OUT = '../Fictiv_Quote_Comparison_V4.xlsx'
F='Arial'
NAVY,GREEN_H,GREY_H,YELLOW,SECT='FF1F4E78','FFC6E0B4','FFEDEDED','FFFFF2CC','FFD9E1F2'
ORNG_H,ORNG_D='FFF8CBAD','FFFCE4D6'
CUR='\\$#,##0.00'; CURS='\\$#,##0.00;[RED]"($"#,##0.00\\)'; PCT='0.0%;[RED]\\-0.0%'
PCT2='0.00%'; CNT='0" of 15"'
THIN=Border(*[Side(style='thin')]*4)
C='Five-Quote Comparison'; D='Quote 5 Detail'

def sty(c,size=10,b=False,i=False,color=None,fill=None,fmt=None,h=None,v=None,wrap=False,border=True):
    c.font=Font(name=F,sz=size,b=b,i=i,color=color)
    if fill: c.fill=PatternFill('solid',start_color=fill)
    if fmt: c.number_format=fmt
    if h or v or wrap: c.alignment=Alignment(horizontal=h,vertical=v,wrap_text=wrap)
    if border: c.border=THIN
def put(ws,coord,val,**kw):
    cc=ws[coord]; cc.value=val; sty(cc,**kw); return cc

wb=openpyxl.load_workbook(OUT)
idx=wb.sheetnames.index('Summary'); wb.remove(wb['Summary'])
ws=wb.create_sheet('Summary',idx)
for col,w in [('A',62),('B',18),('C',16),('D',16)]: ws.column_dimensions[col].width=w

def section(r,text):
    ws.merge_cells(f'A{r}:D{r}'); put(ws,f'A{r}',text,b=True,fill=SECT,border=False)
    ws.row_dimensions[r].height=15
def kv(r,label,formula,fmt,fill=None,bold=False):
    put(ws,f'A{r}',label,fill=fill,b=bold); put(ws,f'B{r}',formula,fmt=fmt,fill=fill)
    ws.row_dimensions[r].height=15
def obs(r,text):
    ws.merge_cells(f'A{r}:D{r}')
    put(ws,f'A{r}',text,border=False,h='left',v='top',wrap=True)
    ws.row_dimensions[r].height=54.75

ws.merge_cells('A1:D1')
put(ws,'A1','Summary & Insights — Fictiv 3DP Quote Journey (V4, through Sep 3, 2026)',size=14,b=True,border=False)
ws.row_dimensions[1].height=17.35

section(3,'Headline totals (part production, @ Q2 quantities)')
kv(4,'Quote 1 — Fictiv (AI, original)',        f"='{C}'!J21",CUR)
kv(5,'Quote 2 — Fictiv (AI re-quote, Apr 23)', f"='{C}'!K21",CUR)
kv(6,'Quote 3 — Fictiv (MP w/ error, May 1)',  f"='{C}'!L21",CUR)
kv(7,'Quote 4 — Fictiv (MP corrected, May 11) ★',f"='{C}'!M21",CUR,GREEN_H,True)
kv(8,'Quote 5 — MJF China production (Sep 3) ◆ — Tier 1 unit price, like-for-like',f"='{C}'!N21",CUR,ORNG_H,True)

section(10,'The corrected-quote story (Q1 → Q4), unchanged from V3')
kv(11,'Δ Q1 → Q4 ($) — full journey',   f"='{C}'!M21-'{C}'!J21",CURS)
kv(12,'Δ Q1 → Q4 (%) — full journey',   f"=('{C}'!M21-'{C}'!J21)/'{C}'!J21",PCT)
kv(13,'Δ Q2 → Q4 ($) — MP net value',   f"='{C}'!M21-'{C}'!K21",CURS)
kv(14,'Δ Q2 → Q4 (%) — MP net value',   f"='{C}'!Q21",PCT)
kv(15,'Δ Q3 → Q4 ($) — correction',     f"='{C}'!M21-'{C}'!L21",CURS)
kv(16,'Δ Q3 → Q4 (%) — correction',     f"='{C}'!P21",PCT)

section(18,'The new quote (Q5, Sep 3, 2026) against the journey so far')
kv(19,'Δ Q4 → Q5 ($) — the current move',              f"='{C}'!N21-'{C}'!M21",CURS,ORNG_D)
kv(20,'Δ Q4 → Q5 (%) — the current move',              f"='{C}'!R21",PCT,ORNG_D)
kv(21,'Δ Q1 → Q5 ($) — Q5 vs the original AI quote',   f"='{C}'!N21-'{C}'!J21",CURS,ORNG_D)
kv(22,'Δ Q1 → Q5 (%) — Q5 vs the original AI quote',   f"=('{C}'!N21-'{C}'!J21)/'{C}'!J21",PCT,ORNG_D)
kv(23,'Q5 landed total — Tier 1 as quoted (qty 2/part, incl. 7.5% tax + DAP freight)',f"='{D}'!G13",CUR,ORNG_D)
kv(24,'Q5 landed total — Tier 2 as quoted (qty 30/part)',f"='{D}'!G14",CUR,ORNG_D)
kv(25,'Q5 blended landed cost per piece — Tier 1',      f"='{D}'!G53",CUR,ORNG_D)
kv(26,'Q5 blended landed cost per piece — Tier 2',      f"='{D}'!K53",CUR,ORNG_D)

section(28,'Reference — Xometry benchmark (@ Q2 qty, parts only)')
kv(29,'Xometry total',                  f"='{C}'!T21",CUR,GREY_H)
kv(30,'Q4 premium over Xometry ($)',    f"='{C}'!M21-'{C}'!T21",CURS,GREY_H)
kv(31,'Q4 premium over Xometry (%)',    f"=('{C}'!M21-'{C}'!T21)/'{C}'!T21",PCT,GREY_H)
kv(32,'Q5 premium over Xometry ($)',    f"='{C}'!N21-'{C}'!T21",CURS,GREY_H)
kv(33,'Q5 premium over Xometry (%)',    f"=('{C}'!N21-'{C}'!T21)/'{C}'!T21",PCT,GREY_H)

section(35,'MP value-add decomposition (Q2 → Q4)')
for col,txt in [('A','Category'),('B','# Parts'),('C','Q2 Ext ($)'),('D','Q4 Ext ($)')]:
    put(ws,f'{col}36',txt,size=11,b=True,color='FFFFFFFF',fill=NAVY,h='center',v='center')
ws.row_dimensions[36].height=15
put(ws,'A37','Parts rolled back to Q2 price (no MP value)',fill=SECT)
put(ws,'B37',f"=COUNTIF('{C}'!Q6:Q20,\"=0\")",h='center',v='center')
put(ws,'C37',f"=SUMIF('{C}'!Q6:Q20,\"=0\",'{C}'!K6:K20)",fmt=CUR)
put(ws,'D37',f"=SUMIF('{C}'!Q6:Q20,\"=0\",'{C}'!M6:M20)",fmt=CUR)
put(ws,'A38','Parts kept at MP discount (genuine MP value) ★',fill=GREEN_H)
put(ws,'B38',f"=COUNTIF('{C}'!Q6:Q20,\"<0\")",h='center',v='center')
put(ws,'C38',f"=SUMIF('{C}'!Q6:Q20,\"<0\",'{C}'!K6:K20)",fmt=CUR)
put(ws,'D38',f"=SUMIF('{C}'!Q6:Q20,\"<0\",'{C}'!M6:M20)",fmt=CUR)
for r in (37,38): ws.row_dimensions[r].height=15

section(40,'Quote 5 audit findings (detail and formulas on the "Quote 5 Detail" tab)')
kv(41,'Volume-tier discount, Tier 1 → Tier 2 (applied uniformly to all 15 parts)',f"='{D}'!D60",PCT,ORNG_D)
kv(42,'Spread in that tier ratio across the 15 parts',f"='{D}'!D59",PCT2,ORNG_D)
kv(43,'Parts whose Tier-1 price back-solves to a round-dollar base at 85%',f"='{D}'!D61",CNT,ORNG_D)
kv(44,'Implied gross margin at that back-solved base',f"='{D}'!D62",PCT,ORNG_D)
kv(45,'DAP freight as % of parts subtotal — Tier 1',f"='{D}'!D65",PCT,ORNG_D)
kv(46,'DAP freight as % of parts subtotal — Tier 2',f"='{D}'!D66",PCT,ORNG_D)

section(48,'Key observations')
for n,t in enumerate([
 '1. CONFIRMED (V3, unchanged): the +10.34% systematic markup flagged in V2 was a quoting-team mistake. Q4 surgically rolls back 12 of 15 parts to Q2 prices while preserving the 3 MP-discount parts at Q3 prices.',
 "2. The MP's TRUE value-add (Q2→Q4) is $707.20 (-6.4%), entirely concentrated in three parts: 670832 Rim Right (-$333.90), 670833 Rim Left (-$333.20), and 670845 Hanging Plate (-$40.10). Sum = exactly $707.20.",
 '3. The two big-ticket discounts (670832/670833) are mirrored parts with identical Q2→Q4 savings to four sig figs. Strongly suggests these parts nest or process together more efficiently than the AI quoter modeled.',
 '4. Q4 Head Cap (670836) is still quoted at qty 4 in the PDF — confirmed as intentional (not a quoting bug), so the per-unit story is clean even though the as-issued totals differ.',
 '5. Q4 sits ~17% above the Xometry benchmark at like-for-like quantities (down from ~26% in Q3). Meaningful narrowing of the gap, but still a material premium worth thinking about as a sourcing question.',
 '6. The original V1/V2 hypothesis is vindicated — pushing back on the +10.34% pattern was the right call. When MP holistic re-quotes show suspiciously uniform price moves on most parts but big concessions on a few, default to suspecting a multiplier error.',
 '7. NEW — Q5 lands almost exactly back at Q1. At like-for-like quantities Q5 totals ~$27.4k against Q1\'s $27.5k, within ~0.4%. Sixteen months of re-quoting and one acknowledged correction have, at prototype volume, returned to the original AI quote\'s level. That is the headline to take into the next conversation.',
 '8. NEW — the Q5 volume discount is a flat multiplier, not part economics. Every one of the 15 Tier-2 prices is exactly 45.00% of its Tier-1 price; the spread across all 15 parts is effectively zero. A genuine volume curve would differ part by part, because nesting efficiency, part height and post-processing labour do not scale identically. This is a pricing policy applied on top, which means it is negotiable — and it is worth asking for a mid-tier (qty 5–10) rather than being pushed from 2 straight to 30.',
 '9. NEW — 13 of 15 Tier-1 prices back-solve to a round-dollar base at an 85% divisor ($200, $260, $280, $300, $375, $1,000, $1,100, $1,150, $1,480, $1,850 and so on), implying a round internal cost with a 15% margin on top. The two that break the pattern are 670832 and 670833 — the same mirrored rim pair that carried the real MP discounts in Q3/Q4. Those two appear to have been priced by hand while the other 13 came off a rate card.',
 '10. NEW — freight gives no leverage. DAP freight runs ~4.4% of parts subtotal at Tier 1 and ~5.3% at Tier 2, so it scales with value rather than flattening out. Ordering more does not amortise shipping; the case for Tier 2 has to be made on the 55% part discount alone.',
 '11. OPEN — process parity is unverified. Q5 is explicitly MJF / Nylon 12 / Black / Vapor Smoothed. The workbook never recorded the process for Q1–Q4, and vapor smoothing is a real cost adder. Confirm Q1–Q4 were quoted to the same finish spec before treating Δ Q4→Q5 as a like-for-like price move — if they were not, most of the Q4→Q5 jump may be scope, not inflation.',
 '12. OPEN — the vendor on the Q5 pages is not named. The pages supplied show no vendor identity, and the quote is China production while the Fictiv history is not documented as such. Confirm the issuer before this row is cited internally as a Fictiv quote.',
]):
    obs(49+n,t)
wb.save(OUT)
print('stage 2 saved. sheets:',wb.sheetnames)
