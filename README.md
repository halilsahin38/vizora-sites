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

De foto's in `assets/foto/` zijn rechtenvrij (CC0, vrij te gebruiken, ook commercieel), gevonden via Openverse:

- `werkplek` – https://www.rawpixel.com/image/8809250/photo-image-books-hands-social-media
- `schets` – https://stocksnap.io/photo/office-work-PE894KZLRX
- `groeiplan` – https://www.rawpixel.com/image/11515751/persons-hands-notebook-and-cup-coffee

Ze zijn tijdelijk en kunnen later vervangen worden door eigen foto's of Higgsfield-beelden (zelfde bestandsnaam = direct vervangen).
