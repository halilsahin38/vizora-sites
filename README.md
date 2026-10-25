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
Op de telefoon- en laptopfoto's staan de voorbeeldontwerpen uit `concepts/` (merk = Atelier Dorr, licht = Mertens & Verhoef,
warm = Praktijk Wilgenhof; alle drie fictieve bedrijven). Elke stijl heeft een eigen foto:

- merk: laptop https://unsplash.com/photos/s7IIk_2dA7g · telefoon https://unsplash.com/photos/uD5SvzjOsgY
- licht: laptop https://unsplash.com/photos/wnZ3ai3_idw · telefoon https://unsplash.com/photos/J82GxqnwKSs
- warm: laptop https://unsplash.com/photos/ZWfOEaNfelY · telefoon https://unsplash.com/photos/zVraN8Nnc4c

De foto's binnen de voorbeeldontwerpen staan als bron vermeld bovenin elk conceptbestand.
