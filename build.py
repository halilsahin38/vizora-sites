"""Genereert alle HTML-pagina's van vizoradigital.nl.

Gebruik:  python3 build.py
Pas teksten hier aan en draai het script opnieuw; de .html-bestanden
worden dan overschreven. Stijl staat in assets/style.css.
"""
import pathlib, sys

OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).parent)
SITE = "https://vizoradigital.nl"
WA = "https://wa.me/31638705348"
MAIL = "halilsahinai@gmail.com"

I = {
  "web": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 8h18M8 21h8M12 18v3"/></svg>',
  "social": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="3" width="16" height="18" rx="4"/><circle cx="12" cy="12" r="3.5"/><circle cx="16.5" cy="7.5" r=".6"/></svg>',
  "growth": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 19V5M4 19h16M8 15l4-4 3 3 5-6"/><path d="M16 8h4v4"/></svg>',
  "bolt": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg>',
  "chat": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12Z"/></svg>',
  "phone": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="7" y="2" width="10" height="20" rx="2.5"/><path d="M11 18h2"/></svg>',
  "search": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg>',
  "pin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 22s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12Z"/><circle cx="12" cy="10" r="2.5"/></svg>',
  "pen": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16v4Z"/><path d="m13 7 4 4"/></svg>',
  "shield": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6l-8-3Z"/><path d="m9 12 2 2 4-4"/></svg>',
  "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
  "cal": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
  "users": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14.5a6.5 6.5 0 0 1 3.5 5.5"/></svg>',
  "call": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
  "route": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="6" cy="17" r="2"/><circle cx="18" cy="7" r="2"/><path d="M8 17h7a3 3 0 0 0 0-6H9a3 3 0 0 1 0-6h7"/></svg>',
  "reach": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 11v2a1 1 0 0 0 1 1h3l6 4V6L7 10H4a1 1 0 0 0-1 1Z"/><path d="M17 8a5 5 0 0 1 0 8M19.5 5.5a8.5 8.5 0 0 1 0 13"/></svg>',
  "inbox": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 13h5l1.5 3h5L16 13h5"/><path d="M5.5 5h13L21 13v6H3v-6Z"/></svg>',
  "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
}
LOGO_MARK = '<svg class="logo__mark" viewBox="0 0 64 64" aria-hidden="true"><path class="lm-a" d="M8 10h12l15 44h-8z"/><path class="lm-b" d="M56 10H44L29 54h8z"/><circle class="lm-c" cx="32" cy="14" r="5"/></svg>'
LOGO = LOGO_MARK + '<span class="logo__word"><b>Vizora</b><small>Digital</small></span>'
WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2.1 1-2.4c.3-.3.6-.3.8-.3h.6c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.4 0 .5l-.4.6-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.5.1.6-.1l.9-1.1c.2-.3.4-.2.7-.1l2 1c.3.1.5.2.5.3.1.2.1.7-.1 1.3Z"/></svg>'

PAGES = [("index.html", "Home"), ("diensten.html", "Diensten"), ("prijzen.html", "Prijzen"), ("werkwijze.html", "Werkwijze"), ("over-ons.html", "Over ons")]

INLINE_JS = 'document.documentElement.classList.add("js");try{if(sessionStorage.getItem("vz-intro"))document.documentElement.classList.add("intro-seen");sessionStorage.setItem("vz-intro","1")}catch(e){}'

def head(file, title, desc):
    url = SITE + "/" + ("" if file == "index.html" else file)
    return f'''<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#f3ece1">
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
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/style.css">
  <script>{INLINE_JS}</script>
</head>
<body>
  <a class="skip" href="#main">Naar de inhoud</a>
'''

TEL = "tel:+31638705348"
TEL_TXT = "06 38 70 53 48"

def header(active):
    links = "\n".join(
        f'        <a href="{f}"{" aria-current=\"page\"" if f == active else ""}>{n}</a>'
        for f, n in PAGES[1:])
    return f'''  <header class="nav">
    <div class="container nav__inner">
      <a href="index.html" class="logo" aria-label="Vizora Digital, naar de homepage">
        {LOGO}
      </a>
      <nav class="nav__links" id="menu" aria-label="Hoofdmenu">
{links}
        <a href="contact.html" class="btn btn--small"{" aria-current=\"page\"" if active == "contact.html" else ""}>Gratis gesprek</a>
      </nav>
      <a href="{TEL}" class="nav__call" aria-label="Bel ons direct: {TEL_TXT}">{I["call"]}<span>{TEL_TXT}</span></a>
      <button class="nav__toggle" aria-label="Menu openen" aria-expanded="false" aria-controls="menu">
        <span></span><span></span>
      </button>
    </div>
  </header>
'''

FOOTER = f'''  <footer class="footer">
    <div class="container">
      <div class="footer__top">
        <div>
          <a href="index.html" class="logo">
            {LOGO}
          </a>
          <p>Websites, bereik en online groei voor ondernemers die verder willen. Vanuit Breda, voor heel Noord-Brabant.</p>
        </div>
        <div>
          <h4>Pagina's</h4>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="diensten.html">Diensten</a></li>
            <li><a href="prijzen.html">Prijzen</a></li>
            <li><a href="werkwijze.html">Werkwijze</a></li>
            <li><a href="over-ons.html">Over ons</a></li>
          </ul>
        </div>
        <div>
          <h4>Diensten</h4>
          <ul>
            <li><a href="diensten.html#websites">Websites</a></li>
            <li><a href="diensten.html#marketing">Marketing &amp; bereik</a></li>
            <li><a href="diensten.html#social-media">Social media</a></li>
            <li><a href="prijzen.html#abonnement">Website-abonnement</a></li>
          </ul>
        </div>
        <div>
          <h4>Voor wie</h4>
          <ul>
            <li><a href="website-voor-kappers.html">Kappers &amp; barbers</a></li>
            <li><a href="website-voor-restaurants.html">Restaurants</a></li>
            <li><a href="website-voor-beautysalons.html">Beautysalons</a></li>
            <li><a href="website-voor-bakkerijen.html">Bakkerijen &amp; winkels</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <ul>
            <li><a href="{TEL}">Bel: {TEL_TXT}</a></li>
            <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp: {TEL_TXT}</a></li>
            <li><a href="mailto:{MAIL}">{MAIL}</a></li>
            <li>Ma t/m za · 09:00 – 18:00</li>
          </ul>
        </div>
      </div>
      <div class="footer__big" aria-hidden="true">Vizora Digital</div>
      <div class="footer__bottom">
        <span>© <span data-year></span> Vizora Digital · Breda</span>
        <span>Gemaakt met zorg door Halil &amp; Sahin</span>
      </div>
    </div>
  </footer>

  <a href="{WA}" class="wa" target="_blank" rel="noopener" aria-label="Stuur ons een WhatsApp-bericht">{WA_SVG}</a>

  <script src="assets/main.js"></script>
  <script src="assets/mosaic.js"></script>
</body>
</html>
'''

DEFAULT_CTA = "Plan een gratis gesprek of bel ons direct. We maken een concept van jouw website en laten zien hoe jouw zaak online kan groeien. Vrijblijvend, en zonder ingewikkelde praatjes."

def cta(title="Klaar om te <em>groeien?</em>", text=DEFAULT_CTA):
    return f'''    <section class="section section--tight">
      <div class="container">
        <div class="cta reveal" data-mosaic>
          <div class="cta__glow cta__glow--1" aria-hidden="true"></div>
          <div class="cta__glow cta__glow--2" aria-hidden="true"></div>
          <h2 class="split-words">{title}</h2>
          <p>{text}</p>
          <div class="cta__actions">
            <a href="contact.html" class="btn btn--light">Plan een gratis gesprek {I["arrow"]}</a>
            <a href="{TEL}" class="btn btn--ghost">{I["call"]} Bel {TEL_TXT}</a>
          </div>
        </div>
      </div>
    </section>
'''

def page_hero(eyebrow, title, lead):
    return f'''    <section class="page-hero">
      <div class="page-hero__rings" aria-hidden="true" data-speed="-0.15"><i></i><i></i><i></i></div>
      <div class="container">
        <p class="eyebrow reveal">{eyebrow}</p>
        <h1 class="split-words">{title}</h1>
        <p class="lead reveal" data-delay="300">{lead}</p>
      </div>
    </section>
'''

# Realistisch browservenster met een screenshot van een conceptwebsite
def win(img, url, style="", speed=None, eager=False):
    sp = f' data-speed="{speed}"' if speed else ""
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'''<div class="win" style="{style}"{sp}>
            <div class="win__bar"><span class="win__dots"><i></i><i></i><i></i></span><span class="win__url"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>{url}</span><span></span></div>
            <img src="assets/concepts/{img}" alt="" width="2000" height="1000" {load} decoding="async">
          </div>'''

# Realistische telefoon met een screenshot van de mobiele versie
def iphone(img, style="", speed=None, eager=False):
    sp = f' data-speed="{speed}"' if speed else ""
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'''<div class="iphone" style="{style}"{sp}>
            <div class="iphone__screen">
              <img src="assets/concepts/{img}" alt="" width="780" height="1688" {load} decoding="async">
              <span class="iphone__island"></span><span class="iphone__glare"></span>
            </div>
          </div>'''

def shot(img, label):
    return f'''<figure class="shot"><div class="win__bar"><span class="win__dots"><i></i><i></i><i></i></span></div><img src="assets/concepts/{img}" alt="" width="800" height="400" loading="lazy" decoding="async"><figcaption>{label}</figcaption></figure>'''

def shot_phone(img, label):
    return f'''<figure class="shot shot--phone"><div class="iphone"><div class="iphone__screen"><img src="assets/concepts/{img}" alt="" width="312" height="675" loading="lazy" decoding="async"><span class="iphone__island"></span></div></div></figure>'''

ROW1 = "\n            ".join([
  shot("noir-thumb.jpg", "Barbershop"),
  shot_phone("serene-mobile-thumb.jpg", "Beautysalon · mobiel"),
  shot("olivo-thumb-2.jpg", "Restaurant · menukaart"),
  shot("goudkorst-thumb.jpg", "Bakkerij"),
  shot_phone("noir-mobile-thumb.jpg", "Barbershop · mobiel"),
  shot("serene-thumb-2.jpg", "Beautysalon · behandelingen"),
])
ROW2 = "\n            ".join([
  shot("olivo-thumb.jpg", "Restaurant"),
  shot_phone("goudkorst-mobile-thumb.jpg", "Bakkerij · mobiel"),
  shot("noir-thumb-2.jpg", "Barbershop · prijzen"),
  shot("serene-thumb.jpg", "Beautysalon"),
  shot_phone("olivo-mobile-thumb.jpg", "Restaurant · mobiel"),
  shot("goudkorst-thumb-2.jpg", "Bakkerij · assortiment"),
])

PACKAGES = [
  ("Start", "Online zichtbaar", "200", "Voor starters en zzp'ers die snel en professioneel online willen staan.",
   ["One-page website op maat", "Perfect op mobiel", "Bel-, WhatsApp- en contactknoppen", "Basis vindbaarheid in Google", "Koppeling met je eigen domein"], False),
  ("Groei", "Meer klanten", "350", "Voor ondernemers die online echt klanten willen binnenhalen.",
   ["Website tot 5 pagina's", "Uniek ontwerp met animaties", "Online afspraken, reserveren of bestellen", "Google Bedrijfsprofiel ingericht", "Teksten die overtuigen", "Lokale SEO voor jouw regio"], True),
  ("Compleet", "Alles geregeld", "500", "Website, bereik en een helder groeiplan in één keer goed.",
   ["Alles uit Groei", "Logo en huisstijl", "Social media profielen ingericht", "Persoonlijk groeiplan", "Advies voor advertenties", "1 maand gratis aanpassingen"], False),
]

def pricing_cards():
    out = []
    for i, (name, title, price, desc, feats, featured) in enumerate(PACKAGES):
        badge = '<span class="price__badge">Meest gekozen</span>' if featured else ""
        lis = "".join(f"<li>{f}</li>" for f in feats)
        btn = "btn" + ("" if featured else " btn--ghost")
        out.append(f'''          <article class="price{" price--featured" if featured else ""} reveal" data-delay="{i*120}">
            {badge}
            <span class="price__name">{name}</span>
            <h3>{title}</h3>
            <p class="muted">{desc}</p>
            <div class="price__from">vanaf</div>
            <div class="price__amount"><sup>€</sup>{price}</div>
            <p class="price__note">eenmalig</p>
            <ul>{lis}</ul>
            <a href="contact.html?pakket={name}" class="{btn}">Kies {name} {I["arrow"]}</a>
          </article>''')
    return "\n".join(out)

SUB_TIERS = [
  ("Basis", "25", ["Onderhoud &amp; beveiliging", "1 kleine aanpassing per maand", "Hulp via WhatsApp"], False),
  ("Plus", "49", ["Alles uit Basis", "Tot 3 aanpassingen per maand", "Google Bedrijfsprofiel bijhouden", "Maandelijkse groeitips"], True),
  ("Pro", "79", ["Alles uit Plus", "Tot 6 aanpassingen per maand", "Elk kwartaal een nieuwe pagina of actie", "Maandelijks groeigesprek"], False),
]
def sub_tiers():
    out = []
    for name, price, feats, featured in SUB_TIERS:
        lis = "".join(f"<li>{f}</li>" for f in feats)
        out.append(f'''            <div class="tier{" tier--featured" if featured else ""}">
              <span class="tier__name">{name}</span>
              <strong><sup>€</sup>{price}<small> p/m</small></strong>
              <ul>{lis}</ul>
              <a href="contact.html?pakket=Abonnement%20{name}" class="btn {"btn--light" if featured else "btn--ghost"} btn--small">Kies {name}</a>
            </div>''')
    return "\n".join(out)

SUBSCRIPTION = f'''        <div class="sub reveal" id="abonnement">
          <div class="sub__copy">
            <span class="price__name">Website-abonnement</span>
            <h3>Elke maand een website die <em>klopt.</em></h3>
            <p>Een website is nooit af. Met een abonnement houden wij je site up-to-date, veilig en snel, en helpen we je elke maand een stap verder. Je kiest zelf hoeveel hulp je wilt en ontvangt maandelijks een factuur.</p>
          </div>
          <div class="tiers">
{sub_tiers()}
          </div>
        </div>
'''

# ======================= HOME =======================
home = head("index.html", "Vizora Digital | Websites die klanten opleveren | Breda",
            "Websites die klanten opleveren, meer bereik in Google en een plan om te groeien. Vizora Digital uit Breda. Plan een gratis gesprek en ontvang een gratis concept.")
home += header("index.html")
home += f'''
  <main id="main">
    <section class="hero">
      <div class="blob blob--1" data-speed="0.12" aria-hidden="true"></div>
      <div class="blob blob--2" data-speed="-0.1" aria-hidden="true"></div>
      <div class="container hero__grid">
        <div class="hero__copy">
          <p class="eyebrow reveal">Websites · Bereik · Groei</p>
          <h1 class="split-words">Meer klanten, met een online uitstraling die <em>klopt.</em></h1>
          <p class="lead reveal" data-delay="400">Wij zorgen dat jouw zaak online gevonden, gekozen en geboekt wordt. Met een website die vertrouwen wekt, meer bereik in Google en een helder plan om te groeien. Vanuit Breda, voor ondernemers in heel Noord-Brabant.</p>
          <div class="hero__actions reveal" data-delay="550">
            <a href="contact.html" class="btn">Plan een gratis gesprek {I["arrow"]}</a>
            <a href="{TEL}" class="btn btn--ghost">{I["call"]} Bel direct</a>
          </div>
          <ul class="hero__trust reveal" data-delay="700">
            <li>Gratis websiteconcept</li>
            <li>Persoonlijk contact</li>
            <li>Websites vanaf €200</li>
          </ul>
        </div>

        <div class="stage reveal" data-delay="200" aria-hidden="true">
          <div class="stage__plate stage__plate--1" data-speed="0.06"></div>
          <div class="stage__plate stage__plate--2" data-speed="0.03"></div>
          {win("olivo-desktop.jpg", "vizoradigital.nl/concept/olivo", "left:0;top:64px;width:88%", "-0.04", eager=True)}
          {iphone("noir-mobile.jpg", "right:0;bottom:6px", "-0.12", eager=True)}
          <div class="chip-card chip-card--a" data-speed="-0.18">
            <div class="chip-card__icon float">{I["cal"]}</div>
            <div><strong>Nieuwe reservering</strong><small>via je website</small></div>
          </div>
          <div class="chip-card chip-card--b" data-speed="-0.08">
            <div class="chart"><i style="height:30%"></i><i style="height:45%"></i><i style="height:40%"></i><i style="height:65%"></i><i style="height:80%"></i><i style="height:100%"></i></div>
            <div><strong>Meer bereik</strong><small>Google &amp; Maps</small></div>
          </div>
        </div>
      </div>
      <div class="hero__scroll" aria-hidden="true"></div>
    </section>

    <section class="showcase" aria-labelledby="showcase-titel">
      <div class="container">
        <div class="section__head section__head--split">
          <div>
            <p class="eyebrow reveal">Ons werk</p>
            <h2 id="showcase-titel" class="split-words">Design dat je <em>voelt.</em></h2>
          </div>
          <p class="muted reveal" style="max-width:26em">Klik op het beeld. Dit zijn concepten van websites die wij bouwen: elk ontwerp uniek, en elk ontwerp gemaakt om van bezoekers klanten te maken.</p>
        </div>
        <div class="contour reveal" data-contour>
          <canvas role="img" aria-label="Conceptwebsites van een barbershop, restaurant, beautysalon en bakkerij"></canvas>
          <span class="contour__hint">Klik om te ontdekken</span>
          <div class="contour__ui">
            <div class="contour__caption" aria-live="polite">
              <span class="contour__count" data-count>Concept 01 / 04</span>
              <h3 data-title>Barbershop Noir</h3>
              <p data-text>Online boeken, heldere prijzen en openingstijden in één oogopslag.</p>
            </div>
            <button class="contour__next" type="button" data-next aria-label="Volgend concept">{I["arrow"]}</button>
          </div>
          <div class="contour__progress" aria-hidden="true"><i></i></div>
        </div>
      </div>
    </section>

    <section class="section section--tight" aria-labelledby="concepten">
      <div class="container">
        <div class="section__head section__head--split">
          <div>
            <p class="eyebrow reveal">Wat we maken</p>
            <h2 id="concepten" class="split-words">Een website die past bij <em>jouw</em> zaak</h2>
          </div>
          <p class="muted reveal" style="max-width:26em">Een barbershop heeft andere klanten dan een bakkerij. Daarom maken we geen standaard websites, maar ontwerpen die precies passen bij jouw zaak, op elk scherm.</p>
        </div>
      </div>
      <div class="marquee" aria-hidden="true">
        <div class="marquee__track">
            {ROW1}
        </div>
      </div>
      <div class="marquee marquee--reverse" aria-hidden="true">
        <div class="marquee__track">
            {ROW2}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container split">
        <div>
          <p class="eyebrow reveal">Herkenbaar?</p>
          <h2 class="split-words">Goed in je vak, maar online <em>onzichtbaar?</em></h2>
          <p class="lead reveal">Bijna elke klant zoekt eerst online. Vinden ze je niet, of ziet je website er verouderd uit? Dan kiezen ze binnen een paar seconden voor de zaak verderop. Zonde, want misschien ben jij wel de beste.</p>
          <ul class="pain reveal">
            <li><div><strong>Geen of een verouderde website</strong><span>Bezoekers haken af voordat ze hebben gebeld of een afspraak hebben gemaakt.</span></div></li>
            <li><div><strong>Niet te vinden in Google</strong><span>Mensen in jouw buurt zoeken precies wat jij aanbiedt, maar vinden je concurrent.</span></div></li>
            <li><div><strong>Geen tijd om het zelf te regelen</strong><span>Jij runt je zaak. Online groei schiet er dan al snel bij in.</span></div></li>
          </ul>
        </div>
        <div>
          <p class="eyebrow reveal">Met Vizora</p>
          <h2 class="split-words">Wij laten je groeien, jij krijgt de <em>klanten.</em></h2>
          <p class="lead reveal">Eén vast team voor je website, je vindbaarheid en je online groei. Alles sluit op elkaar aan en heeft één doel: meer klanten voor jouw zaak.</p>
          <ul class="pain pain--good reveal">
            <li><div><strong>Een website die verkoopt</strong><span>Snel, mooi en gebouwd om van bezoekers klanten te maken: afspraken, reserveringen of aanvragen.</span></div></li>
            <li><div><strong>Groter bereik</strong><span>Gevonden worden in Google en Google Maps, door mensen die nu zoeken wat jij aanbiedt.</span></div></li>
            <li><div><strong>Een plan om te groeien</strong><span>We nemen stap voor stap met je door hoe je zaak groeit, en zorgen dat je website meegroeit.</span></div></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section section--alt" aria-labelledby="diensten-titel">
      <div class="container">
        <div class="section__head">
          <p class="eyebrow reveal">Diensten</p>
          <h2 id="diensten-titel" class="split-words">Alles voor je online groei, onder één dak</h2>
          <p class="reveal">Kies wat je nodig hebt, of laat ons het complete plaatje verzorgen. Altijd afgestemd op jouw zaak en jouw doelen.</p>
        </div>
        <div class="cards">
          <article class="card reveal">
            <span class="card__num" aria-hidden="true">01</span>
            <div class="card__icon">{I["web"]}</div>
            <h3>Websites</h3>
            <p>Een moderne website die vertrouwen wekt en bezoekers omzet in klanten. Gemaakt op maat, nooit een standaard template.</p>
            <ul><li>Ontwerp op maat</li><li>Online afspraken, reserveren of bestellen</li><li>Perfect op mobiel</li></ul>
            <a href="diensten.html#websites" class="link-arrow">Meer over websites</a>
          </article>
          <article class="card card--dark reveal" data-delay="120">
            <span class="card__num" aria-hidden="true">02</span>
            <div class="card__icon">{I["reach"]}</div>
            <h3>Marketing &amp; bereik</h3>
            <p>Meer bereik in jouw regio. Met een sterk Google-profiel, lokale SEO en gerichte advertenties bereik je mensen die nu zoeken.</p>
            <ul><li>Google Bedrijfsprofiel</li><li>Lokale SEO</li><li>Google &amp; Meta advertenties</li></ul>
            <a href="diensten.html#marketing" class="link-arrow">Meer over marketing</a>
          </article>
          <article class="card reveal" data-delay="240">
            <span class="card__num" aria-hidden="true">03</span>
            <div class="card__icon">{I["social"]}</div>
            <h3>Social media</h3>
            <p>Wij helpen je op weg: profielen die kloppen, een herkenbare stijl en advies over wat werkt. De content bespreken we samen.</p>
            <ul><li>Profielen inrichten</li><li>Huisstijl &amp; templates</li><li>Advies &amp; strategie</li></ul>
            <a href="diensten.html#social-media" class="link-arrow">Meer over social media</a>
          </article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section--dark" style="margin:0;padding:90px 48px;border-radius:40px">
          <div class="section__head center">
            <p class="eyebrow reveal">Waarom Vizora</p>
            <h2 class="split-words">Vizora helpt je <em>groeien.</em></h2>
            <p class="reveal">Geen website die alleen mooi is. Alles wat we doen is gericht op meer bereik, meer aanvragen en meer omzet voor jouw zaak.</p>
          </div>
          <div class="benefits benefits--3">
            <div class="benefit reveal"><div class="icon">{I["growth"]}</div><h3>Wij laten je groeien</h3><p>Alles wat we maken heeft één doel: meer klanten voor jouw zaak. Mooi is mooi meegenomen, resultaat is waar het om draait.</p></div>
            <div class="benefit reveal" data-delay="100"><div class="icon">{I["reach"]}</div><h3>Groter bereik</h3><p>We zorgen dat je gevonden wordt: in Google, op Google Maps en op social media, precies door mensen in jouw regio.</p></div>
            <div class="benefit reveal" data-delay="200"><div class="icon">{I["inbox"]}</div><h3>Meer aanvragen</h3><p>Duidelijke knoppen, online afspraken en WhatsApp: we maken het je klanten zo makkelijk mogelijk om contact op te nemen.</p></div>
            <div class="benefit reveal"><div class="icon">{I["route"]}</div><h3>Een plan, stap voor stap</h3><p>We nemen samen door waar je nu staat, waar je naartoe wilt en hoe we daar komen. Geen vage beloftes, wel een duidelijk plan.</p></div>
            <div class="benefit reveal" data-delay="100"><div class="icon">{I["call"]}</div><h3>Direct contact</h3><p>Bellen, appen of mailen: je spreekt altijd direct met Halil of Sahin. Geen tussenpersonen, geen wachttijden.</p></div>
            <div class="benefit reveal" data-delay="200"><div class="icon">{I["shield"]}</div><h3>Eerlijk &amp; lokaal</h3><p>Vanuit Breda, met duidelijke prijzen vooraf. En als iets niet nodig is voor jouw zaak, zeggen we dat ook.</p></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="demo-titel">
      <div class="container demo" data-demo>
        <div class="demo__controls">
          <div>
            <p class="eyebrow reveal">Gratis websiteconcept</p>
            <h2 id="demo-titel" class="split-words">Zie hoe <em>jouw</em> website eruit kan zien</h2>
            <p class="lead reveal">Plan een afspraak en wij maken vooraf een concept van jouw nieuwe website. In het gesprek nemen we het samen door, en bespreken we stap voor stap hoe jouw zaak gaat groeien en wat wij daarvoor doen. Gratis en vrijblijvend.</p>
          </div>
          <ol class="concept-steps reveal">
            <li><b>Plan een afspraak</b><span>Kies online een moment, of bel of app ons direct.</span></li>
            <li><b>Wij maken je concept</b><span>Een eerste ontwerp van jouw website, in jouw stijl.</span></li>
            <li><b>Samen je groeiplan</b><span>We nemen door hoe je meer bereik en meer klanten krijgt.</span></li>
          </ol>
          <div class="hero__actions reveal" style="margin:0">
            <a href="contact.html" class="btn" data-demo-go>Plan mijn gratis concept {I["arrow"]}</a>
            <a href="{TEL}" class="btn btn--ghost">{I["call"]} Bel direct</a>
          </div>
        </div>
        <div class="demo__side">
          <div class="demo__try reveal">
            <label class="demo__label" for="demo-name">Alvast een voorproefje? Typ je bedrijfsnaam</label>
            <input class="demo__input" id="demo-name" type="text" maxlength="30" placeholder="Bijv. Barbershop Breda" autocomplete="organization" data-demo-input>
            <div class="choices" role="radiogroup" aria-label="Branche">
              <div class="choice"><input type="radio" name="demo-type" id="dt1" value="Kapper" checked><label for="dt1">Kapper</label></div>
              <div class="choice"><input type="radio" name="demo-type" id="dt2" value="Restaurant"><label for="dt2">Restaurant</label></div>
              <div class="choice"><input type="radio" name="demo-type" id="dt3" value="Salon"><label for="dt3">Salon</label></div>
              <div class="choice"><input type="radio" name="demo-type" id="dt4" value="Bedrijf"><label for="dt4">Ander bedrijf</label></div>
            </div>
          </div>
          <div class="demo__view reveal" data-demo-view data-theme="barber" aria-live="polite">
            <div class="site">
              <div class="site__bar"><span class="win__dots"><i></i><i></i><i></i></span><b data-demo-url>jouwzaak.nl</b></div>
              <div class="site__nav">
                <div class="site__brand"><span class="site__logo" data-demo-initial>J</span><span data-demo-name>Jouw Zaak</span></div>
                <div class="site__links" aria-hidden="true"><i></i><i></i><i></i></div>
              </div>
              <div class="site__hero">
                <small data-demo-name>Jouw Zaak</small>
                <strong data-demo-head>Fresh cuts, elke dag</strong>
                <span data-demo-cta>Maak een afspraak</span>
              </div>
              <div class="site__cards">
                <div data-demo-card>Knippen</div><div data-demo-card>Baard</div><div data-demo-card>Styling</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--alt" aria-labelledby="prijzen-titel">
      <div class="container">
        <div class="section__head center">
          <p class="eyebrow reveal">Prijzen</p>
          <h2 id="prijzen-titel" class="split-words">Duidelijke pakketten, <em>eerlijke</em> prijzen</h2>
          <p class="reveal">Geen verrassingen achteraf. Kies een pakket als startpunt; je krijgt altijd eerst een offerte op maat.</p>
        </div>
        <div class="pricing">
{pricing_cards()}
        </div>
{SUBSCRIPTION}
        <p class="pricing__foot reveal"><a href="prijzen.html" class="link-arrow">Vergelijk alle pakketten</a></p>
      </div>
    </section>

    <section class="section" aria-labelledby="werkwijze-titel">
      <div class="container">
        <div class="section__head section__head--split">
          <div>
            <p class="eyebrow reveal">Werkwijze</p>
            <h2 id="werkwijze-titel" class="split-words">Van eerste gesprek tot groei</h2>
          </div>
          <a href="werkwijze.html" class="link-arrow reveal">Bekijk de hele werkwijze</a>
        </div>
        <ol class="steps">
          <li class="step reveal"><span class="step__n" aria-hidden="true">01</span><h3>Kennismaken</h3><p>Gratis gesprek: bellen, appen, video of bij jou langs in de regio Breda.</p></li>
          <li class="step reveal" data-delay="100"><span class="step__n" aria-hidden="true">02</span><h3>Concept &amp; groeiplan</h3><p>We laten je websiteconcept zien en bespreken stap voor stap hoe je groeit.</p></li>
          <li class="step reveal" data-delay="200"><span class="step__n" aria-hidden="true">03</span><h3>Bouwen &amp; lanceren</h3><p>Wij bouwen, testen en zetten alles live. Jij hoeft niks technisch te doen.</p></li>
          <li class="step reveal" data-delay="300"><span class="step__n" aria-hidden="true">04</span><h3>Blijven groeien</h3><p>Met ons abonnement blijft je website elke maand up-to-date.</p></li>
        </ol>
      </div>
    </section>

{cta()}  </main>

'''
home += FOOTER

# ======================= DIENSTEN =======================
dash_svg = '''<svg viewBox="0 0 300 110" preserveAspectRatio="none" aria-hidden="true"><defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d8c6aa"/><stop offset="1" stop-color="#d8c6aa" stop-opacity="0"/></linearGradient></defs><path class="area" d="M0 95 C40 90 60 80 90 78 S140 60 170 55 S230 30 300 10 V110 H0Z"/><path class="line" d="M0 95 C40 90 60 80 90 78 S140 60 170 55 S230 30 300 10"/></svg>'''

dien = head("diensten.html", "Diensten | Websites, marketing & social media | Vizora Digital",
            "Websites die klanten opleveren, meer bereik in Google en hulp bij social media. Vizora Digital uit Breda helpt ondernemers stap voor stap groeien.")
dien += header("diensten.html")
dien += f'''
  <main id="main">
{page_hero("Diensten", "Alles om online te <em>groeien,</em> onder één dak", "Een website die klanten oplevert, meer bereik in jouw regio en hulp bij social media. Los af te nemen of als compleet pakket, en altijd afgestemd op jouw zaak.")}
    <section class="section">
      <div class="container">
        <div class="service" id="websites">
          <div class="service__visual reveal" aria-hidden="true">
            <div class="plate plate--sand" style="inset:30px 0 10px 60px;rotate:6deg" data-speed="0.05"></div>
            <div class="plate plate--soft" style="inset:10px 40px 30px 20px;rotate:-3deg" data-speed="0.02"></div>
            {win("serene-desktop.jpg", "vizoradigital.nl/concept/serene", "left:20px;right:20px;top:90px", "-0.05")}
            <div class="chip-card" style="right:0;bottom:40px" data-speed="-0.14"><div class="chip-card__icon">{I["bolt"]}</div><div><strong>Supersnel</strong><small>laadt in een oogwenk</small></div></div>
          </div>
          <div class="service__copy">
            <p class="eyebrow reveal">01 · Websites</p>
            <h2 class="split-words">Een website die werkt als je <em>beste verkoper</em></h2>
            <p class="lead reveal">Je website is vaak het eerste wat een klant van je ziet, en dat moment telt. Wij zorgen dat die eerste indruk klopt én dat bezoekers ook echt iets doen: bellen, appen, een afspraak maken of reserveren.</p>
            <p class="muted reveal">Elke website ontwerpen we op maat, rond jouw klanten en jouw doelen. Geen standaard template, wel een site die laat zien hoe goed je bent. En met ons abonnement blijft hij elke maand up-to-date.</p>
            <ul class="reveal">
              <li>Uniek ontwerp, geen template</li>
              <li>Perfect op telefoon, tablet en laptop</li>
              <li>Online afspraken, reserveren of bestellen</li>
              <li>Bel- en WhatsApp-knoppen</li>
              <li>Vindbaar in Google (SEO)</li>
              <li>Maandelijks bijgewerkt (abonnement)</li>
            </ul>
            <a href="contact.html" class="btn reveal">Bespreek je website {I["arrow"]}</a>
          </div>
        </div>

        <div class="service service--flip" id="marketing">
          <div class="service__visual reveal" aria-hidden="true">
            <div class="plate plate--soft" style="inset:20px 30px 40px 30px;rotate:4deg" data-speed="0.03"></div>
            <div class="dash" style="left:40px;right:40px;top:110px" data-speed="-0.05">
              <small>Websitebezoekers</small>
              <strong>Meer bezoekers</strong>
              {dash_svg}
            </div>
            <div class="chip-card" style="right:0;top:10px" data-speed="-0.15"><div class="chip-card__icon">{I["search"]}</div><div><strong>Google</strong><small>gevonden worden</small></div></div>
            <div class="chip-card" style="left:0;bottom:30px" data-speed="-0.1"><div class="chip-card__icon">{I["pin"]}</div><div><strong>Google Maps</strong><small>lokaal zichtbaar</small></div></div>
          </div>
          <div class="service__copy">
            <p class="eyebrow reveal">02 · Marketing &amp; bereik</p>
            <h2 class="split-words">Meer bereik, precies in <em>jouw</em> regio</h2>
            <p class="lead reveal">De beste klanten zitten vaak om de hoek. Met een sterk Google-profiel, lokale SEO en gerichte advertenties bereik je mensen die nú zoeken naar wat jij aanbiedt.</p>
            <p class="muted reveal">We beginnen met de basis die het meeste oplevert, en bouwen daarna stap voor stap verder. Zo weet je precies waar je geld naartoe gaat, en wat het oplevert.</p>
            <ul class="reveal">
              <li>Google Bedrijfsprofiel inrichten</li>
              <li>Lokale SEO</li>
              <li>Google Ads campagnes</li>
              <li>Instagram &amp; Facebook advertenties</li>
              <li>Meer en betere reviews</li>
              <li>Duidelijke rapportages</li>
            </ul>
            <a href="contact.html" class="btn reveal">Bespreek marketing {I["arrow"]}</a>
          </div>
        </div>

        <div class="service" id="social-media">
          <div class="service__visual reveal" aria-hidden="true">
            <div class="plate plate--sand" style="inset:40px 50px 0 0;rotate:-6deg" data-speed="0.05"></div>
            <div class="plate plate--soft" style="inset:20px 10px 30px 60px;rotate:3deg" data-speed="0.02"></div>
            {iphone("olivo-mobile.jpg", "left:50%;top:10px;translate:-50% 0", "-0.08")}
            <div class="chip-card" style="left:0;top:80px" data-speed="-0.16"><div class="chip-card__icon">{I["social"]}</div><div><strong>Profiel ingericht</strong><small>Instagram &amp; Facebook</small></div></div>
            <div class="chip-card" style="right:0;bottom:50px" data-speed="-0.12"><div class="chip-card__icon">{I["pen"]}</div><div><strong>Herkenbare stijl</strong><small>overal hetzelfde gevoel</small></div></div>
          </div>
          <div class="service__copy">
            <p class="eyebrow reveal">03 · Social media</p>
            <h2 class="split-words">Social media: wij helpen je <em>op weg</em></h2>
            <p class="lead reveal">Social media werkt het best als het echt van jou is. Jij kent je zaak, je klanten en je verhaal het beste. Wij zorgen dat je profielen professioneel zijn ingericht, alles herkenbaar in jouw stijl is en je weet wat werkt.</p>
            <p class="muted reveal">De content (foto's en video's) komt in principe van jou. Wil je dat wij meer doen, zoals content maken of posten? Dat bespreken we graag samen; dit valt buiten de pakketten en kost extra.</p>
            <ul class="reveal">
              <li>Profielen inrichten</li>
              <li>Huisstijl &amp; templates</li>
              <li>Bio, links en highlights</li>
              <li>Advies &amp; contentplan</li>
              <li>Koppeling met je website</li>
              <li>Content maken in overleg</li>
            </ul>
            <a href="contact.html" class="btn reveal">Bespreek social media {I["arrow"]}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="section__head">
          <p class="eyebrow reveal">Extra</p>
          <h2 class="split-words">Handig om erbij te nemen</h2>
        </div>
        <div class="cards">
          <article class="card reveal"><div class="card__icon">{I["pen"]}</div><h3>Logo &amp; huisstijl</h3><p>Een herkenbaar logo, kleuren en lettertypes die overal terugkomen: van je website tot je visitekaartje en Instagram.</p></article>
          <article class="card reveal" data-delay="120"><div class="card__icon">{I["mail"]}</div><h3>Zakelijke e-mail</h3><p>Mailen vanaf info@jouwzaak.nl in plaats van een Gmail-adres. Klein detail, groot verschil in vertrouwen.</p></article>
          <article class="card card--dark reveal" data-delay="240"><div class="card__icon">{I["shield"]}</div><h3>Website-abonnement</h3><p>Vanaf €25 per maand houden we je website up-to-date: nieuwe teksten, prijzen of foto's, onderhoud en beveiliging.</p><a href="prijzen.html#abonnement" class="link-arrow">Meer over het abonnement</a></article>
        </div>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container">
        <div class="section__head">
          <p class="eyebrow reveal">Voor wie</p>
          <h2 class="split-words">Gemaakt voor lokale ondernemers</h2>
        </div>
        <ul class="tags reveal">
          <li><a href="website-voor-kappers.html">Kappers &amp; barbers →</a></li><li><a href="website-voor-restaurants.html">Restaurants &amp; cafés →</a></li><li><a href="website-voor-beautysalons.html">Beautysalons &amp; nagelstudio's →</a></li><li><a href="website-voor-bakkerijen.html">Bakkerijen →</a></li>
          <li>Winkels</li><li>Sportscholen &amp; personal trainers</li><li>Zorg &amp; fysio</li><li>Bouw &amp; vakmensen</li><li>Starters &amp; zzp'ers</li>
        </ul>
      </div>
    </section>

{cta("Niet zeker wat je <em>nodig</em> hebt?", "Geen probleem. In een gratis gesprek kijken we samen wat het meeste oplevert voor jouw zaak, en wat je beter (nog) niet kunt doen. Bellen mag ook gewoon.")}  </main>

'''
dien += FOOTER

# ======================= WERKWIJZE =======================
werk = head("werkwijze.html", "Werkwijze | Stap voor stap groeien | Vizora Digital",
            "Van gratis kennismaking en websiteconcept tot een website die elke maand meegroeit. Zo werkt Vizora Digital uit Breda.")
werk += header("werkwijze.html")
werk += f'''
  <main id="main">
{page_hero("Werkwijze", "Stap voor stap naar <em>meer klanten</em>", "Je weet altijd waar je aan toe bent. Van het eerste gesprek tot een website die elke maand meegroeit.")}
    <section class="section">
      <div class="container--narrow">
        <div class="timeline">
          <div class="timeline__line" aria-hidden="true"><i></i></div>
          <article class="tl-item"><div class="tl-item__dot">1</div><span class="tl-item__meta">Gratis · bellen, appen of plannen</span><h3>Kennismaken</h3><p>Bel of app ons direct, of plan online een moment. We leren je zaak kennen: wat doe je, wie zijn je klanten en waar wil je naartoe? Telefonisch, via video of bij jou op locatie in de regio Breda.</p></article>
          <article class="tl-item"><div class="tl-item__dot">2</div><span class="tl-item__meta">Gratis · tijdens de afspraak</span><h3>Jouw concept &amp; groeiplan</h3><p>We maken vooraf een concept van hoe jouw website eruit kan zien. Samen nemen we het door, en bespreken we stap voor stap hoe jouw zaak gaat groeien en wat wij daarvoor doen.</p></article>
          <article class="tl-item"><div class="tl-item__dot">3</div><span class="tl-item__meta">Duidelijk vooraf</span><h3>Voorstel &amp; offerte</h3><p>Je krijgt een helder voorstel: wat we gaan doen, wat het kost en wanneer het klaar is. Geen kleine lettertjes, geen verrassingen.</p></article>
          <article class="tl-item"><div class="tl-item__dot">4</div><span class="tl-item__meta">Wij doen het werk</span><h3>Bouwen &amp; lanceren</h3><p>We bouwen alles, schrijven de teksten mee en testen op elk apparaat. Daarna gaat je site live op je eigen domein.</p>
            <ul><li>Domein en hosting geregeld</li><li>Snel en veilig (https)</li><li>Aangemeld bij Google</li></ul></article>
          <article class="tl-item"><div class="tl-item__dot">5</div><span class="tl-item__meta">Doorlopend</span><h3>Blijven groeien</h3><p>Met ons website-abonnement (vanaf €25 per maand) houden we je website elke maand up-to-date. Wil je verder groeien met advertenties of social media? Dan schakel je ons direct in.</p></article>
        </div>
      </div>
    </section>

    <section class="section section--alt" id="faq">
      <div class="container--narrow">
        <div class="section__head center">
          <p class="eyebrow reveal">FAQ</p>
          <h2 class="split-words">Veelgestelde vragen</h2>
        </div>
        <div class="faq reveal">
          <details><summary>Krijg ik vooraf een ontwerp te zien?</summary><p>Ja. Als je een afspraak plant, maken we gratis een concept van jouw website. Zo zie je meteen hoe het eruit kan zien, nog voordat je iets beslist.</p></details>
          <details><summary>Hoe lang duurt het voordat mijn website online staat?</summary><p>Dat hangt af van de grootte van je website en hoe snel de inhoud (teksten, foto's) rond is. In het gesprek krijg je een duidelijke planning.</p></details>
          <details><summary>Wat kost een website?</summary><p>Onze pakketten beginnen bij €200 (Start), €350 (Groei) en €500 (Compleet). Na het gesprek krijg je een vaste prijs op maat. Bekijk alle details op de <a href="prijzen.html" class="link-arrow">prijzenpagina</a></p></details>
          <details><summary>Moet ik zelf teksten en foto's aanleveren?</summary><p>Teksten schrijven we graag met je mee. Foto's en video's komen het liefst van jou, want niemand kent je zaak beter. We adviseren je wel over wat goed werkt.</p></details>
          <details><summary>Kan ik later nog dingen laten aanpassen?</summary><p>Ja. Met ons website-abonnement (vanaf €25 per maand) werken we je website elke maand bij. Zonder abonnement kan het ook; dan spreken we per aanpassing een prijs af.</p></details>
          <details><summary>Maken jullie ook posts voor social media?</summary><p>Dat bespreken we graag. We richten je profielen in en helpen met stijl en strategie. Content maken of posten valt buiten de pakketten en kost extra.</p></details>
          <details><summary>Ik heb al een website. Kunnen jullie die verbeteren?</summary><p>Zeker. We kijken eerst gratis naar je huidige site en vertellen eerlijk of verbeteren of opnieuw bouwen slimmer is.</p></details>
          <details><summary>Waar zitten jullie?</summary><p>We zitten in Breda en komen graag bij je langs in Noord-Brabant. Daarbuiten werken we net zo makkelijk via video of telefoon.</p></details>
        </div>
      </div>
    </section>

{cta()}  </main>

'''
werk += FOOTER

# ======================= OVER ONS =======================
over = head("over-ons.html", "Over ons | Halil & Sahin | Vizora Digital",
            "Vizora Digital is opgericht door de broers Halil en Sahin uit Breda. Een persoonlijk digitaal bureau voor ondernemers die willen groeien.")
over += header("over-ons.html")
over += f'''
  <main id="main">
{page_hero("Over ons", "Twee broers, één doel: jouw zaak laten <em>groeien</em>", "Wij zijn Halil en Sahin, de oprichters van Vizora Digital uit Breda.")}
    <section class="section">
      <div class="container split">
        <div class="duo reveal" aria-hidden="true">
          <div class="duo__card duo__card--1" data-speed="0.05"><span>H</span><p>Halil</p></div>
          <div class="duo__card duo__card--2" data-speed="-0.06"><span>S</span><p>Sahin</p></div>
          <div class="chip-card duo__badge" data-speed="-0.14"><div class="chip-card__icon">{I["users"]}</div><div><strong>Oprichters</strong><small>Vizora Digital</small></div></div>
        </div>
        <div>
          <p class="eyebrow reveal">Ons verhaal</p>
          <h2 class="split-words">Waarom we Vizora zijn <em>begonnen</em></h2>
          <p class="lead reveal">We zagen het overal om ons heen: ondernemers die keihard werken en echt goed zijn in hun vak, maar online bijna niet te vinden zijn. Of een website hebben die niet laat zien hoe goed ze eigenlijk zijn.</p>
          <p class="muted reveal">Grote bureaus zijn vaak duur en onpersoonlijk. Zelf doen kost te veel tijd. Daarom zijn we Vizora Digital gestart: een bureau dat de kwaliteit levert van een groot bureau, met de aandacht en snelheid van mensen die je gewoon even kunt bellen of appen.</p>
          <p class="muted reveal">De naam Vizora komt van <em>visie</em> en <em>zichtbaarheid.</em> Precies waar we je mee helpen: een duidelijk plan, en een zaak die gezien wordt.</p>
          <div class="hero__actions reveal" style="margin-top:1.4rem">
            <a href="contact.html" class="btn">Maak kennis met ons {I["arrow"]}</a>
            <a href="{TEL}" class="btn btn--ghost">{I["call"]} Bel direct</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--dark">
      <div class="container">
        <p class="quote split-words">“Jouw succes is ons visitekaartje. Als jouw zaak groeit, <em>groeien wij mee.</em>”</p>
        <p class="quote-by reveal">Halil &amp; Sahin</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section__head">
          <p class="eyebrow reveal">Waar we voor staan</p>
          <h2 class="split-words">Onze beloftes aan jou</h2>
        </div>
        <div class="values">
          <div class="value reveal"><span class="value__n" aria-hidden="true">01</span><h3>Persoonlijk</h3><p>Je werkt direct met ons. We kennen je zaak en denken met je mee alsof het onze eigen zaak is.</p></div>
          <div class="value reveal" data-delay="120"><span class="value__n" aria-hidden="true">02</span><h3>Eerlijk</h3><p>Duidelijke prijzen, heldere afspraken. En als iets niet nodig is, zeggen we dat ook.</p></div>
          <div class="value reveal" data-delay="240"><span class="value__n" aria-hidden="true">03</span><h3>Gericht op groei</h3><p>Mooi is niet genoeg. Alles wat we maken heeft één doel: meer bereik en meer klanten voor jou.</p></div>
        </div>
      </div>
    </section>

{cta("Zullen we <em>kennismaken?</em>", "We horen graag over jouw zaak. Plan een gratis gesprek of bel ons even; dan laten we zien wat we voor je kunnen doen.")}  </main>

'''
over += FOOTER

# ======================= CONTACT =======================
times = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
time_html = "\n".join(f'              <div class="choice"><input type="radio" name="tijd" id="t{i}" value="{t}"><label for="t{i}">{t}</label></div>' for i, t in enumerate(times))
cont = head("contact.html", "Plan een gratis gesprek | Contact | Vizora Digital",
            "Plan een gratis gesprek met Vizora Digital en ontvang een gratis concept van je website. Of bel direct: 06 38 70 53 48.")
cont += header("contact.html")
cont += f'''
  <main id="main">
{page_hero("Contact", "Plan een gratis gesprek, of <em>bel direct</em>", "Kies een moment dat jou uitkomt. Wij maken vooraf een concept van jouw website en nemen in het gesprek samen door hoe je zaak kan groeien. Liever meteen even bellen? Dat kan natuurlijk ook.")}
    <section class="section" style="padding-top:60px">
      <div class="container contact">
        <aside class="contact__aside">
          <p class="eyebrow reveal">Direct contact</p>
          <h2 class="split-words" style="font-size:clamp(1.7rem,3vw,2.3rem)">Bel, app of mail ons</h2>
          <ul class="contact__list reveal">
            <li><a href="{TEL}"><span class="icon">{I["call"]}</span><div><strong>Bel direct</strong><span>{TEL_TXT}</span></div></a></li>
            <li><a href="{WA}" target="_blank" rel="noopener"><span class="icon">{I["chat"]}</span><div><strong>WhatsApp</strong><span>{TEL_TXT}</span></div></a></li>
            <li><a href="mailto:{MAIL}"><span class="icon">{I["mail"]}</span><div><strong>E-mail</strong><span>{MAIL}</span></div></a></li>
          </ul>
          <p class="area reveal">{I["pin"]} Breda &amp; Noord-Brabant · ma t/m za 09:00 – 18:00</p>
          <div class="promise reveal" style="margin-top:1.2rem">
            <h3>Wat je van het gesprek krijgt</h3>
            <ul>
              <li>Een gratis concept van je nieuwe website</li>
              <li>Een eerlijke blik op je online uitstraling</li>
              <li>Een stappenplan om te groeien</li>
              <li>100% vrijblijvend</li>
            </ul>
          </div>
        </aside>

        <form class="booking reveal" id="booking" novalidate>
          <fieldset class="booking__step">
            <legend><span>1</span>Hoe wil je het gesprek voeren?</legend>
            <div class="choices">
              <div class="choice"><input type="radio" name="vorm" id="v1" value="Videogesprek" checked><label for="v1">Videogesprek</label></div>
              <div class="choice"><input type="radio" name="vorm" id="v2" value="Telefonisch gesprek"><label for="v2">Telefonisch</label></div>
              <div class="choice"><input type="radio" name="vorm" id="v3" value="Afspraak op locatie"><label for="v3">Op locatie <small>regio Breda</small></label></div>
            </div>
          </fieldset>

          <fieldset class="booking__step">
            <legend><span>2</span>Kies een dag</legend>
            <div class="dates"></div>
          </fieldset>

          <fieldset class="booking__step">
            <legend><span>3</span>Kies een tijd</legend>
            <div class="choices">
{time_html}
            </div>
          </fieldset>

          <fieldset class="booking__step">
            <legend><span>4</span>Waar ben je in geïnteresseerd?</legend>
            <div class="choices">
              <div class="choice"><input type="checkbox" name="dienst" id="d1" value="Website"><label for="d1">Website</label></div>
              <div class="choice"><input type="checkbox" name="dienst" id="d2" value="Marketing &amp; bereik"><label for="d2">Marketing &amp; bereik</label></div>
              <div class="choice"><input type="checkbox" name="dienst" id="d3" value="Social media"><label for="d3">Social media</label></div>
              <div class="choice"><input type="checkbox" name="dienst" id="d5" value="Website-abonnement"><label for="d5">Abonnement</label></div>
              <div class="choice"><input type="checkbox" name="dienst" id="d4" value="Weet ik nog niet"><label for="d4">Weet ik nog niet</label></div>
            </div>
          </fieldset>

          <fieldset class="booking__step">
            <legend><span>5</span>Je gegevens</legend>
            <div class="fields">
              <div class="fields__row">
                <label class="field">Naam *<input name="naam" type="text" required autocomplete="name" maxlength="80"></label>
                <label class="field">Bedrijfsnaam<input name="bedrijf" type="text" autocomplete="organization" maxlength="80"></label>
              </div>
              <label class="field">Telefoonnummer *<input name="telefoon" type="tel" required autocomplete="tel" inputmode="tel" maxlength="20"></label>
              <label class="field">Waar kunnen we je mee helpen? (optioneel)<textarea name="bericht" rows="3" maxlength="1000"></textarea></label>
            </div>
          </fieldset>

          <div class="booking__summary">{I["cal"]}<span data-summary aria-live="polite"></span></div>
          <p class="booking__error" role="alert"></p>
          <div class="booking__actions">
            <button type="submit" class="btn">{WA_SVG.replace('<svg ', '<svg fill="currentColor" ')} Verstuur via WhatsApp</button>
            <button type="button" class="btn btn--ghost" data-email>Via e-mail</button>
          </div>
          <p class="booking__note">We bevestigen je afspraak zo snel mogelijk. Past het moment niet? Dan stellen we een ander tijdstip voor.</p>
        </form>
      </div>
    </section>
  </main>

'''
cont += FOOTER


# ======================= PRIJZEN =======================
def row(label, a, b, c):
    cell = lambda v: '<td class="y">✓</td>' if v is True else ('<td class="n">—</td>' if v is False else f"<td>{v}</td>")
    return f"              <tr><td>{label}</td>{cell(a)}{cell(b)}{cell(c)}</tr>"

ROWS = "\n".join([
    row("Aantal pagina's", "1", "tot 5", "tot 5"),
    row("Ontwerp op maat", True, True, True),
    row("Perfect op mobiel", True, True, True),
    row("Bel-, WhatsApp- &amp; contactknoppen", True, True, True),
    row("Koppeling eigen domein", True, True, True),
    row("Basis vindbaarheid in Google", True, True, True),
    row("Animaties &amp; interactie", False, True, True),
    row("Online afspraken, reserveren of bestellen", False, True, True),
    row("Google Bedrijfsprofiel", False, True, True),
    row("Teksten schrijven", False, True, True),
    row("Lokale SEO", False, True, True),
    row("Logo &amp; huisstijl", False, False, True),
    row("Social media profielen inrichten", False, False, True),
    row("Persoonlijk groeiplan", False, False, True),
    row("1 maand gratis aanpassingen", False, False, True),
])

prijs = head("prijzen.html", "Prijzen | Websites vanaf €200 | Vizora Digital",
             "Duidelijke pakketten: Start vanaf €200, Groei vanaf €350, Compleet vanaf €500. Website-abonnement vanaf €25 per maand. Vizora Digital uit Breda.")
prijs += header("prijzen.html")
prijs += f"""
  <main id="main">
{page_hero("Prijzen", "Duidelijke pakketten, <em>eerlijke</em> prijzen", "Kies een pakket als startpunt. Na een gratis gesprek krijg je altijd eerst een offerte op maat, zodat je precies weet waar je aan toe bent.")}
    <section class="section" style="padding-top:70px">
      <div class="container">
        <div class="pricing">
{pricing_cards()}
        </div>
{SUBSCRIPTION}
        <p class="pricing__foot reveal">Alle pakketprijzen zijn vanaf-prijzen voor een eenmalig project. De definitieve prijs hangt af van je wensen.</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="section__head">
          <p class="eyebrow reveal">Vergelijken</p>
          <h2 class="split-words">Wat zit er in elk pakket?</h2>
        </div>
        <div class="table-wrap reveal">
          <table class="compare">
            <thead><tr><th scope="col">Inbegrepen</th><th scope="col">Start</th><th scope="col">Groei</th><th scope="col">Compleet</th></tr></thead>
            <tbody>
{ROWS}
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section__head">
          <p class="eyebrow reveal">Uitbreiden</p>
          <h2 class="split-words">Verder groeien, <em>wanneer</em> jij wilt</h2>
          <p class="reveal">Klaar voor de volgende stap? Deze diensten stemmen we samen af op jouw zaak.</p>
        </div>
        <div class="cards">
          <article class="card reveal"><div class="card__icon">{I["reach"]}</div><h3>Advertenties</h3><p>Google- en Meta-campagnes die nieuwe klanten uit jouw regio opleveren, met duidelijke rapportages.</p><a href="contact.html" class="link-arrow">Prijs op aanvraag</a></article>
          <article class="card reveal" data-delay="120"><div class="card__icon">{I["social"]}</div><h3>Social media content</h3><p>Content maken of posten voor jouw zaak. De invulling en prijs bespreken we samen, afhankelijk van wat je nodig hebt.</p><a href="contact.html" class="link-arrow">In overleg</a></article>
          <article class="card card--dark reveal" data-delay="240"><div class="card__icon">{I["shield"]}</div><h3>Website-abonnement</h3><p>Je website elke maand up-to-date, veilig en snel. Inclusief kleine aanpassingen en groeitips.</p><a href="contact.html?pakket=Abonnement" class="link-arrow">Vanaf €25 per maand</a></article>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container--narrow">
        <div class="section__head center">
          <p class="eyebrow reveal">Vragen over prijzen</p>
          <h2 class="split-words">Goed om te weten</h2>
        </div>
        <div class="faq reveal">
          <details><summary>Waarom staat er "vanaf"?</summary><p>Elke zaak is anders. De vanaf-prijs is wat je minimaal betaalt voor het pakket. Na het gratis gesprek krijg je een vaste prijs, zonder verrassingen.</p></details>
          <details><summary>Zijn er maandelijkse kosten?</summary><p>De pakketten zijn eenmalig. Wil je dat we je website elke maand bijwerken en onderhouden? Dan kun je een abonnement nemen vanaf €25 per maand. Je domeinnaam betaal je zelf (meestal een paar euro per jaar).</p></details>
          <details><summary>Welke abonnementen zijn er?</summary><p>Basis (€25 p/m): onderhoud, beveiliging en 1 kleine aanpassing per maand. Plus (€49 p/m): tot 3 aanpassingen, je Google Bedrijfsprofiel bijhouden en maandelijkse groeitips. Pro (€79 p/m): tot 6 aanpassingen, elk kwartaal een nieuwe pagina of actie en een maandelijks groeigesprek. Je ontvangt elke maand een factuur.</p></details>
          <details><summary>Maken jullie ook posts voor social media?</summary><p>In de pakketten richten we je profielen in en helpen we met stijl en strategie. Content maken of posten valt daarbuiten; dat bespreken we graag samen en kost extra.</p></details>
          <details><summary>Kan ik later upgraden?</summary><p>Ja. Begin je met Start, dan kun je altijd uitbreiden naar Groei of Compleet. Wat al gemaakt is, bouwen we gewoon verder uit.</p></details>
          <details><summary>Hoe betaal ik?</summary><p>Dat spreken we samen af in de offerte. Je weet vooraf precies wat je betaalt en wanneer.</p></details>
        </div>
      </div>
    </section>

{cta("Welk pakket past bij <em>jou?</em>", "Twijfel je? Plan een gratis gesprek of bel ons. We denken met je mee en adviseren eerlijk, ook als een kleiner pakket genoeg is.")}  </main>

"""
prijs += FOOTER

# ======================= EXTRA ONDERDELEN =======================
SWAP_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6 3 12l6 6M15 6l6 6-6 6"/></svg>'

BEFORE_AFTER = f'''    <section class="section" aria-labelledby="voorna-titel">
      <div class="container">
        <div class="section__head center">
          <p class="eyebrow reveal">Voor &amp; na</p>
          <h2 id="voorna-titel" class="split-words">Van verouderd naar <em>Vizora.</em></h2>
          <p class="reveal">Sleep de schuif en zie het verschil. Dezelfde barbershop, dezelfde prijzen. Alleen nu met een website die vertrouwen wekt en waar klanten direct online boeken.</p>
        </div>
        <div class="ba reveal" data-ba style="--pos:50%">
          <picture class="ba__img"><source media="(max-width: 640px)" srcset="assets/concepts/noir-mobile-45.jpg"><img src="assets/concepts/noir-desktop.jpg" alt="Nieuwe website van de barbershop, ontworpen door Vizora" width="2000" height="1000" loading="lazy" decoding="async" draggable="false"></picture>
          <div class="ba__before"><picture class="ba__img"><source media="(max-width: 640px)" srcset="assets/concepts/oud-mobile-45.jpg"><img src="assets/concepts/oud-desktop.jpg" alt="Oude, verouderde website van dezelfde barbershop" width="2000" height="1000" loading="lazy" decoding="async" draggable="false"></picture></div>
          <span class="ba__tag ba__tag--before">Voor</span>
          <span class="ba__tag ba__tag--after">Na · Vizora</span>
          <div class="ba__handle" aria-hidden="true"><span>{SWAP_ICON}</span></div>
          <input class="ba__range" type="range" min="0" max="100" value="50" aria-label="Schuif tussen de oude en de nieuwe website">
        </div>
        <ul class="ba__points reveal">
          <li><b>Online boeken</b><span>in plaats van bellen tijdens openingstijden</span></li>
          <li><b>Perfect op mobiel</b><span>waar de meeste klanten zoeken</span></li>
          <li><b>Professionele uitstraling</b><span>die past bij de kwaliteit van je werk</span></li>
        </ul>
      </div>
    </section>

'''

CALC = f'''    <section class="section" aria-labelledby="calc-titel">
      <div class="container calc" data-calc>
        <div class="calc__form">
          <p class="eyebrow reveal">Rekenvoorbeeld</p>
          <h2 id="calc-titel" class="split-words">Wat levert een betere website <em>jou</em> op?</h2>
          <p class="lead reveal">Vul je eigen cijfers in en zie hoe snel een nieuwe website zichzelf terugverdient. Schuif gerust: het zijn jouw getallen.</p>
          <div class="calc__fields reveal">
            <div class="choices" role="radiogroup" aria-label="Jouw branche">
              <div class="choice"><input type="radio" name="calc-type" id="ct1" value="kapper" checked><label for="ct1">Kapper</label></div>
              <div class="choice"><input type="radio" name="calc-type" id="ct2" value="restaurant"><label for="ct2">Restaurant</label></div>
              <div class="choice"><input type="radio" name="calc-type" id="ct3" value="salon"><label for="ct3">Salon</label></div>
              <div class="choice"><input type="radio" name="calc-type" id="ct4" value="bakkerij"><label for="ct4">Bakkerij</label></div>
              <div class="choice"><input type="radio" name="calc-type" id="ct5" value="anders"><label for="ct5">Anders</label></div>
            </div>
            <label class="slider"><span>Gemiddelde besteding per klant <output data-out="spend"></output></span><input type="range" name="spend" min="5" max="300" step="5"></label>
            <label class="slider"><span>Extra nieuwe klanten per maand <output data-out="extra"></output></span><input type="range" name="extra" min="1" max="40" step="1"></label>
            <label class="slider"><span>Bezoeken per klant per jaar <output data-out="freq"></output></span><input type="range" name="freq" min="1" max="30" step="1"></label>
          </div>
        </div>
        <div class="calc__result reveal" aria-live="polite">
          <span class="calc__label">Extra omzet in het eerste jaar</span>
          <strong class="calc__big" data-res="year">€ 0</strong>
          <div class="calc__rows">
            <div><span>Waarde van één vaste klant per jaar</span><b data-res="client">€ 0</b></div>
            <div><span>Groei-pakket (€350) terugverdiend na</span><b data-res="payback">0 bezoeken</b></div>
          </div>
          <p class="calc__note">Dit is een rekenvoorbeeld op basis van jouw eigen invoer, geen garantie. In het gratis gesprek kijken we samen wat realistisch is voor jouw zaak.</p>
          <a href="contact.html" class="btn btn--light">Bespreek mijn groei {I["arrow"]}</a>
        </div>
      </div>
    </section>

'''

INTRO = '''<div class="intro" aria-hidden="true">
    <div class="intro__logo">
      <svg viewBox="0 0 64 64"><path class="i-a" d="M8 10h12l15 44h-8z"/><path class="i-b" d="M56 10H44L29 54h8z"/><circle class="i-c" cx="32" cy="14" r="5"/></svg>
      <span class="intro__word"><b>Vizora</b><small>Digital</small></span>
    </div>
  </div>
  '''

home = home.replace('''    <section class="section section--alt" aria-labelledby="diensten-titel">''', BEFORE_AFTER + '''    <section class="section section--alt" aria-labelledby="diensten-titel">''', 1)
home = home.replace('''    <section class="section section--alt" aria-labelledby="prijzen-titel">''', CALC + '''    <section class="section section--alt" aria-labelledby="prijzen-titel">''', 1)
home = home.replace('<a class="skip" href="#main">Naar de inhoud</a>', INTRO + '<a class="skip" href="#main">Naar de inhoud</a>', 1)

# ======================= BRANCHE-PAGINA'S =======================
BRANCHES = [
  dict(file="website-voor-kappers.html", label="Kappers &amp; barbers", concept="noir", url="noir",
       title="Website voor kappers in Breda | Vizora Digital",
       desc="Een website voor je kapsalon of barbershop met online afspraken, prijslijst en vindbaarheid in Google. Vanuit Breda. Plan een gratis gesprek.",
       eyebrow="Voor kappers &amp; barbers in Breda",
       h1="Een website die je <em>agenda</em> vult",
       lead="Jij staat de hele dag achter de stoel. Je website werkt ondertussen door: klanten zien je prijzen, kiezen een tijd en boeken direct, ook 's avonds en in het weekend.",
       intro="Een goede kapperswebsite doet drie dingen: hij laat zien hoe goed je werk is, maakt boeken kinderlijk eenvoudig en zorgt dat mensen in de buurt je vinden als ze zoeken op 'kapper Breda' of 'barber in de buurt'.",
       features=["Online afspraken, 24/7", "Prijslijst die altijd klopt", "Team en specialisaties", "Openingstijden en walk-in", "Koppeling met je Instagram", "Gevonden in Google Maps"],
       why=[("Minder telefoontjes", "Geen gebel meer tijdens het knippen: klanten plannen zelf een moment dat past."),
            ("Boeken wanneer het uitkomt", "Veel afspraken worden 's avonds gemaakt, als je zaak dicht is. Je website is altijd open."),
            ("Een uitstraling met stijl", "Je zaak heeft een eigen sfeer. Je website laat die al zien voordat iemand binnenstapt.")],
       faq=[("Kan ik mijn bestaande boekingssysteem gebruiken?", "Ja. Gebruik je al een online agenda of boekingssysteem? Dan koppelen we dat aan je website. Heb je nog niets, dan adviseren we je wat het beste past."),
            ("Kan ik zelf mijn prijzen aanpassen?", "Met ons website-abonnement passen wij je prijzen, openingstijden en acties voor je aan. Stuur een appje en het staat erop."),
            ("Hoe word ik beter gevonden als kapper in Breda?", "Met een snelle website, de juiste teksten en een goed ingericht Google Bedrijfsprofiel. Dat zit in het pakket Groei en Compleet.")]),
  dict(file="website-voor-restaurants.html", label="Restaurants &amp; horeca", concept="olivo", url="olivo",
       title="Website voor restaurants in Breda | Vizora Digital",
       desc="Een restaurantwebsite met menukaart, online reserveren en afhalen. Meer gasten via Google. Vizora Digital uit Breda. Plan een gratis gesprek.",
       eyebrow="Voor restaurants &amp; horeca in Breda",
       h1="Een website die zin geeft om te <em>reserveren</em>",
       lead="Gasten kiezen met hun ogen, en ze kiezen online. Met een website die je sfeer laat proeven, een menukaart die altijd klopt en reserveren in een paar tikken.",
       intro="Mensen bekijken eerst je menu, je sfeer en je openingstijden voordat ze reserveren. Een sterke restaurantwebsite maakt die keuze makkelijk en zorgt dat je gevonden wordt als iemand zoekt naar 'uit eten in Breda'.",
       features=["Online reserveren", "Menukaart die altijd klopt", "Afhalen en bestellen", "Openingstijden en route", "Groepen en events", "Gevonden in Google Maps"],
       why=[("Meer reserveringen", "Een duidelijke reserveerknop op elke pagina. Geen gemiste telefoontjes in de spits."),
            ("Je menu als verleiding", "Een menukaart die er net zo goed uitziet als je gerechten, op elk scherm."),
            ("Altijd actueel", "Nieuw seizoensmenu of feestdag? Met het abonnement passen wij het voor je aan.")],
       faq=[("Kunnen jullie mijn reserveringssysteem koppelen?", "Ja. Gebruik je al een online reserveringssysteem, dan koppelen we dat. Zo niet, dan kiezen we samen een oplossing die past."),
            ("Kan de menukaart regelmatig veranderen?", "Zeker. Met het website-abonnement werken we je menu bij wanneer je wilt."),
            ("Kunnen gasten ook online bestellen voor afhalen?", "Dat kan. We bespreken in het gesprek wat het beste werkt voor jouw keuken.")]),
  dict(file="website-voor-beautysalons.html", label="Beautysalons", concept="serene", url="serene",
       title="Website voor beautysalons in Breda | Vizora Digital",
       desc="Een website voor je beauty- of nagelsalon met behandelingen, online boeken en cadeaubonnen. Vizora Digital uit Breda. Plan een gratis gesprek.",
       eyebrow="Voor beauty- en nagelsalons in Breda",
       h1="Een website die <em>rust</em> uitstraalt en boekt",
       lead="Je klanten komen bij jou om even tot rust te komen. Je website geeft dat gevoel al vanaf de eerste klik, en laat ze direct een behandeling plannen.",
       intro="Een salonwebsite moet vertrouwen geven: heldere behandelingen met prijzen en duur, een rustige uitstraling en boeken zonder gedoe. Zo kiezen nieuwe klanten voor jou in plaats van voor de salon verderop.",
       features=["Behandelingen met prijs en duur", "Online boeken", "Cadeaubonnen", "Resultaten van je werk", "Rustige, eigen huisstijl", "Gevonden in Google Maps"],
       why=[("Vertrouwen vanaf de eerste klik", "Een verzorgde website laat zien dat je net zo zorgvuldig werkt als je behandelingen."),
            ("Boeken zonder gedoe", "Klanten kiezen hun behandeling en een tijd, wanneer het hen uitkomt."),
            ("Meer uit je vaste klanten", "Cadeaubonnen en acties maken van tevreden klanten ambassadeurs.")],
       faq=[("Kan ik mijn bestaande agenda koppelen?", "Ja. Werk je al met een online agenda of boekingssysteem, dan koppelen we dat aan je website."),
            ("Kunnen klanten online een cadeaubon kopen?", "Dat bespreken we graag. Er zijn verschillende mogelijkheden, afhankelijk van hoe je nu werkt."),
            ("Kunnen jullie ook mijn Instagram inrichten?", "Ja. In het pakket Compleet richten we je profielen in, in dezelfde stijl als je website.")]),
  dict(file="website-voor-bakkerijen.html", label="Bakkerijen &amp; winkels", concept="goudkorst", url="goudkorst",
       title="Website voor bakkerijen in Breda | Vizora Digital",
       desc="Een website voor je bakkerij of winkel met assortiment, online bestellen en ophalen. Vizora Digital uit Breda. Plan een gratis gesprek.",
       eyebrow="Voor bakkerijen &amp; winkels in Breda",
       h1="Vandaag bestellen, morgen <em>vers</em> ophalen",
       lead="Je klanten willen weten wat er vandaag ligt, wanneer je open bent en of ze hun taart al kunnen bestellen. Je website regelt het, zodat jij kunt doen waar je goed in bent.",
       intro="Een bakkerij- of winkelwebsite laat je assortiment zien, maakt bestellen makkelijk en zorgt dat buurtbewoners je vinden. Minder telefoontjes, meer bestellingen en een uitstraling die net zo goed is als je producten.",
       features=["Online bestellen en ophalen", "Assortiment met prijzen", "Taarten op bestelling", "Openingstijden", "Acties van de week", "Gevonden in Google Maps"],
       why=[("Meer bestellingen", "Klanten bestellen 's avonds voor de volgende ochtend. Jij weet precies wat je moet bakken."),
            ("Minder telefoontjes", "Geen gebel over openingstijden of taarten: het staat allemaal duidelijk online."),
            ("Trots op je producten", "Je assortiment verdient een etalage die net zo verzorgd is als je vitrine.")],
       faq=[("Kunnen klanten online betalen?", "Dat kan, afhankelijk van wat je wilt. We bespreken samen of betalen bij het ophalen of online betalen het beste past."),
            ("Kan ik acties van de week laten plaatsen?", "Ja. Met het website-abonnement zetten we je acties en nieuwe producten online wanneer je wilt."),
            ("Werkt dit ook voor andere winkels?", "Zeker. Of je nu een bakkerij, slagerij, bloemenwinkel of boetiek hebt: de aanpak is hetzelfde.")]),
]

def branche_page(b):
    html = head(b["file"], b["title"], b["desc"])
    html += header("")
    feats = "".join(f"<li>{f}</li>" for f in b["features"])
    whys = "".join(f'<div class="benefit reveal" data-delay="{i*100}"><div class="icon">{I[ic]}</div><h3>{t}</h3><p>{d}</p></div>'
                   for i, ((t, d), ic) in enumerate(zip(b["why"], ["inbox", "growth", "shield"])))
    faqs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in b["faq"])
    others = " ".join(f'<a href="{o["file"]}" class="tag">{o["label"]}</a>' for o in BRANCHES if o is not b)
    html += f'''
  <main id="main">
{page_hero(b["eyebrow"], b["h1"], b["lead"])}
    <section class="section">
      <div class="container service">
        <div class="service__visual reveal" aria-hidden="true">
          <div class="plate plate--sand" style="inset:30px 0 10px 60px;rotate:6deg" data-speed="0.05"></div>
          <div class="plate plate--soft" style="inset:10px 40px 30px 20px;rotate:-3deg" data-speed="0.02"></div>
          {win(b["concept"] + "-desktop.jpg", "vizoradigital.nl/concept/" + b["url"], "left:0;right:70px;top:70px", "-0.04")}
          {iphone(b["concept"] + "-mobile.jpg", "right:0;bottom:0", "-0.1")}
        </div>
        <div class="service__copy">
          <p class="eyebrow reveal">Wat je website moet kunnen</p>
          <h2 class="split-words">Gemaakt voor <em>jouw</em> vak</h2>
          <p class="lead reveal">{b["intro"]}</p>
          <ul class="reveal">{feats}</ul>
          <div class="hero__actions reveal" style="margin:0">
            <a href="contact.html?branche={b["label"].split(" ")[0]}" class="btn">Plan een gratis gesprek {I["arrow"]}</a>
            <a href="{TEL}" class="btn btn--ghost">{I["call"]} Bel direct</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section--dark" style="margin:0;padding:90px 48px;border-radius:40px">
          <div class="section__head center">
            <p class="eyebrow reveal">Wat het je oplevert</p>
            <h2 class="split-words">Meer klanten, <em>minder</em> gedoe</h2>
          </div>
          <div class="benefits benefits--3">{whys}</div>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="section__head center">
          <p class="eyebrow reveal">Prijzen</p>
          <h2 class="split-words">Duidelijke pakketten, <em>eerlijke</em> prijzen</h2>
          <p class="reveal">Inclusief een gratis concept van je nieuwe website tijdens het eerste gesprek.</p>
        </div>
        <div class="pricing">
{pricing_cards()}
        </div>
        <p class="pricing__foot reveal"><a href="prijzen.html" class="link-arrow">Alle pakketten en abonnementen</a></p>
      </div>
    </section>

    <section class="section">
      <div class="container--narrow">
        <div class="section__head center">
          <p class="eyebrow reveal">Vragen</p>
          <h2 class="split-words">Goed om te weten</h2>
        </div>
        <div class="faq reveal">{faqs}</div>
        <p class="pricing__foot reveal">Ook voor: {others}</p>
      </div>
    </section>

{cta()}  </main>

'''
    return html + FOOTER

branche_pages = [(b["file"], branche_page(b)) for b in BRANCHES]

# ======================= 404 =======================
nf = head("404.html", "Pagina niet gevonden | Vizora Digital", "Deze pagina bestaat niet (meer).")
nf += header("")
nf += f'''
  <main id="main">
{page_hero("404", "Oeps, deze pagina is <em>zoek</em>", "De pagina die je zoekt bestaat niet (meer). Geen zorgen, we helpen je terug op weg.")}
    <section class="section section--tight"><div class="container"><a href="index.html" class="btn">Terug naar home {I["arrow"]}</a></div></section>
  </main>

'''
nf += FOOTER

import json
LD = {
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Vizora Digital",
  "url": SITE,
  "logo": SITE + "/assets/logo.svg",
  "image": SITE + "/assets/og.png",
  "description": "Websites, social media en marketing voor ondernemers in Breda en Noord-Brabant.",
  "telephone": "+31638705348",
  "email": MAIL,
  "priceRange": "€€",
  "address": {"@type": "PostalAddress", "addressLocality": "Breda", "addressRegion": "Noord-Brabant", "addressCountry": "NL"},
  "areaServed": [{"@type": "City", "name": "Breda"}, {"@type": "AdministrativeArea", "name": "Noord-Brabant"}],
  "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "09:00", "closes": "18:00"}],
  "founder": [{"@type": "Person", "name": "Halil"}, {"@type": "Person", "name": "Sahin"}],
}
home = home.replace("</head>", '  <script type="application/ld+json">' + json.dumps(LD, ensure_ascii=False) + "</script>\n</head>")
home = home.replace('<script src="assets/mosaic.js"></script>', '<script src="assets/mosaic.js"></script>\n  <script src="assets/contour.js"></script>')
home = home.replace('<link rel="stylesheet" href="assets/style.css">', '<link rel="preload" as="image" href="assets/concepts/olivo-desktop.jpg">\n  <link rel="stylesheet" href="assets/style.css">')

for name, html in [("index.html", home), ("diensten.html", dien), ("prijzen.html", prijs), ("werkwijze.html", werk), ("over-ons.html", over), ("contact.html", cont), ("404.html", nf)] + branche_pages:
    (OUT / name).write_text(html, encoding="utf-8")

(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /concepts/\nDisallow: /tools/\n\nSitemap: {SITE}/sitemap.xml\n")
urls = "".join(f"  <url><loc>{SITE}/{'' if p == 'index.html' else p}</loc></url>\n" for p in ["index.html", "diensten.html", "prijzen.html", "werkwijze.html", "over-ons.html", "contact.html"] + [b["file"] for b in BRANCHES])
(OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
print("ok")
