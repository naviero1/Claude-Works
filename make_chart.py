# Generate a self-contained, theme-aware HTML chart (static SVG).
prices=[390,395,399,405,410]           # $k (409.9 rounded label handled separately)
plabels=["$390k","$395k","$399k","$405k","$409.9k"]
# probability sold by end of Oct
p_agent=[80,77,74,70,66]
p_fsbo =[72,68,65,61,57]
# house return as % of her $48k
h_agent=[20,30,38,50,59]
h_fsbo =[44,55,63,75,85]
GIFT=29                                 # $14k / $48k
t_agent=[h+GIFT for h in h_agent]
t_fsbo =[h+GIFT for h in h_fsbo]

def x_even(i,n,x0,x1):
    return x0+(x1-x0)*i/(n-1)

# ---------- Panel A: probability lines ----------
AW,AH=760,340; ax0,ax1,ay0,ay1=70,660,50,290
def ay(v): return ay1-(v/100)*(ay1-ay0)
def ax(i): return x_even(i,5,ax0,ax1)
def poly(vals): return " ".join(f"{ax(i):.1f},{ay(v):.1f}" for i,v in enumerate(vals))
gridA=""
for g in [0,20,40,60,80,100]:
    y=ay(g); gridA+=f'<line class="grid" x1="{ax0}" y1="{y:.1f}" x2="{ax1}" y2="{y:.1f}"/>'
    gridA+=f'<text class="tick" x="{ax0-10}" y="{y+4:.1f}" text-anchor="end">{g}%</text>'
xlabA=""
for i,l in enumerate(plabels):
    xlabA+=f'<text class="tick" x="{ax(i):.1f}" y="{ay1+22}" text-anchor="middle">{l}</text>'
dotsA=""
for i,(a,f) in enumerate(zip(p_agent,p_fsbo)):
    dotsA+=f'<circle class="s1 mk" cx="{ax(i):.1f}" cy="{ay(a):.1f}" r="4.5"/>'
    dotsA+=f'<circle class="s2 mk" cx="{ax(i):.1f}" cy="{ay(f):.1f}" r="4.5"/>'
endA =f'<text class="lab s1t" x="{ax(4)+8:.1f}" y="{ay(p_agent[4]):.1f}">With agent</text>'
endA+=f'<text class="lab s2t" x="{ax(4)+8:.1f}" y="{ay(p_fsbo[4])+14:.1f}">FSBO</text>'

# ---------- Panel B: two small-multiple stacked bar charts ----------
def bars(house,total,title):
    W,H=380,320; x0,x1,y0,y1=54,352,46,286
    def yy(v): return y1-(v/120)*(y1-y0)
    n=5; slot=(x1-x0)/n; bw=34
    grid=""
    for g in [0,50,100]:
        y=yy(g); grid+=f'<line class="grid" x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}"/>'
        grid+=f'<text class="tick" x="{x0-8}" y="{y+4:.1f}" text-anchor="end">{g}%</text>'
    whole=yy(100)
    ref=f'<line class="ref" x1="{x0}" y1="{whole:.1f}" x2="{x1}" y2="{whole:.1f}"/>'
    ref+=f'<text class="reflab" x="{x0+2}" y="{whole-6:.1f}" text-anchor="start">her full $48k</text>'
    rects=""; labs=""; xl=""
    for i in range(n):
        cx=x0+slot*i+slot/2
        bx=cx-bw/2
        hb=yy(house[i]); tb=yy(total[i]); base=y1
        # house segment
        rects+=f'<rect class="s1 fill" x="{bx:.1f}" y="{hb:.1f}" width="{bw}" height="{base-hb:.1f}" rx="3"/>'
        # gift segment (2px surface gap below it)
        gy=tb; gh=(hb-2)-tb
        rects+=f'<rect class="s8 fill" x="{bx:.1f}" y="{gy:.1f}" width="{bw}" height="{max(gh,1):.1f}" rx="3"/>'
        labs+=f'<text class="tot" x="{cx:.1f}" y="{tb-7:.1f}" text-anchor="middle">{total[i]}%</text>'
        xl+=f'<text class="tick" x="{cx:.1f}" y="{y1+20}" text-anchor="middle">{plabels[i]}</text>'
    return f'''<svg viewBox="0 0 {W} {H}" class="chart" role="img" aria-label="{title}">
      <text class="ptitle" x="{x0-8}" y="26">{title}</text>
      {grid}{ref}{rects}{labs}{xl}
    </svg>'''

barsA=bars(h_agent,t_agent,"If sold with an agent")
barsF=bars(h_fsbo,t_fsbo,"If sold FSBO (your cheaper route)")

html=f'''<div class="viz-root">
<style>
.viz-root{{--surface:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--grid:#e1e0d9;--axis:#c3c2b7;
  --s1:#2a78d6;--s2:#1baf7a;--s8:#eb6834;--ref:#d03b3b;
  font-family:system-ui,-apple-system,"Segoe UI",sans-serif;background:var(--surface);color:var(--ink);
  padding:22px 20px 26px;max-width:820px;margin:0 auto;}}
@media (prefers-color-scheme:dark){{.viz-root{{--surface:#1a1a19;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;
  --grid:#2c2c2a;--axis:#383835;--s1:#3987e5;--s2:#199e70;--s8:#d95926;--ref:#e66767;}}}}
:root[data-theme=dark] .viz-root{{--surface:#1a1a19;--ink:#fff;--ink2:#c3c2b7;--grid:#2c2c2a;--axis:#383835;
  --s1:#3987e5;--s2:#199e70;--s8:#d95926;--ref:#e66767;}}
:root[data-theme=light] .viz-root{{--surface:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--grid:#e1e0d9;--axis:#c3c2b7;
  --s1:#2a78d6;--s2:#1baf7a;--s8:#eb6834;--ref:#d03b3b;}}
.viz-root h1{{font-size:20px;margin:0 0 4px;}}
.viz-root .sub{{color:var(--ink2);font-size:13.5px;margin:0 0 18px;line-height:1.5;}}
.viz-root h2{{font-size:14px;margin:22px 0 2px;}}
.chart{{width:100%;height:auto;overflow:visible;}}
.grid{{stroke:var(--grid);stroke-width:1;}}
.ref{{stroke:var(--ref);stroke-width:1.5;stroke-dasharray:5 4;}}
.reflab{{fill:var(--ref);font-size:11px;font-weight:600;}}
.tick{{fill:var(--muted);font-size:11.5px;font-variant-numeric:tabular-nums;}}
.ptitle{{fill:var(--ink);font-size:13px;font-weight:600;}}
.tot{{fill:var(--ink);font-size:12px;font-weight:700;font-variant-numeric:tabular-nums;}}
.line{{fill:none;stroke-width:2.5;}}
.s1{{stroke:var(--s1);}} .s2{{stroke:var(--s2);}}
.fill.s1{{fill:var(--s1);stroke:none;}} .fill.s8{{fill:var(--s8);stroke:none;}}
.mk.s1{{fill:var(--s1);stroke:var(--surface);stroke-width:2;}}
.mk.s2{{fill:var(--s2);stroke:var(--surface);stroke-width:2;}}
.lab{{font-size:12px;font-weight:600;}} .s1t{{fill:var(--s1);}} .s2t{{fill:var(--s2);}}
.legend{{display:flex;gap:18px;flex-wrap:wrap;font-size:12.5px;color:var(--ink2);margin:6px 0 0;}}
.legend span{{display:inline-flex;align-items:center;gap:7px;}}
.sw{{width:14px;height:14px;border-radius:3px;display:inline-block;}}
.grid2{{display:flex;gap:14px;flex-wrap:wrap;justify-content:space-between;}}
.grid2>div{{flex:1 1 330px;}}
.note{{background:rgba(235,104,52,0.08);border-left:3px solid var(--s8);padding:12px 14px;border-radius:6px;
  margin-top:20px;font-size:13px;line-height:1.55;color:var(--ink);}}
.note b{{color:var(--s8);}}
</style>

<h1>The house sale is uncertain — the $14k is not</h1>
<p class="sub">The market decides the sale price and whether it even sells this fall. Your $14,000 is a fixed
29% of her $48k that lands in her hands no matter which way that goes.</p>

<h2>1 · How likely is the house to be under contract by end of October?</h2>
<svg viewBox="0 0 {AW} {AH}" class="chart" role="img" aria-label="Probability of sale by end of October">
  {gridA}
  <polyline class="line s1" points="{poly(p_agent)}"/>
  <polyline class="line s2" points="{poly(p_fsbo)}"/>
  {dotsA}{endA}{xlabA}
  <text class="tick" x="{(ax0+ax1)/2:.0f}" y="{ay1+40}" text-anchor="middle">list / sale price</text>
</svg>
<div class="legend"><span><i class="sw" style="background:var(--s1)"></i>With agent</span>
<span><i class="sw" style="background:var(--s2)"></i>FSBO</span></div>
<p class="sub" style="margin-top:8px">Even at the most sellable end, it's a <b>57–80% chance</b> — not a certainty — and the
higher the price, the lower the odds.</p>

<h2>2 · Where the $14k puts her recovery of the $48k</h2>
<div class="grid2"><div>{barsA}</div><div>{barsF}</div></div>
<div class="legend"><span><i class="sw" style="background:var(--s1)"></i>What the house returns her</span>
<span><i class="sw" style="background:var(--s8)"></i>+ your $14k (a flat 29%)</span>
<span><i class="sw" style="border:1.5px dashed var(--ref);background:transparent"></i>her full $48k</span></div>

<div class="note">
<b>Why it's an overly generous gesture, on every measure:</b><br>
• <b>Against the law</b> — a court would likely make you pay her almost nothing extra; she takes what the house
returns and absorbs the rest as a loss on her own money. The whole orange band is a gift, not a debt.<br>
• <b>Against reality</b> — $14k is <b>guaranteed cash today</b>, while the blue bar is a maybe: it depends on a
price no one controls and a sale that's only 57–80% likely this fall. You're handing her certainty and keeping
the risk.<br>
• <b>Against the outcome</b> — that flat 29% lifts her to roughly three-quarters, and often past 100%, of every
dollar she put in — in most cases making her whole or better while the market loss stays yours.
</div>
</div>'''

open("/home/user/Claude-Works/why_14k_chart.html","w").write(html)
print("wrote", len(html), "bytes")
