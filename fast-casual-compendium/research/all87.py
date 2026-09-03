"""The one canonical table: all 87 dishes, one schema, ranked together.

The compendium keeps the original sixty and the twenty-seven additions in
separate sections, because the analysis is scoped to the sixty - the additions
were chosen to fill named gaps, so they are a purposive sample and pooling them
into a correlation would measure the selection rather than the food.

Presentation is a different problem. A reader wants one ranked list, and every
guide in the precedent set publishes the whole corpus in one sequence. The
scores are directly comparable because all 87 went through the identical model
(build/score.py), so ranking them together is sound even where averaging them
would not be. `cohort` preserves the distinction for anyone who needs it.
"""
import json, os, sys

B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'build')
CRIT = ['KID', 'LIV', 'MUS', 'GUT', 'ENE', 'INF', 'SUG']
SOUND = ['KID', 'LIV', 'MUS', 'SUG']          # arithmetic on macros; the audit did not dispute these
FIELDS = ('restaurant dish build cuisine prep price cal protein sodium satfat '
          'fiber sugar health overall FLAVOR COST data miles store').split()


def tier(d):
    """The compound rule from tiers.py: a top billing needs a good overall score
    AND no collapse on any criterion that is plain arithmetic on the macros."""
    worst = min(d[c] for c in SOUND)
    if d['overall'] >= 6.5 and worst >= 4.0: return 'Order these'
    if d['overall'] >= 6.0:                  return 'Worth ordering'
    if d['overall'] >= 5.0:                  return 'With reservations'
    return 'Not recommended'


def load():
    orig = json.load(open(os.path.join(B, 'details_corrected.json')))
    added = json.load(open(os.path.join(B, 'additions.json')))
    out = []
    for src, cohort in ((orig, 'first edition'), (added, 'added this edition')):
        for d in src:
            e = {k: d.get(k) for k in FIELDS}
            e.update({c: d[c] for c in CRIT})
            e['cohort'] = cohort
            e['band'] = ('under $12' if e['price'] < 12 else
                         '$12 to $16' if e['price'] < 16 else
                         '$16 to $20' if e['price'] < 20 else '$20 and up')
            e['hpd'] = e['health'] / e['price']            # health per dollar
            e['dpp'] = e['price'] / e['protein']           # dollars per gram of protein
            e['ppc'] = e['protein'] / (e['cal'] / 100)     # protein density
            e['sodium_day'] = e['sodium'] / 2300           # share of a day's limit
            e['weakest'] = min(CRIT, key=lambda c: e[c])
            e['tier'] = tier(e)
            out.append(e)
    out.sort(key=lambda e: (-e['overall'], -e['health'], e['price']))
    for i, e in enumerate(out, 1):
        e['rank'] = i
    return out


def frontier(rows):
    """Dishes no other dish beats on both price and health - the Pareto set."""
    return [a for a in rows
            if not any(b['price'] <= a['price'] and b['health'] >= a['health']
                       and (b['price'], -b['health']) != (a['price'], -a['health'])
                       for b in rows)]


if __name__ == '__main__':
    rows = load()
    json.dump(rows, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      'all87.json'), 'w'), indent=1)
    print(f'{len(rows)} dishes, ranked together\n')
    for t in ['Order these', 'Worth ordering', 'With reservations', 'Not recommended']:
        n = [e for e in rows if e['tier'] == t]
        print(f'  {t:<20} {len(n):>3}   ranks {n[0]["rank"]}-{n[-1]["rank"]}')
    print('\nby price band       n   mean health   mean overall   mean price')
    for b in ['under $12', '$12 to $16', '$16 to $20', '$20 and up']:
        g = [e for e in rows if e['band'] == b]
        print(f'  {b:<16} {len(g):>3}      {sum(e["health"] for e in g)/len(g):>5.2f}'
              f'         {sum(e["overall"] for e in g)/len(g):>5.2f}'
              f'        ${sum(e["price"] for e in g)/len(g):>5.2f}')
    f = sorted(frontier(rows), key=lambda e: e['price'])
    print(f'\nprice-health frontier ({len(f)} of {len(rows)}):')
    for e in f:
        print(f'  ${e["price"]:>5.2f}  health {e["health"]:>4.1f}  #{e["rank"]:<3} '
              f'{e["dish"][:38]:<38} {e["restaurant"][:22]}')
    print('\ntop 10 by health per dollar:')
    for e in sorted(rows, key=lambda e: -e['hpd'])[:10]:
        print(f'  {e["hpd"]:.3f}  ${e["price"]:>5.2f}  #{e["rank"]:<3} '
              f'{e["dish"][:38]:<38} {e["restaurant"][:22]}')
