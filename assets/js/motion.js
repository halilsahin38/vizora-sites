/* Vizora Digital — beweging (GSAP + ScrollTrigger + Lenis, lokaal in assets/vendor/)
 *
 * Gebruik met data-attributen in de HTML:
 *   data-lines        hoofdtitel: regels schuiven één voor één omhoog bij het laden (alleen h1)
 *   data-reveal       element komt zacht omhoog in beeld
 *   data-fill         alinea kleurt woord voor woord van lichtgrijs naar inkt tijdens het scrollen
 *   data-clip         beeld opent als een gordijn en zoomt licht uit
 *   data-grow         groot beeld groeit mee tijdens het scrollen (hero)
 *   data-speed="-0.1" parallax: beweegt langzamer/sneller dan de pagina
 *   data-switcher     voorbeelden: knoppen wisselen de website op laptop/telefoon; op desktop ook door te scrollen (pin)
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
      const inner = ws.map((w) => w.outerHTML).join(' ');
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

  /* hoofdtitel: regels omhoog */
  const start = () => {
    document.querySelectorAll('[data-lines]').forEach((el) => {
      const inners = splitLines(el);
      gsap.from(inners, { yPercent: 110, duration: 1.2, ease: 'expo.out', stagger: 0.09, delay: 0.1 });
    });
    done();
  };
  (document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve()).then(start);

  /* zacht in beeld */
  gsap.utils.toArray('[data-reveal]').forEach((el) => {
    gsap.from(el, { y: 36, opacity: 0, duration: 1.1, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 90%', once: true } });
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

  window.addEventListener('load', () => ScrollTrigger.refresh());
})();
