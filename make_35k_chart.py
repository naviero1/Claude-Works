plabels=["$390k","$395k","$399k","$405k","$409.9k"]
agent35=[25380,20665,16893,11235,6614]
fsbo35=[13680,8815,4923,-915,-5683]
REF14=14000

AW,AH=780,460; ax0,ax1,ay0,ay1=86,660,54,380
VMIN,VMAX=-8000,28000
def ay(v): return ay1-(v-VMIN)/(VMAX-VMIN)*(ay1-ay0)
def ax(i): return ax0+(ax1-ax0)*i/4
def poly(vals): return " ".join(f"{ax(i):.1f},{ay(v):.1f}" for i,v in enumerate(vals))

grid=""
for g in [-5000,0,5000,10000,15000,20000,25000]:
    y=ay(g); cls="zero" if g==0 else "grid"
    grid+=f'<line class="{cls}" x1="{ax0}" y1="{y:.1f}" x2="{ax1}" y2="{y:.1f}"/>'
    lab=f"${g:,.0f}".replace("$-","–$")
    grid+=f'<text class="tick" x="{ax0-10}" y="{y+4:.1f}" text-anchor="end">{lab}</text>'
# green band below zero (you gain)
yz=ay(0); yb=ay(VMIN)
band=f'<rect class="gainband" x="{ax0}" y="{yz:.1f}" width="{ax1-ax0}" height="{yb-yz:.1f}"/>'
xlab=""
for i,l in enumerate(plabels):
    xlab+=f'<text class="tick" x="{ax(i):.1f}" y="{ay1+22}" text-anchor="middle">{l}</text>'
# ref line at 14k
yr=ay(REF14)
ref=f'<line class="ref14" x1="{ax0}" y1="{yr:.1f}" x2="{ax1}" y2="{yr:.1f}"/>'
ref+=f'<text class="ref14t" x="{ax0+6}" y="{yr-7:.1f}">your old $14k plan (≈ flat)</text>'
dots=""
for i,(a,f) in enumerate(zip(agent35,fsbo35)):
    dots+=f'<circle class="s8 mk" cx="{ax(i):.1f}" cy="{ay(a):.1f}" r="4.5"/>'
    dots+=f'<circle class="s1 mk" cx="{ax(i):.1f}" cy="{ay(f):.1f}" r="4.5"/>'
end =f'<text class="lab s8t" x="{ax(4)+8:.1f}" y="{ay(agent35[4]):.1f}">Agent</text>'
end+=f'<text class="lab s1t" x="{ax(4)+8:.1f}" y="{ay(fsbo35[4])+4:.1f}">FSBO</text>'
# value labels on FSBO endpoints (highlight the gain)
vlab=f'<text class="vtag" x="{ax(3):.1f}" y="{ay(-915)-10:.1f}" text-anchor="middle">–$915</text>'
vlab+=f'<text class="vtag" x="{ax(4):.1f}" y="{ay(-5683)+18:.1f}" text-anchor="middle">–$5,683</text>'

html=f'''<div class="viz-root">
<style>
.viz-root{{--surface:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--grid:#e1e0d9;--axis:#c3c2b7;
  --s1:#2a78d6;--s8:#eb6834;--ref:#d03b3b;--good:#0ca30c;
  font-family:system-ui,-apple-system,"Segoe UI",sans-serif;background:var(--surface);color:var(--ink);
  padding:22px 20px 26px;max-width:840px;margin:0 auto;}}
@media (prefers-color-scheme:dark){{.viz-root{{--surface:#1a1a19;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;
  --grid:#2c2c2a;--axis:#383835;--s1:#3987e5;--s8:#d95926;--ref:#e66767;--good:#0ca30c;}}}}
:root[data-theme=dark] .viz-root{{--surface:#1a1a19;--ink:#fff;--ink2:#c3c2b7;--grid:#2c2c2a;--axis:#383835;--s1:#3987e5;--s8:#d95926;--ref:#e66767;}}
:root[data-theme=light] .viz-root{{--surface:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--grid:#e1e0d9;--axis:#c3c2b7;--s1:#2a78d6;--s8:#eb6834;--ref:#d03b3b;}}
.viz-root h1{{font-size:20px;margin:0 0 4px;}}
.viz-root .sub{{color:var(--ink2);font-size:13.5px;margin:0 0 16px;line-height:1.5;}}
.chart{{width:100%;height:auto;overflow:visible;}}
.grid{{stroke:var(--grid);stroke-width:1;}}
.zero{{stroke:var(--axis);stroke-width:1.6;}}
.gainband{{fill:var(--good);opacity:.08;}}
.ref14{{stroke:var(--muted);stroke-width:1.6;stroke-dasharray:5 4;}}
.ref14t{{fill:var(--muted);font-size:11.5px;font-weight:600;}}
.tick{{fill:var(--muted);font-size:11.5px;font-variant-numeric:tabular-nums;}}
.line{{fill:none;stroke-width:2.5;}}
.s1{{stroke:var(--s1);}} .s8{{stroke:var(--s8);}}
.mk.s1{{fill:var(--s1);stroke:var(--surface);stroke-width:2;}}
.mk.s8{{fill:var(--s8);stroke:var(--surface);stroke-width:2;}}
.lab{{font-size:12.5px;font-weight:700;}} .s1t{{fill:var(--s1);}} .s8t{{fill:var(--s8);}}
.vtag{{fill:var(--good);font-size:11px;font-weight:700;font-variant-numeric:tabular-nums;}}
.legend{{display:flex;gap:18px;flex-wrap:wrap;font-size:12.5px;color:var(--ink2);margin:8px 0 0;}}
.legend span{{display:inline-flex;align-items:center;gap:7px;}}
.sw{{width:14px;height:3px;border-radius:2px;display:inline-block;}}
.note{{background:rgba(42,120,214,0.07);border-left:3px solid var(--s1);padding:12px 14px;border-radius:6px;margin-top:18px;font-size:13px;line-height:1.55;color:var(--ink);}}
.note b{{color:var(--s1);}}
</style>
<h1>Your cost under Francie's $35k-total offer</h1>
<p class="sub">She gets a flat $35,000 no matter what. Your cash = $35,000 minus whatever the house nets — so the
better the house sells, the less you pay. Below the green line you actually come out ahead.</p>
<svg viewBox="0 0 {AW} {AH}" class="chart" role="img" aria-label="Your cost under the 35k total offer by sale price">
  {band}{grid}{ref}
  <polyline class="line s8" points="{poly(agent35)}"/>
  <polyline class="line s1" points="{poly(fsbo35)}"/>
  {dots}{end}{vlab}{xlab}
  <text class="tick" x="{(ax0+ax1)/2:.0f}" y="{ay1+42}" text-anchor="middle">list / sale price</text>
  <text class="ref14t" x="{ax0+6}" y="{ay(-6500):.0f}" style="fill:var(--good)">below $0 = you keep money (proceeds exceed $35k)</text>
</svg>
<div class="legend">
<span><i class="sw" style="background:var(--s1)"></i>$35k deal — FSBO (your likely route)</span>
<span><i class="sw" style="background:var(--s8)"></i>$35k deal — with an agent</span>
<span><i class="sw" style="background:var(--muted)"></i>your old $14k plan</span></div>
<div class="note"><b>What it shows:</b> on your likely <b>FSBO</b> route the blue line sits at or below your old
$14k plan across the board, and dips <b>below zero</b> at the higher prices — you'd pay nothing and keep the
excess. It only costs you more than $14k in the poor-sale corner (an <b>agent</b> sale under ~$405k). Guaranteeing
her $35k means you carry that downside — which is why you'd want to control the sale and lean FSBO.</div>
</div>'''
open("/home/user/Claude-Works/cost_35k_chart.html","w").write(html)
print("wrote",len(html))
