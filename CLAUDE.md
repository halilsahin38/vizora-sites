# Vizora Digital – projectafspraken

Website van Vizora Digital (vizoradigital.nl), gerund door de broers Halil en Sahin vanuit Breda.
Communicatie met Halil: Nederlands, eenvoudige taal, kort en concreet. Eerst vragen als iets onduidelijk is,
dan pas bouwen. Geen dingen toevoegen waar niet om gevraagd is.

## Wat Vizora is
- Vizora verkoopt **websites + online groei** (vindbaarheid in Google, marketing, hulp bij social media)
  aan ondernemers in **heel Nederland** (vanuit Breda). Niet alleen Noord-Brabant.
- Hoofdboodschap: een website die je meer klanten oplevert.
- Haakje: gratis websiteconcept bij het eerste (gepland) gesprek, plus groeiplan stap voor stap.
- Tevredenheidsgarantie: pas betalen als je blij bent met het ontwerp.
- Toekomst: e-commerce / Shopify. Focus nu: Vizora.

## Contact en praktisch
- E-mail halilsahinai@gmail.com · WhatsApp/bellen 06 38 70 53 48 (wa.me/31638705348, tel:+31638705348)
- Ma t/m za 09:00–18:00 (afspraken 09:00–17:00). Geen Instagram nog. KvK-nummer volgt.
- Agenda komt later via Cal.com (Halil stuurt de link).
- Online zetten via Vercel/merge alleen na expliciete toestemming van Halil.

## Prijzen (huidige stand op de site)
- Pakketten eenmalig: Start €200 · Groei €350 · Compleet €500.
- Abonnementen per maand, maandelijkse factuur: Basis €25 · Plus €49 · Pro €79 (Pro = tot 6 aanpassingen, niet onbeperkt).
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
- Voorbeeldontwerpen staan in `concepts/` (merk, licht, warm); foto's in `assets/foto/`.

## Techniek
- Alle pagina's worden gegenereerd door `python3 build.py` (f-strings: letterlijke accolades als `{{ }}`).
- Teksten en pagina's in `src/` (core.py + pages/), stijl in `assets/css/`, gedrag in `assets/js/` (site.js, motion.js).
- CSP in `vercel.json` bevat een hash van het inline script; herberekenen als `INLINE_JS` verandert.
- Testscreenshots en tijdelijke bestanden nooit in deze map zetten (gebruik een scratchpad).
