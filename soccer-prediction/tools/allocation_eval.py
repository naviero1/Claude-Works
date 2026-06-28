import math
def pois(k,l): return math.exp(-l)*l**k/math.factorial(k)
RHO=-0.06
def tau(i,j,lh,la):
    if (i,j)==(0,0): return 1-lh*la*RHO
    if (i,j)==(1,0): return 1+la*RHO
    if (i,j)==(0,1): return 1+lh*RHO
    if (i,j)==(1,1): return 1-RHO
    return 1.0
def scenarios(lh,la,N=7):
    g={}; s=0
    for i in range(N):
        for j in range(N):
            p=pois(i,lh)*pois(j,la)*tau(i,j,lh,la); g[(i,j)]=p; s+=p
    for k in g: g[k]/=s
    hw=sum(p for (i,j),p in g.items() if i>j); aw=sum(p for (i,j),p in g.items() if i<j)
    q=0.5+0.5*((hw-aw)/(hw+aw))
    sc=[]
    for (i,j),p in g.items():
        if i>j: sc.append((i,j,'H',p))
        elif j>i: sc.append((i,j,'A',p))
        else:
            sc.append((i,j,'H',p*q)); sc.append((i,j,'A',p*(1-q)))
    return sc
# bet predicates
def exact(i0,j0): return lambda s: s[0]==i0 and s[1]==j0
def adv(t): return lambda s: s[2]==t
def under(line): return lambda s: s[0]+s[1] < line
def res(r): return lambda s: ('H' if s[0]>s[1] else 'A' if s[1]>s[0] else 'D')==r
def dc(rs): return lambda s: ('H' if s[0]>s[1] else 'A' if s[1]>s[0] else 'D') in rs
def evaluate(name, lh, la, bets):
    # bets: list of (label, stake, decimal_odds, predicate)
    sc=scenarios(lh,la)
    ev=0; pprof=0; best=-1e9; worst=1e9
    for (i,j,adv_,p) in sc:
        ret=sum(stake*od for (lab,stake,od,pred) in bets if pred((i,j,adv_)))
        pnl=ret-100
        ev+=p*pnl
        if pnl>1e-6: pprof+=p
        best=max(best,pnl); worst=min(worst,pnl)
    tot=sum(stake for (_,stake,_,_) in bets)
    print(f"  {name}: stake ${tot:.0f}  EV ${ev:+.1f}  P(profit) {pprof*100:.0f}%  best ${best:+.0f} worst ${worst:+.0f}")

print("=== NETHERLANDS vs MOROCCO (lh1.3 la1.2)  [H=NED A=Morocco] ===")
LH,LA=1.3,1.2
# odds from market: MAR adv .38->2.63, NED adv .62->1.61; exacts 1/price; Under2.5 est .56->1.79
evaluate("A) Max-EV (Morocco value)",LH,LA,[
  ("MAR advance",65,2.63,adv('A')),("1-1",20,6.67,exact(1,1)),("MAR 1-0",15,12.5,exact(0,1))])
evaluate("B) Max P(profit) (NED-anchored)",LH,LA,[
  ("NED advance",80,1.61,adv('H')),("1-1",20,6.67,exact(1,1))])
evaluate("C) Balanced spread",LH,LA,[
  ("MAR advance",30,2.63,adv('A')),("1-1",18,6.67,exact(1,1)),("NED 1-0",12,8.33,exact(1,0)),
  ("0-0",12,10.0,exact(0,0)),("NED 2-1",14,10.0,exact(2,1)),("MAR 2-1",14,14.3,exact(1,2))])
evaluate("D) Low-scoring thesis",LH,LA,[
  ("Under 2.5 (est)",35,1.79,under(2.5)),("1-1",20,6.67,exact(1,1)),("0-0",20,10.0,exact(0,0)),
  ("MAR advance",25,2.63,adv('A'))])

print("=== GERMANY vs PARAGUAY (lh1.6 la0.8)  [H=GER A=Paraguay] ===")
LH,LA=1.6,0.8
# PAR adv .15->6.67, GER adv .86->1.16; Under2.5 est .60->1.67
evaluate("A) Max-EV (Paraguay dart)",LH,LA,[
  ("PAR advance",30,6.67,adv('A')),("Under 2.5 (est)",40,1.67,under(2.5)),("1-1",15,11.1,exact(1,1)),("0-0",15,16.7,exact(0,0))])
evaluate("B) Max P(profit) (GER-anchored)",LH,LA,[
  ("GER advance",90,1.16,adv('H')),("PAR advance",10,6.67,adv('A'))])
evaluate("C) Balanced spread",LH,LA,[
  ("GER 1-0",16,8.33,exact(1,0)),("GER 2-0",16,7.14,exact(2,0)),("GER 2-1",12,10.0,exact(2,1)),
  ("1-1",12,11.1,exact(1,1)),("GER 3-0",10,9.1,exact(3,0)),("PAR advance",34,6.67,adv('A'))])
evaluate("D) Low-scoring / value thesis",LH,LA,[
  ("Under 2.5 (est)",45,1.67,under(2.5)),("PAR advance",20,6.67,adv('A')),("1-1",20,11.1,exact(1,1)),("GER 1-0",15,8.33,exact(1,0))])
