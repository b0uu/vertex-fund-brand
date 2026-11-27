# Slide decks & data visualization

## 0. The reference: our Event Slideshow

**`assets/examples/event-slideshow/` is the deck reference.** It holds all 15 slides of "Vertex Fund @ University of Maryland: Event Slideshow", the deck we presented at the Nov 18, 2026 interest meeting, exported straight from Google Slides. Look at the slides before building any deck, and match them.

This deck **intentionally differs from the general theme**, and for decks the deck wins:

| | Event Slideshow (use this in decks) | General theme (social, documents) |
|---|---|---|
| Font | **Georgia** throughout | EB Garamond |
| Accent | **Oxblood `#A7221D`** for role titles, bullets and the one key stat | Gold identity, red signal |
| Header subline | "UNIVERSITY OF MARYLAND" in capitals | Either case |
| Centering | Centered titles on single-message slides (Check-in, Questions, Thank you) | Left-aligned |

Don't "correct" decks toward the general theme. Only change the deck style if the exec board decides to.

## 1. The slide master (measured from the reference)

Decks are built in **Google Slides** (16:9, 960×540pt).

| Element | Spec |
|---|---|
| Background | `#FAFAF8` on every slide |
| Header | Logo image (mark + "Vertex Fund" + "UNIVERSITY OF MARYLAND") at (54, 24)pt, 166×30pt; 1pt `#E1E1DF` hairline at y = 63pt across the 852pt content width |
| Margins | 54pt left and right |
| Title | Georgia 400, 36pt, `#13120E`, left-aligned below the header |
| Corners / shadows | Square, no shadows, except the two QR cards on the "Stay connected" slide |

**Type (pt):**

| Role | Size | Style |
|---|---|---|
| Opening / section title | 59–64 | Georgia 400, `#13120E` |
| Quote | 50 | Georgia 400, in curly quotes |
| Slide title | 36 | Georgia 400, `#13120E` |
| Lead-in | 19.5 | Georgia **bold**, `#13120E` |
| Body under a lead-in | 17.5 | Georgia 400, `#45403B` |
| Team name | 15 | Georgia bold, `#13120E` |
| Team role | 12.7 | Georgia 400, oxblood `#A7221D` |
| Secondary callout | 25.5 | Georgia 400, `#888888` (e.g. "Applications open early in the Spring!") |
| Key stat | 25.5 | Georgia 400, oxblood `#A7221D` (e.g. "Starting AUM >$5,000") |

Turn off autofit in Slides and stick to these sizes. The reference drifted in a few places (16.25–21.2pt body sizes, `#000000`, `#4B5563` and `#434343` text on two slides); don't copy those.

## 2. Slide types (all from the reference)

| # | Type | Reference slide | Structure |
|---|---|---|---|
| R1 | Opening title | 1 | Big title left-aligned, one-line description in body grey below. No image |
| R2 | Centered single message | 2, 14, 15 | One centered title (Check-in, Questions?, Thank you); optionally one QR code centered below |
| R3 | Team grid | 3 | Title, 5×2 portraits (same crop), bold name, oxblood role |
| R4 | Lead-in list | 4, 8, 12 | Title, stacked {bold lead-in / one body line} pairs; optionally a side column (grey callout + oxblood stat, or a QR code with a bold label) |
| R5 | Partner | 5 | Title with the partner logo inline to its right; two columns of {bold small heading / body} |
| R6 | Speaker | 6 | Headshot left with name under it; title, credentials (bold, centered) and company logo right |
| R7 | Three columns | 7 | Title plus logos at right; three columns of {bold heading / body} |
| R8 | Two columns | 9 | Left: list with oxblood bullets. Right: lead-in pairs |
| R9 | Section statement | 10 | Big title (~64pt) left-aligned, one instruction line below |
| R10 | Quote + prompts | 11 | Centered quote ~50pt; four small prompts scattered below |
| R11 | Call to action | 13 | Two bulleted steps left; QR cards right (white rounded card, bold label above each code) |

**Draft slide types (no approved reference yet).** For a chart, a stat strip, a table or a section divider, build it carefully in the reference's style (Georgia, oxblood, header) and run Visual QA twice. Tell the user the slide uses a draft layout.

## 3. Equity pitch structure (stock pitches to the fund)

No real pitch exists yet, so this is v1. Revise after the first one.

1. **Cover (R1):** company, ticker, exchange, presenting analysts, sector team, date.
2. **The call (draft stat strip), always slide 2:** rating (Buy / Hold / Sell, written in sentence case; Sell in red), current price, price target, implied upside or downside, time horizon, proposed position size (% of AUM).
3. **Business snapshot (R4, or a draft table):** what they sell, to whom, how they make money, 3–4 key metrics.
4. **Thesis overview (R4 or R7):** exactly 3 pillars, each one sentence.
5. **Pillars 1–3 (draft chart slide), one slide each:** an action title stating the claim, evidence chart, 2–3 notes.
6. **Valuation (draft chart + table):** DCF summary (WACC, terminal growth, implied value), comps table, football field.
7. **Catalysts (R4):** dated events that close the gap to the target.
8. **Risks and mitigants (R4, or a draft table):** the risk, its likelihood and impact, the mitigant, and what would change our mind.
9. **Recommendation (draft stat strip):** repeat the call, entry/exit criteria, position sizing.
10. **Appendix:** model detail, sources.

**Rules**
- Action titles state conclusions ("Margins are inflecting, not peaking"), not topics ("Margins").
- One message per slide. ≤40 words of body text.
- Every chart and number has a source line with the date.
- The last line on slide 2 and the closing slide: *For educational purposes only. Not investment advice.*

**Club decks** (events, interest meetings, sponsor pitches) use R1–R11. Copy the reference's order.
- Interest meeting order: Cover → Check-in → Team → Why we exist → What we do → Partners → Program → Activity → CTA → Questions → Thank you.

## 4. Data visualization

> **Draft.** No real Vertex chart exists yet, so these rules are untested. In decks, the reference's accent is oxblood, which also reads as "loss" in finance. Ask the user which color marks the subject before building the first real chart.

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
