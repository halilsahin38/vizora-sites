from core import *  # noqa: F401,F403

FILE = "index.html"

STYLES = [
    ("merk", "Donker &amp; luxe", "Diep zwart met warm goud. Voor een zaak die indruk wil maken."),
    ("licht", "Licht &amp; strak", "Veel wit en één rustige kleur. Helder, modern en zakelijk."),
    ("warm", "Warm &amp; persoonlijk", "Zachte tinten en ronde vormen. Vriendelijk en uitnodigend."),
]

SERVICES = [
    ("Websites", "Een website op maat die vertrouwen wekt en van bezoekers klanten maakt. Van one-pager tot complete site.", "vanaf €200", "diensten.html#websites"),
    ("Gevonden worden", "Een sterk Google Bedrijfsprofiel en lokale SEO, zodat mensen in jouw omgeving jou vinden.", "in Groei &amp; Compleet", "diensten.html#marketing"),
    ("Social media", "Profielen die kloppen, een herkenbare stijl en eerlijk advies over wat werkt.", "in Compleet", "diensten.html#social-media"),
    ("Onderhoud &amp; groei", "Elke maand een website die up-to-date, veilig en snel is, met hulp bij de volgende stap.", "vanaf €25 p/m", "prijzen.html#abonnement"),
]

STEPS = [
    ("Plan een gesprek", "Kies een moment dat jou uitkomt, of bel of app ons direct. Videobellen, telefonisch of op locatie in overleg.", ["± 30 minuten", "Gratis", "Vrijblijvend"]),
    ("Wij maken je concept", "Voor het gesprek ontwerpen we alvast een eerste versie van jouw website, in jouw stijl en met jouw zaak als uitgangspunt.", ["Op maat", "Op telefoon én laptop", "Voor het gesprek klaar"]),
    ("Pas dan beslis je", "We nemen het concept en een groeiplan samen door. Ben je enthousiast? Dan bouwen we verder. Zo niet, dan heb je niets betaald.", ["Twee feedbackrondes", "Vaste prijs vooraf", "Niet blij = niet betalen"]),
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

    services = "\n".join(f'''          <a class="sv" href="{href}" data-reveal>
            <span class="sv__n label">0{i}</span>
            <span class="sv__row">
              <span class="sv__t">{t}</span>
              <span class="sv__d">{d}</span>
              <span class="sv__p">{p}</span>
              <span class="sv__go">{I["arrow"]}</span>
            </span>
          </a>''' for i, (t, d, p, href) in enumerate(SERVICES, 1))

    steps = "\n".join(f'''          <article class="st" style="--i:{i}">
            <div class="st__in">
              <p class="st__n">0{i + 1}</p>
              <div class="st__body">
                <h3>{t}</h3>
                <p>{d}</p>
                <ul>{"".join(f"<li>{x}</li>" for x in tags)}</ul>
              </div>
            </div>
          </article>''' for i, (t, d, tags) in enumerate(STEPS))

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

    <section class="sec intro wrap" aria-label="Wat we doen">
      {label("01", "Wat we doen")}
      <p class="intro__text" data-fill>Een mooie website alleen is niet genoeg. Wij zorgen ook dat je gevonden wordt. Eén vast team voor je website, je vindbaarheid en je groei, zodat jij je kunt richten op je zaak.</p>
    </section>

    <section class="work" data-theme="dark" aria-labelledby="work-title" data-hscroll>
      <div class="work__head wrap">
        {label("02", "Voorbeelden")}
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
      <div class="steps__head">
        {label("03", "Zo werkt het")}
        <h2 id="steps-title" class="h2 steps__title" data-reveal>Eerst zien.<br><span>Dan beslissen.</span></h2>
        <p class="steps__intro" data-reveal>Waarom betalen voordat je weet hoe je website eruitziet? Bij ons zie je eerst gratis je concept.</p>
      </div>
      <div class="steps__list">
{steps}
      </div>
    </section>

    <section class="sec services wrap" aria-labelledby="sv-title">
      <div class="split">
        {label("04", "Diensten")}
        <h2 id="sv-title" class="h2" data-reveal>Alles voor je online groei, onder één dak.</h2>
      </div>
      <div class="sv__list">
{services}
      </div>
    </section>

    <section class="sec prices wrap" id="prijzen" aria-labelledby="pr-title">
      <div class="split">
        {label("05", "Prijzen")}
        <div>
          <h2 id="pr-title" class="h2" data-reveal>Duidelijke prijzen.<br>Eenmalig, geen verrassingen.</h2>
          <p class="prices__intro" data-reveal>Kies een pakket als startpunt. Na het gratis gesprek krijg je altijd eerst een vaste prijs op maat.</p>
        </div>
      </div>
      <div class="pk__grid">
{price_columns()}
      </div>
      <div class="sub" id="abonnement">
        <div class="sub__head">
          <p class="label">Website-abonnement · maandelijks opzegbaar</p>
          <p class="sub__lead">Een website is nooit af. Wij houden hem up-to-date, veilig en snel. Je ontvangt elke maand een factuur.</p>
        </div>
{sub_rows()}
      </div>
    </section>

    <section class="gu" aria-labelledby="gu-title">
      <div class="wrap">
        <div class="split">
          {label("06", "Garanties")}
          <h2 id="gu-title" class="h2" data-reveal>Zwart op wit.<br><span>Nul risico.</span></h2>
        </div>
        <div class="gu__grid">
{guarantees()}
        </div>
      </div>
    </section>

    <section class="sec about wrap" aria-labelledby="ab-title">
      <div class="split">
        {label("07", "Wie zijn wij")}
        <div>
          <h2 id="ab-title" class="h2" data-reveal>Halil &amp; Sahin.<br><span>Twee broers, één aanspreekpunt.</span></h2>
          <div class="about__cols" data-reveal>
            <p>Wij zijn een jong bureau uit Breda. Dat betekent: geen accountmanagers of wachtrijen, maar alle aandacht voor jouw project. Je spreekt altijd een van ons tweeën.</p>
            <p>We bouwen elke website zelf, van eerste schets tot livegang, en blijven daarna bereikbaar voor vragen en aanpassingen. Gewoon via WhatsApp of telefoon.</p>
          </div>
          <dl class="about__facts" data-reveal>
            <div><dt>Werkgebied</dt><dd>Heel Nederland</dd></div>
            <div><dt>Bereikbaar</dt><dd>Ma–za 09–18</dd></div>
            <div><dt>Contact</dt><dd><a href="{TEL}">{TEL_TXT}</a></dd></div>
          </dl>
          <a href="over-ons.html" class="link" data-reveal>Meer over ons {I["arrow"]}</a>
        </div>
      </div>
    </section>

    <section class="sec qa wrap" aria-labelledby="qa-title">
      <div class="split">
        <div>
          {label("08", "Vragen")}
          <h2 id="qa-title" class="h2 qa__title" data-reveal>Veelgestelde vragen</h2>
          <p class="qa__help" data-reveal>Staat je vraag er niet bij? <a href="{WA}" target="_blank" rel="noopener">App ons</a> of bel <a href="{TEL}">{TEL_TXT}</a>.</p>
        </div>
        <div class="qa__list" data-reveal>
{faq_list(FAQ)}
        </div>
      </div>
    </section>
  </main>

'''
    html += footer()
    return html
