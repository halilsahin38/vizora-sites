from core import *  # noqa: F401,F403

FILE = "prijzen.html"

CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true" class="i cmp__y"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
DASH = '<svg viewBox="0 0 24 24" aria-hidden="true" class="i cmp__n"><path d="M8 12h8"/></svg>'

# Vergelijking: (groep, [(onderdeel, Start, Groei, Compleet)]). True = inbegrepen, False = niet, tekst = waarde.
COMPARE = [
    ("Website", [
        ("Aantal pagina's", "1", "tot 5", "tot 5"),
        ("Ontwerp op maat", True, True, True),
        ("Perfect op mobiel", True, True, True),
        ("Bel-, WhatsApp- &amp; contactknoppen", True, True, True),
        ("Koppeling met je eigen domein", True, True, True),
        ("Hosting", "gratis", "gratis", "gratis"),
        ("Animaties &amp; interactie", False, True, True),
        ("Online afspraken, reserveren of bestellen", False, True, True),
        ("Teksten die overtuigen", False, True, True),
    ]),
    ("Gevonden worden", [
        ("Basis vindbaarheid in Google", True, True, True),
        ("Google Bedrijfsprofiel ingericht", False, True, True),
        ("Lokale SEO voor jouw regio", False, True, True),
    ]),
    ("Merk &amp; groei", [
        ("Logo &amp; huisstijl", False, False, True),
        ("Profielen op social media ingericht", False, False, True),
        ("Persoonlijk groeiplan", False, False, True),
        ("Advies voor advertenties", False, False, True),
        ("1 maand gratis aanpassingen", False, False, True),
    ]),
]

EXTRAS = [
    ("Advertenties", "Campagnes in Google en op Instagram en Facebook, met duidelijke rapportages.", "Prijs op aanvraag"),
    ("Content voor social media", "Content maken of posten voor jouw zaak. Wat je nodig hebt en wat het kost, bespreken we samen.", "In overleg"),
    ("Losse aanpassingen", "Geen abonnement? Dan kan het ook. We spreken per aanpassing vooraf een prijs af.", "Per keer"),
]


def _faq():
    b, p, r = SUB_TIERS
    st, gr, co = PACKAGES
    return [
        ("Wat kost een website laten maken?", f"Bij ons begint een website bij €{st['price']} voor {st['name']} (een one-page website), €{gr['price']} voor {gr['name']} (tot 5 pagina's) of €{co['price']} voor {co['name']} (met logo en huisstijl). Dat zijn eenmalige vanaf-prijzen, exclusief btw. Hosting is gratis; alleen je domeinnaam betaal je zelf, meestal €10 tot €15 per jaar. Voor grotere projecten, zoals een webshop of een website met veel pagina's, maken we maatwerk; de prijs bespreken we samen. Na het gratis gesprek krijg je altijd een vaste prijs op maat."),
        ("Waarom staat er “vanaf”?", "Elke zaak is anders. De vanaf-prijs is wat je minimaal betaalt voor het pakket. Na het gratis gesprek krijg je een vaste prijs, zonder verrassingen."),
        ("Zijn er maandelijkse kosten?", f"De pakketten zijn eenmalig. Wil je dat we je website elke maand bijwerken en onderhouden? Dan kun je een abonnement nemen vanaf €{b['price']} per maand, excl. btw. Hosting is gratis inbegrepen. Alleen je domeinnaam betaal je zelf, meestal €10 tot €15 per jaar."),
        ("Welke abonnementen zijn er?", f"{b['name']} (€{b['price']} p/m): onderhoud, beveiliging en 1 kleine aanpassing per maand. {p['name']} (€{p['price']} p/m): tot 3 aanpassingen, je Google Bedrijfsprofiel bijhouden en maandelijkse groeitips. {r['name']} (€{r['price']} p/m): tot 6 aanpassingen per maand, elk kwartaal een nieuwe pagina of actie en een maandelijks groeigesprek. Alle bedragen excl. btw. Je ontvangt elke maand een factuur en kunt per maand opzeggen."),
        ("Maken jullie ook posts voor social media?", "In het pakket Compleet richten we je profielen in en helpen we met stijl en strategie. Content maken of posten valt daarbuiten; dat bespreken we graag samen en kost extra."),
        ("Kan ik later upgraden?", "Ja. Begin je met Start, dan kun je altijd uitbreiden naar Groei of Compleet. Wat al gemaakt is, bouwen we gewoon verder uit."),
        ("Hoe betaal ik?", "Dat spreken we samen af in de offerte. Je weet vooraf precies wat je betaalt en wanneer. Het abonnement betaal je per maand, op factuur."),
        ("Wat als ik niet tevreden ben?", "Dan betaal je niets. Je ziet eerst het ontwerp en we passen het twee keer aan naar jouw wensen. Pas als jij tevreden bent, gaan we verder en ontvang je de factuur."),
    ]


def _cell(v, featured):
    cls = ' class="is-f"' if featured else ""
    if v is True:
        return f'<td{cls}>{CHECK}<span class="vh">Inbegrepen</span></td>'
    if v is False:
        return f'<td{cls}>{DASH}<span class="vh">Niet inbegrepen</span></td>'
    return f'<td{cls}><span class="cmp__v">{v}</span></td>'


def _compare():
    feat = [p["featured"] for p in PACKAGES]
    heads = "".join(
        f'<th scope="col"{" class=\"is-f\"" if p["featured"] else ""}><span class="cmp__pk">{p["name"]}</span>'
        f'<span class="cmp__pr"><span class="cmp__from">vanaf </span>€{p["price"]}</span></th>' for p in PACKAGES)
    groups = []
    for g, rows in COMPARE:
        empty = "".join(f'<td{" class=\"is-f\"" if f else ""}></td>' for f in feat)
        trs = [f'              <tr class="cmp__grp"><th scope="rowgroup">{g}</th>{empty}</tr>']
        for name, *vals in rows:
            cells = "".join(_cell(v, f) for v, f in zip(vals, feat))
            trs.append(f'              <tr><th scope="row">{name}</th>{cells}</tr>')
        groups.append("            <tbody data-stagger>\n" + "\n".join(trs) + "\n            </tbody>")
    return f'''          <table class="cmp__table">
            <caption class="vh">Wat zit er in de pakketten {", ".join(p["name"] for p in PACKAGES)}</caption>
            <thead data-stagger><tr><th scope="col"><span class="label">Inbegrepen</span></th>{heads}</tr></thead>
{chr(10).join(groups)}
          </table>'''


def _tiers():
    out = []
    for t in SUB_TIERS:
        feats = "".join(f"<li>{f}</li>" for f in t["feats"])
        out.append(f'''          <article class="tier">
            <h3 class="tier__name">{t["name"]}</h3>
            <p class="tier__price">€{t["price"]}<span>per maand · excl. btw</span></p>
            <ul class="tier__list">{feats}</ul>
            <a href="contact.html?pakket=Abonnement%20{t["name"]}" class="btn btn--line tier__btn">Kies {t["name"]} {I["arrow"]}</a>
          </article>''')
    return "\n".join(out)


def render():
    start = PACKAGES[0]["price"]
    extras = "\n".join(f'''          <div class="ex">
            <span class="label">0{i}</span>
            <div class="ex__row">
              <h3 class="ex__t">{t}</h3>
              <p class="ex__d">{d}</p>
              <p class="ex__p">{p}</p>
            </div>
          </div>''' for i, (t, d, p) in enumerate(EXTRAS, 1))

    html = head(FILE, f"Prijzen | Websites vanaf €{start} | Vizora Digital",
                f"Je eigen website vanaf €{start} excl. btw. Drie pakketten, eenmalig, en een abonnement vanaf "
                f"€{SUB_TIERS[0]['price']} per maand. Eerst gratis je concept zien, dan pas beslissen.",
                css=("prijzen",))
    html += header(FILE)
    html += f'''
  <main id="main">
{page_head("", "Prijzen", "Duidelijke pakketten, <em>eerlijke</em> prijzen.", "Eén keer betalen voor je website, en als je wilt een vast bedrag per maand voor onderhoud en groei. Je ziet eerst gratis je concept. Pas als je blij bent, betaal je.")}
    <section class="pp wrap" id="pakketten" aria-labelledby="pk-title">
      <div class="split">
        {label("01", "Pakketten")}
        <div>
          <h2 id="pk-title" class="h2" data-reveal>Drie pakketten.<br><span>Eén keer betalen.</span></h2>
          <p class="pp__intro" data-reveal>Kies een pakket als startpunt. Na het gratis gesprek krijg je altijd eerst een vaste prijs op maat, zodat je precies weet waar je aan toe bent. Prijzen voor ondernemers, exclusief btw.</p>
        </div>
      </div>
      <div class="pk__grid" data-stagger>
{price_columns()}
      </div>
{maatwerk()}
      <p class="pp__foot" data-reveal>Alle pakketprijzen zijn vanaf-prijzen voor een eenmalig project. De definitieve prijs hangt af van je wensen en hoor je vooraf.</p>
    </section>

    <section class="sec cmp stack" id="vergelijken" aria-labelledby="cmp-title">
      <div class="cmp__split wrap">
        <div class="cmp__aside">
          {label("02", "Vergelijken")}
          <h2 id="cmp-title" class="h2 cmp__title" data-reveal>Wat zit er in elk pakket?</h2>
          <p class="cmp__help" data-reveal>Twijfel je tussen twee pakketten? <a href="{WA}" target="_blank" rel="noopener">App</a>, <a href="mailto:{MAIL}">mail</a> of bel <a href="{TEL}">{TEL_TXT}</a>. We adviseren eerlijk, ook als een kleiner pakket genoeg is. Alle prijzen excl. btw.</p>
        </div>
        <div class="cmp__wrap">
{_compare()}
        </div>
      </div>
    </section>

    <section class="abo sheet stack" id="abonnement" data-theme="dark" aria-labelledby="abo-title">
      <div class="wrap">
        <div class="split">
          {label("03", "Website-abonnement")}
          <div>
            <h2 id="abo-title" class="h2" data-reveal>Een website is nooit af.<br><span>Wij houden hem bij.</span></h2>
            <p class="abo__lead" data-reveal>Met een abonnement houden wij je site up-to-date, veilig en snel, en helpen we je elke maand een stap verder. Je kiest zelf hoeveel hulp je wilt.</p>
          </div>
        </div>
        <div class="abo__grid" data-stagger>
{_tiers()}
        </div>
        <dl class="abo__terms" data-stagger>
          <div><dt>Factuur</dt><dd>Elke maand</dd></div>
          <div><dt>Opzeggen</dt><dd>Per maand</dd></div>
          <div><dt>Jaarcontract</dt><dd>Geen</dd></div>
        </dl>
        <p class="abo__free" data-reveal><b>Nooit vastzitten.</b> Geen opstartkosten, geen jaarcontract en je domein staat op jouw naam. Stop je met het abonnement? Dan blijft je website gewoon van jou.</p>
      </div>
    </section>

    <section class="gu sheet stack" id="garanties" aria-labelledby="gu-title">
      <div class="wrap">
        <div class="split">
          {label("04", "Garanties")}
          <div>
            <h2 id="gu-title" class="h2" data-reveal>Zwart op wit.<br><span>Nul risico.</span></h2>
            <p class="gu__lead" data-reveal>Je ziet eerst het ontwerp. Pas als jij zegt “zo wil ik het”, gaan we verder en ontvang je de factuur.</p>
          </div>
        </div>
        <div class="gu__grid" data-stagger>
{guarantees()}
        </div>
      </div>
    </section>

    <section class="sec ext sheet" id="extra" aria-labelledby="ex-title">
      <div class="wrap">
      <div class="split">
        {label("05", "Uitbreiden")}
        <div>
          <h2 id="ex-title" class="h2" data-reveal>Verder groeien,<br><span>wanneer jij wilt.</span></h2>
          <p class="pp__intro" data-reveal>Klaar voor de volgende stap? Deze diensten stemmen we samen af op jouw zaak.</p>
        </div>
      </div>
      <div class="ex__list" data-stagger>
{extras}
      </div>
      </div>
    </section>

    <section class="sec qa stack" aria-labelledby="qa-title">
      <div class="split wrap">
        <div>
          {label("06", "Vragen over prijzen")}
          <h2 id="qa-title" class="h2 qa__title" data-reveal>Goed om te weten</h2>
          <p class="qa__help" data-reveal>Staat je vraag er niet bij? <a href="{WA}" target="_blank" rel="noopener">App ons</a> of bel <a href="{TEL}">{TEL_TXT}</a>.</p>
        </div>
        <div class="qa__list" data-stagger>
{faq_list(_faq())}
        </div>
      </div>
    </section>
  </main>

'''
    html += footer()
    return html
