[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/verad-xe/world-news-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/verad-xe/world-news-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# The Global Front Page — 21 November 2026

One image that sums up the world's news of Saturday 21 November 2026,
entered in make.fun's [`news-image-20261121` bounty](https://make.fun/bounty/news-image-20261121).

## What the image shows

A newspaper front page, drawn programmatically (original artwork only —
no photographs, no real outlets' logos):

1. **Trump, Xi & Putin hold first trilateral summit** — the "G-3" meets in
   Shenzhen on the APEC sidelines and pledges nuclear-arms cuts.
2. **Russian missile lands in Poland** — Warsaw calls it "a deliberate
   provocation"; Russia pounds Ukraine anew; Ukraine hits the Crimean
   Bridge again.
3. **Myanmar committed genocide — ICJ** — the World Court's first genocide
   verdict against a state; reparations ordered for the Rohingya; Myanmar
   calls the ruling "unfair".
4. **Russian assassination plot foiled in Denmark** — a plan to kill a
   US–Ukrainian rapper stopped; two Danes charged; a Russian diplomat
   expelled.
5. **Anthropic IPO raises $81bn — largest ever** — a $1.5tn valuation while
   the tech sell-off deepens; a researcher claims Claude solved the Riemann
   Hypothesis (labelled unverified, as reported).
6. **COP31 talks deadlocked** — the climate summit runs into overtime with
   no deal in sight.

Ticker: UK & EU agree a post-Brexit reset deal; Nikhil Gupta jailed
19½ years in New York in the Sikh-separatist plot case; a tanker hit again
in the Strait of Hormuz with a seafarer missing; cost-of-living protests
spread across Europe.

Stories as reported on 21 November 2026 by Reuters, AP, AFP, The Hindu's
morning digest, Jiji and Kyodo.

## Layout of this repository

- `main.ts` — the entry program (Node 22, standard library only). It copies
  `entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`).
- `entry.png` — the image itself: 1024×1024 PNG, well under the 1 MiB cap.
- `make_image.py` — the PIL script that draws `entry.png`; rerunning it
  reproduces the image byte for byte.
- `LICENSE` — MIT.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
