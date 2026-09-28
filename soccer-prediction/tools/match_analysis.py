import math
def pois(k,l): return math.exp(-l)*l**k/math.factorial(k)
RHO=-0.06
def tau(i,j,lh,la):
    if i==0 and j==0: return 1-lh*la*RHO
    if i==1 and j==0: return 1+la*RHO
    if i==0 and j==1: return 1+lh*RHO
    if i==1 and j==1: return 1-RHO
    return 1.0
def analyze(h,a,lh,la,N=9):
    g={}; s=0
    for i in range(N):
        for j in range(N):
            p=pois(i,lh)*pois(j,la)*tau(i,j,lh,la); g[(i,j)]=p; s+=p
    for k in g: g[k]/=s
    top=sorted(g.items(),key=lambda x:-x[1])[:3]
    hw=sum(p for (i,j),p in g.items() if i>j); dr=sum(p for (i,j),p in g.items() if i==j); aw=1-hw-dr
    ov25=sum(p for (i,j),p in g.items() if i+j>=3); ov35=sum(p for (i,j),p in g.items() if i+j>=4)
    bt=sum(p for (i,j),p in g.items() if i>=1 and j>=1)
    # half splits: ~45% of goals 1H, 55% 2H
    l1=0.45*(lh+la); l2=0.55*(lh+la)
    early=1-math.exp(-(lh+la)*15/90)   # P(>=1 goal in first 15 min, either team)
    print(f"{h} vs {a}  (lh={lh} la={la})")
    print("  top scores:", ", ".join(f"{i}-{j} {p*100:.0f}%" for (i,j),p in top))
    print(f"  W/D/W {hw*100:.0f}/{dr*100:.0f}/{aw*100:.0f}  O2.5 {ov25*100:.0f}  O3.5 {ov35*100:.0f}  BTTS {bt*100:.0f}")
    print(f"  goals 1H~{l1:.2f} 2H~{l2:.2f}  P(goal in first15')~{early*100:.0f}%")
# demo: Argentina vs Cabo Verde
analyze("Argentina","Cabo Verde",2.2,0.7)
