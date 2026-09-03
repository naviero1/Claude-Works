# What Delivery Costs You — the brochure

A short, public-facing piece drawn from the same dataset as the full compendium.
It carries the controversial findings and a shortlist; it carries none of the
edition history, verification log or methodology chapters.

    dishes.py          original flat SVG drawings of dish types
    brochure.css       the market-stall identity: butcher paper, price-tag red
    build_brochure.py  reads ../build/*.json and emits brochure.html

Rebuild with `python3 build_brochure.py`. Every figure comes from the compendium's
own `figures.json` and `details_corrected.json`, so the two cannot drift apart.

## On the illustrations

They are drawings of dish *types*, not photographs. Photographs were not possible:
the artifact sandbox admits no external images, and captioning stock photography as
a named restaurant's dish would misrepresent a real business. The footer says so.
