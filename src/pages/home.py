from core import *  # noqa: F401,F403

FILE = "index.html"

STYLES = [
    ("merk", "Donker &amp; luxe", "Diep zwart met warm goud. Voor een zaak die indruk wil maken."),
    ("licht", "Licht &amp; strak", "Veel wit en één rustige kleur. Helder, modern en zakelijk."),
    ("warm", "Warm &amp; persoonlijk", "Zachte tinten en ronde vormen. Vriendelijk en uitnodigend."),
]

STEPS = [
    ("Plan een gesprek", "Kies een moment dat jou uitkomt, of bel of app ons direct. Gratis en vrijblijvend."),
    ("Wij maken je concept", "Voor het gesprek ontwerpen we alvast een eerste versie van jouw website, op maat."),
    ("Pas dan beslis je", "Enthousiast? Dan bouwen we verder. Zo niet, dan heb je niets betaald."),
]


def _shots():
    # De laptop- en telefoonfoto's zijn per stijl identiek, alleen het scherm verschilt.
    # Daardoor lijkt het alsof alleen de website wisselt.
    out = []
    for i, (key, name, _) in enumerate(STYLES):
        on = " is-on" if i == 0 else ""
        plain = name.replace("&amp;", "en")
        laptop = pic(f"{key}-laptop", f"Voorbeeldwebsite in de stijl {plain} op een laptop", 1500, 1213)
        phone = pic(f"{key}-telefoon", f"Dezelfde website in de stijl {plain} op een telefoon", 1100, 1286, pos="52% 40%")
        out.append(f'''            <div class="sw__shot{on}" data-sw-shot="{i}"{"" if i == 0 else ' aria-hidden="true"'}>
              <div class="sw__laptop">{laptop}</div>
              <div class="sw__phone">{phone}</div>
            </div>''')
    return "\n".join(out)


def _tabs():
    return "\n".join(f'''            <li><button type="button" class="sw__tab{" is-on" if i == 0 else ""}" data-sw-tab="{i}" aria-pressed="{"true" if i == 0 else "false"}">
              <span class="sw__n">0{i + 1}</span>
              <span class="sw__name">{name}</span>
              <span class="sw__desc">{desc}</span>
            </button></li>''' for i, (_, name, desc) in enumerate(STYLES))


def _steps():
    return "\n".join(f'''          <li class="st" data-reveal>
            <p class="st__n">0{i}</p>
            <h3>{t}</h3>
            <p>{d}</p>
          </li>''' for i, (t, d) in enumerate(STEPS, 1))


def _packs():
    out = []
    for pk in PACKAGES:
        feat = pk["featured"]
        tag = '<span class="tag">Onze aanrader</span>' if feat else ""
        out.append(f'''          <a class="pk{" pk--featured" if feat else ""}" href="contact.html?pakket={pk["name"]}">
            <span class="pk__top"><span class="label">{pk["name"]}</span>{tag}</span>
            <span class="pk__price"><span class="pk__from">vanaf</span>€{pk["price"]}</span>
            <span class="pk__title">{pk["title"]}</span>
            <span class="pk__desc">{pk["desc"]}</span>
            <span class="pk__go">Kies {pk["name"]} {I["arrow"]}</span>
          </a>''')
    return "\n".join(out)


def render():
    promises = "".join(f"<li>{t}</li>" for t, _ in GUARANTEES)

    html = head(FILE, "Vizora Digital | Je nieuwe website zie je al in het eerste gesprek",
                "Vizora Digital bouwt websites die klanten opleveren en helpt je om gevonden te worden in Google. Eerst gratis je concept zien, dan pas beslissen. Voor ondernemers in heel Nederland.",
                css=("home",), preload="assets/foto/licht-laptop.webp", ld=True)
    html += header(FILE)
    html += f'''
  <main id="main">
    <section class="hero wrap">
      <h1 class="hero__title" data-lines>Je nieuwe website zie je al in het <em>eerste gesprek</em>.</h1>
      <div class="hero__row">
        <p class="hero__lead" data-reveal>Wij maken vooraf gratis een concept van jouw website. Daarna helpen we je om gevonden te worden in Google. Pas betalen als je blij bent.</p>
        <div class="hero__cta" data-reveal>
          <a href="contact.html" class="btn">Plan je gratis concept {I["arrow"]}</a>
          <p class="hero__trust label">Gratis concept · Vanaf €200 · Reactie dezelfde dag</p>
        </div>
      </div>
      <div class="hero__media" data-grow>
        {pic("licht-laptop", "Laptop op een houten bureau met een voorbeeldwebsite van Vizora op het scherm", 1500, 1213, eager=True, pos="45% 55%")}
      </div>
    </section>

    <section class="sw sheet" data-theme="dark" aria-labelledby="sw-title" data-switcher>
      <div class="sw__sticky">
        <div class="sw__grid wrap">
          <div class="sw__side">
            {label("", "Voorbeelden")}
            <h2 id="sw-title" class="sw__title">Zo kan jouw website eruitzien.</h2>
            <p class="sw__intro">Zelfde laptop, zelfde telefoon. Alleen de website verandert. Zo maken we elke site op maat: jouw kleuren, jouw teksten, jouw zaak.</p>
            <ul class="sw__tabs" aria-label="Kies een voorbeeldstijl">
{_tabs()}
            </ul>
          </div>
          <div class="sw__stage">
{_shots()}
          </div>
          <a href="contact.html" class="sw__cta">Jouw website hier? Plan je gratis concept {I["arrow"]}</a>
        </div>
      </div>
    </section>

    <section class="steps sheet" aria-labelledby="steps-title">
      <div class="wrap">
        <div class="split">
          {label("", "Zo werkt het")}
          <div>
            <h2 id="steps-title" class="steps__title" data-reveal>Eerst zien.<br><span>Dan beslissen.</span></h2>
            <p class="steps__intro" data-reveal>Waarom betalen voordat je weet hoe je website eruitziet? Bij ons zie je eerst gratis je concept.</p>
          </div>
        </div>
        <ol class="steps__list">
{_steps()}
        </ol>
        <ul class="promise" aria-label="Onze garanties" data-reveal>{promises}</ul>
      </div>
    </section>

    <section class="prices sheet" id="prijzen" aria-labelledby="pr-title">
      <div class="wrap">
        <div class="split">
          {label("", "Prijzen")}
          <div>
            <h2 id="pr-title" class="h2 home__h2" data-reveal>Duidelijke prijzen, eenmalig.</h2>
            <p class="prices__intro" data-reveal>Alle prijzen exclusief btw, hosting gratis inbegrepen. Na het gratis gesprek krijg je altijd eerst een vaste prijs op maat.</p>
          </div>
        </div>
        <div class="pk__grid" data-reveal>
{_packs()}
        </div>
        <p class="prices__more" data-reveal><span>Geen opstartkosten, geen jaarcontract. Onderhoud vanaf €{SUB_TIERS[0]["price"]} per maand, maandelijks opzegbaar.</span> <a href="prijzen.html" class="link">Bekijk alle prijzen {I["arrow"]}</a></p>
      </div>
    </section>

    <section class="about sheet" aria-labelledby="ab-title">
      <div class="about__in wrap">
        <figure class="about__photo" data-clip>{pic("halil", "Halil, medeoprichter van Vizora Digital", 640, 800, pos="50% 20%")}</figure>
        <div class="about__body">
          {label("", "Wie zijn wij")}
          <h2 id="ab-title" class="h2 home__h2" data-reveal>Halil &amp; Sahin. Twee broers, één aanspreekpunt.</h2>
          <p class="about__text" data-reveal>Wij zijn Halil en Sahin, twee broers uit de omgeving van Breda. Wij bouwen je website en helpen je met je marketing: je Google Bedrijfsprofiel, je vindbaarheid in je regio en je social media. Alles in één hand, en je spreekt altijd een van ons tweeën.</p>
          <blockquote class="about__why" data-reveal>
            <p class="label">Waarom we zijn begonnen</p>
            <p>We zagen hoe vaak ondernemers te veel betalen voor een website die hen niet verder helpt. Dat vonden we zonde, en dat willen wij voorkomen. Daarom werken we anders: eerst plannen we samen een gesprek, en daarin laten we je al zien hoe jouw nieuwe website eruit kan zien. Pas als je blij bent, gaan we verder. Daarna helpen we je om online gevonden te worden.</p>
          </blockquote>
          <a href="over-ons.html" class="link" data-reveal>Meer over ons {I["arrow"]}</a>
        </div>
      </div>
    </section>
  </main>

'''
    html += footer()
    return html
