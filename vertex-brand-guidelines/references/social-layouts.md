# Social layouts — composable primitives

Every social graphic = **Canvas → (Texture) → Masthead → ONE Body primitive → (CTA)**.
No all-caps text (the lockup's "UNIVERSITY OF MARYLAND" subline is the one exception) and no monospace on social graphics. Labels are EB Garamond italic in sentence case.
Don't make single-purpose templates ("Thank You post"). Pick a primitive, a mode, and a format, then fill it in.
References: the posted originals are in `assets/examples/`. `templates/ig-post-master.html` holds the same two posts rebuilt on the tokens, as starting code.

## 1. Canvas: format × mode

| Format | Size | Margin / safe zone | Notes |
|---|---|---|---|
| IG feed portrait (default) | 1080×1350 | 96px | Instagram crops a carousel to its first slide's ratio, so make every slide 4:5 |
| IG / LinkedIn square | 1080×1080 | 88px | Grid previews crop 4:5 posts to 3:4: keep the headline inside the central 1012×1350 |
| IG story / reel cover | 1080×1920 | 96px sides, 220px top, 300px bottom | Top and bottom are covered by app UI |
| LinkedIn feed | 1080×1350 (preferred) or 1200×627 | 96px / 64px | 4:5 reuses the IG artwork unchanged |
| LinkedIn personal banner | 1584×396 | Keep the left 480px empty (profile photo overlap on desktop and mobile); content in the right ~60% | Dark mode, hairline frame inset 60px |
| LinkedIn company cover | 1128×191 | Keep the left 300px empty (logo overlap) | Lockup only, no copy |
| Profile avatar | 1080×1080 master (export 400) | Monogram width ≤ 50% of the canvas, centered | Gets cropped to a circle; use `assets/logo/vf-avatar-*.svg` |
| OG / link preview | 1200×630 | 64px | Dark lockup |

**Mode**
- **Dark** (`.vf-dark`, ink background) for announcements, statements, banners and avatars. This is the default for the feed.
- **Light** (`.vf-light`, paper or paper-2) for informational and roster posts.
- Alternate the two across the feed so the grid reads as a rhythm. Keep one mode within a carousel.

## 2. Texture modules (optional, max 2)

| Module | Spec | Use with |
|---|---|---|
| Photo cover | **Full-colour** event photo, brightness 0.9, top ~65% (882px), 300px top scrim ink 60%→0, 128px seam into ink | Dark + Statement. **Approved reference:** `assets/examples/thanks-for-coming-posted.jpg` |
| Photo band | Grayscale photo, contrast 1.08, 30% over ink, gold-deep wash at 62%, top ~56% of the canvas, ≤120px seam into ink | Dark + Statement |
| Watermark | Monogram 600px wide, 15–17% opacity, bleeding off the top-right (right −60px, top 80px) | Dark + Statement |
| Gilt frame | 1.5px `--vf-gold-deep`, inset 32px (from the website's 2026 new-exec post) | Light, formal posts |
| Hairline frame | 2px `--vf-frame-dark`, inset 48px | Banners, OG images |

Never use both frames together. Never put text smaller than 60px over the gold wash (cream on wash is under 3:1).

## 3. Masthead (choose one)
- **Corner lockup** (default): monogram 92px wide, then "Vertex *Fund*" (STIX 40px) over "University of Maryland" (STIX 20px, `--fg-3`). Top-left at the margin.
- **Wordmark XL:** "Vertex *Fund*" at 84px, "University of Maryland" at 28px, no monogram. Pairs with a watermark.
- **Inline lockup:** monogram 84px + "Vertex *Fund*" at 64px on one line, no subline. Use it over a photo cover, top-left.
- **Subline in capitals (optional):** any masthead with a subline may set it as "UNIVERSITY OF MARYLAND" (STIX, tracking 0.2em, ~75% of the sentence-case size). This is the only all-caps text allowed.

## 4. Body primitives (choose ONE)

Only **P1 Statement** is approved, in two variants, and both come from posts we actually published. Every other layout (facts/ledger, big numbers, sidebar recap, people grid) was removed until it's designed with the exec board. Don't improvise substitutes: if a post needs one, propose it to the user as a new design and get approval before using it.

### P1 · Statement
A huge headline anchored bottom-left, then a two-line detail stack (line 1 in accent, line 2 in `--fg-2`), then a CTA line.
- **Slots:** `display` headline (≤2 lines, ≤14 characters per line at 140px), `lead` × 2, `cta`, optional partner row higher up.
- **Use for:** event announcements, thank-yous, "applications open", quotes (set quotes in italic at h1 size, attribution as a label).
- **Photo cover variant (approved, posted):** photo cover + inline lockup + `display` headline + one gold line. The reference is the interest-meeting thank-you: "Thanks for coming!" / "Stay tuned for future public events & for Spring cohort!". It's rendered in `templates/ig-post-master.html`, and the posted version is in `assets/examples/`.

## 5. CTA line
A 56×2px dash, then an italic line at 32px.
- **Gold** (identity) by default.
- **`.signal` red** on light posts when it's an action with a deadline ("Apply by Feb 9").
- On dark, CTAs stay gold.

## 6. Carousels
- **Slide 1:** usually P1.
- **Slides 2–n:** photos only, cropped 4:5 by hand, one consistent light edit, no tint, no text, no logos.
- **Order:** the room, then the presenters, then the team, then partners, then the crowd.
- **Optional end slide:** P1 dark statement thanking the sponsor, with their logo.
- 5–7 slides total. The details go in the caption, not on the photos.

## 7. Captions (copy around the graphic)
- **Line 1:** the fact (what, when, where).
- **Line 2:** the why, or the perk.
- **Line 3:** the CTA (e.g. "Link in bio").
- Then thanks with @-handles.
- Max 3 hashtags (#UMD #Terps #InvestmentClub). No emoji walls; at most one.

## 8. Adapting a layout (worked examples)
| Need | Composition |
|---|---|
| Event announcement | portrait · dark · photo band · Wordmark XL · P1 · gold CTA |
| Post-event thank-you | portrait · dark · **photo cover** · inline lockup · P1 ("Thanks for coming!") — the approved reference |
| Applications open | portrait · light · corner lockup · P1 (headline carries the specifics) · red CTA |
| New exec board | **No approved layout yet.** Propose one and get approval first |
| Speaker announcement | **No approved layout yet.** Propose one and get approval first |
| Sponsor recap | carousel: P1 photo-cover thank-you, untouched photo slides, P1 dark sponsor end slide ("Thank you, Brown Advisory." + their logo) |
| Stock pitch teaser | portrait · dark · corner lockup · P1 (headline states the call) + disclaimer as the last line |
