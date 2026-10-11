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


def render():
    work = []
    for i, (key, name, desc) in enumerate(STYLES, 1):
        work.append(f'''          <figure class="wk wk--laptop">
            <div class="wk__media" data-clip>{pic(f"{key}-laptop", f"Voorbeeldwebsite in de stijl {name.replace('&amp;', 'en')} op een laptop", 1500, 1213)}</div>
            <figcaption><span class="label">0{i} — Voorbeeldontwerp</span><strong>{name}</strong><span>{desc}</span></figcaption>
          </figure>
          <figure class="wk wk--phone">
            <div class="wk__media" data-clip>{pic(f"{key}-telefoon", "Dezelfde voorbeeldwebsite op een telefoon", 1100, 1286, pos="52% 40%")}</div>
            <figcaption><span class="label">0{i} — Mobiel</span></figcaption>
          </figure>''')
    work_html = "\n".join(work)

    steps = "\n".join(f'''          <li class="st" data-reveal>
            <p class="st__n">0{i}</p>
            <h3>{t}</h3>
            <p>{d}</p>
          </li>''' for i, (t, d) in enumerate(STEPS, 1))

    promises = "".join(f"<li>{t}</li>" for t, _ in GUARANTEES)

    packs = "\n".join(f'''          <a class="pk{" pk--featured" if pk["featured"] else ""}" href="contact.html?pakket={pk["name"]}" data-reveal>
            <span class="pk__top"><span class="label">{pk["name"]}</span>{'<span class="tag">Meest gekozen</span>' if pk["featured"] else ""}</span>
            <span class="pk__price"><span class="pk__from">vanaf</span>€{pk["price"]}</span>
            <span class="pk__title">{pk["title"]}</span>
            <span class="pk__desc">{pk["desc"]}</span>
            <span class="pk__go">Kies {pk["name"]} {I["arrow"]}</span>
          </a>''' for pk in PACKAGES)

    html = head(FILE, "Vizora Digital | Een website die je klanten oplevert",
                "Vizora Digital bouwt websites die klanten opleveren en zorgt dat je gevonden wordt in Google. Eerst gratis je concept zien, dan pas beslissen. Voor ondernemers in heel Nederland.",
                css=("home",), preload="assets/foto/licht-laptop.webp", ld=True)
    html += header(FILE)
    html += f'''
  <main id="main">
    <section class="hero wrap">
      <h1 class="hero__title" data-lines>Een website die je <em>klanten</em> oplevert.</h1>
      <div class="hero__row">
        <p class="hero__lead" data-reveal>Wij bouwen je website én zorgen dat klanten je vinden in Google. Voor ondernemers in heel Nederland, met een vast aanspreekpunt.</p>
        <div class="hero__cta" data-reveal>
          <a href="contact.html" class="btn">Plan je gratis concept {I["arrow"]}</a>
          <p class="hero__trust label">Gratis concept · Vanaf €200 · Niet blij = niet betalen</p>
        </div>
      </div>
      <div class="hero__media" data-grow>
        {pic("licht-laptop", "Laptop op een houten bureau met een voorbeeldwebsite van Vizora op het scherm", 1500, 1213, eager=True, pos="45% 55%")}
      </div>
    </section>

    <section class="work" data-theme="dark" aria-labelledby="work-title" data-hscroll>
      <div class="work__head wrap">
        {label("01", "Voorbeelden")}
        <h2 id="work-title" class="h2">Zo kan jouw website eruitzien.</h2>
        <p class="work__intro">Drie voorbeeldontwerpen die we zelf maakten. Jouw website maken we altijd op maat: jouw kleuren, jouw teksten, jouw zaak.</p>
      </div>
      <div class="work__viewport">
        <div class="work__track" data-hscroll-track>
{work_html}
          <a class="wk wk--end" href="contact.html">
            <span class="label">Jouw beurt</span>
            <strong>Jouw website hier?</strong>
            <span class="wk__endcta">Plan je gratis concept {I["arrow"]}</span>
          </a>
        </div>
      </div>
    </section>

    <section class="sec steps wrap" aria-labelledby="steps-title">
      <div class="split">
        {label("02", "Zo werkt het")}
        <div>
          <h2 id="steps-title" class="h2 steps__title" data-reveal>Eerst zien.<br><span>Dan beslissen.</span></h2>
          <p class="steps__intro" data-reveal>Waarom betalen voordat je weet hoe je website eruitziet? Bij ons zie je eerst gratis je concept.</p>
        </div>
      </div>
      <ol class="steps__list">
{steps}
      </ol>
      <ul class="promise" aria-label="Onze garanties" data-reveal>{promises}</ul>
    </section>

    <section class="sec prices wrap" id="prijzen" aria-labelledby="pr-title">
      <div class="split">
        {label("03", "Prijzen")}
        <div>
          <h2 id="pr-title" class="h2" data-reveal>Duidelijke prijzen.<br><span>Eenmalig, geen verrassingen.</span></h2>
          <p class="prices__intro" data-reveal>Hosting gratis inbegrepen. Na het gratis gesprek krijg je altijd eerst een vaste prijs op maat.</p>
        </div>
      </div>
      <div class="pk__grid">
{packs}
      </div>
      <p class="prices__more" data-reveal><span>Onderhoud en aanpassingen vanaf €{SUB_TIERS[0]["price"]} per maand, maandelijks opzegbaar.</span> <a href="prijzen.html" class="link">Bekijk alle prijzen {I["arrow"]}</a></p>
    </section>

    <section class="sec about wrap" aria-labelledby="ab-title">
      <figure class="about__photo" data-clip>{pic("halil", "Halil, medeoprichter van Vizora Digital", 640, 800, pos="50% 20%")}</figure>
      <div class="about__body">
        {label("04", "Wie zijn wij")}
        <h2 id="ab-title" class="h2" data-reveal>Halil &amp; Sahin.<br><span>Twee broers, één aanspreekpunt.</span></h2>
        <p class="about__text" data-reveal>Wij bouwen elke website zelf, van eerste schets tot livegang. Geen accountmanagers of wachtrijen: je spreekt altijd een van ons tweeën, gewoon via WhatsApp of telefoon. Voor ondernemers in heel Nederland.</p>
        <div class="about__cta" data-reveal>
          <a href="over-ons.html" class="link">Meer over ons {I["arrow"]}</a>
        </div>
      </div>
    </section>
  </main>

'''
    html += footer()
    return html
