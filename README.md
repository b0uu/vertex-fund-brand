# vertex-fund-brand

**Looking for a logo, profile picture, banner, colors or photos?** Go to [`brand-assets/`](brand-assets/).

The single source of truth for Vertex Fund's visual identity (University of Maryland · [vertexumd.com](https://vertexumd.com)).

```
vertex-fund-brand/
├── README.md
├── brand-assets/                ← TEAM DOWNLOADS: logos (SVG/PNG), social images, favicons, colors, fonts, photos
├── brand-guidelines.md          ← the manual (read this first)
├── site-contradictions.md       ← where vertexumd.com disagrees with the system (no site changes made)
├── tools/
│   ├── make_logos.py            ← regenerates outlined logo SVGs from the STIX font files
│   ├── build_template.py        ← inlines tokens.css + logo paths into the HTML masters
│   ├── export_assets.py         ← regenerates brand-assets/ from the master SVGs and tokens
│   ├── ig-post-master.src.html  ← social template source
│   └── deck-master.src.html     ← slide template source
└── vertex-brand-guidelines/     ← the Claude Skill (zip this folder to install)
    ├── SKILL.md                 ← core rules + routing (<200 lines)
    ├── references/
    │   ├── social-layouts.md    ← IG / LinkedIn / avatar primitives
    │   ├── pitch-deck-rubric.md ← slides, stock pitches, charts, tables
    │   ├── documents.md         ← memos, recap letters, one-pagers, flyers
    │   └── anti-slop.md         ← guardrails against generic AI-looking design and copy
    ├── templates/
    │   ├── ig-post-master.html  ← approved social layouts, rendered (generated)
    │   └── deck-master.html     ← approved slide layouts, rendered (generated)
    ├── scripts/
    │   └── render_check.py      ← visual QA: screenshots + automated checks (run on every design)
    └── assets/
        ├── tokens.css           ← EVERY color, font, and size. Source of truth.
        └── logo/                ← outlined SVGs: monogram, lockup, avatars
```

## Install the skill
- **Claude.ai:**
  1. Zip the `vertex-brand-guidelines/` folder so the zip contains the folder itself.
  2. Go to Settings → Capabilities → Skills → Upload.
- **Claude Code:** copy or symlink `vertex-brand-guidelines/` into `.claude/skills/`.

## Change something
1. Edit `vertex-brand-guidelines/assets/tokens.css`.
2. Run `python3 tools/build_template.py` and `python3 tools/export_assets.py --photos ../vertex-fund-website/pictures`.
3. Update the matching tables in `brand-guidelines.md` and `SKILL.md`.
4. Bump the version in `brand-guidelines.md`.

To regenerate logos (needs `fonttools`), run:

```
python3 tools/make_logos.py path/to/STIX/fonts vertex-brand-guidelines/assets/logo
```

The fonts are in `vertex-fund-website/branding/fonts/`.
