/* Vizora Digital — beweging (GSAP + ScrollTrigger + Lenis, lokaal in assets/vendor/)
 *
 * Gebruik met data-attributen in de HTML:
 *   data-lines        hoofdtitel: regels schuiven één voor één omhoog bij het laden (alleen h1)
 *   data-reveal       element komt zacht omhoog in beeld
 *   data-stagger      op een lijst/raster/tabeldeel: de kinderen komen kort na elkaar omhoog in beeld
 *                     (y 30 → 0, opacity 0 → 1, één keer; wat tegelijk binnenkomt, komt na elkaar). Zet dan
 *                     géén data-reveal op die kinderen. Begintoestand staat in base.css (html.js:not(.ready)).
 *   data-fill         alinea kleurt woord voor woord van lichtgrijs naar inkt tijdens het scrollen
 *   data-clip         beeld opent als een gordijn en zoomt licht uit
 *   data-drift        beeld schuift rustig binnen zijn kader (parallax op de <picture>; samen met data-clip te gebruiken)
 *   data-grow         groot beeld groeit mee tijdens het scrollen (hero)
 *   data-speed="-0.1" parallax: beweegt langzamer/sneller dan de pagina
 *   data-switcher     voorbeelden: knoppen wisselen de website op laptop/telefoon; op desktop ook door te scrollen (pin)
 *
 * Met classes:
 *   .sheet            vel met afgeronde bovenkant dat over het vorige deel schuift (stijl in base.css)
 *   .stack            het deel vóór een .sheet (of het laatste deel vóór de voet): krimpt licht en wordt donkerder
 *                     als het volgende vel eroverheen schuift. Geen .stack op een deel met een vastgezette (pin) laptop.
 *   .ph__title        titel van de subpagina-kop: schuift bij scrollen langzaam omhoog en vervaagt een beetje
 *
 * Bij prefers-reduced-motion of zonder GSAP blijft alles gewoon zichtbaar en statisch.
 */
(() => {
  const root = document.documentElement;
  const done = () => root.classList.add('ready');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const { gsap, ScrollTrigger, Lenis } = window;

  // woorden in spans (voor data-fill)
  const splitWords = (el) => {
    const walk = (node) => {
      [...node.childNodes].forEach((n) => {
        if (n.nodeType === 3) {
          const frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach((part) => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.append(part); return; }
            const s = document.createElement('span'); s.className = n.parentElement.closest('em') ? 'w is-em' : 'w'; s.textContent = part; frag.append(s);
          });
          n.replaceWith(frag);
        } else if (n.nodeType === 1) walk(n);
      });
    };
    walk(el);
    el.classList.add('is-split');
    return el.querySelectorAll('.w');
  };

  // titel in regels (voor data-lines): meet woordposities en groepeer per regel
  const splitLines = (el) => {
    const words = splitWords(el);
    const lines = [];
    let top = null;
    words.forEach((w) => {
      const t = w.offsetTop;
      if (top === null || Math.abs(t - top) > 4) { lines.push([]); top = t; }
      lines[lines.length - 1].push(w);
    });
    const html = lines.map((ws) => {
      // geen spatie vóór leestekens die direct aan het vorige woord vastzitten (bv. 'gesprek</em>.')
      const inner = ws.map((w, k) => (k && !/^[.,!?:;]/.test(w.textContent) ? ' ' : '') + w.outerHTML).join('');
      return `<span class="tl"><span class="tl__in">${inner}</span></span>`;
    }).join('');
    el.setAttribute('aria-label', el.textContent.trim());
    el.innerHTML = html;
    el.querySelectorAll('.tl').forEach((l) => l.setAttribute('aria-hidden', 'true'));
    return el.querySelectorAll('.tl__in');
  };

  /* voorbeelden: één scherm, drie websites (knoppen werken altijd, ook zonder GSAP) */
  const sw = document.querySelector('[data-switcher]');
  let swSet = () => {};
  if (sw) {
    const tabs = [...sw.querySelectorAll('[data-sw-tab]')];
    const shots = [...sw.querySelectorAll('[data-sw-shot]')];
    let cur = 0;
    swSet = (i) => {
      if (i === cur) return;
      cur = i;
      tabs.forEach((t, k) => { t.classList.toggle('is-on', k === i); t.setAttribute('aria-pressed', String(k === i)); });
      shots.forEach((s, k) => { s.classList.toggle('is-on', k === i); if (k === i) s.removeAttribute('aria-hidden'); else s.setAttribute('aria-hidden', 'true'); });
    };
    tabs.forEach((t, i) => t.addEventListener('click', () => {
      // vastgezet: naar het stuk van de sectie scrollen dat bij deze stijl hoort
      if (sw.classList.contains('is-pinned')) {
        const top = sw.getBoundingClientRect().top + window.scrollY;
        const y = top + (sw.offsetHeight - window.innerHeight) * (i + 0.5) / tabs.length;
        if (window.__lenis) window.__lenis.scrollTo(y); else window.scrollTo({ top: y, behavior: 'smooth' });
      }
      swSet(i);
    }));
  }

  if (!gsap || !ScrollTrigger || reduce) {
    document.querySelectorAll('[data-fill]').forEach((el) => el.classList.add('is-static'));
    done();
    return;
  }

  gsap.registerPlugin(ScrollTrigger);
  ScrollTrigger.config({ ignoreMobileResize: true });
  const desktop = window.matchMedia('(min-width: 961px) and (hover: hover) and (pointer: fine)').matches;

  /* soepel scrollen (alleen met muis/trackpad) */
  if (Lenis && desktop) {
    const lenis = new Lenis({ autoRaf: false, anchors: true, lerp: 0.1 }); // anchors volgen scroll-padding-top uit base.css
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add((t) => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
    window.__lenis = lenis;
  }

  /* subpagina-kop: de titel als geheel (niet per woord) schuift langzaam omhoog en vervaagt een beetje
     (tot 0.8, terwijl hij uit beeld gaat: zo blijft ook het terracotta woord leesbaar, contrast > 3:1).
     Pas na het opsplitsen in regels starten: anders zou de titel even zichtbaar worden vóór zijn intro. */
  const ph = document.querySelector('.ph');
  const phTitle = ph && ph.querySelector('.ph__title');
  const phDrift = () => {
    if (!phTitle) return;
    gsap.timeline({ scrollTrigger: { trigger: ph, start: 'top top', end: 'bottom top', scrub: true, invalidateOnRefresh: true } })
      .fromTo(phTitle, { y: 0 }, { y: () => -ph.offsetHeight * (desktop ? 0.15 : 0.1), ease: 'none', duration: 1 }, 0)
      .fromTo(phTitle, { opacity: 1 }, { opacity: 0.8, ease: 'none', duration: 0.6 }, 0);
  };

  /* hoofdtitel: regels omhoog */
  const start = () => {
    document.querySelectorAll('[data-lines]').forEach((el) => {
      const inners = splitLines(el);
      gsap.from(inners, { yPercent: 110, duration: 1.2, ease: 'expo.out', stagger: 0.09, delay: 0.1 });
    });
    done();
    phDrift();
  };
  (document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve()).then(start);

  /* zacht in beeld (niet binnen een data-stagger-lijst: daar bewegen de kinderen al) */
  gsap.utils.toArray('[data-reveal]').forEach((el) => {
    if (el.closest('[data-stagger] > *')) return;
    gsap.from(el, { y: 36, opacity: 0, duration: 1.1, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 90%', once: true } });
  });

  /* lijsten, rasters en tabelrijen: kinderen komen kort na elkaar in beeld. Per lijst een batch, zodat lange
     lijsten meelopen met het scrollen en wat tegelijk binnenkomt (bv. drie kolommen) netjes na elkaar komt. */
  gsap.utils.toArray('[data-stagger]').forEach((list) => {
    const items = [...list.children];
    if (!items.length) return;
    gsap.set(items, { y: 30, opacity: 0 });
    ScrollTrigger.batch(items, {
      start: 'top 92%', once: true,
      onEnter: (batch) => gsap.to(batch, { y: 0, opacity: 1, duration: 0.9, ease: 'power3.out', stagger: 0.06, overwrite: true, clearProps: 'transform' }),
    });
  });

  /* alinea kleurt mee */
  gsap.utils.toArray('[data-fill]').forEach((el) => {
    const words = splitWords(el);
    gsap.fromTo(words, { opacity: 0.18 }, {
      opacity: 1, ease: 'none', stagger: 0.08,
      scrollTrigger: { trigger: el, start: 'top 82%', end: 'bottom 50%', scrub: true },
    });
  });

  /* beeld opent als gordijn */
  gsap.utils.toArray('[data-clip]').forEach((el) => {
    const img = el.querySelector('img');
    const tl = gsap.timeline({ scrollTrigger: { trigger: el, start: 'top 92%', end: 'top 40%', scrub: 0.6 } });
    tl.fromTo(el, { clipPath: 'inset(9% 7% 9% 7% round 14px)' }, { clipPath: 'inset(0% 0% 0% 0% round 8px)', ease: 'none' }, 0);
    if (img) tl.fromTo(img, { scale: 1.18 }, { scale: 1, ease: 'none' }, 0);
  });

  /* beeld schuift rustig binnen zijn kader: de <picture> beweegt (data-clip schaalt de <img> zelf).
     Schaal 1.15 dekt een verschuiving van 7% naar boven en beneden, zodat de rand van het kader nooit leeg is. */
  gsap.utils.toArray('[data-drift]').forEach((frame) => {
    const media = frame.querySelector('picture') || frame.querySelector('img');
    if (!media) return;
    gsap.fromTo(media, { yPercent: -7, scale: 1.15 }, {
      yPercent: 7, scale: 1.15, ease: 'none',
      scrollTrigger: { trigger: frame, start: 'top bottom', end: 'bottom top', scrub: true },
    });
  });

  /* hero-beeld groeit mee */
  gsap.utils.toArray('[data-grow]').forEach((el) => {
    const img = el.querySelector('img');
    gsap.fromTo(el, { scale: 0.9, borderRadius: 24 }, {
      scale: 1, borderRadius: 8, ease: 'none',
      scrollTrigger: { trigger: el, start: 'top 95%', end: 'top 20%', scrub: 0.6 },
    });
    if (img) gsap.fromTo(img, { yPercent: -6, scale: 1.12 }, { yPercent: 4, scale: 1, ease: 'none', scrollTrigger: { trigger: el, start: 'top bottom', end: 'bottom top', scrub: true } });
  });

  /* parallax */
  gsap.utils.toArray('[data-speed]').forEach((el) => {
    const s = parseFloat(el.dataset.speed) || 0;
    gsap.fromTo(el, { yPercent: -s * 100 }, { yPercent: s * 100, ease: 'none', scrollTrigger: { trigger: el.parentElement, start: 'top bottom', end: 'bottom top', scrub: true } });
  });

  /* voorbeelden vastzetten op desktop: scrollen wisselt de website */
  if (sw && desktop) {
    const n = sw.querySelectorAll('[data-sw-tab]').length;
    sw.classList.add('is-pinned');
    ScrollTrigger.create({
      trigger: sw, start: 'top top', end: 'bottom bottom',
      onUpdate: (st) => swSet(Math.min(n - 1, Math.floor(st.progress * n))),
    });
  }

  /* hero: inzoomen op het zwarte laptopscherm tot het het hele beeld vult; het scherm kleurt naar inkt
     en loopt zo naadloos over in het donkere voorbeelden-deel eronder (alleen desktop) */
  const zoom = document.querySelector('[data-zoom]');
  if (zoom && desktop) {
    const media = zoom.querySelector('.hero__media');
    const screenEl = zoom.querySelector('.hero__screen');
    const S = { x: 0.1287, y: 0.1864, w: 0.5535, h: 0.6072 }; // schermvlak in de foto (zie .hero__screen)
    const geo = () => {
      const W = zoom.offsetWidth, H = zoom.offsetHeight, left = zoom.getBoundingClientRect().left;
      const sx = left + (S.x + S.w / 2) * W, sy = window.innerHeight / 2 - H / 2 + (S.y + S.h / 2) * H; // bij vastzetten staat de foto midden in beeld
      return {
        s: Math.max(window.innerWidth / (S.w * W), window.innerHeight / (S.h * H)) * 1.12,
        dx: window.innerWidth / 2 - sx, dy: window.innerHeight / 2 - sy,
      };
    };
    gsap.set(media, { transformOrigin: `${(S.x + S.w / 2) * 100}% ${(S.y + S.h / 2) * 100}%` });
    gsap.timeline({ scrollTrigger: { trigger: zoom, start: 'center center', end: '+=120%', pin: true, scrub: true, invalidateOnRefresh: true, anticipatePin: 1 } })
      // de wrapper wordt vastgezet, het beeld erin schaalt (pin en transform niet op hetzelfde element)
      .to(media, { scale: () => geo().s, x: () => geo().dx, y: () => geo().dy, ease: 'power2.in', duration: 1 }, 0)
      .to(media, { borderRadius: 0, ease: 'none', duration: 0.3 }, 0)
      .to(screenEl, { opacity: 1, ease: 'none', duration: 0.3 }, 0.7);
    gsap.fromTo('.hero__title, .hero__row', { yPercent: 0, opacity: 1 }, { yPercent: -30, opacity: 0, ease: 'none', immediateRender: false, scrollTrigger: { trigger: '.hero', start: 'top top', end: () => '+=' + Math.max(200, zoom.getBoundingClientRect().top + window.scrollY + zoom.offsetHeight / 2 - window.innerHeight / 2), scrub: true, invalidateOnRefresh: true } });
  }

  /* telefoon/tablet: geen vastzetten, wel rustig inzoomen op het scherm terwijl de hero wegscrollt */
  if (zoom && !desktop) {
    const media = zoom.querySelector('.hero__media');
    gsap.fromTo(media, { scale: 1 }, { scale: 1.45, transformOrigin: '37.4% 49%', ease: 'none', scrollTrigger: { trigger: media, start: 'top 55%', end: 'bottom top', scrub: true } });
  }

  /* stapelende vlakken: het vorige deel krimpt licht en wordt donkerder als het volgende eroverheen schuift */
  gsap.utils.toArray('.sheet, .ft').forEach((next) => {
    const prev = next.classList.contains('ft') ? document.querySelector('main > .stack:last-of-type') : next.previousElementSibling;
    if (!prev || !prev.classList.contains('stack')) return;
    // hero niet schalen: een transform op de hero breekt de vastgezette (gepinde) laptop
    const scale = !prev.querySelector('[data-zoom]');
    gsap.fromTo(prev, scale ? { scale: 1, '--dim': 0 } : { '--dim': 0 }, {
      ...(scale ? { scale: desktop ? 0.95 : 0.97 } : {}), '--dim': 0.5, ease: 'none',
      scrollTrigger: { trigger: next, start: 'top bottom', end: 'top top', scrub: true },
    });
  });

  /* grote 'Vizora' onderaan schuift omhoog in beeld */
  const word = document.querySelector('.ft__word');
  if (word) gsap.fromTo(word, { yPercent: 35 }, { yPercent: 0, ease: 'none', scrollTrigger: { trigger: word, start: 'top bottom', end: 'bottom bottom', scrub: true } });

  window.addEventListener('load', () => ScrollTrigger.refresh());
})();
