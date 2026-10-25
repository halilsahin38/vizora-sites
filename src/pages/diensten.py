from core import *  # noqa: F401,F403

FILE = "diensten.html"

P = {p["name"]: p["price"] for p in PACKAGES}
S = {t["name"]: t["price"] for t in SUB_TIERS}

# Overzicht bovenaan (ankerlinks naar de drie diensten)
INDEX = [
    ("websites", "Websites", "Een website op maat, gemaakt voor jouw klanten.", f"vanaf €{P['Start']} excl. btw"),
    ("marketing", "Marketing", "Gevonden worden in Google en Google Maps, en meer bereik.", "in Groei &amp; Compleet"),
    ("social-media", "Social media", "Profielen die kloppen en een herkenbare stijl.", "in Compleet"),
]

# Extra diensten: rustige lijst, geen kaarten
EXTRA = [
    ("Website-abonnement", "Onderhoud, beveiliging en elke maand aanpassingen aan je website. Maandelijks opzegbaar, met een maandelijkse factuur.", f"vanaf €{S['Basis']} p/m excl. btw", "prijzen.html#abonnement"),
    ("Logo &amp; huisstijl", "Een herkenbaar logo, kleuren en lettertypes die overal terugkomen: van je website tot je visitekaartje en social media.", "in Compleet · los op aanvraag", None),
    ("Google Bedrijfsprofiel", "Ingericht met de juiste gegevens, zodat je goed in Google en Google Maps staat. Bijhouden kan via het abonnement.", "in Groei &amp; Compleet", None),
    ("Advertenties", "Campagnes in Google en op Instagram en Facebook, opgezet rond één duidelijk doel.", "op maat", None),
    ("Zakelijke e-mail", "Mailen vanaf info@jouwzaak.nl in plaats van een Gmail-adres. Klein detail, groot verschil in vertrouwen.", "op aanvraag", None),
    ("Content voor social media", "Foto's, video's of posts laten maken of plaatsen. Valt buiten de pakketten.", "in overleg · meerprijs", None),
]


def facts(items):
    rows = "".join(f"<div><dt>{t}</dt><dd>{d}</dd></div>" for t, d in items)
    return f'<dl class="svc__facts">{rows}</dl>'


def gets(items, title="Wat je krijgt"):
    lis = "".join(f"<li>{x}</li>" for x in items)
    return f'''<div class="svc__block" data-reveal>
            <p class="label">{title}</p>
            <ul class="svc__list">{lis}</ul>
          </div>'''


def packs(rows, more=True):
    out = "".join(f'''
              <div class="pkr"><span class="pkr__n">{n}</span><span class="pkr__d">{d}</span><span class="pkr__p">{p}</span></div>''' for n, d, p in rows)
    link = f'\n            <a href="prijzen.html" class="link svc__more">Alle pakketten en prijzen {I["arrow"]}</a>' if more else ""
    return f'''<div class="svc__block" data-reveal>
            <p class="label">In welk pakket · prijzen excl. btw</p>
            <div class="pkr__list">{out}
            </div>{link}
          </div>'''


def note(*texts):
    paras = "".join(f'\n            <p class="svc__note">{t}</p>' for t in texts)
    return f'''<div class="svc__block svc__block--note" data-reveal>
            <p class="label">Goed om te weten</p>{paras}
          </div>'''


def side(num, name, items):
    return f'''<div class="svc__side">
          <p class="svc__n" aria-hidden="true">{num}</p>
          <p class="label">Dienst {num} — {name}</p>
          {facts(items)}
        </div>'''


def render():
    index = "\n".join(f'''        <li class="dx__item"><a class="dx__link" href="#{a}">
          <span class="dx__top"><span class="label">0{i}</span><span class="dx__go">{I["arrow"]}</span></span>
          <span class="dx__t">{t}</span>
          <span class="dx__d">{d}</span>
          <span class="dx__p">{p}</span>
        </a></li>''' for i, (a, t, d, p) in enumerate(INDEX, 1))

    extra = []
    for n, d, tag, href in EXTRA:
        inner = f'''<span class="xtr__name">{n}</span>
            <span class="xtr__rest"><span class="xtr__desc">{d}</span><span class="xtr__tag">{tag}</span><span class="xtr__go">{I["arrow"] if href else ""}</span></span>'''
        if href:
            extra.append(f'''          <a class="xtr__row xtr__row--link" href="{href}" data-reveal>
            {inner}
          </a>''')
        else:
            extra.append(f'''          <div class="xtr__row" data-reveal>
            {inner}
          </div>''')
    extra_html = "\n".join(extra)

    html = head(FILE, "Diensten | Websites, marketing en social media | Vizora Digital",
                "Een website op maat, hulp om gevonden te worden in Google en hulp bij social media. Voor ondernemers in heel Nederland, vanuit Breda.",
                css=("diensten",))
    html += header(FILE)
    html += f'''
  <main id="main">
{page_head("", "Diensten", "Alles om online te <em>groeien.</em>", "Een website op maat, hulp om gevonden te worden in Google en hulp bij social media. Los af te nemen of als compleet pakket, en altijd afgestemd op jouw zaak.")}
    <nav class="dx wrap" aria-label="Diensten op deze pagina">
      <ol class="dx__list">
{index}
      </ol>
    </nav>

    <section class="svc" id="websites" aria-labelledby="websites-title">
      <div class="svc__grid wrap">
        {side("01", "Websites", [("Voor wie", "Starters, zzp'ers en ondernemers die online meer klanten willen"), ("Prijs", f"Vanaf €{P['Start']}, eenmalig, excl. btw"), ("Daarna", f"Abonnement vanaf €{S['Basis']} p/m excl. btw, niet verplicht")])}
        <div class="svc__main">
          <h2 id="websites-title" class="h2" data-reveal>Een website die werkt<br><span>als je beste verkoper.</span></h2>
          <p class="svc__lead" data-reveal>Je website is vaak het eerste wat een klant van je ziet. Wij zorgen dat die eerste indruk klopt, en dat bezoekers makkelijk kunnen bellen, appen of een afspraak maken.</p>
          <div class="svc__cols" data-reveal>
            <p>Elke website ontwerpen we op maat, rond jouw klanten en jouw doelen. Geen standaard template, wel een site die laat zien hoe goed je bent en die op elke telefoon goed werkt.</p>
            <p>Wij regelen het ontwerp, de bouw, de koppeling met je domein, de hosting en het livezetten. Jij vertelt over je zaak; bij de teksten helpen we je. Technische kennis heb je niet nodig.</p>
          </div>
          {gets(["Uniek ontwerp, geen template", "Perfect op telefoon, tablet en laptop", "Bel-, WhatsApp- en contactknoppen", "Online afspraken, reserveren of bestellen (vanaf Groei)", "Basis vindbaarheid in Google", "Domeinnaam op jouw naam", "Twee feedbackrondes in de prijs", "Onderhoud en aanpassingen via het abonnement"])}
          {packs([("Start", "One-page website op maat, perfect op mobiel, met bel-, WhatsApp- en contactknoppen", f"€{P['Start']}"), ("Groei", "Tot 5 pagina's, uniek ontwerp met animaties en online afspraken, reserveren of bestellen", f"€{P['Groei']}"), ("Compleet", "Alles uit Groei, plus logo en huisstijl en een persoonlijk groeiplan", f"€{P['Compleet']}")])}
          {note("Je ziet eerst gratis een concept van je website. Pas als je blij bent met het ontwerp, betaal je. Ben je na de feedbackrondes niet tevreden, dan betaal je niets.")}
          <div class="svc__actions" data-reveal>
            <a href="contact.html" class="btn">Bespreek je website {I["arrow"]}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="svc svc--alt" id="marketing" aria-labelledby="marketing-title">
      <div class="svc__grid wrap">
        {side("02", "Marketing", [("Voor wie", "Ondernemers die gevonden willen worden door klanten in hun regio"), ("Zit in", f"Groei (€{P['Groei']}) en Compleet (€{P['Compleet']}), excl. btw"), ("Advertenties", "Op maat, altijd eerst in overleg")])}
        <div class="svc__main">
          <h2 id="marketing-title" class="h2" data-reveal>Gevonden worden<br><span>door wie nu zoekt.</span></h2>
          <p class="svc__lead" data-reveal>Je beste klanten zijn vaak mensen die al zoeken naar wat jij aanbiedt. Met een sterk Google Bedrijfsprofiel, lokale SEO en waar het past gerichte advertenties, helpen we je gevonden te worden waar zij zoeken.</p>
          <ol class="ladder" aria-label="Zo bouwen we het op">
            <li data-reveal><span class="ladder__n label">Stap 1</span><span class="ladder__t">De basis</span><span class="ladder__d">Google Bedrijfsprofiel en lokale SEO, zodat je zichtbaar bent in Google en Google Maps.</span></li>
            <li data-reveal><span class="ladder__n label">Stap 2</span><span class="ladder__t">Vertrouwen</span><span class="ladder__d">Hulp bij het vragen om reviews, zodat nieuwe klanten zien dat anderen tevreden zijn.</span></li>
            <li data-reveal><span class="ladder__n label">Stap 3</span><span class="ladder__t">Extra bereik</span><span class="ladder__d">Advertenties in Google en op Instagram en Facebook. Pas als de basis staat.</span></li>
          </ol>
          <div class="svc__cols" data-reveal>
            <p>We beginnen met de basis en bouwen daarna stap voor stap verder. Zo weet je precies waar je geld naartoe gaat.</p>
            <p>In het eerste gesprek kijken we samen hoe klanten jou nu vinden, en wat de logische volgende stap is. Zonder vakjargon.</p>
          </div>
          {gets(["Google Bedrijfsprofiel inrichten", "Lokale SEO voor jouw regio", "Hulp bij het vragen om reviews", "Google Ads-campagnes", "Advertenties op Instagram en Facebook", "Duidelijke rapportages"], "Waarmee we helpen")}
          {packs([("Start", "Basis vindbaarheid in Google", f"€{P['Start']}"), ("Groei", "Google Bedrijfsprofiel ingericht en lokale SEO voor jouw regio", f"€{P['Groei']}"), ("Compleet", "Alles uit Groei, plus een persoonlijk groeiplan en advies voor advertenties", f"€{P['Compleet']}"), ("Plus", "Abonnement: Google Bedrijfsprofiel bijhouden en maandelijkse groeitips", f"€{S['Plus']}<small> p/m</small>")])}
          {note("We beloven geen plek 1 in Google; dat kan niemand eerlijk. Wel dat alles goed staat: je Google Bedrijfsprofiel, je pagina's en je regio.",
               "Advertentiecampagnes zitten niet in de pakketten. In Compleet krijg je advies; het opzetten en beheren van campagnes spreken we op maat met je af.")}
          <div class="svc__actions" data-reveal>
            <a href="contact.html" class="btn">Bespreek marketing {I["arrow"]}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="svc" id="social-media" aria-labelledby="social-title">
      <div class="svc__grid wrap">
        {side("03", "Social media", [("Voor wie", "Ondernemers die online overal herkenbaar willen zijn"), ("Zit in", f"Compleet (€{P['Compleet']}), excl. btw"), ("Content", "Komt van jou. Maken of posten in overleg, tegen meerprijs")])}
        <div class="svc__main">
          <h2 id="social-title" class="h2" data-reveal>Social media:<br><span>wij helpen je op weg.</span></h2>
          <p class="svc__lead" data-reveal>Social media werkt het best als het echt van jou is. Jij kent je zaak, je klanten en je verhaal. Wij zorgen dat je profielen professioneel zijn ingericht, dat alles herkenbaar is in jouw stijl en dat je weet wat werkt.</p>
          <div class="svc__say" data-reveal>
            <p class="svc__quote">De content komt van jou. Wij zorgen voor de stijl.</p>
            <p>Foto's en video's maak en plaats je zelf; van ons krijg je de inrichting, de templates en een plan. Wil je dat wij content maken of posten? Dat kan, in overleg en tegen meerprijs. Het valt buiten de pakketten.</p>
          </div>
          {gets(["Profielen inrichten op Instagram en Facebook", "Huisstijl en templates", "Bio, links en highlights", "Advies en een contentplan", "Koppeling met je website", "Content maken of posten: in overleg, meerprijs"])}
          {packs([("Compleet", "Profielen op social media ingericht, logo en huisstijl en een persoonlijk groeiplan", f"€{P['Compleet']}"), ("Los", "Alleen hulp bij social media, of content laten maken? Dat bespreken we samen.", "in overleg")])}
          <div class="svc__actions" data-reveal>
            <a href="contact.html" class="btn">Bespreek social media {I["arrow"]}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="xtr wrap" aria-labelledby="xtr-title">
      <div class="split">
        {label("04", "Extra")}
        <div>
          <h2 id="xtr-title" class="h2" data-reveal>Handig om<br><span>erbij te nemen.</span></h2>
          <p class="xtr__intro" data-reveal>Los te combineren met elke website. Wat het kost, hoor je vooraf; zonder verrassingen achteraf.</p>
        </div>
      </div>
      <div class="xtr__list">
{extra_html}
      </div>
    </section>

    <section class="help" aria-labelledby="help-title">
      <div class="wrap split">
        {label("05", "Twijfel je?")}
        <div>
          <h2 id="help-title" class="h2" data-reveal>Niet zeker wat je<br><span>nodig hebt?</span></h2>
          <p class="help__text" data-reveal>Geen probleem. In een gratis gesprek kijken we samen wat jouw zaak nodig heeft, en wat je beter (nog) niet kunt doen. Even bellen of appen mag ook gewoon.</p>
          <p class="help__text" data-reveal>We werken vanuit de regio Breda (o.a. Breda, Tilburg, Etten-Leur, Oosterhout) en online voor ondernemers in heel Nederland.</p>
          <div class="help__actions" data-reveal>
            <a href="{TEL}" class="btn">{I["call"]} Bel {TEL_TXT}</a>
            <a href="{WA}" class="btn btn--ghost" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a>
          </div>
          <p class="help__more" data-reveal><span class="label">Ma t/m za 09:00–18:00</span><a href="contact.html" class="link">Of plan je gratis gesprek {I["arrow"]}</a></p>
        </div>
      </div>
    </section>
  </main>

'''
    html += footer()
    return html
