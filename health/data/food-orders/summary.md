# DoorDash Eating Pattern — Analysis (Oct 2025 – Jul 2026)

Source: 103 order confirmations extracted from Gmail (`doordash-orders.json`).
DoorDash emails carry no item-level detail, so this analyzes restaurants, timing,
and spend. Item detail can be added later from a DoorDash account export.

## The core habit: weekday work lunch delivery

- **~2.6 orders/week**, almost entirely **weekday lunches**: 97 of 103 orders are
  Mon–Fri, and 91 of 103 arrive between 10 AM and 1 PM local.
- **89 of 103 orders deliver to 1650 TW Alexander Dr, Durham NC** (workplace);
  only 11 deliver home to Fuquay-Varina — those skew evening/fast-food
  (McDonald's 8:26 PM, Arby's, pizza).
- Average order **$26.29**; ~$270–420/month; **$2,708 total** over 9 months.

## Restaurant mix (count)

| Restaurant | Orders | Rough profile |
|---|---|---|
| Farmside Kitchen | 28 | farm bowls — generally solid choice |
| Chipotle | 21 | can be healthy; depends on build |
| Bul Box | 18 | Korean bowls — protein + rice |
| Chick-fil-A | 7 | fried chicken, fries |
| Mexican jv American | 4 | tex-mex |
| Arby's | 3 | fast food |
| CAVA / Mahana Fresh / Will & Well Salads | 5 | salad/bowl — newest additions |
| Others (McDonald's, Chuy's, Pei Wei, Firehouse, Khao Sen, tacos, etc.) | ~15 | mixed |
| Groceries via DoorDash | 3 | Food Lion (6/21), ALDI (6/6), Food Lion |

**~65% of orders are bowl-format restaurants** (Farmside, Bul Box, Chipotle, CAVA,
Mahana, Guasaca, Will & Well) — a real, sustained shift from the 2021–2024 history,
which was almost entirely McDonald's / pizza / Arby's.

## Timing signals

- Busiest days: Tue (24), Wed (22), Fri (20), Thu (17), Mon (14). Weekends: only 6
  orders — weekend eating is invisible to this dataset (home cooking? eating out?).
- June 2026 was the heaviest month (15 orders, $424) — trending up.

## What's unknown (gaps to fill)

1. Actual menu items and macros — needs DoorDash export or Oscar's descriptions.
2. Breakfast and dinner on weekdays; all weekend meals.
3. Beverages, snacks, alcohol.
