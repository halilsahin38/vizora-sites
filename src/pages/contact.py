from core import *  # noqa: F401,F403

FILE = "contact.html"

CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true" class="i"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'

# Hoe wil je het gesprek voeren? (value = wat in het bericht komt)
VORM = [
    ("Videogesprek", "Videogesprek", "Online, vanaf je laptop of telefoon"),
    ("Telefonisch gesprek", "Telefonisch", "Wij bellen jou op het afgesproken moment"),
    ("Afspraak op locatie", "Op locatie", "Bij jou in de zaak, in overleg"),
]
DIENST = [
    ("Website", "Website"),
    ("Marketing &amp; bereik", "Marketing &amp; bereik"),
    ("Social media", "Social media"),
    ("Website-abonnement", "Website-abonnement"),
    ("Weet ik nog niet", "Weet ik nog niet"),
]
# Zo gaat het (onder de intro bovenaan)
HOW = [
    "Je vult het formulier in (1 minuut).",
    "Wij stellen via WhatsApp of e-mail een moment voor en maken alvast je concept. Soms bellen we eerst kort om je wensen te horen.",
    "In het gesprek (± 30 min) zie je je website. Daarna beslis jij.",
]

GAINS = [
    "Een gratis concept van je nieuwe website",
    "Een eerlijke blik op je online uitstraling",
    "Een groeiplan, stap voor stap",
    "100% vrijblijvend",
]


def _direct():
    items = [
        (TEL, "Bellen", TEL_TXT, "Ma t/m za, 09:00 – 18:00", I["call"], ""),
        (WA, "WhatsApp", "Stuur een appje", f"Ook op {TEL_TXT}", WA_SVG, ' target="_blank" rel="noopener"'),
        (f"mailto:{MAIL}", "E-mail", MAIL, "Handig voor langere vragen of bestanden", I["mail"], ""),
    ]
    return "\n".join(f'''        <li class="cd__item"><a class="cd__a" href="{href}"{extra}>
          <span class="cd__top"><span class="label">{lab}</span><span class="cd__ic">{ic}</span></span>
          <span class="cd__v">{val}</span>
          <span class="cd__d">{desc}</span>
        </a></li>''' for href, lab, val, desc, ic, extra in items)


def _form():
    vorm = "\n".join(
        f'''              <div class="choice"><input type="radio" name="vorm" id="v{i}" value="{v}"{" checked" if i == 1 else ""}><label for="v{i}"><b>{t}</b><small>{s}</small></label></div>'''
        for i, (v, t, s) in enumerate(VORM, 1))
    dienst = "\n".join(
        f'''              <div class="choice"><input type="checkbox" name="dienst" id="d{i}" value="{v}"><label for="d{i}"><span class="bk__box">{CHECK}</span>{t}</label></div>'''
        for i, (v, t) in enumerate(DIENST, 1))
    return f'''        <form class="bk__form" id="booking" novalidate aria-labelledby="bk-title">
          <fieldset class="bk__step">
            <legend><span class="bk__n">01</span>Hoe wil je het gesprek voeren?</legend>
            <div class="bk__vorm">
{vorm}
            </div>
          </fieldset>

          <fieldset class="bk__step">
            <legend><span class="bk__n">02</span>Waar ben je in geïnteresseerd?</legend>
            <p class="bk__hint">Je mag er meerdere kiezen. Twijfel je nog? Dan zoeken we het samen uit.</p>
            <div class="bk__tags">
{dienst}
            </div>
          </fieldset>

          <fieldset class="bk__step">
            <legend><span class="bk__n">03</span>Je gegevens</legend>
            <div class="bk__fields">
              <label class="bk__field"><span class="bk__lab">Naam <span aria-hidden="true">*</span></span><input name="naam" type="text" required autocomplete="name" maxlength="80"></label>
              <label class="bk__field"><span class="bk__lab">Telefoonnummer <span aria-hidden="true">*</span></span><input name="telefoon" type="tel" required autocomplete="tel" inputmode="tel" maxlength="20"></label>
              <label class="bk__field"><span class="bk__lab">Bedrijfsnaam</span><input name="bedrijf" type="text" autocomplete="organization" maxlength="80"></label>
              <div class="bk__field bk__field--full"><label class="bk__lab" for="bk-website">Link naar je huidige website of Instagram (optioneel)</label><input id="bk-website" name="website" type="text" inputmode="url" autocomplete="url" autocapitalize="off" spellcheck="false" maxlength="200" aria-describedby="bk-website-hint"><span class="bk__fhint" id="bk-website-hint">Helpt ons bij je concept</span></div>
              <label class="bk__field bk__field--full"><span class="bk__lab">Waar kunnen we je mee helpen? (optioneel)</span><textarea name="bericht" rows="3" maxlength="1000"></textarea></label>
            </div>
            <p class="bk__req">Velden met * zijn verplicht.</p>
          </fieldset>

          <div class="bk__send">
            <div class="bk__sum">
              <p class="label">Je aanvraag</p>
              <p class="bk__sumpk" data-summary-pakket hidden></p>
              <p class="bk__sumt" data-summary aria-live="polite">Videogesprek. Wij stellen een moment voor dat jou uitkomt.</p>
            </div>
            <p class="booking__error" role="alert"></p>
            <div class="bk__actions">
              <button type="submit" class="btn bk__wa">{WA_SVG} Verstuur via WhatsApp</button>
              <button type="button" class="btn btn--ghost" data-email>{I["mail"]} Verstuur via e-mail</button>
            </div>
            <p class="bk__note"><b>Je bericht staat daarna klaar in WhatsApp of in je mail. Druk daar nog op verzenden, dan is het geregeld.</b> Binnen werktijd (ma–za 9–18 uur) antwoord dezelfde dag, met een voorstel voor een moment.</p>
          </div>
        </form>'''


def render():
    gains = "".join(f'<li><span class="label">0{i}</span><span>{g}</span></li>' for i, g in enumerate(GAINS, 1))
    how_items = "".join(f'<li><span class="label" aria-hidden="true">0{i}</span><span>{t}</span></li>' for i, t in enumerate(HOW, 1))
    how = f'''
      <div class="how">
        <h2 class="label" id="how-title" data-reveal>Zo gaat het</h2>
        <ol class="how__list" data-stagger>{how_items}</ol>
      </div>'''

    html = head(FILE, "Contact | Plan een gratis gesprek | Vizora Digital",
                f"Plan een gratis gesprek en zie vooraf een gratis concept van je nieuwe website. "
                f"Of bel of app direct: {TEL_TXT}. Voor ondernemers in heel Nederland.",
                css=("contact",))
    html += header(FILE)
    html += f'''
  <main id="main">
{page_head("", "Contact", "Plan een gratis gesprek, of <em>bel direct.</em>", "Laat je gegevens achter, dan stellen wij een moment voor. Wij maken vooraf een concept van jouw website en laten het in het gesprek zien. Liever meteen even bellen, appen of mailen? Dat kan natuurlijk ook.", how, cls="stack")}
    <section class="cd sheet" aria-label="Direct contact">
      <div class="wrap">
      <ul class="cd__list" data-stagger>
{_direct()}
      </ul>
      </div>
    </section>

    <section class="bk sheet" id="plannen" aria-labelledby="bk-title">
      <div class="wrap">
      <div class="split">
        {label("01", "Gesprek plannen")}
        <div>
          <h2 id="bk-title" class="h2" data-reveal>Vul het in.<br><span>Wij maken je concept.</span></h2>
          <p class="bk__intro" data-reveal>Drie korte stappen. Je aanvraag gaat via WhatsApp of e-mail naar ons, en wij stellen een moment voor dat jou uitkomt.</p>
        </div>
      </div>
      <div class="bk__grid">
        <aside class="bk__aside" aria-label="Over het gesprek">
          <p class="label">Wat je van het gesprek krijgt</p>
          <ol class="bk__gains" data-stagger>{gains}</ol>
          <dl class="bk__facts" data-stagger>
            <div><dt>Werkgebied</dt><dd>Heel Nederland, vanuit Breda</dd></div>
            <div><dt>Afspraken</dt><dd>Ma t/m za, 09:00 – 17:00</dd></div>
            <div><dt>Vorm</dt><dd>Video, telefonisch of op locatie</dd></div>
          </dl>
          <p class="bk__help">Eerst een vraag? Bel <a href="{TEL}">{TEL_TXT}</a> of <a href="{WA}" target="_blank" rel="noopener">app ons</a>.</p>
        </aside>
{_form()}
      </div>
      </div>
    </section>
  </main>

'''
    html += footer(FILE, cta=False)
    return html
