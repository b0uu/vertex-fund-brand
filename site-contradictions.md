# vertexumd.com vs. the brand system: known contradictions

Audited against `b0uu/vertex-fund-website` @ `b605a14` (Nov 25, 2026). **No site changes have been made.** This is a to-do list for whenever the site is next touched, ordered by visibility.

The site is the *origin* of the palette (`--white`, `--off`, `--ink`, `--ink-s`, `--ink-m`, `--red`, `--gold`, `--gold-d` map 1:1 onto the `--vf-*` tokens). Most of it already follows the "gold = identity, red = signal" rule: the nav *f* is gold, and Apply links and member roles are red. The conflicts are below.

## High visibility

| # | Where | What it does | Brand rule | Suggested fix |
|---|---|---|---|---|
| 1 | `branding/og-image.svg/.png` (link preview for every share), `branding/social/linkedin-cover-*.svg`, `vertex-profile-*.svg`, `vertex-social-post-1080.svg` | Red *f* and red "Fund" on ink | Gold is identity; red on ink is only 2.7:1 | Re-export with `--vf-gold` (`#D6A72A`) for the *f* and "Fund". Ready-made avatars: `assets/logo/vf-avatar-ink-1080.svg` |
| 2 | Same SVGs, plus `favicon.svg` / `favicon-red.svg` | The logo is **live text** (`<text>` + `@font-face`). Favicons ask for Georgia, and the others fall back to Georgia if the TTF doesn't load (GitHub previews, many uploaders) | The mark must be outlined | Swap in the outlined `assets/logo/*.svg` paths |
| 3 | `favicon-red.svg` (unused but in the repo) | Red *f* on ink | Gold identity | Delete, or regenerate in gold |
| 4 | `index.html` `.apply-cta` | **Libre Baskerville** 700, uppercase, tracked | EB Garamond everywhere; no all caps | EB Garamond 500, sentence case, red |

## Medium

| # | Where | What it does | Brand rule | Suggested fix |
|---|---|---|---|---|
| 5 | `index.html` `.split-media-muted img`, `.exhibit-mat` | Large soft drop shadows (`0 22px 60px`, `0 28px 72px`) | No drop shadows | Remove. Use a 1px `--rule` border or the paper-2 mat alone |
| 6 | `index.html` `.split-media-muted img` | `grayscale(18%) sepia(8%)` photo filter | Photos are untinted full colour, or 100% grayscale in a gold photo band | Remove the filter, or commit to one documented treatment |
| 7 | `#page-transition` bar | index uses gold-deep/white/ink stripes; team uses red/gold/ink. The two pages disagree | One accent per element; pages consistent | A single 3px gold-deep bar on both pages |
| 8 | `.footer-l`, `.member-detail`, `.logo-sub`, `.page-tag` | Small text in `--ink-m` `#8C867E` on `#FAFAF8` = 3.45:1 | Small text ≥4.5:1 | Use `--vf-ink-3` `#6E685F` (5.3:1) |
| 9 | `team.html` `.member-linkedin` | DM Mono at 0.58rem (≈9px) for a link | Mono is for table figures only; minimum readable sizes | EB Garamond italic, ≥0.85rem, `--vf-ink-3` |
| 10 | Headings and stats never set `font-variant-numeric`, so EB Garamond may show old-style figures ("2026", "$5,000" bounce) | — | Lining figures wherever numbers matter | `font-variant-numeric: lining-nums` on headings and stats |

## Low / housekeeping

| # | Where | Note |
|---|---|---|
| 11 | Hard-coded colors | `#2A2520` (hero placeholder), `rgba(255,255,255,…)` nav text (should derive from `--white` `#FAFAF8`), `rgba(196,154,34,.34)` mat border (an off-token gold) |
| 12 | `html designs/vertex-fund-typography.html` | An old exploration with a different palette (navy, green, UMD red/gold, Inter, Cormorant). Mark it as archived so nobody samples from it |
| 13 | `branding/social/new-exec-2026.html` | `--ink-s: #5E5850` differs from the site's `#46403A`. Otherwise on-brand: gilt frame, gold-deep *f*, EB Garamond |
| 14 | Token names | The site's names (`--white`, `--ink-m`) differ from the brand's (`--vf-paper`, `--vf-stone`). Values match. When the site is refactored, import `tokens.css` and alias the old names to the new |
