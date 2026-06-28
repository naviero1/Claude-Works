import math
def pois(k,l): return math.exp(-l)*l**k/math.factorial(k)
RHO=-0.06
def tau(i,j,lh,la):
    if i==0 and j==0: return 1-lh*la*RHO
    if i==1 and j==0: return 1+la*RHO
    if i==0 and j==1: return 1+lh*RHO
    if i==1 and j==1: return 1-RHO
    return 1.0
def grid(lh,la,N=8):
    g={}
    s=0
    for i in range(N):
        for j in range(N):
            p=pois(i,lh)*pois(j,la)*tau(i,j,lh,la)
            g[(i,j)]=p; s+=p
    for k in g: g[k]/=s
    return g
# home team first; lambdas (home, away)
games=[
 ("South Africa","Canada",1.05,1.35),
 ("Brazil","Japan",1.55,1.00),
 ("Germany","Paraguay",1.60,0.80),
 ("Netherlands","Morocco",1.30,1.20),
 ("Cote d'Ivoire","Norway",1.10,1.40),
 ("France","Sweden",2.00,0.90),
 ("Mexico","Ecuador",1.20,1.00),
 ("England","DR Congo",2.00,0.80),
 ("Belgium","Senegal",1.40,1.20),
 ("USA","Bosnia",1.40,1.10),
 ("Spain","Austria",2.00,0.80),
 ("Portugal","Croatia",1.50,1.10),
 ("Switzerland","Algeria",1.40,1.10),
 ("Colombia","Ghana",1.60,0.90),
 ("Australia","Egypt",1.10,1.20),
 ("Argentina","Cabo Verde",2.20,0.70),
]
for h,a,lh,la in games:
    g=grid(lh,la)
    top=sorted(g.items(),key=lambda x:-x[1])[:5]
    hw=sum(p for (i,j),p in g.items() if i>j)
    dr=sum(p for (i,j),p in g.items() if i==j)
    aw=sum(p for (i,j),p in g.items() if i<j)
    ov=sum(p for (i,j),p in g.items() if i+j>=3)
    bt=sum(p for (i,j),p in g.items() if i>=1 and j>=1)
    print(f"## {h} vs {a}   (lh={lh}, la={la})")
    for (i,j),p in top:
        lab=f"{h} {i}-{j}" if i>j else (f"{a} {j}-{i}" if j>i else f"draw {i}-{j}")
        print(f"  {i}-{j}  {p*100:4.1f}%   [{lab}]")
    print(f"  W/D/W: {h} {hw*100:.0f}% / draw {dr*100:.0f}% / {a} {aw*100:.0f}%   |  O2.5 {ov*100:.0f}%  BTTS {bt*100:.0f}%")
    print()
