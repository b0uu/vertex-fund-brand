"""Inline assets/tokens.css and the outlined monogram into the HTML masters.
Run from the repo root:  python3 tools/build_template.py
Builds: templates/ig-post-master.html"""
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SK = os.path.join(ROOT, 'vertex-brand-guidelines')
svg = open(os.path.join(SK, 'assets/logo/vf-monogram-on-light.svg')).read()
vb = [float(x) for x in re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
V, F = re.findall(r' d="([^"]+)"', svg)[:2]
tok = open(os.path.join(SK, 'assets/tokens.css')).read()
COVER = open(os.path.join(ROOT, 'tools/photo-src/cover-crop.b64')).read().strip()

for name in ('ig-post-master',):
    src = open(os.path.join(ROOT, f'tools/{name}.src.html')).read()
    out = (src.replace('/*__TOKENS__*/', '/* ===== Inlined from assets/tokens.css — edit tokens there, then rebuild ===== */\n' + tok)
              .replace('__VB__', ' '.join(f'{x:.2f}' for x in vb)).replace('__V__', V).replace('__F__', F)
              .replace('__AR__', f'{vb[2]:.2f} / {vb[3]:.2f}').replace('__COVER__', COVER))
    assert '__' not in out.replace('__TOKENS__', ''), f'unreplaced placeholder in {name}'
    open(os.path.join(SK, f'templates/{name}.html'), 'w').write(out)
    print(f'wrote templates/{name}.html', len(out), 'bytes')
