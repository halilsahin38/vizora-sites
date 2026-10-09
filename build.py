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
  "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
}
LOGO_MARK = '<svg class="logo__mark" viewBox="0 0 64 64" aria-hidden="true"><path class="lm-a" d="M8 10h12l15 44h-8z"/><path class="lm-b" d="M56 10H44L29 54h8z"/><circle class="lm-c" cx="32" cy="14" r="5"/></svg>'
LOGO = LOGO_MARK + '<span class="logo__word"><b>Vizora</b><small>Digital</small></span>'
WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2.1 1-2.4c.3-.3.6-.3.8-.3h.6c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.4 0 .5l-.4.6-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.5.1.6-.1l.9-1.1c.2-.3.4-.2.7-.1l2 1c.3.1.5.2.5.3.1.2.1.7-.1 1.3Z"/></svg>'

PAGES = [("index.html", "Home"), ("diensten.html", "Diensten"), ("prijzen.html", "Prijzen"), ("werkwijze.html", "Werkwijze"), ("over-ons.html", "Over ons")]

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
  <script>document.documentElement.classList.add("js")</script>
</head>
<body>
  <a class="skip" href="#main">Naar de inhoud</a>
'''

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
          <p>Websites, social media en marketing voor ondernemers die willen groeien. Vanuit Breda, voor heel Noord-Brabant.</p>
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
            <li><a href="diensten.html#social-media">Social media</a></li>
            <li><a href="diensten.html#marketing">Marketing</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <ul>
            <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp: 06 38 70 53 48</a></li>
            <li><a href="mailto:{MAIL}">{MAIL}</a></li>
            <li>Ma t/m za · 09:00 – 18:00</li>
            <li><a href="contact.html">Plan een gratis gesprek →</a></li>
          </ul>
        </div>
      </div>
      <div class="footer__big" aria-hidden="true">Vizora Digital</div>
      <div class="footer__bottom">
        <span>© <span data-year></span> Vizora Digital</span>
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

def cta(title="Klaar om online te <em>groeien?</em>", text="Plan een gratis kennismakingsgesprek van 20 minuten. We kijken samen naar je bedrijf en geven eerlijk advies, ook als je (nog) niets afneemt."):
    return f'''    <section class="section section--tight">
      <div class="container">
        <div class="cta reveal" data-mosaic>
          <div class="cta__glow cta__glow--1" aria-hidden="true"></div>
          <div class="cta__glow cta__glow--2" aria-hidden="true"></div>
          <h2 class="split-words">{title}</h2>
          <p>{text}</p>
          <div class="cta__actions">
            <a href="contact.html" class="btn btn--light">Plan een gratis gesprek {I["arrow"]}</a>
            <a href="{WA}" class="btn btn--ghost" target="_blank" rel="noopener">WhatsApp ons direct</a>
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

def browser(cls="", url="jouwbedrijf.nl", speed=None):
    sp = f' data-speed="{speed}"' if speed else ""
    return f'''<div class="browser {cls}"{sp}>
            <div class="browser__bar"><i></i><i></i><i></i><b>{url}</b></div>
            <div class="browser__body">
              <div class="browser__hero"></div>
              <div class="browser__line" style="width:70%"></div>
              <div class="browser__line" style="width:45%"></div>
              <div class="browser__row"><span></span><span></span><span></span></div>
            </div>
          </div>'''

def phone(style="", speed=None):
    sp = f' data-speed="{speed}"' if speed else ""
    return f'''<div class="phone" style="{style}"{sp}>
            <div class="phone__screen">
              <div class="phone__top"><i></i><b></b></div>
              <div class="phone__post"></div>
              <div class="phone__meta"><b></b><b></b></div>
            </div>
          </div>'''

def tile(cls, brand, headline, tag):
    return f'''<div class="tile {cls}"><div class="tile__bar">{brand}<span><i></i><i></i><i></i></span></div><div class="tile__hero"><b>{headline}</b><small></small></div><div class="tile__foot"><i></i><i></i><i></i></div><span class="tile__tag">{tag}</span></div>'''

def social(handle, text, bg, likes):
    return f'''<div class="tile tile--social"><div class="s-head"><i></i>{handle}</div><div class="s-img" style="background:{bg}">{text}</div><div class="s-meta"><span>♥ {likes}</span><span>💬 Reacties</span></div></div>'''

def stat(label, value, bars):
    b = "".join(f'<i style="height:{h}%"></i>' for h in bars)
    return f'''<div class="tile tile--stat"><small>{label}</small><strong>{value}</strong><div class="bars">{b}</div></div>'''

ROW1 = "\n            ".join([
  tile("t-barber", "BARBERSHOP", "Fresh cuts,<br>elke dag", "Kapper"),
  social("@jouwzaak", "Nieuwe look<br>voor de zomer", "linear-gradient(135deg,#6b5440,#d8c6aa)", "Likes"),
  tile("t-resto", "RISTORANTE", "Proef Italië<br>in jouw stad", "Restaurant"),
  stat("Online afspraken", "24/7 boekbaar", [30, 45, 40, 60, 55, 80, 95]),
  tile("t-beauty", "BEAUTY STUDIO", "Jouw moment<br>van rust", "Salon"),
  social("@jouwzaak", "Vandaag vers<br>uit de oven", "linear-gradient(135deg,#a37845,#e7c896)", "Likes"),
  tile("t-bakery", "BAKKERIJ", "Vers gebakken<br>met liefde", "Bakkerij"),
])
ROW2 = "\n            ".join([
  tile("t-coffee", "KOFFIEBAR", "Specialty<br>coffee &amp; brunch", "Horeca"),
  stat("Gevonden in Google", "Lokaal zichtbaar", [20, 35, 30, 50, 65, 70, 90]),
  tile("t-fysio", "FYSIOPRAKTIJK", "Weer zonder<br>pijn bewegen", "Zorg"),
  social("@jouwzaak", "Reserveer<br>je tafel", "linear-gradient(135deg,#7a3e22,#c98a55)", "Likes"),
  tile("t-build", "BOUW &amp; KLUS", "Vakwerk waar je<br>op kunt bouwen", "Vakman"),
  social("@jouwzaak", "Behind the<br>scenes", "linear-gradient(135deg,#2b241d,#6b5440)", "Likes"),
  stat("Nieuwe aanvragen", "Via je website", [25, 30, 45, 40, 60, 75, 100]),
])

PACKAGES = [
  ("Start", "Online zichtbaar", "200", "Voor starters en zzp'ers die snel en professioneel online willen.",
   ["One-page website op maat", "Perfect op mobiel", "WhatsApp-knop en contactformulier", "Basis vindbaarheid in Google", "Koppeling met je eigen domein"], False),
  ("Groei", "Meer klanten", "350", "Voor ondernemers die online echt klanten willen binnenhalen.",
   ["Website tot 5 pagina's", "Uniek ontwerp met animaties", "Online afspraken of reserveren", "Google Bedrijfsprofiel ingericht", "Teksten die overtuigen", "SEO voor jouw regio"], True),
  ("Compleet", "Alles geregeld", "500", "Website, social media en marketing in één keer goed.",
   ["Alles uit Groei", "Logo en huisstijl", "Instagram en Facebook ingericht", "9 startposts in jouw stijl", "Advies voor advertenties", "1 maand gratis aanpassingen"], False),
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

# ======================= HOME =======================
home = head("index.html", "Vizora Digital | Websites, social media & marketing die laten groeien",
            "Vizora Digital bouwt moderne websites en verzorgt social media en marketing voor kappers, restaurants en ondernemers die meer klanten willen. Plan een gratis gesprek.")
home += header("index.html")
home += f'''
  <main id="main">
    <section class="hero">
      <div class="blob blob--1" data-speed="0.12" aria-hidden="true"></div>
      <div class="blob blob--2" data-speed="-0.1" aria-hidden="true"></div>
      <div class="container hero__grid">
        <div class="hero__copy">
          <p class="eyebrow reveal">Websites · Social media · Marketing</p>
          <h1 class="split-words">Meer klanten, met een online uitstraling die <em>klopt.</em></h1>
          <p class="lead reveal" data-delay="400">Wij bouwen websites, social media en campagnes die jouw zaak laten opvallen. Vanuit Breda helpen we kappers, restaurants en elke ondernemer die verder wil groeien.</p>
          <div class="hero__actions reveal" data-delay="550">
            <a href="contact.html" class="btn">Plan een gratis gesprek {I["arrow"]}</a>
            <a href="diensten.html" class="btn btn--ghost">Bekijk diensten</a>
          </div>
          <ul class="hero__trust reveal" data-delay="700">
            <li>Persoonlijk contact</li>
            <li>Vanuit Breda</li>
            <li>Websites vanaf €200</li>
          </ul>
        </div>

        <div class="stage reveal" data-delay="200" aria-hidden="true">
          <div class="stage__plate stage__plate--1" data-speed="0.06"></div>
          <div class="stage__plate stage__plate--2" data-speed="0.03"></div>
          {browser(speed="-0.04", url="jouwzaak.nl")}
          {phone(speed="-0.12")}
          <div class="chip-card chip-card--a" data-speed="-0.18">
            <div class="chip-card__icon float">{I["cal"]}</div>
            <div><strong>Nieuwe afspraak</strong><small>via je website</small></div>
          </div>
          <div class="chip-card chip-card--b" data-speed="-0.08">
            <div class="chart"><i style="height:30%"></i><i style="height:45%"></i><i style="height:40%"></i><i style="height:65%"></i><i style="height:80%"></i><i style="height:100%"></i></div>
            <div><strong>Meer bereik</strong><small>social &amp; Google</small></div>
          </div>
        </div>
      </div>
      <div class="hero__scroll" aria-hidden="true"></div>
    </section>

    <section class="showcase" aria-labelledby="showcase-titel">
      <div class="container">
        <div class="section__head section__head--split">
          <div>
            <p class="eyebrow reveal">Ontwerp</p>
            <h2 id="showcase-titel" class="split-words">Design dat je <em>voelt.</em></h2>
          </div>
          <p class="muted reveal" style="max-width:24em">Klik op het beeld. Zo voelt een website die met aandacht is gemaakt: tot in de kleinste beweging.</p>
        </div>
        <div class="contour reveal" data-contour>
          <canvas role="img" aria-label="Wisselende beelden in beige tinten: architectuur, duinen, gelaagde vlakken en trappen"></canvas>
          <span class="contour__hint">Klik om te ontdekken</span>
          <div class="contour__ui">
            <div class="contour__caption" aria-live="polite">
              <span class="contour__count" data-count>01 / 04</span>
              <h3 data-title>Websites met karakter</h3>
              <p data-text>Geen standaard template, maar een ontwerp dat past bij jouw zaak.</p>
            </div>
            <button class="contour__next" type="button" data-next aria-label="Volgend beeld">{I["arrow"]}</button>
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
            <h2 id="concepten" class="split-words">Een uitstraling die past bij <em>jouw</em> zaak</h2>
          </div>
          <p class="muted reveal" style="max-width:26em">Van barbershop tot bakkerij: elk bedrijf krijgt een eigen ontwerp. Hieronder een paar concepten van wat mogelijk is.</p>
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
          <p class="lead reveal">Klanten zoeken eerst online. Vinden ze je niet, of ziet het er verouderd uit? Dan kiezen ze de zaak verderop.</p>
          <ul class="pain reveal">
            <li><div><strong>Geen of een verouderde website</strong><span>Mensen haken af voordat ze je hebben gebeld.</span></div></li>
            <li><div><strong>Social media zonder plan</strong><span>Af en toe een post, maar geen nieuwe klanten.</span></div></li>
            <li><div><strong>Geen tijd om het zelf te doen</strong><span>Jij runt je zaak, marketing schiet erbij in.</span></div></li>
          </ul>
        </div>
        <div>
          <p class="eyebrow reveal">Met Vizora</p>
          <h2 class="split-words">Wij regelen het, jij krijgt de <em>klanten.</em></h2>
          <p class="lead reveal">Eén vast team voor je website, social media en marketing. Alles klopt met elkaar en werkt samen.</p>
          <ul class="pain pain--good reveal">
            <li><div><strong>Een website die verkoopt</strong><span>Snel, mooi en gemaakt om afspraken of aanvragen op te leveren.</span></div></li>
            <li><div><strong>Content die opvalt</strong><span>Een vaste planning met posts die bij je merk passen.</span></div></li>
            <li><div><strong>Gevonden worden</strong><span>In Google, Google Maps en op social media.</span></div></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section section--alt" aria-labelledby="diensten-titel">
      <div class="container">
        <div class="section__head">
          <p class="eyebrow reveal">Diensten</p>
          <h2 id="diensten-titel" class="split-words">Alles voor je online groei, onder één dak</h2>
          <p class="reveal">Kies wat je nodig hebt, of laat ons het complete plaatje verzorgen.</p>
        </div>
        <div class="cards">
          <article class="card reveal">
            <span class="card__num">01</span>
            <div class="card__icon">{I["web"]}</div>
            <h3>Websites</h3>
            <p>Een moderne website die vertrouwen geeft en bezoekers omzet in klanten.</p>
            <ul><li>Ontwerp op maat</li><li>Online afspraken of reserveren</li><li>Perfect op mobiel</li></ul>
            <a href="diensten.html#websites" class="link-arrow">Meer over websites</a>
          </article>
          <article class="card card--dark reveal" data-delay="120">
            <span class="card__num">02</span>
            <div class="card__icon">{I["social"]}</div>
            <h3>Social media</h3>
            <p>Professionele content en een vaste planning, zodat je top-of-mind blijft.</p>
            <ul><li>Instagram, TikTok &amp; Facebook</li><li>Posts, reels en stories</li><li>Herkenbare huisstijl</li></ul>
            <a href="diensten.html#social-media" class="link-arrow">Meer over social media</a>
          </article>
          <article class="card reveal" data-delay="240">
            <span class="card__num">03</span>
            <div class="card__icon">{I["growth"]}</div>
            <h3>Marketing</h3>
            <p>Gerichte campagnes die nieuwe klanten naar je zaak of website brengen.</p>
            <ul><li>Google &amp; Meta advertenties</li><li>Google Bedrijfsprofiel</li><li>Heldere resultaten</li></ul>
            <a href="diensten.html#marketing" class="link-arrow">Meer over marketing</a>
          </article>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="demo-titel">
      <div class="container demo" data-demo>
        <div class="demo__controls">
          <div>
            <p class="eyebrow reveal">Probeer het zelf</p>
            <h2 id="demo-titel" class="split-words">Zie direct hoe <em>jouw</em> website eruit kan zien</h2>
            <p class="lead reveal">Typ je bedrijfsnaam, kies je branche en bekijk een eerste voorproefje. Het echte ontwerp maken we samen, helemaal op maat.</p>
          </div>
          <div class="reveal">
            <label class="demo__label" for="demo-name">Bedrijfsnaam</label>
            <input class="demo__input" id="demo-name" type="text" maxlength="30" placeholder="Bijv. Barbershop Breda" autocomplete="organization" data-demo-input>
          </div>
          <fieldset class="reveal" style="border:0;padding:0;margin:0">
            <legend class="demo__label">Branche</legend>
            <div class="choices">
              <div class="choice"><input type="radio" name="demo-type" id="dt1" value="Kapper" checked><label for="dt1">Kapper</label></div>
              <div class="choice"><input type="radio" name="demo-type" id="dt2" value="Restaurant"><label for="dt2">Restaurant</label></div>
              <div class="choice"><input type="radio" name="demo-type" id="dt3" value="Salon"><label for="dt3">Salon</label></div>
              <div class="choice"><input type="radio" name="demo-type" id="dt4" value="Bedrijf"><label for="dt4">Ander bedrijf</label></div>
            </div>
          </fieldset>
          <div class="reveal"><a href="contact.html" class="btn" data-demo-go>Dit wil ik voor mijn zaak {I["arrow"]}</a></div>
        </div>
        <div class="demo__view reveal" data-demo-view data-theme="barber" aria-live="polite">
          <div class="site">
            <div class="site__bar"><i></i><i></i><i></i><b data-demo-url>jouwzaak.nl</b></div>
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
    </section>

    <section class="section">
      <div class="container">
        <div class="section--dark" style="margin:0;padding:90px 48px;border-radius:40px">
          <div class="section__head center">
            <p class="eyebrow reveal">Waarom Vizora</p>
            <h2 class="split-words">Geen groot bureau, wel <em>grote</em> aandacht</h2>
            <p class="reveal">Je werkt direct met de makers. Geen accountmanagers, geen wachttijden.</p>
          </div>
          <div class="benefits">
            <div class="benefit reveal"><div class="icon">{I["chat"]}</div><h3>Direct contact</h3><p>Gewoon even appen. Je spreekt altijd met Halil of Sahin.</p></div>
            <div class="benefit reveal" data-delay="100"><div class="icon">{I["bolt"]}</div><h3>Korte lijnen</h3><p>Geen lange trajecten of wachttijden. We schakelen snel en houden je steeds op de hoogte.</p></div>
            <div class="benefit reveal" data-delay="200"><div class="icon">{I["phone"]}</div><h3>Mobiel eerst</h3><p>De meeste klanten kijken op hun telefoon. Daar ontwerpen we voor.</p></div>
            <div class="benefit reveal" data-delay="300"><div class="icon">{I["shield"]}</div><h3>Eerlijk advies</h3><p>Vooraf een duidelijke offerte. Geen verrassingen achteraf.</p></div>
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
          <li class="step reveal"><span class="step__n">01</span><h3>Kennismaken</h3><p>Gratis gesprek over je zaak, je klanten en je doelen.</p></li>
          <li class="step reveal" data-delay="100"><span class="step__n">02</span><h3>Ontwerp</h3><p>Je ziet eerst een ontwerp. Pas als jij blij bent, bouwen we.</p></li>
          <li class="step reveal" data-delay="200"><span class="step__n">03</span><h3>Lancering</h3><p>We bouwen, testen en zetten alles live. Jij hoeft niks technisch te doen.</p></li>
          <li class="step reveal" data-delay="300"><span class="step__n">04</span><h3>Groeien</h3><p>Met social media en marketing zorgen we voor nieuwe klanten.</p></li>
        </ol>
      </div>
    </section>

{cta()}  </main>

'''
home += FOOTER

# ======================= DIENSTEN =======================
dash_svg = '''<svg viewBox="0 0 300 110" preserveAspectRatio="none" aria-hidden="true"><defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d8c6aa"/><stop offset="1" stop-color="#d8c6aa" stop-opacity="0"/></linearGradient></defs><path class="area" d="M0 95 C40 90 60 80 90 78 S140 60 170 55 S230 30 300 10 V110 H0Z"/><path class="line" d="M0 95 C40 90 60 80 90 78 S140 60 170 55 S230 30 300 10"/></svg>'''

dien = head("diensten.html", "Diensten | Websites, social media & marketing | Vizora Digital",
            "Websites op maat, social media beheer en online marketing voor lokale ondernemers. Ontdek wat Vizora Digital voor jouw bedrijf kan doen.")
dien += header("diensten.html")
dien += f'''
  <main id="main">
{page_hero("Diensten", "Alles wat je nodig hebt om online te <em>groeien</em>", "Een sterke website, social media die opvalt en marketing die klanten oplevert. Los af te nemen of als compleet pakket.")}
    <section class="section">
      <div class="container">
        <div class="service" id="websites">
          <div class="service__visual reveal" aria-hidden="true">
            <div class="plate plate--sand" style="inset:30px 0 10px 60px;rotate:6deg" data-speed="0.05"></div>
            <div class="plate plate--soft" style="inset:10px 40px 30px 20px;rotate:-3deg" data-speed="0.02"></div>
            {browser(speed="-0.05", url="jouwzaak.nl").replace('class="browser "', 'class="browser" style="inset:50px 60px 60px 40px"')}
            <div class="chip-card" style="right:0;bottom:30px" data-speed="-0.14"><div class="chip-card__icon">{I["bolt"]}</div><div><strong>Supersnel</strong><small>laadt in een oogwenk</small></div></div>
          </div>
          <div class="service__copy">
            <p class="eyebrow reveal">01 · Websites</p>
            <h2 class="split-words">Een website die werkt als je <em>beste verkoper</em></h2>
            <p class="lead reveal">Je website is vaak het eerste wat een klant van je ziet. Wij zorgen dat die indruk klopt, en dat bezoekers ook echt contact opnemen of een afspraak maken.</p>
            <ul class="reveal">
              <li>Uniek ontwerp, geen standaard template</li>
              <li>Perfect op telefoon, tablet en laptop</li>
              <li>Online afspraken, reserveren of offertes</li>
              <li>Basis voor vindbaarheid in Google (SEO)</li>
              <li>Teksten die klanten overtuigen</li>
              <li>Hosting, beveiliging en onderhoud geregeld</li>
            </ul>
            <a href="contact.html" class="btn reveal">Bespreek je website {I["arrow"]}</a>
          </div>
        </div>

        <div class="service service--flip" id="social-media">
          <div class="service__visual reveal" aria-hidden="true">
            <div class="plate plate--sand" style="inset:40px 50px 0 0;rotate:-6deg" data-speed="0.05"></div>
            <div class="feed" style="left:20px;top:30px;width:300px" data-speed="-0.04"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
            {phone("right:10px;top:70px", speed="-0.12")}
            <div class="chip-card" style="left:0;bottom:20px" data-speed="-0.18"><div class="chip-card__icon">{I["social"]}</div><div><strong>Vaste planning</strong><small>elke week zichtbaar</small></div></div>
          </div>
          <div class="service__copy">
            <p class="eyebrow reveal">02 · Social media</p>
            <h2 class="split-words">Zichtbaar blijven, zonder dat jij er <em>omkijken</em> naar hebt</h2>
            <p class="lead reveal">Klanten volgen je op Instagram en TikTok. Wij zorgen voor content die bij je zaak past, consistent wordt geplaatst en mensen naar binnen trekt.</p>
            <ul class="reveal">
              <li>Contentplanning per maand</li>
              <li>Posts, reels en stories</li>
              <li>Herkenbare huisstijl en templates</li>
              <li>Teksten en hashtags</li>
              <li>Profiel optimaliseren</li>
              <li>Maandelijks overzicht van resultaten</li>
            </ul>
            <a href="contact.html" class="btn reveal">Bespreek social media {I["arrow"]}</a>
          </div>
        </div>

        <div class="service" id="marketing">
          <div class="service__visual reveal" aria-hidden="true">
            <div class="plate plate--soft" style="inset:20px 30px 40px 30px;rotate:4deg" data-speed="0.03"></div>
            <div class="dash" style="left:40px;right:40px;top:110px" data-speed="-0.05">
              <small>Websitebezoekers</small>
              <strong>Meer bezoekers</strong>
              {dash_svg}
            </div>
            <div class="chip-card" style="right:0;top:10px" data-speed="-0.15"><div class="chip-card__icon">{I["search"]}</div><div><strong>Google</strong><small>bovenaan gevonden</small></div></div>
            <div class="chip-card" style="left:0;bottom:30px" data-speed="-0.1"><div class="chip-card__icon">{I["pin"]}</div><div><strong>Google Maps</strong><small>lokaal zichtbaar</small></div></div>
          </div>
          <div class="service__copy">
            <p class="eyebrow reveal">03 · Marketing</p>
            <h2 class="split-words">Nieuwe klanten, precies uit <em>jouw</em> omgeving</h2>
            <p class="lead reveal">Met gerichte advertenties en een sterk Google-profiel bereik je mensen die nu op zoek zijn naar wat jij aanbiedt.</p>
            <ul class="reveal">
              <li>Google Ads campagnes</li>
              <li>Instagram &amp; Facebook advertenties</li>
              <li>Google Bedrijfsprofiel inrichten</li>
              <li>Meer en betere reviews krijgen</li>
              <li>Lokale SEO</li>
              <li>Duidelijke rapportages</li>
            </ul>
            <a href="contact.html" class="btn reveal">Bespreek marketing {I["arrow"]}</a>
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
          <article class="card reveal"><div class="card__icon">{I["pen"]}</div><h3>Logo &amp; huisstijl</h3><p>Een herkenbaar logo, kleuren en lettertypes die overal terugkomen: van je website tot je Instagram.</p></article>
          <article class="card reveal" data-delay="120"><div class="card__icon">{I["mail"]}</div><h3>Zakelijke e-mail</h3><p>Mailen vanaf info@jouwzaak.nl in plaats van een Gmail-adres. Direct professioneler.</p></article>
          <article class="card reveal" data-delay="240"><div class="card__icon">{I["shield"]}</div><h3>Onderhoud</h3><p>Wij houden je website snel, veilig en up-to-date. Even iets aanpassen? Stuur een appje.</p></article>
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
          <li>Kappers &amp; barbers</li><li>Restaurants &amp; cafés</li><li>Beautysalons &amp; nagelstudio's</li><li>Bakkerijen</li>
          <li>Winkels</li><li>Sportscholen &amp; personal trainers</li><li>Zorg &amp; fysio</li><li>Bouw &amp; vakmensen</li><li>Starters &amp; zzp'ers</li>
        </ul>
      </div>
    </section>

{cta("Niet zeker wat je <em>nodig</em> hebt?", "Geen probleem. In een gratis gesprek kijken we samen wat het meeste oplevert voor jouw zaak, en wat je beter (nog) niet kunt doen.")}  </main>

'''
dien += FOOTER

# ======================= WERKWIJZE =======================
werk = head("werkwijze.html", "Werkwijze | Zo werken wij | Vizora Digital",
            "Van gratis kennismaking tot een website die klanten oplevert. Bekijk in 5 duidelijke stappen hoe Vizora Digital werkt.")
werk += header("werkwijze.html")
werk += f'''
  <main id="main">
{page_hero("Werkwijze", "Duidelijk, persoonlijk en <em>snel</em> online", "Je weet altijd waar je aan toe bent. Zo gaan we stap voor stap van idee naar resultaat.")}
    <section class="section">
      <div class="container--narrow">
        <div class="timeline">
          <div class="timeline__line" aria-hidden="true"><i></i></div>
          <article class="tl-item"><div class="tl-item__dot">1</div><span class="tl-item__meta">Gratis · ± 20 minuten</span><h3>Kennismaken</h3><p>We leren je bedrijf kennen: wat doe je, wie zijn je klanten en wat wil je bereiken? Telefonisch, via video of bij jou op locatie in de regio Breda.</p></article>
          <article class="tl-item"><div class="tl-item__dot">2</div><span class="tl-item__meta">Binnen een paar dagen</span><h3>Voorstel &amp; offerte</h3><p>Je krijgt een helder voorstel met wat we gaan doen, wat het kost en wanneer het klaar is. Geen kleine lettertjes.</p></article>
          <article class="tl-item"><div class="tl-item__dot">3</div><span class="tl-item__meta">Jij denkt mee</span><h3>Ontwerp</h3><p>We maken een ontwerp dat past bij jouw zaak. Je geeft feedback en wij passen aan tot je er helemaal blij mee bent.</p></article>
          <article class="tl-item"><div class="tl-item__dot">4</div><span class="tl-item__meta">Wij doen het werk</span><h3>Bouwen &amp; lanceren</h3><p>We bouwen alles, schrijven de teksten mee en testen op elk apparaat. Daarna gaat je site live op je eigen domein.</p>
            <ul><li>Domein en hosting geregeld</li><li>Snel en veilig (https)</li><li>Aangemeld bij Google</li></ul></article>
          <article class="tl-item"><div class="tl-item__dot">5</div><span class="tl-item__meta">Doorlopend</span><h3>Groeien</h3><p>Een website is pas het begin. Met social media, advertenties en een sterk Google-profiel zorgen we dat er ook klanten blijven komen.</p></article>
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
          <details><summary>Hoe lang duurt het voordat mijn website online staat?</summary><p>Dat hangt af van de grootte van je website en hoe snel de inhoud (teksten, foto's) rond is. In het kennismakingsgesprek krijg je een duidelijke planning.</p></details>
          <details><summary>Wat kost een website of social media?</summary><p>Dat hangt af van wat je nodig hebt. Na het gratis kennismakingsgesprek krijg je een duidelijke offerte op maat, zonder verrassingen achteraf.</p></details>
          <details><summary>Moet ik zelf teksten en foto's aanleveren?</summary><p>Dat mag, maar het hoeft niet. We schrijven de teksten graag met je mee en adviseren over foto's.</p></details>
          <details><summary>Kan ik later nog dingen laten aanpassen?</summary><p>Ja, natuurlijk. Stuur een berichtje en we passen het aan. Met een onderhoudsabonnement zit dat er gewoon bij in.</p></details>
          <details><summary>Ik heb al een website. Kunnen jullie die verbeteren?</summary><p>Zeker. We kijken eerst gratis naar je huidige site en vertellen eerlijk of verbeteren of opnieuw bouwen slimmer is.</p></details>
          <details><summary>Kan ik ook alleen social media of marketing afnemen?</summary><p>Ja. Je kunt elke dienst los afnemen, ook zonder nieuwe website.</p></details>
          <details><summary>Waar zitten jullie?</summary><p>We zitten in Breda en komen graag bij je langs in Noord-Brabant. Daarbuiten werken we net zo makkelijk via video of telefoon.</p></details>
        </div>
      </div>
    </section>

{cta()}  </main>

'''
werk += FOOTER

# ======================= OVER ONS =======================
over = head("over-ons.html", "Over ons | Halil & Sahin | Vizora Digital",
            "Vizora Digital is opgericht door de broers Halil en Sahin. Een persoonlijk digitaal bureau voor ondernemers die willen groeien.")
over += header("over-ons.html")
over += f'''
  <main id="main">
{page_hero("Over ons", "Twee broers, één doel: jouw zaak laten <em>groeien</em>", "Wij zijn Halil en Sahin, de oprichters van Vizora Digital.")}
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
          <p class="muted reveal">Grote bureaus zijn vaak duur en onpersoonlijk. Zelf doen kost te veel tijd. Daarom zijn we Vizora Digital gestart: een bureau dat de kwaliteit levert van een groot bureau, met de aandacht en snelheid van mensen die je gewoon even kunt appen.</p>
          <p class="muted reveal">De naam Vizora komt van <em>visie</em> en <em>zichtbaarheid.</em> Precies waar we je mee helpen.</p>
          <a href="contact.html" class="btn reveal" style="margin-top:1rem">Maak kennis met ons {I["arrow"]}</a>
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
          <div class="value reveal"><span class="value__n">01</span><h3>Persoonlijk</h3><p>Je werkt direct met ons. We kennen je zaak en denken met je mee alsof het onze eigen zaak is.</p></div>
          <div class="value reveal" data-delay="120"><span class="value__n">02</span><h3>Eerlijk</h3><p>Duidelijke prijzen, heldere afspraken. En als iets niet nodig is, zeggen we dat ook.</p></div>
          <div class="value reveal" data-delay="240"><span class="value__n">03</span><h3>Resultaatgericht</h3><p>Mooi is niet genoeg. Alles wat we maken heeft één doel: meer klanten voor jou.</p></div>
        </div>
      </div>
    </section>

{cta("Zullen we <em>kennismaken?</em>", "We horen graag over jouw zaak. Plan een gratis gesprek, dan drinken we (virtueel) een kop koffie.")}  </main>

'''
over += FOOTER

# ======================= CONTACT =======================
times = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
time_html = "\n".join(f'              <div class="choice"><input type="radio" name="tijd" id="t{i}" value="{t}"><label for="t{i}">{t}</label></div>' for i, t in enumerate(times))
cont = head("contact.html", "Plan een gratis gesprek | Contact | Vizora Digital",
            "Plan een gratis kennismakingsgesprek met Vizora Digital. Kies een dag en tijd, of stuur direct een WhatsApp-bericht.")
cont += header("contact.html")
cont += f'''
  <main id="main">
{page_hero("Contact", "Plan een gratis <em>kennismakingsgesprek</em>", "Kies een moment dat jou uitkomt. Binnen 20 minuten weet je wat wij voor jouw zaak kunnen betekenen. Vrijblijvend.")}
    <section class="section" style="padding-top:60px">
      <div class="container contact">
        <aside class="contact__aside">
          <p class="eyebrow reveal">Liever direct contact?</p>
          <h2 class="split-words" style="font-size:clamp(1.7rem,3vw,2.3rem)">We reageren meestal dezelfde dag</h2>
          <ul class="contact__list reveal">
            <li><a href="{WA}" target="_blank" rel="noopener"><span class="icon">{I["chat"]}</span><div><strong>WhatsApp</strong><span>06 38 70 53 48</span></div></a></li>
            <li><a href="tel:+31638705348"><span class="icon">{I["phone"]}</span><div><strong>Bellen</strong><span>06 38 70 53 48</span></div></a></li>
            <li><a href="mailto:{MAIL}"><span class="icon">{I["mail"]}</span><div><strong>E-mail</strong><span>{MAIL}</span></div></a></li>
          </ul>
          <p class="area reveal">{I["pin"]} Breda &amp; Noord-Brabant · ma t/m za 09:00 – 18:00</p>
          <div class="promise reveal" style="margin-top:1.2rem">
            <h3>Wat je van het gesprek krijgt</h3>
            <ul>
              <li>Eerlijke blik op je huidige online uitstraling</li>
              <li>Concrete tips die je direct kunt gebruiken</li>
              <li>Een voorstel op maat, als je dat wilt</li>
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
              <div class="choice"><input type="checkbox" name="dienst" id="d2" value="Social media"><label for="d2">Social media</label></div>
              <div class="choice"><input type="checkbox" name="dienst" id="d3" value="Marketing"><label for="d3">Marketing</label></div>
              <div class="choice"><input type="checkbox" name="dienst" id="d4" value="Weet ik nog niet"><label for="d4">Weet ik nog niet</label></div>
            </div>
          </fieldset>

          <fieldset class="booking__step">
            <legend><span>5</span>Je gegevens</legend>
            <div class="fields">
              <div class="fields__row">
                <label class="field">Naam *<input name="naam" type="text" required autocomplete="name"></label>
                <label class="field">Bedrijfsnaam<input name="bedrijf" type="text" autocomplete="organization"></label>
              </div>
              <label class="field">Telefoonnummer *<input name="telefoon" type="tel" required autocomplete="tel" inputmode="tel"></label>
              <label class="field">Waar kunnen we je mee helpen? (optioneel)<textarea name="bericht" rows="3"></textarea></label>
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
    row("WhatsApp-knop &amp; contactformulier", True, True, True),
    row("Koppeling eigen domein", True, True, True),
    row("Basis vindbaarheid in Google", True, True, True),
    row("Animaties &amp; interactie", False, True, True),
    row("Online afspraken of reserveren", False, True, True),
    row("Google Bedrijfsprofiel", False, True, True),
    row("Teksten schrijven", False, True, True),
    row("Logo &amp; huisstijl", False, False, True),
    row("Social media profielen inrichten", False, False, True),
    row("9 startposts", False, False, True),
    row("1 maand gratis aanpassingen", False, False, True),
])

prijs = head("prijzen.html", "Prijzen | Websites vanaf €200 | Vizora Digital",
             "Duidelijke pakketten voor je website, social media en marketing. Start vanaf €200, Groei vanaf €350, Compleet vanaf €500. Vanuit Breda.")
prijs += header("prijzen.html")
prijs += f"""
  <main id="main">
{page_hero("Prijzen", "Duidelijke pakketten, <em>eerlijke</em> prijzen", "Kies een pakket als startpunt. Na een gratis gesprek krijg je altijd eerst een offerte op maat, zodat je precies weet waar je aan toe bent.")}
    <section class="section" style="padding-top:70px">
      <div class="container">
        <div class="pricing">
{pricing_cards()}
        </div>
        <p class="pricing__foot reveal">Alle prijzen zijn vanaf-prijzen voor een eenmalig project. De definitieve prijs hangt af van je wensen.</p>
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
          <p class="eyebrow reveal">Doorlopend</p>
          <h2 class="split-words">Na de lancering <em>blijven</em> groeien</h2>
          <p class="reveal">Naast een pakket kun je ons ook maandelijks inschakelen. De prijs stemmen we af op wat je nodig hebt.</p>
        </div>
        <div class="cards">
          <article class="card reveal"><div class="card__icon">{I["social"]}</div><h3>Social media beheer</h3><p>Wij maken en plaatsen elke maand content, zodat je zichtbaar blijft.</p><a href="contact.html" class="link-arrow">Prijs op aanvraag</a></article>
          <article class="card card--dark reveal" data-delay="120"><div class="card__icon">{I["growth"]}</div><h3>Advertenties</h3><p>Google- en Meta-campagnes die nieuwe klanten uit jouw regio opleveren.</p><a href="contact.html" class="link-arrow">Prijs op aanvraag</a></article>
          <article class="card reveal" data-delay="240"><div class="card__icon">{I["shield"]}</div><h3>Onderhoud</h3><p>Je website snel, veilig en up-to-date. Even iets aanpassen? Stuur een appje.</p><a href="contact.html" class="link-arrow">Prijs op aanvraag</a></article>
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
          <details><summary>Zijn er maandelijkse kosten?</summary><p>De pakketten zijn eenmalig. Je betaalt zelf je domeinnaam (meestal een paar euro per jaar). Social media beheer, advertenties en onderhoud zijn optioneel.</p></details>
          <details><summary>Kan ik later upgraden?</summary><p>Ja. Begin je met Start, dan kun je altijd uitbreiden naar Groei of Compleet. Wat al gemaakt is, bouwen we gewoon verder uit.</p></details>
          <details><summary>Hoe betaal ik?</summary><p>Dat spreken we samen af in de offerte. Je weet vooraf precies wat je betaalt en wanneer.</p></details>
        </div>
      </div>
    </section>

{cta("Welk pakket past bij <em>jou?</em>", "Twijfel je? Plan een gratis gesprek. We denken met je mee en adviseren eerlijk, ook als een kleiner pakket genoeg is.")}  </main>

"""
prijs += FOOTER

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

for name, html in [("index.html", home), ("diensten.html", dien), ("prijzen.html", prijs), ("werkwijze.html", werk), ("over-ons.html", over), ("contact.html", cont), ("404.html", nf)]:
    (OUT / name).write_text(html, encoding="utf-8")

(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
urls = "".join(f"  <url><loc>{SITE}/{'' if p == 'index.html' else p}</loc></url>\n" for p in ["index.html", "diensten.html", "prijzen.html", "werkwijze.html", "over-ons.html", "contact.html"])
(OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
print("ok")
