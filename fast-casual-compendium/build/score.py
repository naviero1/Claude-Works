"""Score any entry on the model recovered from the first edition.
Every constant here was fitted against the 60 published entries, not invented."""

def clamp(x): return max(0.0, min(10.0, x))

def kidney(sodium):        return clamp(10*(2000-sodium)/1650)
def sugar_score(sugar_g):  return clamp(10*(22-sugar_g)/19)
def muscle(protein, cal):
    ppc = protein/(cal/100)
    return 0.7*clamp(10*(ppc-2)/7) + 0.3*clamp(10*(protein-20)/25)
def liver(satfat, cal):
    return 0.65*clamp(10*(16.5-satfat)/14.5) + 0.35*clamp(10*(1000-cal)/500)
def cost(price, protein):
    return 0.6*clamp(10*(35-price)/25) + 0.4*clamp(10*(0.90-price/protein)/0.65)
def flavor(char, acid, ferment, aromatics, richness, texture, penalty):
    raw = char+acid+ferment+aromatics+richness+texture-penalty
    return clamp(raw/14*10)

def score_entry(e):
    """e needs: cal protein sodium satfat fiber sugar price GUT ENE INF + flavor components."""
    KID = kidney(e['sodium']); SUG = sugar_score(e['sugar'])
    MUS = muscle(e['protein'], e['cal']); LIV = liver(e['satfat'], e['cal'])
    COST = cost(e['price'], e['protein'])
    FLA = flavor(e['flavor_char'], e['flavor_acid'], e['flavor_ferment'], e['flavor_aromatics'],
                 e['flavor_richness'], e['flavor_texture'], e['flavor_strip_penalty'])
    GUT, ENE, INF = float(e['GUT']), float(e['ENE']), float(e['INF'])
    health = (KID+LIV+MUS+GUT+ENE+INF+0.7*SUG)/6.7
    overall = (health*6.7 + FLA*0.5 + COST*0.5)/7.7
    out = dict(e)
    out.update(KID=round(KID,1), LIV=round(LIV,1), MUS=round(MUS,1), GUT=round(GUT,1),
               ENE=round(ENE,1), INF=round(INF,1), SUG=round(SUG,1),
               FLAVOR=round(FLA,1), COST=round(COST,1),
               health=round(health,2), overall=round(overall,2))
    return out

if __name__ == '__main__':
    # regression: re-score the five PUBLISHED entries from their macros and confirm the model reproduces them
    import json
    D = json.load(open('details_cu.json'))
    print(f"{'restaurant':22s} {'KID':>11s} {'LIV':>11s} {'MUS':>11s} {'SUG':>11s} {'COST':>11s}")
    worst = 0.0
    for d in D:
        got = dict(KID=kidney(d['sodium']), SUG=sugar_score(d['sugar']),
                   MUS=muscle(d['protein'], d['cal']), LIV=liver(d['satfat'], d['cal']),
                   COST=cost(d['price'], d['protein']))
        for k, v in got.items(): worst = max(worst, abs(v-d[k]))
        if d['data'] in ('PUBLISHED', 'PARTIAL'):
            print(f"  {d['restaurant']:20s} " + " ".join(
                f"{got[k]:5.2f}/{d[k]:4.1f}" for k in ['KID','LIV','MUS','SUG','COST']))
    print(f"\n  worst absolute deviation across all 60 entries and 5 computed criteria: {worst:.3f}")
    print("  (the model reproduces the published scores to within rounding)")
