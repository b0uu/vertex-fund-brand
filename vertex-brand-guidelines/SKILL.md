---
name: vertex-brand-guidelines
description: Vertex Fund (UMD student investment fund, vertexumd.com) visual identity. Use for ANY Vertex Fund deliverable — Instagram or LinkedIn posts, banners, profile avatars, slide decks, stock pitches, investment memos, recap letters, one-pagers, flyers, charts, or web pages — so it matches the house style without re-explaining it.
---

# Vertex Fund brand system

One invariant system + composable layouts. Never design from first principles; assemble from the tokens and primitives below.
**Source of truth for every value:** `assets/tokens.css`. If anything here disagrees with it, the CSS wins.

## Routing — read the reference before building
| Deliverable | Read | Start from |
|---|---|---|
| Instagram / LinkedIn post, story, carousel, banner, avatar | `references/social-layouts.md` | `templates/ig-post-master.html` |
| Slide deck (club, event, sponsor, or stock pitch) | `references/pitch-deck-rubric.md` | `templates/deck-master.html` |
| Memo, recap letter, one-pager, flyer, PDF | `references/documents.md` | — |
| Any chart or table with numbers | `references/pitch-deck-rubric.md` § Data visualization | — |
| Logo needed | `assets/logo/` (outlined SVGs — never retype the mark) | — |
| **Every deliverable, before showing it** | `references/anti-slop.md` (hard fails, banned copy, process) | — |

## Identity in one paragraph
Editorial, quiet, and confident, like a well-set financial broadsheet. Warm paper and warm ink, one serif voice, gold used sparingly as the signature, hairlines instead of boxes. No gradients-as-decoration, no shadows, no rounded cards, no icons-as-decoration, no stock-photo glamour.
**Specificity is the brand.** Cream + serif + hairlines is also a recognized *AI* look ("warm editorial" / "broadsheet cosplay"). It only reads as Vertex when filled with real photos, names, dates, and sourced numbers in plain copy.

## Color (two modes, one palette)
| Token | Hex | Use |
|---|---|---|
| `--vf-ink` | `#14120E` | Text on light; dark-mode background |
| `--vf-ink-2` | `#46403A` | Secondary text on light |
| `--vf-ink-3` | `#6E685F` | Small meta text on light (captions, sources) |
| `--vf-stone` | `#8C867E` | Large/non-text on light; tertiary text on dark |
| `--vf-paper` | `#FAFAF8` | Light background; text on dark |
| `--vf-paper-2` | `#F2EFE9` | Alternate light surface, print stock, photo mats |
| `--vf-paper-dim` | `#C9C3B8` | Secondary text on dark |
| `--vf-gold` | `#D6A72A` | Gold **on dark** |
| `--vf-gold-deep` | `#A98018` | Gold **on light** — ≥24px text or graphics only (3.5:1) |
| `--vf-red` | `#B8000F` | Red **on light** |
| `--vf-red-bright` | `#E8695C` | Red **on dark** — negative numbers only |
| `--vf-rule-light` / `--vf-rule-dark` | ink 10% / paper 14% | Hairlines |

**Accent law**
- **Gold = identity.** The italic *f*, the word "Fund", divider dashes, frames, highlights, the primary chart series. Default accent everywhere.
- **Red = signal.** "Apply", deadlines, "new/live", negative values, executive role titles, and *small* accent text on light where gold is too faint. Never decorative, never on dark except `--vf-red-bright` for negative numbers.
- One accent per element. Never gold and red side by side in the same line.

**Ratio:** about 85% background + neutrals, 10% text, ≤5% accent. A gold photo wash counts as texture, not accent.

**Forbidden:** pure `#000`/`#FFF`, cool greys (`#4B5563`, `#E5E7EB`, `#888`…), navy, green, UMD red `#E21833` or UMD gold `#FFD200`, brand colors of sponsors (show their logo, never their color), gradients except the photo-band seam, neon/glow, more than one accent hue per element.

## Typography
| Role | Family | Notes |
|---|---|---|
| Logo + typeset "Vertex Fund" | **STIX Two Text** | Lockup only. V upright (500), *f* italic (400), tracking −0.04em |
| Headlines + body | **EB Garamond** | 400 for headlines, 500–600 for names and lead-ins, italic for CTA lines |
| Supporting data only: table figures, tickers inside tables, chart axes | **DM Mono** | Never the focal point. Approved alternate: IBM Plex Mono; never both in one piece |

- Fallbacks: `Georgia, 'Times New Roman', serif` / `ui-monospace, Menlo, monospace`. All three are Google Fonts, so they're available in Google Slides via *More fonts*.
- **Monospace stays small.** Never use DM Mono for headlines, big stats, dates, labels, or anything the eye lands on first. Hero numbers are EB Garamond.
- **Numerals:** EB Garamond can render old-style (bouncing) figures. In HTML always apply `font-variant-numeric: lining-nums` (class `.vf-nums`). In Google Slides, if big stats show old-style figures, set just those numbers in STIX Two Text (lining by design).
- **No all caps, with one exception.** Not for headlines, eyebrows, labels, buttons, or table headers. No `text-transform: uppercase`, no small caps. Tickers (NVDA) and acronyms (UMD, AUM, FY26E) keep their capitals.
- **The one exception is the wordmark subline.** "UNIVERSITY OF MARYLAND" may be set in tracked capitals (0.2em) directly under "Vertex Fund" as part of the lockup (`vf-lockup-*-caps.svg`). Sentence case ("University of Maryland") is the default; pick one per piece. Nothing else on the piece may be in capitals.
- **Labels/eyebrows:** EB Garamond *italic*, sentence case, `--fg-3`, no extra tracking ("Spring 2027 · Analyst cohort").
- **Headlines:** short; Title Case for event names ("Interest Meeting"), sentence case for slide action titles and statements. ≤2 lines on social, ≤2 lines on slides.
- **Scales** (all in tokens.css):
  - Social (px @1080w): display 140, h1 104, h2 72, lead 44, body 34, small 28, label 26
  - Slides (pt @960×540): cover 60, section 48, title 36, lead-in 20, body 17 (min 16), small 13, label 14, stat 48
  - Documents (pt, Letter): title 28, h2 14, body 11, small 9, label 9
- Never use Georgia, Libre Baskerville, Cormorant, Inter, or Consolas as a designed choice.

## Geometry & texture
- **Corners:** square, always. Circles only for headshots (with a 1.5px `--vf-gold-deep` ring offset by 7px on light).
- **No drop shadows, glows, blur, bevels, or cards.** Separate content with whitespace and hairlines (1px; 2px on 1080 canvases).
- **Margins:** social 96px (portrait/square; 88px on 1080×1080), story 220px top / 300px bottom; slides 54pt left/right; Letter 0.75in.
- **Frames (optional):** gilt frame on light = 1.5px `--vf-gold-deep` inset 32px; hairline frame on dark = 2px `--vf-frame-dark` inset 48px. Never both.
- **Photo treatments (dark posts), pick one:**
  - **Photo cover:** a full-colour event photo (brightness 0.9) on the top ~65%, with a 300px top scrim (ink 60%→0) and a 128px seam into ink. This is the default for recaps and thank-yous; the approved reference is `assets/examples/thanks-for-coming-posted.jpg`.
  - **Photo band:** a grayscale photo at 30% under a gold-deep wash at 62%, covering the top ~56%. Use it for announcements where the photo is texture rather than the subject. No text smaller than 60px over the wash.
- **Watermark (optional):** monogram 600px wide, 15–17% opacity, bleeding off the top-right. Max one per piece.
- **Signature motif:** 56×2px dash in the accent color, then an italic line ("RSVP via link in bio").
- **Photos:** real members, rooms, and events over stock. Consistent light edit across a set. No filters, tints, or text on carousel photo slides; the cover carries the design.
- Max two texture modules per piece (frame, photo band, watermark).

## Logo rules
- Files: `assets/logo/vf-monogram-{on-light|on-dark|mono-ink|mono-paper}.svg`, `vf-lockup-…svg` (mark + "Vertex Fund" + "University of Maryland"; `-caps` variants set it in tracked capitals; `-short` variants drop the subline for small sizes), `vf-avatar-{ink|paper}-1080.svg`. All outlined — use them, never retype in a font.
- On light: ink V + `--vf-gold-deep` *f*. On dark: paper V + `--vf-gold` *f*. Mono versions for one-color printing or over photos.
- Clear space ≥ 25% of the monogram's height on all sides. Minimum monogram width 24px / 0.25in.
- Placement: top-left at the margin (default), centered above a headline (formal/roster), or as a watermark. Never center-bottom, never rotated, never outlined, recolored, stretched, or given effects.
- Sponsor logos sit in a labeled partner row ("Sponsored by"), never locked up with the Vf mark.

## Voice
- Plain, specific, confident; no hype. "Applications are open", not "Don't miss out!!".
- Lead with the fact (what, when, where), then the reason. Numbers beat adjectives.
- Exclamation marks: at most one per line, and only in warm moments (a thank-you, "Free food!"), never in announcements of facts. No emoji in graphics.
- House style: "Vertex Fund" (never "VF" or "Vertex" alone in headings), "University of Maryland" / "UMD", en dashes for ranges (30–50), curly apostrophes in years ('27), "6:00 PM", "Wednesday, November 18".
- Investment content (pitches, theses, positions) carries: *For educational purposes only. Not investment advice.*

## Anti-slop core (full list: `references/anti-slop.md`)
- **Two families max** (EB Garamond + the logo; DM Mono only inside tables). Never add a font for "contrast".
- **Zero eyebrows by default**, one at most, never repeating the headline. No subhead that restates the headline. No decorative meta strings or numbered labels.
- **Fill the canvas with content, not air.** No empty band >25% of the canvas; if it looks empty, scale up the headline or photo. Never add filler.
- **Plain copy:** headline = the event or fact in ≤5 words. No "elevate / unlock / journey / by the numbers / where X meets Y / not just X but Y", no adjective triads, no rhetorical hooks.
- **Never invent** numbers, names, quotes, or partners. Unknowns stay as `[brackets]`.
- **Subtract pass + name-swap test** before delivering: delete anything that carries no information; if another club's name fits just as well, add our specifics.

## Visual QA (mandatory, every deliverable, every revision)
Never deliver a design you haven't looked at. Code that "should" render correctly isn't checked.
1. Render: `python3 scripts/render_check.py <file.html> --out qa/` writes one PNG per artboard or slide, phone-size thumbnails, and a contact sheet. It also flags overflow, out-of-bounds elements, off-brand fonts, too-small text, all caps, monospace as a focal element, and dead zones (>25% empty).
2. Fix every automated finding and re-run until it reports none.
3. **Open and look at every PNG** (full size and thumbnail). Check what scripts can't: awkward line breaks (a word or year alone on a line), collisions, uneven spacing, elements crowding the margin or frame, weak hierarchy, anything in `references/anti-slop.md` §1.
4. Fix, re-render, look again. Repeat until clean.
5. If the brand fonts didn't load in the sandbox, say the preview used fallback fonts. If nothing can render at all, tell the user plainly that the design was **not** visually checked.
6. Non-HTML outputs (Google Slides, PPTX, PDF, images): export or screenshot each page or slide and inspect it the same way.

## Build checklist (run before delivering)
1. Every color is a token; every size is on a scale; one accent per element.
2. Fonts: EB Garamond everywhere; DM Mono only in tables/axes; STIX only in the lockup. Lining numerals. No all caps except the lockup subline.
3. Logo from `assets/logo/`, correct mode variant, clear space respected.
4. Margins and safe zones held; nothing smaller than the label size.
5. Contrast: small text ≥4.5:1 (never gold-deep or stone for small text on light).
6. No shadows, rounded cards, gradients, emoji, or sponsor colors.
7. Copy passes the voice rules; investment content has the disclaimer.
8. `references/anti-slop.md` §1 hard fails: zero.
9. Visual QA done: rendered, automated checks clean, every page inspected by eye.
