# Health & Nutrition Tracker — Oscar Penny

Purpose: a single organized home for Oscar's health data — nutrition habits (what he
eats, primarily via DoorDash), Oura Ring biometrics, and other health signals — so
Claude can track trends over time and recommend healthier options (e.g., when choosing
between DoorDash restaurants/menu items).

## Structure

```
health/
├── README.md                     ← this file
├── profile.md                    ← baseline health profile & context
├── data/
│   ├── food-orders/
│   │   ├── doordash-orders.json  ← item-level order history (extracted from Gmail)
│   │   └── summary.md            ← eating-pattern analysis of the order history
│   └── oura/                     ← Oura Ring exports/data shared by Oscar (drop here)
└── logs/                         ← ongoing nutrition/health log entries
```

## Data sources

| Source | Status | Coverage |
|---|---|---|
| DoorDash order emails (Gmail) | Collected | Oct 2025 – Jul 2026 item-level; sparse history back to 2021 |
| Oura Ring 5 | Awaiting data — ring delivered 2026-06-29 | ~Jun 30, 2026 onward |
| Google Calendar | Checked — no fitness/medical events | n/a |
| Google Drive | `nutrition` folder found (reference books only, no personal data) | n/a |
| Labs / medical records | None found in Gmail | — |

## Workflow

1. Oscar shares Oura data (screenshots, CSV exports, or summaries) → store in `data/oura/`.
2. Oscar shares DoorDash options he's considering → Claude cross-references order
   history + Oura trends and recommends the healthier choice.
3. New orders/meals get appended to `logs/` and periodically rolled into the data files.
