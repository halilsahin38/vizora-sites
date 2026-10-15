# Vizora Digital

Website van Vizora Digital (vizoradigital.nl): websites en online groei voor ondernemers in heel Nederland, vanuit Breda.

Statische site (HTML/CSS/JS), geen frameworks. Open `index.html` in je browser.

## Aanpassen

De HTML-pagina's worden gemaakt door `build.py` uit de bestanden in `src/`. Pas teksten daar aan en draai:

```
python3 build.py
```

Online via Cloudflare Pages: build command `python3 build.py`, output directory `dist`.

## Bestanden

| Bestand | Inhoud |
|---|---|
| `src/core.py` | Gedeelde delen: kop, voet, prijzen, garanties, vragen |
| `src/pages/*.py` | Eén bestand per pagina (home, diensten, prijzen, werkwijze, over-ons, contact, 404) |
| `assets/css/base.css` | Basisstijl (kleuren, letters, knoppen) |
| `assets/css/<pagina>.css` | Stijl per pagina |
| `assets/js/site.js` | Menu, contactknop, vragen, gesprek plannen |
| `assets/js/motion.js` | Beweging bij scrollen (GSAP, ScrollTrigger, Lenis in `assets/vendor/`) |
| `assets/foto/` | Telefoon- en laptopfoto's met de voorbeeldontwerpen |
| `concepts/` | Voorbeeldontwerpen merk, licht en warm (bron voor de foto's) |
| `tools/render-concepts.mjs` | Maakt screenshots van de voorbeeldontwerpen |
| `dist/` | Wordt gemaakt door `build.py`: alleen de website, plus `_headers` voor Cloudflare Pages (niet in git) |

## Foto's

De foto's in `assets/foto/` komen van Unsplash en vallen onder de Unsplash-licentie (gratis te gebruiken, ook commercieel, naamsvermelding niet verplicht).
Op de telefoon- en laptopfoto's zijn de voorbeeldontwerpen uit `concepts/merk.html`, `licht.html` en `warm.html` op het scherm gezet (`merk-`, `licht-`, `warm-`).

- telefoonfoto (`*-telefoon`) – https://unsplash.com/photos/person-holding-white-iphone-5-c-ikAlhV_zCHo
- laptopfoto (`*-laptop`) – https://unsplash.com/photos/black-and-silver-laptop-computer-on-brown-wooden-table-1Ps-Oi64lOA

Vervang een foto door een bestand met dezelfde naam (.jpg en .webp) om hem te wisselen.
