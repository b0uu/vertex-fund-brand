#!/usr/bin/env python3
"""Vertex Fund visual QA: render every artboard/slide to PNG and run automated checks.

Usage:
  python3 scripts/render_check.py path/to/design.html [--out qa/] [--selector ".slide, .vf-canvas"]

Writes, per artboard: <out>/<n>.png at full size and <out>/<n>-thumb.png at phone-thumbnail
size, plus <out>/contact-sheet.png. Prints automated findings. The automated checks are a floor,
not a pass: you must still OPEN AND LOOK AT the PNGs (see SKILL.md › Visual QA).

Needs Playwright (python) with a Chromium/Chrome browser. If neither is available it falls back to
headless Chrome's --screenshot for a single full-page image. If no browser exists, it exits non-zero:
report that the design was NOT visually checked.
"""
import argparse, os, shutil, subprocess, sys

ALLOWED_FONTS = ('eb garamond', 'stix two text', 'dm mono', 'ibm plex mono', 'georgia')  # georgia: slide decks only
MIN_PX = {'.vf-canvas': 20, '.slide': 14.6}  # 20px on 1080 social canvases; 11pt (14.6px) on slides

CHECK_JS = r"""
(sel) => {
  const out = [];
  const boards = [...document.querySelectorAll(sel)];
  const acr = /^(?:[A-Z]{2,5}\d*[A-Z]*E?|Q[1-4]|FY\d{2}E?|\[.*\])$/;  // tickers, acronyms, FY26E, [placeholders]
  boards.forEach((b, i) => {
    const br = b.getBoundingClientRect();
    const isSlide = b.matches('.slide');
    const minPx = isSlide ? 14.6 : 20;
    b.querySelectorAll('*').forEach(el => {
      const cs = getComputedStyle(el);
      if (cs.display === 'none' || cs.visibility === 'hidden') return;
      const r = el.getBoundingClientRect();
      const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
      const tag = el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.split(' ')[0] : '');
      // 1. overflow: text clipped inside its own box
      if (hasText && (el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 1) && cs.overflow !== 'visible')
        out.push([i, 'overflow', tag, el.textContent.trim().slice(0, 40)]);
      // 2. out of bounds: element pokes outside the artboard (watermarks are allowed to bleed)
      if (!el.closest('.watermark, .photo-band') && r.width > 0 &&
          (r.left < br.left - 1 || r.right > br.right + 1 || r.top < br.top - 1 || r.bottom > br.bottom + 1))
        out.push([i, 'out-of-bounds', tag, (el.textContent || '').trim().slice(0, 40)]);
      if (!hasText) return;
      const txt = [...el.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent).join(' ').trim();
      // 3. fonts
      const fam = cs.fontFamily.split(',')[0].replace(/["']/g, '').trim().toLowerCase();
      if (!%ALLOWED%.includes(fam)) out.push([i, 'font', tag, fam + ' :: ' + txt.slice(0, 30)]);
      // 4. minimum size
      if (parseFloat(cs.fontSize) < minPx - 0.1) out.push([i, 'too-small', tag, cs.fontSize + ' :: ' + txt.slice(0, 30)]);
      // 5. all caps
      if (cs.textTransform === 'uppercase' || cs.fontVariantCaps !== 'normal') out.push([i, 'all-caps', tag, txt.slice(0, 40)]);
      const words = txt.replace(/UNIVERSITY OF MARYLAND/g, '').split(/\s+/).filter(w => /[A-Z]{4,}/.test(w) && !acr.test(w.replace(/[^\w\[\]]/g, '')));  // the lockup subline is the one allowed exception
      if (words.length >= 2) out.push([i, 'all-caps', tag, txt.slice(0, 40)]);
      // 6. monospace as a focal element
      if (fam.includes('mono') && parseFloat(cs.fontSize) > (isSlide ? 17.4 : 24) && !el.closest('table'))
        out.push([i, 'mono-focal', tag, txt.slice(0, 40)]);
    });
    // 7. dead zone: largest empty horizontal band
    const rows = new Array(Math.ceil(br.height)).fill(false);
    b.querySelectorAll('*').forEach(el => {
      if (el.closest('.photo-band, .watermark')) { const r = el.getBoundingClientRect(); for (let y = Math.max(0, r.top - br.top | 0); y < Math.min(rows.length, r.bottom - br.top); y++) rows[y] = true; return; }
      const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
      const visual = ['IMG', 'svg', 'SVG'].includes(el.tagName) || el.classList.contains('slot') || el.classList.contains('headshot');
      if (!hasText && !visual) return;
      const r = el.getBoundingClientRect();
      for (let y = Math.max(0, r.top - br.top | 0); y < Math.min(rows.length, r.bottom - br.top); y++) rows[y] = true;
    });
    let run = 0, best = 0; rows.forEach(f => { run = f ? 0 : run + 1; best = Math.max(best, run); });
    const pct = Math.round(100 * best / rows.length);
    if (pct > 25) out.push([i, 'dead-zone', 'board', pct + '% of the height is empty in one band']);
  });
  return {count: boards.length, findings: out, fonts: [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family)};
}
""".replace('%ALLOWED%', str(list(ALLOWED_FONTS)))


def with_playwright(html, out, sel):
    from playwright.sync_api import sync_playwright
    from PIL import Image
    exe = next((p for p in (shutil.which('google-chrome'), shutil.which('chromium'), shutil.which('chromium-browser')) if p), None)
    with sync_playwright() as p:
        kw = {'args': ['--no-sandbox', '--allow-file-access-from-files']}
        if exe: kw['executable_path'] = exe
        b = p.chromium.launch(**kw)
        pg = b.new_page(viewport={'width': 2200, 'height': 1600}, device_scale_factor=1)
        pg.goto('file://' + os.path.abspath(html)); pg.wait_for_timeout(1500)
        res = pg.evaluate(CHECK_JS, sel)
        files = []
        for i, el in enumerate(pg.query_selector_all(sel)):
            f = os.path.join(out, f'{i + 1:02d}.png'); el.screenshot(path=f); files.append(f)
        b.close()
    tiles = [Image.open(f).convert('RGB') for f in files]
    for f, t in zip(files, tiles):
        w = 360; t.resize((w, round(t.height * w / t.width))).save(f.replace('.png', '-thumb.png'))
    if tiles:
        H = max(t.height for t in tiles); W = sum(t.width for t in tiles) + 40 * (len(tiles) + 1)
        sheet = Image.new('RGB', (W, H + 80), (221, 216, 207)); x = 40
        for t in tiles: sheet.paste(t, (x, 40)); x += t.width + 40
        sheet.save(os.path.join(out, 'contact-sheet.png'))
    return res, files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('html'); ap.add_argument('--out', default='qa'); ap.add_argument('--selector', default='.slide, .vf-canvas')
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    try:
        res, files = with_playwright(a.html, a.out, a.selector)
    except Exception as e:
        exe = shutil.which('google-chrome') or shutil.which('chromium') or shutil.which('chromium-browser')
        if not exe:
            print(f'NO BROWSER AVAILABLE ({e}). The design was NOT visually checked. Say so explicitly.'); sys.exit(2)
        f = os.path.join(a.out, 'full-page.png')
        subprocess.run([exe, '--headless=new', '--no-sandbox', '--hide-scrollbars', '--window-size=2200,8000',
                        f'--screenshot={os.path.abspath(f)}', 'file://' + os.path.abspath(a.html)], capture_output=True)
        print(f'Playwright unavailable ({e}); wrote one full-page screenshot: {f}. Automated checks skipped. Inspect it visually.')
        return
    print(f'Rendered {res["count"]} artboard(s) → {a.out}/  (full size, -thumb.png, contact-sheet.png)')
    fams = sorted({f.lower() for f in res['fonts']})
    missing = [f for f in ('eb garamond',) if f not in fams]
    if missing:
        print(f'! Brand fonts did not load ({", ".join(missing)}). Screenshots use fallbacks; spacing and line breaks may differ from the real thing.')
    if not res['findings']:
        print('Automated checks: no findings. Now open every PNG and inspect it (SKILL.md › Visual QA).')
    else:
        print(f'Automated checks: {len(res["findings"])} finding(s). Fix, rebuild, and re-run:')
        for i, kind, tag, info in res['findings']:
            print(f'  artboard {i + 1:02d}  {kind:<14} {tag:<22} {info}')
        sys.exit(1)


if __name__ == '__main__':
    main()
