import re

from core import *  # noqa: F401,F403

FILE = "404.html"

LINKS = [
    ("index.html", "Home", "Terug naar het begin"),
    ("prijzen.html", "Prijzen", "Bekijk de pakketten en prijzen"),
    ("contact.html", "Contact", "Plan je gratis gesprek"),
]


def render():
    rows = "\n".join(f'''          <li><a class="nf__a" href="{href}">
            <span class="nf__t">{t}</span>
            <span class="nf__d">{d}</span>
            <span class="nf__go">{I["arrow"]}</span>
          </a></li>''' for href, t, d in LINKS)

    html = head(FILE, "Pagina niet gevonden | Vizora Digital",
                "Deze pagina bestaat niet (meer). Ga terug naar de homepage of neem contact op met Vizora Digital.",
                css=("notfound",))
    html += header(FILE)
    html += f'''
  <main id="main">
{page_head("404", "Pagina niet gevonden", "Deze pagina is <em>zoek.</em>", "De pagina die je zoekt bestaat niet (meer), of het adres is net iets anders. Geen zorgen, hier vind je de weg terug.")}
    <nav class="nf wrap" aria-label="Verder naar">
      <div class="split">
        {label("", "Verder naar")}
        <ul class="nf__list" data-reveal>
{rows}
        </ul>
      </div>
    </nav>
  </main>

'''
    html += footer()

    # Deze pagina wordt ook getoond op diepere adressen (bv. /iets/anders),
    # dus alle eigen links en bestanden vanaf de root laden.
    html = re.sub(r'(href|src|srcset)="(?!https?:|#|mailto:|tel:|/)', r'\1="/', html)
    html = html.replace('href="/index.html"', 'href="/"')
    html = re.sub(r'\s*<link rel="canonical"[^>]*>', "", html)
    html = html.replace('<meta name="description"', '<meta name="robots" content="noindex">\n  <meta name="description"', 1)
    return html
