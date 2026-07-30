#!/usr/bin/env python3
"""PVA_Supplier_Longlist.xlsx — consolidated ranked longlist of US PVA toll candidates."""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

ARIAL="Arial"
def f(bold=False,size=10,color="000000",italic=False):
    return Font(name=ARIAL,bold=bold,size=size,color=color,italic=italic)
HDR=PatternFill("solid",fgColor="1F3864")
SUB=PatternFill("solid",fgColor="D6DCE5")
A_FILL=PatternFill("solid",fgColor="C6EFCE")   # tier A green
B_FILL=PatternFill("solid",fgColor="FFF2CC")   # tier B amber
C_FILL=PatternFill("solid",fgColor="F2F2F2")   # tier C grey
thin=Side(style="thin",color="D9D9D9")
BORD=Border(left=thin,right=thin,top=thin,bottom=thin)
LINK=Font(name=ARIAL,size=9,color="0563C1",underline="single")

wb=openpyxl.Workbook()

# ============ TAB 1 — Criteria & Method ============
c=wb.active; c.title="Criteria & Method"
c.sheet_view.showGridLines=False
c.column_dimensions['A'].width=2; c.column_dimensions['B'].width=30; c.column_dimensions['C'].width=90
c['B2']="US PVA Toll-Supplier Longlist — Criteria & Method"; c['B2'].font=f(bold=True,size=15,color="1F3864")
c['B3']="42 real US candidates (websites verified during research), found to be 'alikes to SNP' — able to toll-make our aqueous PVA solution."
c['B3'].font=f(italic=True,size=9,color="595959")

def sec(r,t):
    cell=c.cell(row=r,column=2,value=t); cell.font=f(bold=True,color="FFFFFF")
    for col in (2,3): c.cell(row=r,column=col).fill=HDR
def kv(r,k,v):
    c.cell(row=r,column=2,value=k).font=f(bold=True); c.cell(row=r,column=2).alignment=Alignment(vertical="top")
    cell=c.cell(row=r,column=3,value=v); cell.font=f(); cell.alignment=Alignment(wrap_text=True,vertical="top")

sec(5,"SCREENING CRITERIA (used to rank/tier)")
crit=[("1. HARD GATE — heat","Jacketed, temp-controlled reactors that reach 90-95 C (near-boiling aqueous) and HOLD 30-45 min. Steam or hot-oil jacket = strong positive."),
 ("2. Toll / custom liquid","US custom/toll LIQUID chemical blender, or a maker of PVA solutions — makes to a customer's formula."),
 ("3. PVA / polymer","Experience dissolving PVA or water-soluble / high-MW polymers (rarely advertised — mostly 'verify')."),
 ("4. Small batch / MOQ","Drum-scale, make-to-order, low MOQ — fits ~1 drum/week and the 18-day shelf life."),
 ("5. QC / materials","QC lab (% solids, pH, Brookfield viscosity), 316L SS, 200-micron filtration."),
 ("6. Bonus","ISO 9001 / 13485, pigment-dispersion capability, freight-friendly to a GA-area incumbent, financial stability.")]
r=6
for k,v in crit: kv(r,k,v); r+=1

sec(13,"TIERS")
kv(14,"Tier A (best fit)","Clears or very likely clears the hard gate AND is toll + small-batch + polymer/aqueous-relevant. Call first.")
kv(15,"Tier B (good, verify)","Capable tollers; heat or PVA experience plausible but unconfirmed — one phone call from the shortlist.")
kv(16,"Tier C (special role / weaker)","Resin suppliers, PVA distributors, film casters, or scale/focus mismatches — useful for materials or as technical resources, not primary tollers.")

sec(18,"METHOD & CAVEATS")
kv(19,"How found","Five parallel research streams: national toll blenders; PVA/PVOH specialists; waterborne coatings/adhesives tollers; textile/paper/sizing houses; regional small-batch tollers. All excluded the existing roster.")
kv(20,"Confidence","H/M/L reflects how well the public evidence fits. 'unknown - verify' means the website was silent; capability was NOT assumed.")
kv(21,"Two things to verify on EVERY candidate","(1) Exact reachable/holdable batch temp (90-95 C for 30-45 min) where a page only said 'jacketed/heated'; (2) willingness to take a small ~1-drum/week (~50 drum/yr) recurring job — several lean large-batch.")
kv(22,"Price reality","~$0.75/lb delivered (SNP) is aggressive for a US specialty toller on a pigmented, filtered, heated aqueous product — expect most quotes above that (see the market model: base ~$1.40/lb).")
kv(23,"Already on file (existing roster)","APV, CJB, Piedmont, Columbus/CCI, CORECHEM, Northstar, Sekisui, + dropped/eliminated — see the Supplier Roster tab in PVA_Second_Source_Pricing_Model.xlsx. These 42 are NEW, additional options.")

# ============ TAB 2 — Longlist ============
L=wb.create_sheet("Longlist (42)")
L.sheet_view.showGridLines=False
heads=["Tier","Company","Location","Website","Lane","Toll liquid?","PVA / polymer exp","Heat 90-95 C?","Small-batch / MOQ fit","QC / ISO / 316L","Why alike to SNP (notes)","Conf."]
widths=[6,26,26,26,20,14,20,20,24,20,40,7]
for i,w in enumerate(widths): L.column_dimensions[chr(65+i)].width=w
for i,h in enumerate(heads):
    cell=L.cell(row=1,column=1+i,value=h); cell.font=f(bold=True,color="FFFFFF"); cell.fill=HDR
    cell.alignment=Alignment(horizontal="center",wrap_text=True,vertical="center"); cell.border=BORD
L.freeze_panes="A2"; L.row_dimensions[1].height=30

rows=[
# Tier, Company, Location, Website, Lane, Toll?, PVA/poly, Heat, Smallbatch, QC/ISO, Why, Conf
("A","PhilChem (Mount Vernon Chem)","Greer, SC","https://www.philchem.us","Textile sizing / paper","Y toll+repackage","Y — PVA sizing heritage","Y jacketed heat/cool SS","Excellent — 3 to 100 drum batches","verify ISO/316L","Sizing house that already cooks aqueous PVA to spec at drum scale — closest process analog","H"),
("A","Tiarco / TRCC (Tiarco Chemical)","Dalton, GA","https://trcc.com","Aqueous coatings/adhesives toll","Y custom/toll","Partial — aqueous + emulsion polymer","Y — 316L heated/cooled reactors","Moderate — 90-gal reactor + pilot; MOQ verify","316L SS; ISO verify","Aqueous polymer toll with 316L heated reactors, in GA","H"),
("A","MFG Chemical","Chattanooga, TN + Dalton, GA","https://mfgchemical.com","Specialty / toll manufacturer","Y core toll","Y — 'water-soluble polymers' listed","Y hot-oil to 550 F, steam","100-gal 316 pilot; prod 2,000 gal+ (MOQ caveat)","ISO 9001","Explicit water-soluble-polymer toller, ISO, drum-out, GA/TN","H (cap)"),
("A","Chemjet","Houston, TX","https://www.chemjet.com","Custom / contract blending","Y custom + contract","unknown - verify","Y — 210 F heat room for HMW intermediates","drum/tote; MOQ verify","ISO 9001 + API Q1, QC lab","Dedicated heat room to dissolve high-MW polymer before dilution = the PVA cook","H"),
("A","REXCO-USA (PARTALL)","Conyers, GA","https://rexco-usa.com","PVA parting-film maker","Maybe — private-label verify","Y — makes pigmented aqueous PVA solutions","Y implied — verify","gallons to bulk; small feasible","verify","Literally makes pigmented aqueous PVA solutions and drums them — best product analog, in GA","H exist / M toll"),
("A","Colonial Chemical Solutions","Savannah, GA (+Atlanta/Charlotte/Richmond)","https://colonialchemicals.com","Regional custom blender","Y custom blending","unknown - verify","Partial — heated SS tank; 90-95 verify","Excellent — 50-gal minimum batch","verify","Tiny 50-gal batches, heated, DI water, GA freight","H fit / M heat"),
("A","Toll Solutions","Duncan, SC","https://tollsolutions.com","Toll chemical manufacturer","Y dedicated toll","unknown - verify","Y jacketed to 150 C","Good — 50 to 5,600 gal, 250-gal pilot","304 SS (not 316L); ISO verify","Jacketed heated vessels, 50-gal batches, SC freight","H cap / M PVA"),
("A","Key Polymer","Lawrence, MA","https://keypolymer.com","Coatings/adhesives toll","Y to customer formula","unknown - verify","Likely Y jacketed heat/cool (temp verify)","Good — 5 to 5,000 gal incl 75-gal 316 SS","ISO 9001, 316 SS","ISO toller with heated 316 SS vessels down to small batch","H / M temp"),
("A","Valpac","Federalsburg + Hurlock, MD","https://valpac.com","Water-based adhesive/coating toll","Y toll since 1983","unknown - verify","Y steam + hot-oil jacketed SS","Good — drums/totes/pails","ISO 9001 (impl) + AS9100","Dedicated water-based adhesive toller, steam-jacketed, drum-out","H"),
# Tier B
("B","Hydrite Chemical","Brookfield, WI (+SC, TX, multi)","https://www.hydrite.com","Custom liquid toll","Y drums to railcars","unknown - verify","Y hot-oil reactors to 575 F","drums OK but large-min caveat","ISO 9001, 24/7 QC lab","National toll with hot-oil reactors and strong QC","H cap / M small-batch"),
("B","Aexcel Corporation","Mentor, OH","https://www.aexcelcorp.com","Waterborne coatings toll","Y toll","unknown - verify","unknown - verify","25 to 8,000 gal; 55-gal drums / IBC","color lab; ISO verify","Proven waterborne coatings toller that drums product","H / M"),
("B","Apollo Chemical (Mount Vernon)","Burlington, NC","https://apollochemical.com","Textile chem + custom mfg","Y custom/specialty","unknown - verify","unknown - verify","verify","verify","Carolina textile-chem with a contract arm (PhilChem's sister)","M-H"),
("B","Nation Ford Chemical","Fort Mill, SC","https://nationfordchem.com","Custom synthesis / toll","Y toll","unknown - verify","Likely Y reactors (verify)","Good — 10 to 250-gal pilot reactors","verify","Small pilot reactors for recurring custom runs, SC freight","M"),
("B","Ethox Chemicals","Greenville, SC","https://www.ethox.com","Custom synthesis / toll","Y toll","unknown (alkoxylation focus)","Y likely heated reactors","lab / pilot / commercial","verify","Upstate-SC toll manufacturer open to custom aqueous projects","M"),
("B","Peach State Labs / PSG","Rome, GA","https://polymersolutionsgroup.com","Water-soluble polymer maker","verify","unknown - verify","Y likely (polymer synthesis)","verify","verify","Textile-rooted water-soluble-polymer maker with reactors","M"),
("B","Polyventive (American Emulsions)","Calhoun + Dalton, GA","https://www.polyventive.com","Textile / paper emulsions","verify","unknown - verify","Likely (emulsion/coating) verify","verify","verify","Textile + paper coating chemistry in the Dalton belt","M"),
("B","Sandstrom Coating Technologies","Port Byron, IL","https://sandstromproducts.com","Waterborne coatings toll","Y toll","unknown - verify","unknown - verify","1 to 5,000 gal","ISO 9001, R&D lab","Long-running waterborne coatings toller, ISO 9001","M"),
("B","Sierra Performance Coatings","Minnetonka, MN","https://sierrapaint.com","Waterborne coatings toll","Y toll","unknown - verify","unknown - verify","single-run to truckloads","color; ISO verify","Waterborne toll dispersions made to spec","M-H"),
("B","American Dispersions","Louisville, KY","http://www.americandispersions.com","Aqueous dispersions / solutions","Y custom","unknown (makes 'solutions')","unknown - verify","verify","verify","Makes exactly the class — aqueous solutions/dispersions","M"),
("B","Alpha Chemical Services","Stoughton, MA","https://alphachemical.com","Liquid blending / filling","Y","unknown - verify","Likely Y steam-jacketed (temp verify)","50 to 5,000 gal","ISO 9001","ISO liquid blender, steam-jacketed from 50 gal","M"),
("B","Hanson Chemicals","Friendship, NY","https://hansonchemicals.com","Toll blending","Y","unknown - verify","Partial — temp-controlled (verify)","Good — pilot to large, drums/totes","ISO-certified","Flexible pilot-batch toller with drum-out, Northeast","M"),
("B","Seacole (Seacole-CRC)","Maple Grove, MN","https://seacole.com","Custom contract mfr","Y","Partial — 'water-soluble organic blends'","Likely Y jacketed (verify)","150 to 3,000 gal","verify","Jacketed heat/cool tanks + water-soluble aqueous blends","M"),
("B","Camco Chemical","Florence, KY","https://www.camco-chem.com","Liquid + powder toll","Y","unknown - verify","unknown - verify","27-mixer fleet","ISO 9001","Established regional liquid toll blender, ISO, drum-out","M"),
("B","TBK One (TBK Mfg)","Carrollton, TX","https://tbk-one.com","Custom / toll blending","Y","unknown - verify","unknown - verify","Strong — low MOQ, startup-friendly","verify","Explicitly courts low-MOQ recurring / startup jobs","M"),
("B","Capital Resin Corporation","Columbus, OH","https://capitalresin.com","Toll resin / polymer","Y toll","unknown (polymer plausible)","Likely Y reactors","early-stage + production","24-hr QC","Toll polymer/resin maker open to early-stage recurring work","M"),
("B","Hubbard-Hall","Waterbury, CT + Inman, SC","https://www.hubbardhall.com","Custom aqueous blender","Y","unknown - verify","unknown - verify","verify","3 labs","Long-established custom aqueous blender with SC footprint","M-L"),
("B","Custom Chemical Formulators (CCFI)","Santa Fe Springs, CA","https://www.customchem.com","Liquid toll (startup-focused)","Y","unknown - verify","unknown — in-process heating; verify temp","Strong — startup, fast batch","chemist QC","West-Coast startup-friendly toller (verify heat gate)","M / L heat"),
("B","Spectrachem","Lodi, NJ","https://spectrachem.net","Pigment dispersion + adhesives","Y custom, short runs","unknown - verify","unknown - verify","short runs / small pack","verify","Pigment dispersion + water-based adhesives, short runs (our product is pigmented)","M"),
("B","Spectra Colorants","Union, SC","https://spectracolorants.com","Water-based pigment dispersions","Y","unknown - verify","unknown - verify","verify","batch QC","Dedicated water-based pigment disperser, SC","M"),
# Tier C
("C","Kuraray America","Houston / Pasadena / La Porte, TX","https://kuraray.us.com","PVOH RESIN producer","N — resin only","Y — makes super-hydrolyzed HMW PVOH","Y (at scale)","bulk resin","ISO 9001 / 14001","RESIN SOURCE — cheapest super-hydrolyzed HMW PVA + technical resource","H (as resin)"),
("C","MonoSol (a Kuraray company)","Merrillville, IN","https://www.monosol.com","PVA film caster","N — captive","Y — heated PVA dissolution is core","Y","large continuous lines","verify","Deepest US PVA-dissolution know-how — possible technical partner","H exist / L toll"),
("C","Mitsubishi Chemical America (Gohsenol)","US sales office","https://us.mitsubishi-chemical.com","Specialty PVOH resin","N — US sales only","Y resin","n/a","resin","mfr QC","Alt specialty/modified PVOH resin source (no US plant)","M"),
("C","Chang Chun Petrochemical","Taiwan (US = distribution)","https://www.ccpgp.com","PVA resin producer","N — import","Y resin","n/a","resin","mfr QC","Competitive imported PVA resin (no US plant)","M"),
("C","Aicello America (Solublon)","Japan (US mfg unconfirmed)","https://www.aicello.com","PVA film","N","Y — film","n/a","film","verify","Deep PVA-dissolution expertise; likely no US production","M / L"),
("C","The Chemical Company (TCC)","Jamestown, RI","https://thechemco.com","PVA distributor","N — distributor","Y — supplies PVA, sometimes as solutions","n/a","repackage","verify","Deep PVA product knowledge; sources solutions rather than cooking them","L"),
("C","Stoner Molding Solutions","Quarryville, PA","https://stonermolding.com","Water-based PVA release maker","Maybe — private-label verify","Y — water-based PVA release","unknown - verify","batch, bulk pack","verify","Formulates water-based PVA release chemistry in-house","M"),
("C","Troy Chemical (Troy Corp)","Florham Park, NJ","https://www.troychemical.com","Toll aqueous + biocide maker","Y toll aqueous","unknown - verify","unknown - verify","drums/totes/bulk","ISO 9001","ISO toll of aqueous solutions + biocide maker (our formula has a biocide)","M-L"),
("C","Chemical Solvents (CSI)","Cleveland, OH","https://chemicalsolvents.com","Aqueous / solvent blends","Y","unknown - verify","unknown - verify","pails to tankers","verify","Aqueous toll blender, high-viscosity capable","L"),
("C","CHT USA (CHT Group)","Richmond, VA","https://www.cht.com/en","Textile specialty chem batch","verify","unknown - verify","unknown - verify","batch production","verify","Textile-chemical batch manufacturer with formulation flexibility","L-M"),
("C","Southern Chemical & Textiles","Dalton, GA","https://southern-chemical.com","Surfactant / textile chem","verify","unknown (surfactant focus)","unknown - verify","verify","advanced QC lab","Dalton-belt textile/adhesive chem; PVA relevance weak","L"),
("C","South Coast Terminals","Houston, TX","https://scterm.com","Toll blender (oil-side)","Y","unknown - verify","Y steam 10-150 psi","too big — 10 MT+ batches","ISO, strong lab","Steam-heated with a real lab, but large-scale and oil-side focus","L"),
("C","Formula Corp","Auburn, WA","https://formulacorp.com","Toll blender (personal care)","Y","unknown - verify","unknown - verify","verify","verify","Real toller but personal-care/cleaning focus — weak industrial-PVA fit","L"),
]

r=2
for row in rows:
    tier=row[0]
    fill = A_FILL if tier=="A" else B_FILL if tier=="B" else C_FILL
    for j,val in enumerate(row):
        cell=L.cell(row=r,column=1+j,value=val)
        cell.alignment=Alignment(wrap_text=True,vertical="top",horizontal="center" if j in (0,5,7,11) else "left")
        cell.border=BORD; cell.font=f(size=9)
        if j==0: cell.font=f(bold=True,size=11)
        if j==3:  # website hyperlink
            cell.hyperlink=val; cell.font=LINK
        L.cell(row=r,column=1+j).fill=fill
    r+=1

# ============ TAB 3 — Shortlist ============
S=wb.create_sheet("Shortlist — call these first")
S.sheet_view.showGridLines=False
S.column_dimensions['A'].width=2; S.column_dimensions['B'].width=30; S.column_dimensions['C'].width=20; S.column_dimensions['D'].width=64
S['B2']="Shortlist — the calls to make first"; S['B2'].font=f(bold=True,size=14,color="1F3864")
S['B3']="Ranked for a small ~1 drum/week recurring toll job, freight-friendly to a GA-area incumbent. Confirm heat-hold + MOQ on each call."
S['B3'].font=f(italic=True,size=9,color="595959")
for i,h in enumerate(["#","Company","Location","Why first / what to confirm"]):
    cell=S.cell(row=5,column=2+i,value=h); cell.font=f(bold=True,color="FFFFFF"); cell.fill=HDR; cell.border=BORD; cell.alignment=Alignment(horizontal="center")
short=[
 ("PhilChem","Greer, SC","Best analog: sizing house already cooking aqueous PVA in jacketed vessels at 3-100 drum batches, toll-blends to spec. Confirm site is live, PVA-cook + MOQ."),
 ("Tiarco / TRCC","Dalton, GA","316L heated/cooled reactors + aqueous/emulsion polymer, in GA. Confirm smallest batch and that they'll take ~1 drum/week."),
 ("REXCO-USA (PARTALL)","Conyers, GA","Literally makes pigmented aqueous PVA solutions and drums them, in GA. Ask about custom/private-label toll and heat process."),
 ("MFG Chemical","Chattanooga, TN / Dalton, GA","Explicit water-soluble polymers + ISO 9001 + hot-oil reactors. Pressure-test willingness on tiny (1-drum) batches via the 100-gal pilot line."),
 ("Chemjet","Houston, TX","210 F heat room purpose-built for dissolving HMW polymer + ISO 9001/API Q1 QC. Confirm PVA experience and small-batch MOQ."),
 ("Colonial Chemical Solutions","Savannah, GA","50-gal minimum batch, heated tank, GA freight. Confirm 90-95 C hold and PVA experience."),
 ("Toll Solutions","Duncan, SC","Jacketed reactors to 150 C, 50-gal batches, SC freight. Note 304 SS (ask about 316L) and PVA willingness."),
 ("Key Polymer","Lawrence, MA","ISO 9001 + heated 316 SS vessels down to 75 gal. Confirm exact reachable temp and PVA experience."),
 ("Valpac","Federalsburg / Hurlock, MD","Water-based adhesive toller, steam + hot-oil jacketed SS, drums/totes, ISO. Our product behaves like a water-soluble adhesive."),
 ("Kuraray America","Houston, TX","Not a toller — the resin source. Line up super-hydrolyzed HMW PVOH supply + free technical support for whichever toller wins."),
]
r=6
for i,(co,loc,why) in enumerate(short,1):
    S.cell(row=r,column=2,value=i if co!="Kuraray America" else "R").font=f(bold=True); S.cell(row=r,column=2).alignment=Alignment(horizontal="center",vertical="top")
    S.cell(row=r,column=3,value=co).font=f(bold=True); S.cell(row=r,column=3).alignment=Alignment(vertical="top")
    S.cell(row=r,column=4,value=loc).font=f(); S.cell(row=r,column=4).alignment=Alignment(vertical="top")  # placeholder shift
    r+=1
# fix: rebuild shortlist rows with proper columns
for row in S.iter_rows(min_row=6):
    for cell in row: cell.value=None
r=6
for i,(co,loc,why) in enumerate(short,1):
    num = i if co!="Kuraray America" else "resin"
    vals=[num,co,loc,why]
    for j,val in enumerate(vals):
        cell=S.cell(row=r,column=2+j,value=val)
        cell.alignment=Alignment(wrap_text=True,vertical="top",horizontal="center" if j==0 else "left")
        cell.border=BORD; cell.font=f(bold=(j in(1,)))
        cell.fill = A_FILL if co!="Kuraray America" else C_FILL
    r+=1

out="/home/user/Claude-Works/PVA second supplier initiative/PVA_Supplier_Longlist.xlsx"
wb.save(out); print("saved",out,"| rows:",len(rows))
