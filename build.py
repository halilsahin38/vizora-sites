"""Genereert alle HTML-pagina's van vizoradigital.nl.

Gebruik:  python3 build.py
Inhoud per pagina staat in src/pages/<naam>.py (functie render()),
gedeelde onderdelen in src/core.py. Stijl in assets/css/, gedrag in assets/js/.
"""
import base64
import hashlib
import importlib
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT / "src"))
import core  # noqa: E402

# (bestand, module). Pagina's waarvan de module nog niet bestaat, worden overgeslagen.
PAGES = [
    ("index.html", "home"),
    ("diensten.html", "diensten"),
    ("prijzen.html", "prijzen"),
    ("werkwijze.html", "werkwijze"),
    ("over-ons.html", "over_ons"),
    ("contact.html", "contact"),
    ("404.html", "notfound"),
]

# Cache-busting: ?v=<korte hash van de inhoud> achter elke CSS- en JS-link,
# zodat terugkerende bezoekers na een wijziging nooit een oude versie uit hun cache gebruiken.
_versions = {}


def version(path):
    if path not in _versions:
        _versions[path] = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()[:10]
    return _versions[path]


def bust(html):
    return re.sub(r'((?:href|src)=")(/?)(assets/[^"?]+\.(?:css|js))"',
                  lambda m: f'{m[1]}{m[2]}{m[3]}?v={version(m[3])}"', html)


built = []
for file, mod in PAGES:
    if not (ROOT / "src" / "pages" / f"{mod}.py").exists():
        continue
    html = bust(importlib.import_module(f"pages.{mod}").render())
    (ROOT / file).write_text(html, encoding="utf-8")
    built.append(file)

(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {core.SITE}/sitemap.xml\n")
urls = "".join(f"  <url><loc>{core.SITE}/{'' if p == 'index.html' else p.removesuffix('.html')}</loc></url>\n"
               for p, _ in PAGES if p != "404.html")
(ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')

# meldpunt voor beveiligingsproblemen (RFC 9116); verloopt na een jaar, dus jaarlijks opnieuw bouwen
(ROOT / ".well-known").mkdir(exist_ok=True)
(ROOT / ".well-known" / "security.txt").write_text(
    f"Contact: mailto:{core.MAIL}\nExpires: {core.SECURITY_EXPIRES}\nPreferred-Languages: nl, en\nCanonical: {core.SITE}/.well-known/security.txt\n")

# ---------- online zetten (Cloudflare Pages) ----------
# Build-instellingen in Cloudflare: build command "python3 build.py", output directory "dist".
# In dist/ komt alleen de website zelf; bronbestanden (src/, tools/, concepts/, build.py, ...) gaan niet online.
csp_hash = base64.b64encode(hashlib.sha256(core.INLINE_JS.encode()).digest()).decode()
CSP = "default-src 'self'; script-src 'self' 'sha256-{hash}'; style-src 'self' 'unsafe-inline'; font-src 'self'; img-src 'self' data:; connect-src 'self'; media-src 'self'; manifest-src 'self'; worker-src 'none'; frame-src 'none'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'; object-src 'none'; upgrade-insecure-requests".replace("{hash}", csp_hash)
HEADERS = [
    ("Content-Security-Policy", CSP),
    ('Strict-Transport-Security', 'max-age=63072000; includeSubDomains; preload'),
    ('X-Content-Type-Options', 'nosniff'),
    ('X-Frame-Options', 'DENY'),
    ('Referrer-Policy', 'strict-origin-when-cross-origin'),
    ('Permissions-Policy', 'camera=(), microphone=(), geolocation=(), payment=(), usb=(), serial=(), hid=(), magnetometer=(), gyroscope=(), accelerometer=(), browsing-topics=()'),
    ('Cross-Origin-Opener-Policy', 'same-origin'),
    ('Cross-Origin-Resource-Policy', 'same-origin'),
    ('X-Permitted-Cross-Domain-Policies', 'none'),
    ('Origin-Agent-Cluster', '?1'),
]

DIST = ROOT / "dist"
if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir()
for p in [f for f, _ in PAGES] + ["robots.txt", "sitemap.xml"]:
    shutil.copy2(ROOT / p, DIST / p)
shutil.copytree(ROOT / ".well-known", DIST / ".well-known")
shutil.copytree(ROOT / "assets", DIST / "assets")

head = "/*\n" + "".join(f"  {k}: {val}\n" for k, val in HEADERS)
head += "\n/assets/*\n  Cache-Control: public, max-age=604800\n"
head += "\n/assets/fonts/*\n  Cache-Control: public, max-age=31536000, immutable\n"
(DIST / "_headers").write_text(head)
# Geen _redirects nodig: Cloudflare serveert /contact voor contact.html, stuurt /contact.html door naar /contact
# en toont 404.html bij onbekende adressen.

print("gebouwd:", ", ".join(built), "→ dist/ klaar voor Cloudflare Pages")
