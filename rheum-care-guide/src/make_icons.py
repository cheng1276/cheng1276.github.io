"""Make the site icons and the link-preview image.

Usage:
  python3 src/make_icons.py [--font-dir DIR]

Writes, next to index.html:
  icon.svg                 browser-tab icon (vector)
  favicon.ico              16, 32 and 48 px, for browsers and search engines that do not use the SVG
  apple-touch-icon.png     180 px, for 「加入主畫面」 on iPhone and iPad (square; iOS rounds the corners)
  icon-192.png, icon-512.png, icon-maskable-512.png   for Android, listed in site.webmanifest
  site.webmanifest
  og.png                   1200 x 630 link preview, screenshotted from src/og.html (rebuilt here from template.html,
                           so the pictograms and colours always match the site)

The mark: a clinic handout card with the site's colour-coded index tabs, and a knee joint on the card.
Rendering uses Playwright with Chromium. The preview image uses the site's display font, Huninn, loaded from
Google Fonts; without internet access, pass --font-dir with a copy of the @fontsource/huninn npm package
(the folder that holds index.css and files/), and the font requests are answered from there.
"""
import asyncio
import base64
import io
import json
import pathlib
import re
import sys

from PIL import Image
from playwright.async_api import async_playwright

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
TEMPLATE = HERE / 'template.html'
OG_HTML = HERE / 'og.html'

TEAL = '#0c6a5e'      # --brand
PAPER = '#f3f5f4'     # --paper
TABS = ('#f0a64a', '#f08aa6', '#8aaaf0')  # gout, urticaria and RA hues (the brighter dark-theme shades)
NAME = '風濕免疫生活照護圖解'
SHORT_NAME = '生活照護圖解'


def mark_body(cy=250):
    """Card, tabs and knee joint on a 512 x 512 grid, without the background."""
    cx = 236
    tabs = ''.join(f'<rect x="322" y="{y}" width="84" height="60" rx="18" fill="{c}"/>'
                   for y, c in zip((124, 204, 284), TABS))
    card = '<rect x="106" y="88" width="260" height="336" rx="44" fill="#fff"/>'
    t = cy - 104  # femur: rounded shaft that flares into the knee end
    femur = (f'M{cx-26} {t} A26 26 0 0 1 {cx+26} {t} V{t+54} C{cx+26} {t+70} {cx+62} {t+70} {cx+62} {t+94} '
             f'Q{cx+62} {t+118} {cx+38} {t+118} H{cx-38} Q{cx-62} {t+118} {cx-62} {t+94} '
             f'C{cx-62} {t+70} {cx-26} {t+70} {cx-26} {t+54} Z')
    b = t + 136  # tibia: flat plateau below the joint space, narrowing into the shaft
    tibia = (f'M{cx-60} {b+12} Q{cx-60} {b} {cx-48} {b} H{cx+48} Q{cx+60} {b} {cx+60} {b+12} '
             f'C{cx+60} {b+30} {cx+25} {b+34} {cx+25} {b+52} V{b+84} A25 25 0 0 1 {cx-25} {b+84} V{b+52} '
             f'C{cx-25} {b+34} {cx-60} {b+30} {cx-60} {b+12} Z')
    joint = f'<path d="{femur}" fill="{TEAL}"/><path d="{tibia}" fill="{TEAL}"/>'
    return tabs + card + joint


def mark_svg(kind='rounded'):
    """rounded: transparent corners (tab icon, Android 'any'); square: full bleed (iOS);
    maskable: full bleed with the mark inside the central safe circle (Android adaptive icons)."""
    if kind == 'rounded':
        body = f'<rect width="512" height="512" rx="112" fill="{TEAL}"/>' + mark_body()
    elif kind == 'square':
        body = f'<rect width="512" height="512" fill="{TEAL}"/>' + mark_body()
    elif kind == 'maskable':
        body = (f'<rect width="512" height="512" fill="{TEAL}"/>'
                f'<g transform="translate(256 256) scale(0.8) translate(-256 -256)">{mark_body()}</g>')
    else:
        raise ValueError(kind)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">{body}</svg>'


def mark16_svg():
    """The same mark drawn on a 16-pixel grid, so the 16 px favicon stays sharp."""
    tabs = ''.join(f'<rect x="11" y="{y}" width="3" height="2" fill="{c}"/>' for y, c in zip((3, 6, 9), TABS))
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" shape-rendering="crispEdges">'
            f'<rect width="16" height="16" rx="3" fill="{TEAL}" shape-rendering="auto"/>{tabs}'
            '<rect x="2" y="2" width="10" height="12" fill="#fff"/>'
            f'<g fill="{TEAL}"><rect x="6" y="4" width="2" height="2"/><rect x="5" y="6" width="4" height="2"/>'
            '<rect x="5" y="9" width="4" height="1"/><rect x="6" y="10" width="2" height="3"/></g></svg>')


def _between(text, start, end, start_at=0):
    i = text.index(start, start_at)
    j = text.index(end, i)
    return text[i:j + len(end)]


# Nine tiles, one per page, in the site's tab colours.
GRID = [('gout', 'gout-food'), ('urticaria', 'urticaria-diary'), ('ra', 'ra-hands'),
        ('axspa', 'axspa-spine'), ('sle', 'sle-sun'), ('sjogren', 'sjogren-eyes'),
        ('oa', 'oa-exercise'), ('osteoporosis', 'osteoporosis-calcium-vitamin-d'), ('common', 'common-activity')]
PILLS = [('gout', '痛風'), ('urticaria', '慢性蕁麻疹'), ('ra', '類風濕性關節炎'), ('axspa', '僵直性脊椎炎'),
         ('sle', '紅斑性狼瘡'), ('sjogren', '乾燥症'), ('oa', '退化性關節炎'), ('osteoporosis', '骨質疏鬆症')]


def build_og_html():
    t = TEMPLATE.read_text(encoding='utf-8')
    root = _between(t, ':root{', '\n}\n')                      # light-theme colour tokens and fonts
    hues = '\n'.join(re.findall(r'^\[data-d="[a-z]+"\]\{--hue:[^\n]*$', t, re.M))
    pic = '\n'.join(re.findall(r'^\.pic[ {][^\n]*$', t, re.M))
    js = t[t.index('const WALK'):]
    js = js[:js.index('\n  };', js.index('const ICONS')) + len('\n  };')]
    for d, key in GRID:
        if f"'{key}':" not in js:
            sys.exit(f'og grid: icon {key} not found in template.html')
    pills = ''.join(f'<span class="og-pill" data-d="{d}">{name}</span>' for d, name in PILLS)
    mark = mark_svg('rounded').replace('<svg ', '<svg class="og-mark" aria-hidden="true" ', 1)
    css = f"""{root}
{hues}
*,*::before,*::after{{box-sizing:border-box}}
html,body{{margin:0;width:1200px;height:630px;overflow:hidden}}
body{{background:var(--paper);color:var(--ink);font-family:var(--f-body)}}
{pic}
.og{{width:1200px;height:630px;padding:46px 72px;display:grid;grid-template-columns:1fr 360px;gap:44px;align-items:center}}
.og-brand{{display:flex;align-items:center;gap:16px}}
.og-mark{{width:64px;height:64px;flex:none;display:block}}
.og-e{{font-family:var(--f-display);font-size:32px;color:var(--brand);letter-spacing:.08em}}
.og-t{{font-family:var(--f-display);font-size:104px;line-height:1.15;margin:18px 0 14px;font-weight:400;white-space:nowrap}}
.og-s{{font-size:30px;color:var(--ink-2);line-height:1.5}}
.og-pills{{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}}
.og-pill{{display:inline-flex;align-items:center;gap:10px;padding:6px 18px;border-radius:999px;background:var(--sheet);
  border:2px solid var(--rule);font-family:var(--f-display);font-size:25px;line-height:1.5;color:var(--ink)}}
.og-pill::before{{content:"";width:14px;height:14px;border-radius:50%;background:var(--hue)}}
.og-x{{font-size:24px;color:var(--ink-2);margin-top:16px}}
.og-grid{{display:grid;grid-template-columns:repeat(3,108px);gap:18px}}
.og-grid .pic{{width:108px;height:108px;border-radius:24px}}
.og-grid .pic svg{{width:84px;height:84px}}"""
    html = f"""<!doctype html>
<!-- Layout for og.png, the link-preview image. Generated by src/make_icons.py from template.html; edit there. -->
<html lang="zh-Hant"><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Huninn&display=block">
<style>
{css}
</style></head><body><div class="og">
<div><div class="og-brand">{mark}<div class="og-e">風濕免疫科衛教</div></div>
<div class="og-t">生活照護圖解</div>
<div class="og-s">每則建議都附上出處與建議強度</div>
<div class="og-pills">{pills}</div>
<div class="og-x">也說明：共通照護、看懂健檢報告、治療期間防感染</div></div>
<div class="og-grid" id="g"></div></div>
<script>
{js}
const GRID = {json.dumps(GRID)};
document.getElementById('g').innerHTML = GRID.map(([d, id]) =>
  `<div class="pic" data-d="${{d}}"><svg viewBox="0 0 96 96">${{ICONS[id]}}</svg></div>`).join('');
</script></body></html>
"""
    OG_HTML.write_text(html, encoding='utf-8')


def _font_routes(font_dir):
    """Answer the Google Fonts requests for Huninn from a local @fontsource/huninn package."""
    font_dir = pathlib.Path(font_dir)
    css = (font_dir / 'index.css').read_text(encoding='utf-8')
    css = re.sub(r"url\(\./files/([^)]+)\)", r"url(https://fonts.gstatic.com/local-huninn/\1)", css)

    async def handle(route):
        url = route.request.url
        if url.startswith('https://fonts.googleapis.com/css2'):
            await route.fulfill(status=200, content_type='text/css', body=css,
                                headers={'Access-Control-Allow-Origin': '*'})
        elif url.startswith('https://fonts.gstatic.com/local-huninn/'):
            name = url.rsplit('/', 1)[1]
            path = font_dir / 'files' / name
            if not path.is_file() or path.parent.resolve() != (font_dir / 'files').resolve():
                await route.fulfill(status=404, body='')
                return
            ctype = 'font/woff2' if name.endswith('.woff2') else 'font/woff'
            await route.fulfill(status=200, content_type=ctype, body=path.read_bytes(),
                                headers={'Access-Control-Allow-Origin': '*'})
        else:
            await route.abort()
    return handle


async def render(font_dir=None):
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        async def svg_png(svg, size):
            page = await browser.new_page(viewport={'width': size, 'height': size}, device_scale_factor=1)
            uri = 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode('utf-8')).decode('ascii')
            await page.set_content(f'<html><body style="margin:0;background:transparent">'
                                   f'<img src="{uri}" width="{size}" height="{size}" style="display:block"></body></html>')
            await page.wait_for_function('document.images[0].complete')
            png = await page.screenshot(omit_background=True, clip={'x': 0, 'y': 0, 'width': size, 'height': size})
            await page.close()
            return Image.open(io.BytesIO(png)).convert('RGBA')

        rounded, square, maskable = mark_svg('rounded'), mark_svg('square'), mark_svg('maskable')
        (ROOT / 'icon.svg').write_text(rounded + '\n', encoding='utf-8')
        (await svg_png(square, 180)).convert('RGB').save(ROOT / 'apple-touch-icon.png', optimize=True)
        (await svg_png(rounded, 192)).save(ROOT / 'icon-192.png', optimize=True)
        (await svg_png(rounded, 512)).save(ROOT / 'icon-512.png', optimize=True)
        (await svg_png(maskable, 512)).convert('RGB').save(ROOT / 'icon-maskable-512.png', optimize=True)
        ico = [await svg_png(rounded, 48), await svg_png(rounded, 32), await svg_png(mark16_svg(), 16)]
        ico[0].save(ROOT / 'favicon.ico', format='ICO', sizes=[(48, 48), (32, 32), (16, 16)], append_images=ico[1:])

        build_og_html()
        page = await browser.new_page(viewport={'width': 1200, 'height': 630}, device_scale_factor=1)
        if font_dir:
            await page.route('https://fonts.googleapis.com/**', _font_routes(font_dir))
            await page.route('https://fonts.gstatic.com/**', _font_routes(font_dir))
        await page.goto(OG_HTML.as_uri())
        await page.evaluate('document.fonts.ready')
        loaded = await page.evaluate("[...document.fonts].filter(f => f.family.replace(/[\"']/g, '') === 'Huninn'"
                                     " && f.status === 'loaded').length")
        if not loaded:
            sys.exit('og.png: the Huninn font did not load (no internet? pass --font-dir)')
        await page.screenshot(path=str(ROOT / 'og.png'))
        await browser.close()

    manifest = {
        'name': NAME, 'short_name': SHORT_NAME, 'lang': 'zh-Hant-TW',
        'start_url': './', 'scope': './', 'display': 'browser',
        'background_color': PAPER, 'theme_color': TEAL,
        'icons': [{'src': 'icon-192.png', 'sizes': '192x192', 'type': 'image/png'},
                  {'src': 'icon-512.png', 'sizes': '512x512', 'type': 'image/png'},
                  {'src': 'icon-maskable-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'}],
    }
    (ROOT / 'site.webmanifest').write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('wrote icon.svg, favicon.ico, apple-touch-icon.png, icon-192.png, icon-512.png, icon-maskable-512.png, '
          'site.webmanifest, src/og.html, og.png')


if __name__ == '__main__':
    args = sys.argv[1:]
    asyncio.run(render(args[args.index('--font-dir') + 1] if '--font-dir' in args else None))
