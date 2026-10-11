from core import *  # noqa: F401,F403

FILE = "werkwijze.html"

P = {p["name"]: p["price"] for p in PACKAGES}
S = {t["name"]: t["price"] for t in SUB_TIERS}

# In het kort (balk onder de kop)
GLANCE = [
    ("Eerste gesprek", "Gratis"),
    ("Je concept", "Gratis, vooraf gemaakt"),
    ("Betalen", "Pas als je blij bent"),
    ("Techniek", "Regelen wij"),
]

# De stappen (titel, tekst, kenmerken)
STEPS = [
    ("Kennismaken",
     "Bel of app ons, of kies een moment dat jou uitkomt. We stellen een paar vragen over je zaak: wat je doet, wie je klanten zijn en waar je naartoe wilt.",
     ["Gratis", "Bellen, appen of plannen", "Vrijblijvend"]),
    ("Jouw concept &amp; groeiplan",
     "Voor het gesprek ontwerpen we alvast een eerste versie van jouw website, in jouw stijl. In het gesprek laten we die zien en bespreken we stap voor stap hoe je zaak online kan groeien. Telefonisch, via video of op locatie in overleg.",
     ["Gratis", "± 30 minuten", "Op laptop én telefoon"]),
    ("Voorstel &amp; vaste prijs",
     "Enthousiast? Dan krijg je een helder voorstel: wat we gaan doen, wat het kost en wanneer het klaar is. Geen kleine lettertjes. Niet enthousiast? Dan stopt het hier en heb je niets betaald.",
     ["Vaste prijs vooraf", "Planning samen afgesproken", "Geen verplichting"]),
    ("Bouwen &amp; live",
     "We werken het concept uit tot je complete website en schrijven de teksten met je mee. Je krijgt twee feedbackrondes; pas als je blij bent met het ontwerp, betaal je. Daarna testen we alles en zetten we je site live op je eigen domein.",
     ["Twee feedbackrondes", "Niet blij = niet betalen", "Getest op elk apparaat"]),
    ("Blijven groeien",
     f"Een website is nooit af. Met het website-abonnement (vanaf €{S['Basis']} per maand) houden we hem veilig en up-to-date en passen we dingen voor je aan. Wil je verder, met advertenties of hulp bij social media? Dan pakken we de volgende stap uit je groeiplan op.",
     [f"Vanaf €{S['Basis']} p/m", "Maandelijks opzegbaar", "Hulp via WhatsApp"]),
]

# Wie doet wat
YOU = [
    "Vertellen over je zaak en je klanten.",
    "Foto's aanleveren, als je die hebt.",
    "Zeggen wat je van het ontwerp vindt.",
]
WE = [
    "Ontwerp op maat",
    "Bouw van de website",
    "Teksten, samen met jou",
    "Domeinnaam koppelen, op jouw naam",
    "Hosting, gratis inbegrepen",
    "Beveiliging (https)",
    "Snel laden op elke telefoon",
    "Aanmelden bij Google",
    "Livezetten",
    "Onderhoud en updates, met het abonnement",
]

QA = [
    ("Krijg ik vooraf een ontwerp te zien?", "Ja. Als je een gesprek plant, maken we gratis een concept van jouw website. Zo zie je meteen hoe het eruit kan zien, nog voordat je iets beslist."),
    ("Wat als ik niet tevreden ben?", "Dan betaal je niets. Je ziet eerst het ontwerp en we passen het twee keer aan naar jouw wensen. Pas als jij tevreden bent, gaan we verder en ontvang je de factuur."),
    ("Moet ik zelf iets technisch doen?", "Nee. Wij regelen het ontwerp, de bouw, de koppeling met je domein, de hosting en het livezetten. Jij vertelt over je zaak; daar helpen we je ook bij."),
    ("Moet ik zelf teksten en foto's aanleveren?", "Teksten schrijven we graag met je mee. Foto's en video's komen het liefst van jou, want niemand kent je zaak beter. We adviseren je wel over wat goed werkt."),
    ("Hoe lang duurt het voordat mijn website online staat?", "Dat hangt af van de grootte van je website en hoe snel de teksten en foto's rond zijn. In het gesprek spreken we samen een planning af die bij jou past."),
    ("Wat kost een website?", f'Onze pakketten beginnen bij €{P["Start"]} (Start), €{P["Groei"]} (Groei) en €{P["Compleet"]} (Compleet), eenmalig. Na het gesprek krijg je een vaste prijs op maat. Alle details staan op de <a href="prijzen.html">prijzenpagina</a>.'),
    ("Kan ik later nog dingen laten aanpassen?", f"Ja. Met het website-abonnement (vanaf €{S['Basis']} per maand) werken we je website elke maand bij. Zonder abonnement kan het ook; dan spreken we per aanpassing een prijs af."),
    ("Maken jullie ook posts voor social media?", "We richten je profielen in en helpen met stijl en strategie. Content maken of posten valt buiten de pakketten; dat bespreken we graag samen en kost extra."),
    ("Ik heb al een website. Kunnen jullie die verbeteren?", "Zeker. We kijken eerst gratis naar je huidige site en vertellen eerlijk of verbeteren of opnieuw bouwen slimmer is."),
    ("Waar zitten jullie?", "In Breda. We werken voor ondernemers in heel Nederland. Kennismaken en overleggen gaat makkelijk via telefoon, WhatsApp of video."),
]


def render():
    glance = "\n".join(f'        <div><dt>{t}</dt><dd>{d}</dd></div>' for t, d in GLANCE)

    steps = "\n".join(f'''        <li class="trj__step">
          <p class="trj__n" aria-hidden="true">0{i}</p>
          <div class="trj__body" data-reveal>
            <p class="label">Stap {i} van {len(STEPS)}</p>
            <h3 class="trj__t">{t}</h3>
            <p class="trj__d">{d}</p>
            <ul class="trj__tags" aria-label="In het kort">{"".join(f"<li>{x}</li>" for x in tags)}</ul>
          </div>
        </li>''' for i, (t, d, tags) in enumerate(STEPS, 1))

    you = "".join(f"<li>{x}</li>" for x in YOU)
    we = "".join(f"<li>{x}</li>" for x in WE)

    html = head(FILE, "Werkwijze | Eerst zien, dan beslissen | Vizora Digital",
                "Van gratis kennismaking en websiteconcept tot een website die elke maand meegroeit. Jij vertelt over je zaak, wij regelen de techniek. Zo werkt Vizora Digital.",
                css=("werkwijze",))
    html += header(FILE)
    html += f'''
  <main id="main">
{page_head("", "Werkwijze", "Stap voor stap naar <em>meer klanten.</em>", "Je weet altijd waar je aan toe bent. Je ziet je website eerst, voordat je iets betaalt. En het technische werk? Dat doen wij.")}
    <div class="glance wrap">
      <dl class="glance__list" data-reveal>
{glance}
      </dl>
    </div>

    <section class="sec tls wrap" aria-labelledby="tl-title">
      <div class="split">
        {label("01", "Het traject")}
        <div>
          <h2 id="tl-title" class="h2" data-reveal>Van eerste gesprek<br><span>tot een site die groeit.</span></h2>
          <p class="tls__intro" data-reveal>Vijf stappen, zonder verrassingen. Je beslist pas bij stap drie, als je jouw website al hebt gezien.</p>
        </div>
      </div>
      <ol class="trj">
{steps}
      </ol>
    </section>

    <section class="see" aria-labelledby="see-title">
      <div class="wrap">
        <div class="split">
          {label("02", "Het gratis concept")}
          <div>
            <h2 id="see-title" class="see__title" data-reveal>Eerst zien.<br><span>Dan beslissen.</span></h2>
            <p class="see__intro" data-reveal>Normaal betaal je eerst en zie je pas later wat je krijgt. Bij ons is het andersom. Plan je een gesprek, dan maken we vooraf een eerste ontwerp van jouw website. Zo zie je hoe het eruit kan zien, nog voordat je iets beslist.</p>
          </div>
        </div>
        <div class="see__media">
          <figure class="see__laptop">
            <div class="see__img" data-clip>{pic("merk-laptop", "Laptop met een donker voorbeeldontwerp van Vizora op het scherm", 1500, 1213, pos="50% 55%")}</div>
          </figure>
          <figure class="see__phone">
            <div class="see__float" data-speed="-0.06">
              <div class="see__img" data-clip>{pic("merk-telefoon", "Hetzelfde voorbeeldontwerp op een telefoon", 1100, 1286, pos="52% 40%")}</div>
            </div>
            <figcaption class="label">Voorbeeld van een concept, op laptop en telefoon</figcaption>
          </figure>
        </div>
        <dl class="see__facts" data-reveal>
          <div><dt>Kosten</dt><dd>€0</dd></div>
          <div><dt>Verplichting</dt><dd>Geen</dd></div>
          <div><dt>Klaar</dt><dd>Vóór het gesprek</dd></div>
        </dl>
        <div class="see__actions" data-reveal>
          <a href="contact.html" class="btn btn--light">Plan je gratis concept {I["arrow"]}</a>
          <a href="{WA}" class="btn btn--line" target="_blank" rel="noopener">{WA_SVG} Liever eerst appen</a>
        </div>
      </div>
    </section>

    <section class="who" aria-labelledby="who-title">
      <div class="wrap">
        <div class="split">
          {label("03", "Wie doet wat")}
          <div>
            <h2 id="who-title" class="h2" data-reveal>Jij kent je zaak.<br><span>Wij doen de rest.</span></h2>
            <p class="who__intro" data-reveal>Je hoeft niets van websites te weten. Geen hosting uitzoeken, geen code, geen instellingen. Dit is de hele verdeling:</p>
          </div>
        </div>
        <div class="who__grid">
          <div class="who__you" data-reveal>
            <p class="label who__head"><span>Jij</span><span>3 dingen</span></p>
            <ol class="who__big">{you}</ol>
          </div>
          <div class="who__we" data-reveal>
            <p class="label who__head"><span>Wij</span><span>al het technische werk</span></p>
            <ol class="who__list">{we}</ol>
          </div>
        </div>
      </div>
    </section>

    <section class="sec qa wrap" aria-labelledby="qa-title">
      <div class="split">
        <div>
          {label("04", "Vragen")}
          <h2 id="qa-title" class="h2 qa__title" data-reveal>Vragen over de werkwijze</h2>
          <p class="qa__help" data-reveal>Staat je vraag er niet bij? <a href="{WA}" target="_blank" rel="noopener">App ons</a> of bel <a href="{TEL}">{TEL_TXT}</a>. Ma t/m za, 09:00–18:00.</p>
        </div>
        <div class="qa__list" data-reveal>
{faq_list(QA)}
        </div>
      </div>
    </section>
  </main>

'''
    html += footer()
    return html
