# Vizora Digital

Website van Vizora Digital (vizoradigital.nl): websites, social media & marketing vanuit Breda.

Statische site (HTML/CSS/JS), geen frameworks. Open `index.html` in je browser.

## Aanpassen

De HTML-pagina's worden gemaakt door `build.py`. Pas teksten daar aan en draai:

```
python3 build.py
```

## Conceptwebsites

In `concepts/` staan vier voorbeeldwebsites (barbershop, restaurant, salon, bakkerij).
Daarvan worden screenshots gemaakt die op de site gebruikt worden (hero, Contour Reveal, strook):

```
npm i playwright
node tools/render-concepts.mjs
```

De screenshots komen in `assets/concepts/`.

## Bestanden

| Bestand | Inhoud |
|---|---|
| `index.html` | Home: hero, Contour Reveal, demo, prijzen |
| `diensten.html` | Websites, social media, marketing |
| `prijzen.html` | Pakketten Start / Groei / Compleet + vergelijking |
| `werkwijze.html` | Stappen + FAQ |
| `over-ons.html` | Halil & Sahin |
| `contact.html` | Gratis gesprek plannen (via WhatsApp of e-mail) |
| `assets/style.css` | Design: beige, zwart-wit, gelaagd |
| `assets/main.js` | Menu, parallax, tekstanimaties, planner, demo, cursor |
| `assets/contour.js` | Contour Reveal (WebGL) |
| `assets/mosaic.js` | Mosaic Trail achter de CTA |
| `assets/logo.svg`, `logo-licht.svg` | Logo voor lichte / donkere achtergrond |
| `assets/profielfoto-*.png` | Profielfoto voor Instagram/TikTok |
| `vercel.json` | Beveiligingsheaders voor hosting op Vercel |
| `concepts/` | Bronbestanden van de conceptwebsites |
| `assets/concepts/` | Screenshots van de concepten |

## Foto's

De foto's in `assets/foto/` komen van Unsplash en vallen onder de Unsplash-licentie (gratis te gebruiken, ook commercieel, naamsvermelding niet verplicht).
Op `telefoon` en `laptop` is het voorbeeldontwerp uit `concepts/merk.html` op het scherm gezet.

- `telefoon` – https://unsplash.com/photos/person-holding-white-iphone-5-c-ikAlhV_zCHo
- `laptop` – https://unsplash.com/photos/black-and-silver-laptop-computer-on-brown-wooden-table-1Ps-Oi64lOA
- `ondernemer-winkel` – https://unsplash.com/photos/elderly-woman-smiling-in-a-room-filled-with-clothes-UZCqtOcY8b4
- `ondernemer-atelier` – https://unsplash.com/photos/woman-working-at-a-desk-with-craft-supplies-ag5H7Nqbf9U
- `ondernemer-zaak` – https://unsplash.com/photos/woman-sitting-in-front-of-brown-wooden-table-NoRsyXmHGpI
- `ondernemer-telefoon` – https://unsplash.com/photos/a-man-in-an-apron-looking-at-a-cell-phone-uk3ey_vhDKA
- `ondernemer-tablet` – https://unsplash.com/photos/woman-sitting-around-table-holding-tablet-JBwcenOuRCg
- `vakman` – https://unsplash.com/photos/a-man-playing-a-piano-96-ZnaO4NfI
- `koffie` – https://unsplash.com/photos/two-people-holding-gray-mugs-at-table-K8XYGbw4Ahg
- `breda` – https://unsplash.com/photos/a-group-of-people-walking-down-a-street-next-to-tall-buildings-U355VSVlL9E

Vervang een foto door een bestand met dezelfde naam (.jpg en .webp) om hem te wisselen.
