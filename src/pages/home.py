from core import *  # noqa: F401,F403

FILE = "index.html"

STEPS = [
    ("Plan een gesprek", "Laat je gegevens achter, of bel of app ons direct. Wij stellen een moment voor. Gratis en vrijblijvend."),
    ("Wij maken je concept", "Voor het gesprek ontwerpen we alvast een eerste versie van jouw website. Soms bellen we eerst kort om je wensen te horen."),
    ("Pas dan beslis je", "Enthousiast? Dan bouwen we verder. Zo niet, dan heb je niets betaald."),
]


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
            <span class="pk__note">eenmalig · excl. btw</span>
            <span class="pk__title">{pk["title"]}</span>
            <span class="pk__desc">{pk["desc"]}</span>
            <span class="pk__go">Kies {pk["name"]} {I["arrow"]}</span>
          </a>''')
    return "\n".join(out)


def render():
    promises = "".join(f"<li>{t}</li>" for t, _ in GUARANTEES)

    html = head(FILE, "Vizora Digital | Zie je nieuwe website al vóór je betaalt",
                "Wij maken gratis een concept van jouw website en laten het zien in het eerste gesprek. Pas betalen als je blij bent. Voor ondernemers in heel Nederland.",
                css=("home",), preload=("hero-laptop", 1280, SIZES["hero"]), ld=True)
    html += header(FILE)
    html += f'''
  <main id="main">
    <section class="hero wrap">
      <h1 class="hero__title" data-lines>Je nieuwe website zie je al in het <em>eerste gesprek</em>.</h1>
      <div class="hero__row">
        <p class="hero__lead" data-reveal>Wij maken vooraf gratis een concept van jouw website. Daarna helpen we je om gevonden te worden in Google. Pas betalen als je blij bent.</p>
        <div class="hero__cta" data-reveal>
          <a href="contact.html" class="btn">Plan je gratis concept {I["arrow"]}</a>
          <p class="hero__trust label">Gratis concept · Vanaf €{PACKAGES[0]["price"]} excl. btw · Binnen werktijd antwoord dezelfde dag</p>
        </div>
      </div>
      <div class="hero__zoom" data-zoom>
        <div class="hero__media">
          {pic("hero-laptop", "Laptop met een zwart scherm op een tafel, met zonlicht op de muur", 1280, 720, eager=True, sizes=SIZES["hero"])}
          <video class="hero__video" muted playsinline preload="none" aria-hidden="true" data-src="assets/video/hero.mp4" data-src-small="assets/video/hero-480.mp4"></video>
          <span class="hero__screen" aria-hidden="true"><span class="hero__mark">{LOGO_MARK}<span>Vizora Digital</span></span></span>
        </div>
      </div>
    </section>

    <section class="vow sheet stack" data-theme="dark" aria-labelledby="vow-title">
      <div class="wrap">
        <div class="split">
          {label("", "Onze belofte")}
          <div>
            <h2 id="vow-title" class="vow__title" data-reveal>Gratis concept.<br><span>Pas betalen als je blij bent.</span></h2>
            <ul class="vow__list" data-stagger>
              <li><span class="label">01</span>Je ziet je nieuwe website al in het eerste gesprek.</li>
              <li><span class="label">02</span>Vaste prijs vooraf. Geen verrassingen.</li>
              <li><span class="label">03</span>Daarna helpen we je gevonden te worden in Google.</li>
            </ul>
            <div class="vow__cta" data-reveal>
              <a href="contact.html" class="btn btn--light">Plan je gratis concept {I["arrow"]}</a>
              <a href="{TEL}" class="vow__tel">of bel {TEL_TXT}</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="steps sheet stack" aria-labelledby="steps-title">
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

    <section class="prices sheet stack" id="prijzen" aria-labelledby="pr-title">
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
  {maatwerk()}
        <p class="prices__more" data-reveal><span>Geen opstartkosten, geen jaarcontract. Onderhoud vanaf €{SUB_TIERS[0]["price"]} per maand excl. btw, maandelijks opzegbaar.</span> <a href="prijzen.html" class="link">Bekijk alle prijzen {I["arrow"]}</a></p>
      </div>
    </section>

    <section class="about sheet stack" aria-labelledby="ab-title">
      <div class="about__in wrap">
        <figure class="about__photo"><div class="about__img" data-clip>{pic("halil", "Halil, medeoprichter van Vizora Digital", 800, 1000, pos="50% 20%")}</div><figcaption class="label about__cap">Halil</figcaption></figure>
        <div class="about__body">
          {label("", "Wie zijn wij")}
          <h2 id="ab-title" class="h2 home__h2" data-reveal>Halil &amp; Sahin. Twee broers, één aanspreekpunt.</h2>
          <p class="about__text" data-reveal>Wij zijn Halil en Sahin, twee broers uit de omgeving van Breda. Wij bouwen je website en helpen je met je marketing: je Google Bedrijfsprofiel, je vindbaarheid in je regio en je social media. Alles in één hand, en je spreekt altijd een van ons tweeën: via WhatsApp, telefoon of e-mail.</p>
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
