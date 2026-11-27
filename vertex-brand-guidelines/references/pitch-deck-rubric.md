# Slide decks & data visualization

Decks are built in **Google Slides** (16:9, 960×540pt). Everything below works with Slides' native tools.
All three fonts are available via *Fonts → More fonts*.

## 1. The slide master (every deck)

| Element | Spec |
|---|---|
| Background | `#FAFAF8` paper (light, the default). Cover and section dividers may use `#14120E` ink |
| Header | Lockup (on-light) top-left at (54, 24)pt, 166pt wide. 1pt `rgba(20,18,14,.10)` hairline full content width at y = 63pt |
| Title | EB Garamond 400, 36pt, `#14120E`, top-left at y ≈ 84pt, ≤2 lines |
| Body area | 54pt left/right margins, from y ≈ 150pt down to 486pt |
| Footer | Source line bottom-left: EB Garamond italic 11pt, `#6E685F`. Slide number bottom-right: EB Garamond 11pt |
| Corners / shadows | Square. None |

**Type scale (pt).** Don't let autofit invent sizes. Turn autofit off and use only these:

| Role | Size | Style |
|---|---|---|
| Cover title | 60 | EB Garamond 400 |
| Section title | 48 | EB Garamond 400 |
| Slide title | 36 | EB Garamond 400 |
| Lead-in | 20 | EB Garamond 600, `#14120E` |
| Body | 17 (min 16) | EB Garamond 400, `#46403A`, line spacing 1.15–1.3 |
| Small / caption | 13 | EB Garamond 400, `#6E685F` |
| Label / eyebrow | 14 | EB Garamond italic, sentence case, `#6E685F` |
| Stat | 48 | EB Garamond 400, `#A98018` (gold-deep) or `#14120E`. If Slides shows old-style figures, STIX Two Text |
| Role under a name | 13 | EB Garamond 400, `#B8000F` red |

**Never in decks:** all-caps text (titles, labels, table headers, ratings) or monospace anywhere except inside tables and chart axes.

**Color in decks**
- **Gold-deep:** stats, the *f*, accent dashes.
- **Red:** role titles, CTA lines ("Applications open early Spring"), negative numbers, bullet glyphs only.
- Never put gold-deep or stone text below 24pt.
- Replace every `#000000`, `#1A1A1A`, `#434343`, `#4B5563` and `#888888` with tokens.

## 2. Slide archetypes

**Approved** layouts come from decks we've presented and are rendered in `templates/deck-master.html`; copy them. **Draft** layouts have no approved reference yet: build them carefully, run Visual QA twice, and tell the user the slide uses a draft layout.

| # | Status | Archetype | Structure | Existing example |
|---|---|---|---|---|
| S1 | Approved | **Cover** | Paper. Monogram large at top-right, title 60pt anchored bottom-left, one-line description 17pt, date and place 13pt | Event deck slide 1 |
| S2 | Draft | **Section divider** | Ink. Italic label "02 · Valuation" in gold, title 48pt | — |
| S3 | Approved | **Point grid** | Title, then a 2×2 grid of {lead-in 20pt / body 17pt}, each cell topped by a hairline, optional red CTA line at the bottom. ≤25 words per body | "Why did we create Vertex Fund?" |
| S4 | Approved | **Statement / question** | One sentence at 48pt, optional 13pt sub-prompts in a row underneath | "What is something you enjoy…" |
| S5 | Draft | **Chart + takeaway** | Action title (the conclusion as a sentence), chart on the left ~60%, 2–3 lead-in notes on the right, source line | — |
| S6 | Draft | **Stat strip** | Title, 3–4 stats (48pt Garamond) with 13pt captions, optional chart below | "Some numbers, projections, goals" |
| S7 | Approved | **Roster** | Title, a grid of 5 per row 3:4 portraits (same crop, same edit), name 15pt 600, role 13pt red, major and year 11pt `#6E685F` | "Our Team" |
| S8 | Approved | **Partner** | Partner logo (actual colors allowed inside the logo only), 2 lead-in pairs, optional speaker headshot | "Corporate Partnership" |
| S9 | Draft | **Table** | Comps or financials. Mono numbers right-aligned, hairline rows, header row in italic sentence case, no fills except a paper-2 highlight on the subject company | — |
| S10 | Approved | **CTA / close** | 1–2 lead-in steps on the left, QR code (black on paper, 216pt = 3in) on the right with the URL beneath it | "Stay Connected" |

## 3. Equity pitch structure (stock pitches to the fund)

No real pitch exists yet, so this is v1. Revise after the first one.

1. **Cover (S1):** company, ticker, exchange, presenting analysts, sector team, date.
2. **The call (S6), always slide 2:** rating (Buy / Hold / Sell, written in sentence case; Sell in red), current price, price target, implied upside or downside, time horizon, proposed position size (% of AUM).
3. **Business snapshot (S3 or S9):** what they sell, to whom, how they make money, 3–4 key metrics.
4. **Thesis overview (S3):** exactly 3 pillars, each one sentence.
5. **Pillars 1–3 (S5), one slide each:** an action title stating the claim, evidence chart, 2–3 notes.
6. **Valuation (S5 + S9):** DCF summary (WACC, terminal growth, implied value), comps table, football field.
7. **Catalysts (S3 or timeline):** dated events that close the gap to the target.
8. **Risks and mitigants (S9):** the risk, its likelihood and impact, the mitigant, and what would change our mind.
9. **Recommendation (S6):** repeat the call, entry/exit criteria, position sizing.
10. **Appendix:** model detail, sources.

**Rules**
- Action titles state conclusions ("Margins are inflecting, not peaking"), not topics ("Margins").
- One message per slide. ≤40 words of body text.
- Every chart and number has a source line with the date.
- The last line on slide 2 and the closing slide: *For educational purposes only. Not investment advice.*

**Club decks** (events, interest meetings, sponsor pitches) use S1, S3, S4, S6, S7, S8 and S10.
- Interest meeting order: Cover → Check-in → Team → Why we exist → What we do → Partners → Program → Activity → CTA → Questions → Thank you.

## 4. Data visualization

### Palette by role, not by rainbow

| Role | On light | On dark |
|---|---|---|
| Subject (the company or the fund) | `#A98018` gold-deep | `#D6A72A` gold |
| Comparison 1 / benchmark | `#14120E` ink | `#FAFAF8` paper |
| Comparison 2 | `#8C867E` stone | `#8C867E` stone |
| Comparison 3+ / context | `#C9C3B8` paper-dim | `#46403A` ink-2 |
| Negative / downside / bear case | `#B8000F` red | `#E8695C` red-bright |
| Positive | the subject gold or ink. **No green.** | gold or paper |
| Gridlines and axes | `rgba(20,18,14,.10)` | `rgba(250,250,248,.14)` |

**Series limits**
- Max 4 colored series. Beyond that, gray the context series and label them directly.
- Highlight one thing per chart. Everything else stays neutral.

### Mark specs
- **Lines:** subject 2.5px, others 1.5px. Benchmark dashed (4/4). No markers except the last point (filled circle plus a label).
- **Bars:** square ends, gap = 40% of bar width, no outlines. Value labels in DM Mono at the bar end.
- **Axes:**
  - No chart border and no vertical gridlines.
  - Horizontal gridlines only, 1px, at clean intervals.
  - Y-axis starts at 0 for bars; lines may zoom.
- **Labels:**
  - Label lines directly at their end instead of using a legend.
  - Axis and tick labels in DM Mono 11pt `#6E685F`.
  - Units in the axis title ("Revenue, $M").
- **Numbers:**
  - Mono, right-aligned in tables.
  - Thousands separators.
  - Negatives as −4.2% in red (true minus sign), not parentheses, except in financial statements, where (4.2) is fine.
  - Format: $1.2B, 18.4x, 12.5%, FY26E, Q3 '26.

### Chart forms
| Question | Form |
|---|---|
| Change over time | Line |
| Compare categories | Horizontal bar, sorted |
| Composition | Stacked bar (≤4 parts). Never pie or donut |
| Valuation range | Football field: horizontal floating bars, a current-price line in ink, the target line in gold |
| Relationship | Scatter, subject dot in gold, peers in stone, all labeled |
| Price performance | Indexed to 100, subject vs. benchmark (S&P 500 dashed ink) |

### Tables (comps, financials)
- Header: EB Garamond italic 11pt, sentence case, `#6E685F`, 1pt ink rule underneath.
- Figures: DM Mono 11–12pt, right-aligned (the one place mono belongs). Labels and company names stay EB Garamond.
- Rows: 1pt hairline separators, no zebra striping, no cell fills.
- Subject row: paper-2 fill plus 600 weight name.
- Median and mean rows: italic, set apart by a 1pt ink rule above.

### Never
3D, pie or donut, dual y-axes (use two charts), rainbow palettes, chart titles that just repeat the axis, screenshots of Excel charts with default styling, green-up/red-down tickers in decorative contexts.
