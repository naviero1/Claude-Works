import math
def pois(k,l): return math.exp(-l)*l**k/math.factorial(k)
RHO=-0.06
def tau(i,j,lh,la):
    if i==0 and j==0: return 1-lh*la*RHO
    if i==1 and j==0: return 1+la*RHO
    if i==0 and j==1: return 1+lh*RHO
    if i==1 and j==1: return 1-RHO
    return 1.0
def calc(h,a,lh,la,mkt=None,N=9):
    g={}; s=0
    for i in range(N):
        for j in range(N):
            p=pois(i,lh)*pois(j,la)*tau(i,j,lh,la); g[(i,j)]=p; s+=p
    for k in g: g[k]/=s
    hw=sum(p for (i,j),p in g.items() if i>j); dr=sum(p for (i,j),p in g.items() if i==j); aw=1-hw-dr
    # shootout edge: conditional on a draw, better side advances more often
    q=0.5+0.5*((hw-aw)/(hw+aw)) if (hw+aw)>0 else 0.5
    adv_h=hw+dr*q; adv_a=1-adv_h
    tag=""
    if mkt is not None:
        tag=f"  | MKT adv {h[:3]} {mkt}  (mine {adv_h*100:.0f}) -> {'FADE fav/dog value' if mkt-adv_h*100>=8 else 'aligned'}"
    print(f"{h} vs {a}: adv {h[:3]} {adv_h*100:.0f}% / {a[:3]} {adv_a*100:.0f}%   W/D/W {hw*100:.0f}/{dr*100:.0f}/{aw*100:.0f}{tag}")
# (home, away, lh, la, market_adv_home_if_known)
games=[
 ("South Africa","Canada",1.05,1.35,None),
 ("Brazil","Japan",1.65,1.00,74),   # nudged BRA 1.55->1.65 (Japan also missing Mitoma/Minamino)
 ("Germany","Paraguay",1.60,0.80,86), # HOLD - 86 looks inflated (volatile Germany)
 ("Netherlands","Morocco",1.30,1.20,62), # HOLD - NED missing both CBs; Morocco value
 ("Cote d'Ivoire","Norway",1.10,1.50,None), # nudged NOR 1.40->1.50 (Haaland)
 ("France","Sweden",2.00,0.90,None),
 ("Mexico","Ecuador",1.20,1.00,None),
 ("England","DR Congo",2.00,0.80,None),
 ("Belgium","Senegal",1.40,1.20,None),
 ("USA","Bosnia",1.40,1.10,None),
 ("Spain","Austria",2.00,0.80,None),
 ("Portugal","Croatia",1.50,1.10,None),
 ("Switzerland","Algeria",1.40,1.10,None),
 ("Colombia","Ghana",1.60,0.90,None),
 ("Australia","Egypt",1.10,1.20,None),
 ("Argentina","Cabo Verde",2.20,0.70,None),
]
for h,a,lh,la,m in games: calc(h,a,lh,la,m)
print()
print("Norway is AWAY vs CIV: NOR adv shown as away side.")
