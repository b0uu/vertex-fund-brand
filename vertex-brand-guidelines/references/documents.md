# Documents — memos, recap letters, one-pagers, flyers

Page: US Letter (8.5×11in; 816×1056 CSS px). Margins 0.75in. Background `#FAFAF8`, or `#F2EFE9` for print and keepsake pieces.
Same tokens, same type families. EB Garamond for everything, DM Mono only for figures inside tables, STIX only in the lockup. No all-caps text.

## 1. Page anatomy (all documents)

| Zone | Spec |
|---|---|
| Masthead | Lockup on-light (monogram ≈ 0.55in wide) top-left; document type plus date as an italic label top-right ("Event recap · November 2026"); 1px `rgba(20,18,14,.10)` rule under it |
| Title | EB Garamond 400, 28pt (up to 40pt for one-word titles), sentence case |
| Body | 11pt, line height 1.5, `#46403A`. Measure 60–75 characters |
| Section heads | 14pt EB Garamond 600, `#14120E`, 14pt space above |
| Labels | 9pt EB Garamond italic, sentence case, `#6E685F` |
| Lists | Em-dash bullets in the accent color (gold-deep), 6pt between items |
| Footer | 8pt EB Garamond, `#6E685F`: "Vertex Fund · University of Maryland · vertexumd.com" left, page number right |

## 2. Layouts
- **D1 · Classic letter:** masthead, title, date, an opening paragraph, a photo pair (same height), a stat strip (3–4 stats in 24pt EB Garamond lining numerals, gold-deep, with labels), "What we covered" / "What's next" lists, sign-off. For sponsor recaps and thank-you letters.
- **D2 · Sidebar (Rail + Column)** *(draft, no approved reference)*: a 2in rail (sponsor logo, date, place, attendance as italic label/value pairs), a 1px vertical rule, then the main column. For recaps, one-pagers and event briefs.
- **D3 · Memo** *(draft, no real memo exists yet)*: a ledger header block, then numbered sections (see §3).
- **D4 · Flyer / poster:** use the P1 Statement layout scaled to Letter. Margins 0.75in, headline 72–96pt, italic labels 12pt, QR code ≥1.25in with a URL beneath it.

## 3. Investment memo (stock pitch write-up)

v1, to revise after the first real memo.

**Header block (ledger)**
- A grid of label/value pairs between a 1.5pt ink rule above and a 1px hairline below:

  Ticker · Rating · Price · Target · Upside · Horizon · Position size · Date · Analysts

- Labels in italic; values in EB Garamond 12pt with lining numerals. Rating in sentence case (Buy / Hold / Sell); Sell in red.

**Sections**
1. **Recommendation:** 3 sentences: the call, why, and why now.
2. **Business overview**
3. **Thesis:** exactly 3 pillars, each a bolded claim followed by evidence.
4. **Valuation:** DCF assumptions table, comps table, implied value range.
5. **Catalysts:** dated.
6. **Risks and mitigants:** a table.
7. **What would change our mind**
8. **Sources**

**Rules**
- Max 2 pages plus appendix.
- Exhibits are numbered ("Exhibit 3 — Gross margin vs. peers") with source lines, and follow the chart rules in `pitch-deck-rubric.md`.
- Footer on every page: *For educational purposes only. Not investment advice.*

## 4. Email and short-form
- Plain text, or a single-column HTML body at 600px on paper, using the same masthead.
- No images of text. Sign-off: name (600 weight), then "Title, Vertex Fund · email" in `#6E685F`.
