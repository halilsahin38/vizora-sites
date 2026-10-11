"""Gedeelde bouwstenen voor alle pagina's: gegevens, kop, voet en kleine helpers.

Pagina's staan in site/pages/<naam>.py en hebben elk een functie render() -> str.
Stijl: assets/css/base.css (gedeeld) + assets/css/<pagina>.css.
Beweging: assets/js/motion.js reageert op data-attributen (zie de uitleg daar).
"""
import json

SITE = "https://vizoradigital.nl"
WA = "https://wa.me/31638705348"
TEL = "tel:+31638705348"
TEL_TXT = "06 38 70 53 48"
MAIL = "halilsahinai@gmail.com"

# Inline script: zet de class "js" (voor begintoestanden van animaties) en zorgt dat alles
# na 2,5 s zichtbaar wordt als motion.js om wat voor reden ook niet laadt.
# Let op: na een wijziging de sha256-hash in vercel.json bijwerken (build.py print hem).
INLINE_JS = 'document.documentElement.classList.add("js");setTimeout(function(){document.documentElement.classList.add("ready")},2500)'

PAGES = [("diensten.html", "Diensten"), ("prijzen.html", "Prijzen"), ("werkwijze.html", "Werkwijze"), ("over-ons.html", "Over ons")]

# ---------- iconen (alleen waar ze echt iets toevoegen) ----------
I = {
    "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true" class="i"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "up": '<svg viewBox="0 0 24 24" aria-hidden="true" class="i"><path d="M7 17 17 7M8 7h9v9"/></svg>',
    "call": '<svg viewBox="0 0 24 24" aria-hidden="true" class="i"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true" class="i"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    "plus": '<svg viewBox="0 0 24 24" aria-hidden="true" class="i"><path d="M12 5v14M5 12h14"/></svg>',
}
WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true" class="i i--fill"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2.1 1-2.4c.3-.3.6-.3.8-.3h.6c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.4 0 .5l-.4.6-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.5.1.6-.1l.9-1.1c.2-.3.4-.2.7-.1l2 1c.3.1.5.2.5.3.1.2.1.7-.1 1.3Z"/></svg>'
LOGO_MARK = '<svg class="logo__mark" viewBox="0 0 64 64" aria-hidden="true"><path class="lm-a" d="M8 10h12l15 44h-8z"/><path class="lm-b" d="M56 10H44L29 54h8z"/><circle class="lm-c" cx="32" cy="14" r="5"/></svg>'

# ---------- aanbod (één bron voor home en prijzen) ----------
PACKAGES = [
    dict(name="Start", title="Online zichtbaar", price="200", featured=False,
         desc="Voor starters en zzp'ers die snel en professioneel online willen staan.",
         feats=["One-page website op maat", "Perfect op mobiel", "Bel-, WhatsApp- en contactknoppen", "Basis vindbaarheid in Google", "Eigen domein + gratis hosting"]),
    dict(name="Groei", title="Meer klanten", price="350", featured=True,
         desc="Voor ondernemers die online echt klanten willen binnenhalen.",
         feats=["Website tot 5 pagina's", "Uniek ontwerp met animaties", "Online afspraken, reserveren of bestellen", "Google Bedrijfsprofiel ingericht", "Teksten die overtuigen", "Lokale SEO voor jouw regio", "Gratis hosting"]),
    dict(name="Compleet", title="Alles geregeld", price="500", featured=False,
         desc="Website, bereik en een helder groeiplan in één keer goed.",
         feats=["Alles uit Groei", "Logo en huisstijl", "Profielen op social media ingericht", "Persoonlijk groeiplan", "Advies voor advertenties", "1 maand gratis aanpassingen"]),
]
SUB_TIERS = [
    dict(name="Basis", price="25", feats=["Onderhoud &amp; beveiliging", "1 kleine aanpassing per maand", "Hulp via WhatsApp"]),
    dict(name="Plus", price="49", feats=["Alles uit Basis", "Tot 3 aanpassingen per maand", "Google Bedrijfsprofiel bijhouden", "Maandelijkse groeitips"]),
    dict(name="Pro", price="79", feats=["Alles uit Plus", "Tot 6 aanpassingen per maand", "Elk kwartaal een nieuwe pagina of actie", "Maandelijks groeigesprek"]),
]
GUARANTEES = [
    ("Niet blij? Niet betalen.", "Je ziet eerst het ontwerp. Ben je na de feedbackrondes niet tevreden, dan betaal je niets."),
    ("Twee feedbackrondes", "Twee keer aanpassen naar jouw wensen zit gewoon in de prijs."),
    ("Domein op jouw naam", "Je domeinnaam is en blijft van jou. Geen gedoe als je ooit wilt overstappen."),
    ("Maandelijks opzegbaar", "Het abonnement loopt per maand. Geen jaarcontract, geen kleine lettertjes."),
]
LD = {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "Vizora Digital",
    "url": SITE,
    "logo": SITE + "/assets/logo.svg",
    "image": SITE + "/assets/og.png",
    "description": "Websites en online groei voor ondernemers in heel Nederland. Vanuit Breda.",
    "telephone": "+31638705348",
    "email": MAIL,
    "priceRange": "€€",
    "address": {"@type": "PostalAddress", "addressLocality": "Breda", "addressRegion": "Noord-Brabant", "addressCountry": "NL"},
    "areaServed": {"@type": "Country", "name": "Nederland"},
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "09:00", "closes": "18:00"}],
    "founder": [{"@type": "Person", "name": "Halil"}, {"@type": "Person", "name": "Sahin"}],
}


# ---------- helpers ----------
def label(num, text):
    """Kleine mono-label zoals '(01) Wat we doen'."""
    n = f"({num}) " if num else ""
    return f'<p class="label">{n}{text}</p>'


def pic(name, alt, w, h, cls="", eager=False, pos=None, attrs=""):
    """<picture> met webp + jpg uit assets/foto/."""
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    style = f' style="object-position:{pos}"' if pos else ""
    return (f'<picture class="{cls}"><source srcset="assets/foto/{name}.webp" type="image/webp">'
            f'<img src="assets/foto/{name}.jpg" alt="{alt}" width="{w}" height="{h}" {load} decoding="async"{style}{attrs}></picture>')


def head(file, title, desc, css=(), preload=None, ld=False):
    url = SITE + "/" + ("" if file == "index.html" else file)
    links = "\n".join(f'  <link rel="stylesheet" href="assets/css/{c}.css">' for c in ("base", *css))
    pre = f'\n  <link rel="preload" as="image" href="{preload}" type="image/webp">' if preload else ""
    ldj = f'\n  <script type="application/ld+json">{json.dumps(LD, ensure_ascii=False)}</script>' if ld else ""
    return f'''<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#faf8f4">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="nl_NL">
  <meta property="og:site_name" content="Vizora Digital">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/og.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Host+Grotesk:wght@300..700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">{pre}
{links}
  <script>{INLINE_JS}</script>{ldj}
</head>
<body>
  <a class="skip" href="#main">Naar de inhoud</a>
'''


def header(active):
    links = ", ".join(
        f'<a href="{f}"{" aria-current=\"page\"" if f == active else ""}>{n}</a>' for f, n in PAGES)
    mobile = "\n".join(
        f'        <a href="{f}"{" aria-current=\"page\"" if f == active else ""}>{n}</a>' for f, n in [("index.html", "Home"), *PAGES, ("contact.html", "Contact")])
    return f'''  <header class="hd" data-header>
    <div class="hd__in wrap">
      <a href="index.html" class="logo" aria-label="Vizora Digital, naar de homepage">{LOGO_MARK}<span>Vizora</span></a>
      <p class="hd__desc">Webstudio — Breda<br>voor heel Nederland</p>
      <nav class="hd__nav" aria-label="Hoofdmenu">{links}</nav>
      <div class="hd__right">
        <a href="{TEL}" class="hd__tel" aria-label="Bel ons: {TEL_TXT}">{I["call"]}<span>{TEL_TXT}</span></a>
        <a href="contact.html" class="hd__cta"{" aria-current=\"page\"" if active == "contact.html" else ""}>Plan je gratis concept {I["up"]}</a>
        <button class="hd__menu" type="button" aria-expanded="false" aria-controls="menu"><span>Menu</span></button>
      </div>
    </div>
    <div class="menu" id="menu" hidden>
      <nav class="menu__links wrap" aria-label="Menu">
{mobile}
      </nav>
      <div class="menu__foot wrap">
        <a href="{TEL}" class="btn btn--light">{I["call"]} Bel {TEL_TXT}</a>
        <a href="{WA}" class="btn btn--line" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a>
      </div>
    </div>
  </header>
'''


def footer(active=""):
    plan = "#plannen" if active == "contact.html" else "contact.html"
    return f'''  <footer class="ft" data-theme="dark">
    <div class="wrap">
      <div class="ft__cta">
        <p class="label">(→) Volgende stap</p>
        <h2 class="ft__title">Klaar voor meer klanten?<br><span>Begin met je gratis concept.</span></h2>
        <div class="ft__actions">
          <a href="{plan}" class="btn btn--light">Plan je gratis concept {I["arrow"]}</a>
          <a href="{TEL}" class="btn btn--line">{I["call"]} Bel {TEL_TXT}</a>
          <a href="{WA}" class="btn btn--line" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a>
        </div>
      </div>
      <div class="ft__cols">
        <div>
          <p class="label">Pagina's</p>
          <ul><li><a href="index.html">Home</a></li><li><a href="diensten.html">Diensten</a></li><li><a href="prijzen.html">Prijzen</a></li><li><a href="werkwijze.html">Werkwijze</a></li><li><a href="over-ons.html">Over ons</a></li><li><a href="contact.html">Contact</a></li></ul>
        </div>
        <div>
          <p class="label">Contact</p>
          <ul><li><a href="{TEL}">{TEL_TXT}</a></li><li><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li></ul>
        </div>
        <div>
          <p class="label">Bereikbaar</p>
          <ul><li>Maandag t/m zaterdag</li><li>09:00 – 18:00</li><li>Vanuit Breda, voor heel Nederland</li></ul>
        </div>
      </div>
      <p class="ft__word" aria-hidden="true">Vizora</p>
      <div class="ft__bottom">
        <span>© <span data-year>2026</span> Vizora Digital</span>
        <span>Gemaakt door Halil &amp; Sahin</span>
      </div>
    </div>
  </footer>

  <div class="dock" data-dock>
    <div class="dock__panel" id="dock-panel" role="dialog" aria-label="Neem contact op" hidden>
      <p class="dock__status" data-dock-status><i></i><span>Nu bereikbaar</span></p>
      <p class="dock__title">Vraag? Stel hem gerust.</p>
      <p class="dock__text">Je spreekt direct met Halil of Sahin.</p>
      <a href="{WA}" class="dock__btn dock__btn--wa" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a>
      <a href="{TEL}" class="dock__btn">{I["call"]} Bel {TEL_TXT}</a>
      <a href="mailto:{MAIL}" class="dock__btn">{I["mail"]} Mail ons</a>
    </div>
    <button type="button" class="dock__fab" aria-expanded="false" aria-controls="dock-panel" aria-label="Contactopties openen">{WA_SVG}<span class="dock__x" aria-hidden="true">{I["plus"]}</span></button>
  </div>

  <script src="assets/vendor/gsap.min.js" defer></script>
  <script src="assets/vendor/ScrollTrigger.min.js" defer></script>
  <script src="assets/vendor/lenis.min.js" defer></script>
  <script src="assets/js/site.js" defer></script>
  <script src="assets/js/motion.js" defer></script>
</body>
</html>
'''


def page_head(num, label_text, title, lead):
    """Kop voor subpagina's: groot, links uitgelijnd, met label."""
    return f'''    <section class="ph wrap">
      {label(num, label_text)}
      <h1 class="ph__title" data-lines>{title}</h1>
      <p class="ph__lead" data-reveal>{lead}</p>
    </section>
'''


def faq_list(items):
    return "\n".join(
        f'''          <details class="qa__item"><summary><span>{q}</span>{I["plus"]}</summary><div class="qa__a"><p>{a}</p></div></details>'''
        for q, a in items)


def price_columns():
    out = []
    for p in PACKAGES:
        feats = "".join(f"<li>{f}</li>" for f in p["feats"])
        badge = '<span class="tag">Meest gekozen</span>' if p["featured"] else ""
        out.append(f'''          <article class="pk{" pk--featured" if p["featured"] else ""}" data-reveal>
            <div class="pk__top"><p class="label">{p["name"]}</p>{badge}</div>
            <p class="pk__price"><span class="pk__from">vanaf</span>€{p["price"]}</p>
            <p class="pk__note">eenmalig</p>
            <h3 class="pk__title">{p["title"]}</h3>
            <p class="pk__desc">{p["desc"]}</p>
            <ul class="pk__list">{feats}</ul>
            <a href="contact.html?pakket={p["name"]}" class="btn{"" if p["featured"] else " btn--ghost"} pk__btn">Kies {p["name"]} {I["arrow"]}</a>
          </article>''')
    return "\n".join(out)


def guarantees():
    return "\n".join(
        f'''          <div class="gu__item" data-reveal><p class="label">0{i}</p><h3>{t}</h3><p>{d}</p></div>'''
        for i, (t, d) in enumerate(GUARANTEES, 1))
