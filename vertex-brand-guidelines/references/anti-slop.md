# Anti-slop guardrails

Generated design drifts to the statistical average: the same fonts, the same layouts, the same copy. Following the Vertex tokens is not enough on its own. Run this file on **every** deliverable, before showing it to anyone.

## 0. The uncomfortable part: our own style is a known AI look

Design reviewers now name two AI clusters that sit right next to our system:
- **"Warm editorial":** cream background, high-contrast serif, clay accent.
- **"Broadsheet cosplay":** thin rules, square corners, newspaper columns.

A third cluster, **"template chrome"**, is what pushed us there: tracked all-caps eyebrows, meta strings with separators, small monospace labels, arrows on every link.

So the Vertex look only reads as *ours* when the content is specific: real photos of our members and rooms, real names, real dates, sourced numbers and plain copy. With placeholder content and decorative rules it reads as AI cosplay of a newspaper. **Specificity is the brand.** Style alone is not.

## 1. Hard fails (any one means redo before delivering)

### Type
- [ ] More than **two type families** on one piece, not counting the logo. No "accent" font added for numbers or quotes. (Past failure: Cormorant Garamond brought in for recap stats.)
- [ ] Any **all-caps** text, letter-spaced labels, or small caps. Excepted: tickers, acronyms, and the lockup subline "UNIVERSITY OF MARYLAND".
- [ ] **Monospace** used for anything the eye lands on first: headlines, stats, dates, labels, links.
- [ ] Gradient text, outlined text, or text with shadows or glows.

### Structure
- [ ] **More than one eyebrow** per piece, or an eyebrow that repeats or decorates the headline. The default is **zero** eyebrows.
- [ ] A **tagline or subhead that restates the headline** ("Interest Meeting" / "Come learn about our fund").
- [ ] **Meta strings stacked as decoration** ("Fall 2026 · Edition 01 · Vol. 1"). Separators (·) are allowed only inside a real date/time or place line.
- [ ] Numbered section labels ("01 —", "No. 3") on anything that isn't a real sequence.
- [ ] Cards, boxes or pills wrapped around content that isn't individually actionable. No pill badge above the title.
- [ ] Three identical items in a row **because three looked balanced**, when the content didn't have three things.
- [ ] Icons or emoji as decoration, arrows (→) on every link, status dots, colored side-stripes.

### Surface
- [ ] Decorative gradients, glows, blurred blobs, glass panels, noise and grain, or drop shadows. The only gradient allowed is the photo-band seam.
- [ ] More than **two texture modules** (frame, photo band, watermark), or a texture added to "make it more interesting".
- [ ] Rules (hairlines) that don't separate two different groups of content. **Max two horizontal rules** per social graphic.
- [ ] Stock imagery, AI-generated images, or illustrations of bulls, charts-going-up, handshakes or skylines.

### Copy
- [ ] Any **invented** number, name, quote, testimonial or partner. Unknown facts stay as visible `[brackets]`.
- [ ] Banned phrasing (§3).

## 2. Space: fill it with content, not air

"Clean" is not the same as empty. AI layouts over-pad and leave dead zones.
- **No dead zone.** No empty band taller than ~25% of the canvas unless it's a photo or the deliberate field around a single statement (P1).
- **If a layout looks empty, scale up the content:** a larger headline, a bigger photo, a tighter grid. Don't add filler elements (eyebrows, rules, icons, taglines) to occupy space.
- **Spacing scale (8px base):**
  - Related elements (label and value, name and role): 4–16px.
  - Elements inside a group: 24–40px.
  - Between groups: 48–80px.
  - The canvas margin (96px) is the largest gap on the page. Nothing inside it should exceed it.
- **One alignment axis per piece.** Default is left-aligned. Center only formal single-column pieces (the P2 roster), and never center body text.
- **Density matches the medium:**
  - A post carries one message and ≤40 words.
  - A slide carries one message and ≤40 words of body.
  - A memo is dense: full paragraphs, tables, no oversized whitespace.

## 3. Copy: write like a person at the fund, not a launch page

**Banned words and phrases** (replace with the plain fact):
- elevate, unlock, empower, unleash, supercharge, level up, transform, revolutionize, reimagine
- journey, ecosystem (as fluff), landscape (as fluff), synergy, leverage (as a verb)
- "game-changer", "cutting-edge", "next-level", "world-class", "premier", "elite", "exclusive", "innovative", "dynamic", "passionate"
- "dive into", "deep dive", "explore the world of", "the future of finance", "where X meets Y"
- "by the numbers", "a look back", "recap" as a headline on its own, "join us for an unforgettable…"
- "don't miss out", "you won't want to miss", "spots are limited" (unless literally true and quantified)

**Banned constructions**
- "It's not X, it's Y" / "not just X, but Y" / "more than just X".
- Adjective triads ("rigorous, collaborative, and driven"). Pick the one that's true.
- Rhetorical-question hooks ("Ready to take the next step?", "The catch?").
- Summary lines that restate what the graphic already says.
- More than one em dash per piece of copy. More than one exclamation mark per line, or any in a plain factual announcement.

**Instead**
- **Headline:** the event or the fact, in ≤5 words. "Interest Meeting." "Applications are open." "Thank you for coming."
- **Details:** what, when, where; then the one reason to care ("Free Chick-fil-A").
- **CTA:** the literal action ("RSVP via link in bio", "Apply by Feb 9").
- **Descriptors:** earn them with a fact. Not "a premier investing club" but "a student-run fund managing a real portfolio".

## 4. Process: how to avoid drifting to the average

1. **Content first.** Write every word, gather the real photos and numbers, *then* pick the primitive. Don't pick a layout and fill it with plausible text.
2. **Start from the master** (`templates/ig-post-master.html`), not from a blank page or a generic "modern" layout.
3. **Subtract pass.** For each element, ask "if I delete this, does the reader lose information?" If not, delete it. Do this before showing anything.
4. **Name-swap test.** Replace "Vertex Fund" with another club's name. If the design still works perfectly, it's generic. Add the specific thing: our photo, our room, our numbers.
5. **Squint test.** Blur your eyes. You should see one dominant element (headline or photo), one secondary element (details), and nothing else competing.
6. **Render and look:** run Visual QA (`SKILL.md` › Visual QA, `scripts/render_check.py`) and inspect every page by eye at full and thumbnail size before calling it done.
7. **Variation comes from content, not chrome.** When making options, vary the primitive, the mode, the photo and the crop. Don't vary by adding new fonts, colors or effects.

## 5. Quick fixes for the most common drifts

| You see | Do instead |
|---|---|
| Eyebrow + headline + subhead stack | Merge into one headline that carries the specific info ("Spring analyst applications are open") |
| Big stats strip as the main visual | Only when the numbers *are* the news and are sourced. Otherwise lead with a photo or statement |
| Three equal cards | A list, a single paragraph, or 2 / 4 / 5 items if that's what's true |
| Everything centered | Left-align; keep center for the formal roster only |
| Empty top half | Enlarge the headline or add the real photo band, not decoration |
| A new font "for contrast" | Use weight (400 vs 500/600) or italic from EB Garamond |
| Hairlines everywhere | Keep the one that separates the masthead or a fact row; delete the rest |
| Clever, abstract headline | The plain event name or fact |
