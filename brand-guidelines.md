# Vertex Fund: Brand Guidelines

**v1.5 · November 2026** (v1.5: approved photo-cover post; caps allowed in the wordmark subline. v1.4: slide master + mandatory visual QA. v1.3: social layouts cut to Statement and Grid. v1.2: anti-slop guardrails. v1.1: no all caps; monospace limited to tables and chart axes)
Owner: Vertex Fund executive board. Applies to everything public (Instagram, LinkedIn, the website, flyers) and private (decks, pitches, memos, sponsor letters).

> **How this repo fits together**
> - `vertex-brand-guidelines/assets/tokens.css` holds **every value** (colors, fonts, sizes). It is the single source of truth.
> - This file explains the *why* and the rules for people.
> - `vertex-brand-guidelines/` is the Claude Skill: the same rules, in the form Claude reads.
> - If two places disagree, `tokens.css` wins. Fix the other place.

---

## 1. Principles

1. **Quiet confidence.** We look like a well-set financial broadsheet, not a startup. Restraint signals discipline, which is the thing we want people to believe about our investing.
2. **One system, many layouts.** A post, a slide and a memo share the same paper, ink, gold and type. Only the layout changes.
3. **Facts first.** Every graphic answers *what, when, where* before it tries to be clever.
4. **Gold means us; red means act.** Gold is our signature. Red appears only when we need you to do something or when a number is going the wrong way.

## 2. Logo

The mark is **V*f***: an upright STIX Two Text **V** (Medium) and an italic STIX ***f***. The lockup adds "Vertex Fund" and "University of Maryland".

| File (`vertex-brand-guidelines/assets/logo/`) | Use |
|---|---|
| `vf-monogram-on-light.svg` | Ink V, gold-deep *f*, on paper backgrounds |
| `vf-monogram-on-dark.svg` | Paper V, gold *f*, on ink backgrounds |
| `vf-monogram-mono-ink.svg` / `-mono-paper.svg` | One-color print; over photos |
| `vf-lockup-*.svg` | Same four variants with the name. `-caps` = capitalized subline; `-short` = no subline, for small sizes |
| `vf-avatar-ink-1080.svg` / `-paper-1080.svg` | Profile pictures (Instagram, LinkedIn, GroupMe, TerpLink) |

All files are **outlined vectors** generated from the font files, so they look identical on every computer. Never retype the logo in a font.

Ready-to-use PNGs, social images, favicons and photos for the team are in `brand-assets/` at the repo root.

**Rules**
- Clear space: at least 25% of the monogram's height on all sides.
- Minimum width: 24px on screen, 0.25in in print.
- Don't recolor, outline, rotate, stretch, add shadows, or lock up with a sponsor's logo.
- Placement: top-left at the margin (default), centered above a headline (formal pieces), or as a large faint watermark (one per piece).

## 3. Color

### Palette

| Name | Token | Hex | Role |
|---|---|---|---|
| Ink | `--vf-ink` | `#14120E` | Text on light; the dark background |
| Ink 2 | `--vf-ink-2` | `#46403A` | Secondary text on light |
| Ink 3 | `--vf-ink-3` | `#6E685F` | Small captions and sources on light |
| Stone | `--vf-stone` | `#8C867E` | Large or decorative grey on light; tertiary text on dark |
| Paper | `--vf-paper` | `#FAFAF8` | The light background; text on dark |
| Paper 2 | `--vf-paper-2` | `#F2EFE9` | Alternate surface, print stock, photo mats |
| Paper dim | `--vf-paper-dim` | `#C9C3B8` | Secondary text on dark |
| Gold | `--vf-gold` | `#D6A72A` | Gold on dark backgrounds |
| Gold deep | `--vf-gold-deep` | `#A98018` | Gold on light backgrounds (large text and graphics only) |
| Red | `--vf-red` | `#B8000F` | Red on light |
| Red bright | `--vf-red-bright` | `#E8695C` | Negative numbers on dark |

Every hex except Ink 3, Paper dim and Red bright comes straight from vertexumd.com. Those three were added because the site's colors fail readability in specific spots (see §3.3).

### Gold vs. red

| Gold (identity) | Red (signal) |
|---|---|
| The *f*, the word "Fund" | "Apply", "RSVP by…", deadlines |
| Accent dashes, frames, highlights | Negative returns, downside, Sell ratings |
| Stats and the main chart series | Executive role titles (as on the website team page) |
| CTA lines on dark posts | Small accent text on light, where gold is too faint to read |

- Never use gold and red in the same line.
- On dark backgrounds, red appears only as `--vf-red-bright` for negative numbers.

### Readability (WCAG contrast)

| Pair | Ratio | Verdict |
|---|---|---|
| Ink on paper | 17.9 | Any size |
| Ink 2 on paper | 9.8 | Any size |
| Ink 3 on paper | 5.3 | Any size (smallest captions) |
| Red on paper | 6.6 | Any size |
| Stone on paper | 3.45 | ≥24px / 18pt only |
| Gold deep on paper | 3.47 | ≥24px / 18pt only |
| Paper on ink | 17.9 | Any size |
| Paper dim on ink | 10.7 | Any size |
| Gold on ink | 8.4 | Any size |
| Stone on ink | 5.2 | Any size |
| Red bright on ink | 5.9 | Any size |
| Red on ink | 2.7 | ✗ never |

### Balance and what's off-limits
- **Balance:** roughly 85% background and neutrals, 10% text, ≤5% accent.
- **Never:**
  - Pure black or white, or cool greys.
  - Navy or green.
  - UMD's official red and gold. We're *at* Maryland, not *the* university.
  - A sponsor's brand color outside their own logo.
  - Decorative gradients.

## 4. Typography

| Role | Typeface | Why |
|---|---|---|
| Logo and the typeset name | **STIX Two Text** | The mark is drawn from it. Used nowhere else |
| Headlines and text | **EB Garamond** | The website's voice: classic, literate, finance-appropriate |
| Table figures, tickers in tables, chart axes | **DM Mono** | Every digit is the same width, so columns line up. A quiet supporting voice, never the focal point. Already on the team page |
| *Alternate mono* | *IBM Plex Mono* | Approved substitute if we ever switch. Never mix with DM Mono in one piece |

All are free Google Fonts and work in Google Slides (*Fonts → More fonts*). Fallbacks: Georgia / Menlo.

**Rules**
- **No all caps, with one exception.** Not in headlines, eyebrows, labels, buttons, table headers or ratings. Tickers (NVDA) and real acronyms (UMD, AUM, DCF) keep their capitals.
- **The one exception: the wordmark subline.** "UNIVERSITY OF MARYLAND" may be set in widely spaced capitals under "Vertex Fund" (logo files ending in `-caps`). Sentence case is the default. Use one or the other in a piece, never both.
- **Monospace is a supporting voice.** DM Mono appears only inside tables and on chart axes. Big stats, dates, and headline numbers are EB Garamond.
- **Numbers:** in HTML, Garamond numerals get `lining-nums` so they don't bounce. In Google Slides, if a big stat shows bouncing figures, set just that number in STIX Two Text.
- **Labels and eyebrows:** EB Garamond italic, sentence case, muted color ("Spring 2027 · Analyst cohort").
- **Headline case:** short. Title Case for event names, sentence case for statements and slide titles.
- **Sizes:** only the sizes in the scales (social px, slide pt, document pt; see `tokens.css`). In Google Slides, turn off autofit; it invents sizes like 21.2pt.
- **Minimums:**
  - Posts: 28px for reading copy, 26px for labels.
  - Slides: 16pt for body.
  - Documents: 9pt.

## 5. Shape, space and texture
- **Square corners everywhere.** Circles are only for headshots, with a thin gold ring.
- **No drop shadows, glows, or rounded "cards".** We separate things with whitespace and hairlines.
- **Margins:**
  - Posts: 96px
  - Slides: 54pt
  - Letter pages: 0.75in
- **Optional textures** (max two per piece):
  - Photo cover: a full-colour event photo across the top of a dark post (our approved "Thanks for coming!" post)
  - Gold photo band: a grayscale photo under a gold wash (dark posts)
  - Faint monogram watermark
  - Gilt frame (light) or hairline frame (dark)
- **Signature detail:** a short gold dash followed by an italic line.
- **Photography:**
  - Our own people and rooms.
  - One consistent, light edit per set.
  - Either untouched color (photo cover, carousel slides) or full grayscale under the gold band; no filters or partial tints.
  - No stock trading-floor photos.

## 6. Layouts (composable, not one-off templates)
We don't keep a "Thank You post template" or an "Interest Meeting template". We keep a small set of building blocks and combine them. Two are approved today:

| Primitive | What it is | Typical use |
|---|---|---|
| **P1 · Statement** | Giant headline at the bottom, details, CTA | Announcements, thank-yous, applications |
| **P2 · Grid** | Repeating cells (people, partners) | Exec boards, speakers, sponsor thanks |

Each works in **light or dark**, and in **portrait, square or story** sizes.
- Full specs: `references/social-layouts.md`.
- Slide equivalents: `references/pitch-deck-rubric.md`.
- Page equivalents: `references/documents.md`.
- Live references: `templates/ig-post-master.html` (social) and `templates/deck-master.html` (slides: cover, point grid, roster, statement, partner, call to action).

## 7. Decks, pitches and charts (summary)
- **Decks:** paper background, lockup plus hairline header on every slide, 36pt titles, 10 slide archetypes (6 approved in `deck-master.html`, 4 drafts).
- **Stock pitches:**
  - Lead with the call on slide 2 (rating, target, upside).
  - Exactly three thesis pillars.
  - Action titles that state conclusions.
  - A source on every number.
- **Charts:**
  - Our subject in gold, comparisons in ink and stone, downside in red, no green, no pies, no 3D.
  - Label lines directly; skip legends.
- Details: `references/pitch-deck-rubric.md`.

## 8. Voice
- **Plain, specific, calm.** "Applications are open", not "Don't miss out!!"
- **What, when, where first;** then why.
- **House style:**
  - "Vertex Fund" (not "VF").
  - "Wednesday, November 18 · 6:00 PM".
  - Ranges with en dashes (30–50).
  - '27 with a curly apostrophe.
- Exclamation marks only in warm moments (thank-yous, "Free food!"), at most one per line. No emoji in graphics.
- Anything about a security, position or return says: *For educational purposes only. Not investment advice.*

## 9. Guardrails against generic, AI-looking design
Our palette and type sit close to two looks that reviewers now flag as AI-made: "warm editorial" (cream background, serif, clay accent) and "broadsheet cosplay" (thin rules, square corners). What keeps us out of that bucket is **specific content**: our members, our rooms, our dates, our numbers, written plainly. The full checklist is `references/anti-slop.md`. The rules people break most:

- **Fonts:** two families max. Never add a font for numbers or "contrast"; use weight or italic instead.
- **Eyebrows and taglines:** none by default. A subhead that restates the headline gets deleted.
- **Space:** fill the canvas with content. If it looks empty, make the headline or photo bigger; don't add decoration.
- **Copy:** the headline is the event or the fact. No "elevate", "unlock", "journey", "by the numbers", "not just X but Y", or three-adjective strings.
- **Honesty:** never invent a number, name, quote or partner. Leave `[brackets]` until it's real.
- **Before posting:**
  - Delete anything that carries no information.
  - Swap in another club's name. If the design still works, it isn't specific enough yet.

## 10. Visual QA
Nothing ships unseen. Every design Claude makes with this skill must be rendered, screenshotted and inspected (`scripts/render_check.py`, then a look at every image) before it's delivered, and again after every revision. If a design couldn't be rendered, Claude must say so. When you make something by hand, export it and check it at full size and at phone-thumbnail size before posting.

## 11. Using Claude with this system
1. **Install the skill.** Zip `vertex-brand-guidelines/` and upload it in Claude → Settings → Capabilities → Skills, or keep it in this repo for Claude Code.
2. **Ask plainly**, e.g. "Make an Instagram post announcing our Polymarket speaker on Dec 3." Claude picks the primitive, mode and format from the rules.
3. **When a new design works well**, add it as a row in the "Adapting a layout" table in `social-layouts.md`, not as a new template file.
4. **Changing a color or size:**
   1. Edit `tokens.css`.
   2. Run `python3 tools/build_template.py` to refresh the HTML master.
   3. Update the tables in this file and `SKILL.md`.
   4. Bump the version above.

## 12. Known gaps (v1)
- **Draft layouts:** slides S2 section divider, S5 chart, S6 stat strip, S9 table; documents D2 sidebar, D3 memo. Pitch and memo specs are written from best practice; no real Vertex equity pitch exists yet. Revise after the first one.
- **The Google Slides master** should be rebuilt to these specs. The current decks use Georgia, oxblood `#A7221D`, and stray blacks.
- **The website** has a short list of conflicts in `site-contradictions.md`. No site changes have been made.
- **Social layouts removed until redesigned:** a facts/ledger layout ("Applications are open"), a big-numbers layout ("Our first semester") and a sidebar recap layout ("What we covered"). Until then, use P1 or P2.
