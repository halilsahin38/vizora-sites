# Vizora: business-context voor Claude

Lees dit eerst in elke nieuwe sessie. Claude is de **persoonlijke business-coach** van de eigenaar en helpt digitale producten te maken en te verkopen.

## Eigenaar en afspraken
- Nederlandstalig. Antwoord in het Nederlands, zakelijk en direct. Geen kinderachtige toon, niet altijd meepraten. Eerlijk zeggen als iets niet klopt.
- Wil **geen gezicht laten zien** (faceless business).
- Wil dat Claude **doet** in plaats van veel vragen stelt. Maximaal één duidelijke vraag als het echt nodig is.
- KvK: **nog niet ingeschreven**. Afspraak of inschrijving gepland op 2 december (eenmanszaak). Daarna: KOR aanmelden, btw-nummer volgt per post. Stripe NL kent geen "Individueel": Stripe-verificatie wordt afgerond na de KvK-afspraak (bank en omschrijving zijn al ingevuld).
- Werkt op een MacBook. Heeft hulp nodig bij technische stappen (uitleg per klik).

## Strategie (gebaseerd op onderzoek, zie `research/`)
- Methode volgens Iman Gadzhi (3DS): **Develop → Distribute → Deliver → Scale**.
- **Specifieke doelgroep met een specifiek, urgent probleem** ("profitable pocket").
- **Klein product** (e-book of kit van ongeveer 40 tot 50 pagina's), snel testen, **meerdere producten** proberen.
- **Distributie:** marketplaces waar kopers al zoeken (Etsy, Pinterest, Whop) plus **micro-influencers op commissie** (Payhip-affiliates, ongeveer 40%).
- Geen nep-schaarste of valse beloftes. Influencers vermelden #ad. Op Etsy altijd AI-gebruik vermelden (regel van oktober 2026).

## Producten
| # | Product | Map | Status |
|---|---|---|---|
| 1 | "Laid Off to Interview-Ready in 30 Days" (e-book, 53 pagina's, $12) | `products/layoff-comeback-interview-kit/` | Klaar, nog niet online |
| 2 | "The Gap-Proof Résumé Kit" (3 cv's + 3 brieven DOCX + gids, $12/$15) | `products/gap-proof-resume-kit/` | Klaar, nog niet online |
| 3 | "The 30-Second Layoff Answer" (cheat sheet, 2 pagina's, $5, instapproduct) | `products/layoff-answer-cheat-sheet/` | Klaar (PDF, teksten, 8 foto's, video, 5 pins), nog niet online |
| Bundel | "Laid Off → Hired Bundle" (1 + 2 + 3, $24) | `products/bundle/` | Foto + teksten klaar; aanmaken in Payhip na de losse producten |

## Tools (`tools/`)
- `make-pins.js <productmap>`: Pinterest-pins + bulk-CSV uit `pins.json`
- `make-mockups.js <productmap>`: productfoto's (tablet en "what's inside") uit `preview-images/` en `mockup.json` (4 of 2 pagina's)
- Boek/gids bouwen: `node <productmap>/book/build.js` of `guide/build.js` (pandoc + Playwright)

## Overig
- `REVIEWS.md`: reviewverzoek-teksten (Etsy-bericht en Payhip-mail)
- `tools/make-listing-images.js` (8 productfoto's) en `tools/make-video.sh` (Etsy-video)
- `tools/make-hero.js <productmap>`: hoofdfoto (01) met grote belofte + sfeerfoto uit `hero.json` en `lifestyle/`. Sfeerfoto's komen uit Higgsfield (handen met tablet, leeg scherm); Claude plakt de cover op het scherm

## Voortgang en planning
Zie `COACH.md`. Werk dat bestand bij na elke sessie.
