# Vizora Digital – projectafspraken

Website van Vizora Digital (vizoradigital.nl), gerund door de broers Halil en Sahin vanuit Breda.
Communicatie met Halil: Nederlands, eenvoudige taal, kort en concreet. Eerst vragen als iets onduidelijk is,
dan pas bouwen. Geen dingen toevoegen waar niet om gevraagd is.

## Wat Vizora is
- Vizora verkoopt **websites + online groei** (vindbaarheid in Google, marketing, hulp bij social media)
  aan ondernemers in **heel Nederland** (vanuit Breda). Niet alleen Noord-Brabant.
- Hoofdtitel (gekozen door Halil): "Je nieuwe website zie je al in het eerste gesprek." Boodschap eronder: meer klanten via Google.
  ("Websites die klanten opleveren" gebruikt concurrent WebBreda al.)
- Haakje: gratis websiteconcept bij het eerste (gepland) gesprek, plus groeiplan stap voor stap.
  Werkwijze (keuze Halil): schets van alleen het bovenste deel van de homepagina op basis van het formulier;
  bij te weinig info eerst kort (±10 min) bellen. Later bij veel aanvragen eventueel: eerst gesprek, dan concept.
- Tevredenheidsgarantie: pas betalen als je blij bent met het ontwerp.
- Toekomst: e-commerce / Shopify. Focus nu: Vizora.

## Contact en praktisch
- E-mail halilsahinai@gmail.com · WhatsApp/bellen 06 38 70 53 48 (wa.me/31638705348, tel:+31638705348)
- Ma t/m za 09:00–18:00 (afspraken 09:00–17:00). Belofte: binnen werktijd antwoord dezelfde dag. Geen Instagram nog. KvK-nummer volgt.
- Agenda komt later via Cal.com (Halil stuurt de link).
- Hosting: Cloudflare Pages (gratis, ook commercieel toegestaan; ook voor klantsites). Online zetten/merge alleen na
  expliciete toestemming van Halil. Cloudflare-instellingen: build command `python3 build.py`, output directory `dist`.

## Prijzen (huidige stand op de site)
- Alle prijzen exclusief btw.
- Pakketten eenmalig: Start €200 · Groei €350 · Compleet €500.
- Abonnementen per maand, maandelijkse factuur: Basis €25 · Plus €49 · Pro €79 (Pro = tot 6 aanpassingen, niet onbeperkt).
- Hosting gratis inbegrepen bij elk pakket; klant betaalt zelf de domeinnaam (ca. €10–15 per jaar).
- Advies gegeven om prijzen te verhogen; nog niet besloten.

## Wat NIET (eerdere feedback)
- Geen voorbeelden per branche (kappers/restaurants/bakkers): klanten moeten niet denken dat we alleen voor één branche werken.
- Geen omzetcalculator, geen oud/nieuw-schuif, geen foto's van willekeurige mensen of "extra" sfeerfoto's.
- Niet beloven dat wij posten op social media: content komt van de klant; content maken/posten in overleg en tegen meerprijs.
- Niets dat "AI-erig" oogt; niet een andere site letterlijk naapen (Quantiz alleen als inspiratie).
- Geen cursor-ring, intro-animatie of woord-voor-woord animatie in koppen (alleen in de hoofdtitel).

## Stijl
- Kleuren: gebroken wit #faf8f4, wit, linnen beige #eee6d9, inkt zwart #121110, accent terracotta #a9583a, salie #7d8a6a.
- Echte apparaten (telefoon/laptop) met eigen voorbeeldontwerpen op het scherm, beweging bij scrollen (parallax).
- Voorbeeldontwerpen staan in `concepts/` (merk = Atelier Dorr, licht = Mertens & Verhoef, warm = Praktijk Wilgenhof:
  echt ogende fictieve bedrijven uit verschillende sectoren, met "fictief bedrijf" in de footer); foto's in `assets/foto/`.
- Nooit AI-trucjes in voorbeelden: geen "Jouw Bedrijf", nepcijfers, zwevende kaartjes, blobs. Elke laptop/telefoonfoto een andere echte omgeving.

## Techniek
- Alle pagina's worden gegenereerd door `python3 build.py` (f-strings: letterlijke accolades als `{{ }}`).
- Teksten en pagina's in `src/` (core.py + pages/), stijl in `assets/css/`, gedrag in `assets/js/` (site.js, motion.js).
- `build.py` maakt `dist/` (alleen de website) met `_headers` (beveiligingsheaders + CSP; de hash van het inline script
  wordt automatisch berekend). `dist/` staat niet in git.
- Beveiliging: alles komt van eigen domein (lettertypes lokaal in `assets/fonts/`, geen Google Fonts of andere externe
  bronnen), strenge headers via `dist/_headers` (staan in build.py). `/.well-known/security.txt` verloopt op `SECURITY_EXPIRES` in core.py: jaarlijks verlengen.
- Testscreenshots en tijdelijke bestanden nooit in deze map zetten (gebruik een scratchpad).
