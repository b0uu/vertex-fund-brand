"""Regenerate brand-assets/ (the team download kit) from the master files.
Run from the repo root:  python3 tools/export_assets.py [--photos path/to/vertex-fund-website/pictures]

Sources of truth (never edit the exports by hand):
  vertex-brand-guidelines/assets/logo/*.svg   → logos, social images, favicons
  vertex-brand-guidelines/assets/tokens.css   → palette
Needs: Pillow, Playwright + Chrome/Chromium (for SVG → PNG).
"""
import argparse, os, re, shutil, glob
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(ROOT, 'vertex-brand-guidelines/assets/logo')
TOK = os.path.join(ROOT, 'vertex-brand-guidelines/assets/tokens.css')
OUT = os.path.join(ROOT, 'brand-assets')
INK, PAPER, GOLD, FRAME = '#14120E', '#FAFAF8', '#D6A72A', 'rgba(250,250,248,0.08)'


def svg_parts(name):
    s = open(os.path.join(LOGO, name)).read()
    vb = [float(x) for x in re.search(r'viewBox="([^"]+)"', s).group(1).split()]
    inner = re.search(r'</title>(.*)</svg>', s, re.S).group(1)
    return vb, inner


def place(name, x, y, w):
    """Nest an outlined logo SVG at (x, y) with width w; returns markup and height."""
    vb, inner = svg_parts(name)
    h = w * vb[3] / vb[2]
    return (f'<svg x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" viewBox="{" ".join(map(str, vb))}">{inner}</svg>', h)


def canvas(w, h, bg, body, frame=None):
    fr = f'<rect x="{frame}" y="{frame}" width="{w - 2 * frame}" height="{h - 2 * frame}" fill="none" stroke="{FRAME}" stroke-width="2"/>' if frame else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Vertex Fund">'
            f'<title>Vertex Fund</title><rect width="{w}" height="{h}" fill="{bg}"/>{fr}{body}</svg>\n')


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True); open(path, 'w').write(text)


def render(jobs):
    """jobs: list of (svg_path, png_path, width, height-or-None). Transparent where the SVG is."""
    from playwright.sync_api import sync_playwright
    exe = shutil.which('google-chrome') or shutil.which('chromium') or shutil.which('chromium-browser')
    with sync_playwright() as p:
        kw = {'args': ['--no-sandbox', '--allow-file-access-from-files']}
        if exe: kw['executable_path'] = exe
        b = p.chromium.launch(**kw); pg = b.new_page()
        for src, dst, w, h in jobs:
            if h is None:
                vb = [float(x) for x in re.search(r'viewBox="([^"]+)"', open(src).read()).group(1).split()]
                h = round(w * vb[3] / vb[2])
            pg.set_viewport_size({'width': w, 'height': h})
            svg = re.sub(r'<svg ', f'<svg style="display:block;width:{w}px;height:{h}px" ', open(src).read(), count=1)
            svg = re.sub(r'(<svg style="[^"]*")([^>]*?) width="[^"]*" height="[^"]*"', r'\1\2', svg, count=1)
            pg.set_content(f'<html><body style="margin:0;background:transparent">{svg}</body></html>')
            pg.wait_for_timeout(150)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            pg.screenshot(path=dst, omit_background=True, clip={'x': 0, 'y': 0, 'width': w, 'height': h})
        b.close()


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--photos', default=None); a = ap.parse_args()
    for sub in ('logos', 'social', 'favicon', 'colors'):
        shutil.rmtree(os.path.join(OUT, sub), ignore_errors=True)
    jobs = []

    # ---- logos: SVG copies + transparent PNGs ----
    for f in sorted(glob.glob(os.path.join(LOGO, 'vf-*.svg'))):
        n = os.path.basename(f)[:-4]
        if n.startswith('vf-avatar'): continue
        d = os.path.join(OUT, 'logos', 'monogram' if 'monogram' in n else 'lockup')
        os.makedirs(d, exist_ok=True); shutil.copy(f, os.path.join(d, n + '.svg'))
        for w in (1024, 2048):
            jobs.append((f, os.path.join(d, f'{n}-{w}w.png'), w, None))

    # ---- social ----
    S = os.path.join(OUT, 'social')
    for mode, bg, logo in (('ink', INK, 'vf-monogram-on-dark.svg'), ('paper', PAPER, 'vf-monogram-on-light.svg')):
        W = 1080; vb, _ = svg_parts(logo); mw = W * 0.5; mh = mw * vb[3] / vb[2]
        m, _ = place(logo, (W - mw) / 2, (W - mh) / 2, mw)
        write(os.path.join(S, f'profile-avatar-{mode}.svg'), canvas(W, W, bg, m))
        for px in (400, 1080):
            jobs.append((os.path.join(S, f'profile-avatar-{mode}.svg'), os.path.join(S, f'profile-avatar-{mode}-{px}.png'), px, px))
    # LinkedIn personal banner: left ~480px is covered by the profile photo → lockup on the right
    l, h = place('vf-lockup-on-dark.svg', 0, 0, 640); l, _ = place('vf-lockup-on-dark.svg', 1584 - 96 - 640, (396 - h) / 2, 640)
    write(os.path.join(S, 'linkedin-banner-1584x396.svg'), canvas(1584, 396, INK, l, frame=40))
    # LinkedIn company page cover: logo overlaps the left ~300px → lockup right-aligned
    l, h = place('vf-lockup-on-dark.svg', 0, 0, 380); l, _ = place('vf-lockup-on-dark.svg', 1128 - 64 - 380, (191 - h) / 2, 380)
    write(os.path.join(S, 'linkedin-company-cover-1128x191.svg'), canvas(1128, 191, INK, l))
    # Link preview (Open Graph): centered lockup
    l, h = place('vf-lockup-on-dark.svg', 0, 0, 760); l, _ = place('vf-lockup-on-dark.svg', (1200 - 760) / 2, (630 - h) / 2, 760)
    write(os.path.join(S, 'link-preview-1200x630.svg'), canvas(1200, 630, INK, l, frame=48))
    for n, w, h in (('linkedin-banner-1584x396', 1584, 396), ('linkedin-company-cover-1128x191', 1128, 191), ('link-preview-1200x630', 1200, 630)):
        jobs.append((os.path.join(S, n + '.svg'), os.path.join(S, n + '.png'), w, h))

    # ---- favicon ----
    F = os.path.join(OUT, 'favicon'); vb, _ = svg_parts('vf-monogram-on-dark.svg'); mw = 64 * 0.78; mh = mw * vb[3] / vb[2]
    m, _ = place('vf-monogram-on-dark.svg', (64 - mw) / 2, (64 - mh) / 2, mw)
    write(os.path.join(F, 'favicon.svg'), canvas(64, 64, INK, m))
    for px, n in ((32, 'favicon-32.png'), (180, 'apple-touch-icon-180.png'), (512, 'icon-512.png')):
        jobs.append((os.path.join(F, 'favicon.svg'), os.path.join(F, n), px, px))

    render(jobs)

    # ---- colors: swatch sheet + plain list (parsed from tokens.css) ----
    C = os.path.join(OUT, 'colors'); os.makedirs(C, exist_ok=True)
    toks = re.findall(r'--(vf-[a-z0-9-]+):\s*(#[0-9A-Fa-f]{6});\s*/\*\s*(.*?)\s*\*/', open(TOK).read())
    lines = ['Vertex Fund palette (generated from vertex-brand-guidelines/assets/tokens.css)', '']
    for name, hx, note in toks:
        r, g, b = (int(hx[i:i + 2], 16) for i in (1, 3, 5))
        lines.append(f'{name:<16} {hx.upper()}  rgb({r}, {g}, {b})  {note.split("(")[0].strip()}')
    write(os.path.join(C, 'palette.txt'), '\n'.join(lines) + '\n')
    sw = ''.join(f'<div style="width:260px"><div style="height:150px;background:{hx};border:1px solid rgba(20,18,14,.12)"></div>'
                 f'<div style="font:600 18px Georgia;margin-top:10px;color:#14120E">{name.replace("vf-", "")}</div>'
                 f'<div style="font:15px Menlo,monospace;color:#46403A;margin-top:4px">{hx.upper()}</div></div>' for name, hx, _ in toks)
    html = os.path.join(C, '_palette.html')
    write(html, f'<html><body style="margin:0;padding:48px;background:#FAFAF8;width:1184px;display:flex;flex-wrap:wrap;gap:36px 32px">{sw}</body></html>')
    from playwright.sync_api import sync_playwright
    exe = shutil.which('google-chrome') or shutil.which('chromium')
    with sync_playwright() as p:
        b = p.chromium.launch(**({'executable_path': exe} if exe else {}), args=['--no-sandbox']); pg = b.new_page(viewport={'width': 1280, 'height': 800})
        pg.goto('file://' + html); pg.screenshot(path=os.path.join(C, 'palette.png'), full_page=True); b.close()
    os.remove(html)

    # ---- photos (optional source: the website repo's pictures/) ----
    if a.photos:
        P = os.path.join(OUT, 'photos'); shutil.rmtree(P, ignore_errors=True)
        events = {'interest-meeting.webp': 'interest-meeting-2026-11-18.jpg', 'image-5.webp': 'members-working-session.jpg',
                  'vf_image_1.webp': 'team-outside-smith-school.jpg'}
        for src, dst in events.items():
            im = Image.open(os.path.join(a.photos, src)).convert('RGB'); im.thumbnail((2400, 2400))
            os.makedirs(os.path.join(P, 'events'), exist_ok=True); im.save(os.path.join(P, 'events', dst), quality=88)
        full = os.path.join(ROOT, 'tools/photo-src/interest-meeting-full-room.jpg')
        if os.path.exists(full): shutil.copy(full, os.path.join(P, 'events', 'interest-meeting-full-room.jpg'))
        for src in sorted(glob.glob(os.path.join(a.photos, '*_headshot.webp'))):
            n = os.path.basename(src).replace('_headshot.webp', '')
            im = Image.open(src).convert('RGB'); im.thumbnail((1000, 1000))
            os.makedirs(os.path.join(P, 'headshots'), exist_ok=True); im.save(os.path.join(P, 'headshots', f'{n}.jpg'), quality=90)
    print('brand-assets/ regenerated')


if __name__ == '__main__':
    main()
