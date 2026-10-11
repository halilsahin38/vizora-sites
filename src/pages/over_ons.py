from core import *  # noqa: F401,F403

FILE = "over-ons.html"

# Foto van Halil & Sahin: zodra die er is, zet hier de bestandsnaam (zonder extensie) uit assets/foto/,
# bijvoorbeeld "halil-sahin" (met halil-sahin.webp + halil-sahin.jpg, staand, liefst 4:5, bv. 1200x1500).
# De opmaak staat al klaar (.duo__photo in assets/css/over-ons.css).
PHOTO = "halil"
PHOTO_SIZE = (640, 800)

PROMISES = [
    ("Persoonlijk", "Je spreekt altijd Halil of Sahin. Geen accountmanager, geen ticketnummer, geen wachtrij. We kennen je zaak en denken mee alsof het onze eigen zaak is."),
    ("Zelf gemaakt", "We ontwerpen en bouwen elke website zelf, van eerste schets tot livegang. Daardoor weten we precies hoe jouw site in elkaar zit en kunnen we snel schakelen."),
    ("Eerlijk", "Duidelijke prijzen en een vaste prijs vooraf. Ben je niet blij met het ontwerp, dan betaal je niets. En als iets niet nodig is, zeggen we dat ook."),
    ("Gericht op groei", "Mooi is niet genoeg. Alles wat we maken moet je iets opleveren: meer bereik, meer aanvragen, meer klanten."),
    ("Bereikbaar", "Maandag t/m zaterdag van 09:00 tot 18:00, via WhatsApp of telefoon. Ook na de livegang blijven we gewoon je aanspreekpunt."),
]


def photo_slot():
    if not PHOTO:
        return "<!-- foto Halil & Sahin -->"
    w, h = PHOTO_SIZE
    return f'<figure class="duo__photo" data-clip>{pic(PHOTO, "Halil, medeoprichter van Vizora Digital", w, h)}</figure>'


def render():
    promises = "\n".join(f'''          <li class="pr__row" data-reveal>
            <span class="pr__n label">0{i}</span>
            <h3 class="pr__t">{t}</h3>
            <p class="pr__d">{d}</p>
          </li>''' for i, (t, d) in enumerate(PROMISES, 1))

    html = head(FILE, "Over ons | Halil &amp; Sahin | Vizora Digital",
                "Vizora Digital is opgericht door de broers Halil en Sahin. Vanuit Breda maken ze websites en zorgen ze voor online groei, voor ondernemers in heel Nederland. Persoonlijk en direct bereikbaar.",
                css=("over-ons",))
    html += header(FILE)
    html += f'''
  <main id="main">
{page_head("", "Over ons", "Twee broers, één doel: jouw zaak laten <em>groeien.</em>", "Wij zijn Halil en Sahin. Vanuit Breda maken we websites die klanten opleveren, en zorgen we dat ondernemers in heel Nederland online gevonden worden.")}
    <section class="duo wrap" aria-labelledby="duo-title">
      <div class="duo__grid">
        <div class="duo__side">
          {label("01", "Wie we zijn")}
          {photo_slot()}
        </div>
        <div class="duo__main">
          <h2 id="duo-title" class="duo__names" data-reveal>Halil <span>&amp;</span><br>Sahin</h2>
          <p class="duo__lead" data-reveal>Twee broers, samen Vizora Digital. Een jonge webstudio uit de omgeving van Breda, voor ondernemers in heel Nederland: van starter tot gevestigde zaak.</p>
          <div class="duo__cols" data-reveal>
            <p>Jong betekent bij ons: geen accountmanagers of wachtrijen, maar alle aandacht voor jouw project. Je spreekt altijd een van ons tweeën, van het eerste gesprek tot lang na de livegang.</p>
            <p>We bouwen elke website zelf, van eerste schets tot livegang, en blijven daarna bereikbaar voor vragen en aanpassingen. Gewoon via WhatsApp of telefoon.</p>
          </div>
          <dl class="duo__facts" data-reveal>
            <div><dt>Gevestigd</dt><dd>Breda</dd></div>
            <div><dt>Werkgebied</dt><dd>Heel Nederland</dd></div>
            <div><dt>Bereikbaar</dt><dd>Ma–za 09–18</dd></div>
          </dl>
        </div>
      </div>
    </section>

    <section class="sec story wrap" aria-labelledby="story-title">
      <div class="split">
        {label("02", "Ons verhaal")}
        <div>
          <h2 id="story-title" class="h2" data-reveal>Waarom we Vizora<br><span>zijn begonnen.</span></h2>
          <p class="story__lead" data-reveal>We zagen het steeds weer: ondernemers die te veel betalen voor een website die hen niet verder helpt. Of ondernemers die echt goed zijn in hun vak, maar online bijna niet te vinden zijn.</p>
          <div class="story__cols" data-reveal>
            <p>Een groot bureau is vaak duur, en je spreekt steeds iemand anders. Zelf een website maken kost veel tijd, en dan moet je nog gevonden worden.</p>
            <p>Dat willen wij voorkomen. Daarom zijn we Vizora begonnen: een website op maat en een plan om te groeien, voor een eerlijke prijs. Van twee mensen die je gewoon kunt bellen of appen.</p>
          </div>
          <div class="name" data-reveal>
            <p class="label">Waar de naam vandaan komt</p>
            <dl class="name__list">
              <div><dt>Visie</dt><dd>Een duidelijk plan: weten welke stap je zet, en waarom.</dd></div>
              <div><dt>Zichtbaarheid</dt><dd>Een zaak die gezien wordt, in Google en daarbuiten.</dd></div>
              <div class="name__sum"><dt>Vizora</dt><dd>Daar helpen we je mee.</dd></div>
            </dl>
          </div>
        </div>
      </div>
    </section>

    <section class="quote" aria-label="Onze belofte">
      <figure class="wrap quote__in">
        <blockquote class="quote__text" data-reveal><p>Jouw succes is ons visitekaartje. <span>Als jouw zaak groeit, groeien wij mee.</span></p></blockquote>
        <figcaption class="label" data-reveal>Halil &amp; Sahin</figcaption>
      </figure>
    </section>

    <section class="sec pr wrap" aria-labelledby="pr-title">
      <div class="split">
        {label("03", "Waar we voor staan")}
        <div>
          <h2 id="pr-title" class="h2" data-reveal>Wat je van ons<br><span>mag verwachten.</span></h2>
        </div>
      </div>
      <ol class="pr__list">
{promises}
      </ol>
    </section>

    <section class="direct" aria-labelledby="direct-title">
      <div class="wrap split">
        {label("04", "Direct contact")}
        <div>
          <h2 id="direct-title" class="h2" data-reveal>Geen wachtrij.<br><span>Gewoon even bellen.</span></h2>
          <p class="direct__text" data-reveal>Een vraag, een idee of twijfel? Bel of app ons. Je krijgt Halil of Sahin aan de lijn, geen callcenter.</p>
          <a href="{TEL}" class="direct__tel" data-reveal aria-label="Bel ons: {TEL_TXT}">{TEL_TXT}</a>
          <div class="direct__actions" data-reveal>
            <a href="{WA}" class="btn" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a>
            <a href="mailto:{MAIL}" class="btn btn--ghost">{I["mail"]} Mail ons</a>
          </div>
          <p class="direct__more" data-reveal><span class="label">Ma t/m za 09:00–18:00</span><a href="contact.html" class="link">Of plan je gratis concept {I["arrow"]}</a></p>
        </div>
      </div>
    </section>
  </main>

'''
    html += footer()
    return html
