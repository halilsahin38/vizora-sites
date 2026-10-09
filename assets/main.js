const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ---------- Navigatie ---------- */
const nav = document.querySelector('.nav');
const toggle = document.querySelector('.nav__toggle');

const onScrollNav = () => nav.classList.toggle('is-scrolled', window.scrollY > 20);
onScrollNav();
window.addEventListener('scroll', onScrollNav, { passive: true });

toggle.addEventListener('click', () => {
  const open = nav.classList.toggle('is-open');
  toggle.setAttribute('aria-expanded', open);
  toggle.setAttribute('aria-label', open ? 'Menu sluiten' : 'Menu openen');
});
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && nav.classList.contains('is-open')) toggle.click();
});

/* ---------- Koppen woord voor woord ---------- */
function splitWords(el) {
  let i = 0;
  const walk = (node) => {
    [...node.childNodes].forEach((child) => {
      if (child.nodeType === Node.TEXT_NODE) {
        const frag = document.createDocumentFragment();
        child.textContent.split(/(\s+)/).forEach((part) => {
          if (!part) return;
          if (/^\s+$/.test(part)) { frag.append(' '); return; }
          const outer = document.createElement('span');
          const inner = document.createElement('span');
          outer.className = 'w';
          inner.textContent = part;
          inner.style.transitionDelay = `${i++ * 55}ms`;
          outer.append(inner);
          frag.append(outer);
        });
        child.replaceWith(frag);
      } else if (child.nodeType === Node.ELEMENT_NODE) {
        walk(child);
      }
    });
  };
  walk(el);
}
document.querySelectorAll('.split-words').forEach(splitWords);

/* ---------- Infaden bij scrollen ---------- */
const io = new IntersectionObserver(
  (entries) => entries.forEach((e) => {
    if (!e.isIntersecting) return;
    e.target.classList.add('is-visible');
    io.unobserve(e.target);
  }),
  { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
);
document.querySelectorAll('.reveal, .split-words, .tl-item, .dash').forEach((el) => {
  if (el.classList.contains('reveal') && el.dataset.delay) {
    el.style.transitionDelay = `${el.dataset.delay}ms`;
  }
  io.observe(el);
});

/* ---------- Schuivende strook: inhoud verdubbelen voor naadloze loop ---------- */
document.querySelectorAll('.marquee__track').forEach((track) => {
  [...track.children].forEach((child) => {
    const clone = child.cloneNode(true);
    clone.setAttribute('aria-hidden', 'true');
    track.append(clone);
  });
});

/* ---------- Parallax + tijdlijn ---------- */
const parallaxEls = [...document.querySelectorAll('[data-speed]')];
const timeline = document.querySelector('.timeline');
let ticking = false;

function onFrame() {
  const vh = window.innerHeight;
  if (!reduceMotion) {
    parallaxEls.forEach((el) => {
      const rect = el.parentElement.getBoundingClientRect();
      if (rect.bottom < -200 || rect.top > vh + 200) return;
      const offset = (rect.top + rect.height / 2 - vh / 2) * parseFloat(el.dataset.speed);
      el.style.transform = `translate3d(0, ${offset.toFixed(1)}px, 0)`;
    });
  }
  if (timeline) {
    const r = timeline.getBoundingClientRect();
    const p = Math.min(1, Math.max(0, (vh * 0.6 - r.top) / r.height));
    timeline.style.setProperty('--progress', p.toFixed(3));
  }
  ticking = false;
}
const requestFrame = () => {
  if (!ticking) { requestAnimationFrame(onFrame); ticking = true; }
};
if (parallaxEls.length || timeline) {
  onFrame();
  window.addEventListener('scroll', requestFrame, { passive: true });
  window.addEventListener('resize', requestFrame);
}

/* ---------- Gesprek plannen ---------- */
const booking = document.getElementById('booking');
if (booking) {
  const WHATSAPP = '31638705348';
  const EMAIL = 'halilsahinai@gmail.com';
  const datesEl = booking.querySelector('.dates');
  const summary = booking.querySelector('[data-summary]');
  const errorEl = booking.querySelector('.booking__error');
  const dayFmt = new Intl.DateTimeFormat('nl-NL', { weekday: 'short' });
  const monthFmt = new Intl.DateTimeFormat('nl-NL', { month: 'short' });
  const fullFmt = new Intl.DateTimeFormat('nl-NL', { weekday: 'long', day: 'numeric', month: 'long' });

  // Volgende 12 werkdagen (ma t/m za), vanaf morgen
  const d = new Date();
  let added = 0;
  while (added < 12) {
    d.setDate(d.getDate() + 1);
    if (d.getDay() === 0) continue;
    const id = `date-${added}`;
    const value = fullFmt.format(d);
    const wrap = document.createElement('div');
    wrap.className = 'choice';
    wrap.innerHTML =
      `<input type="radio" name="datum" id="${id}" value="${value}">` +
      `<label for="${id}"><small>${dayFmt.format(d).replace('.', '')}</small>` +
      `<b>${d.getDate()}</b><small>${monthFmt.format(d).replace('.', '')}</small></label>`;
    datesEl.append(wrap);
    added++;
  }

  const val = (name) => booking.querySelector(`[name="${name}"]:checked`)?.value;

  const updateSummary = () => {
    const datum = val('datum');
    const tijd = val('tijd');
    const vorm = val('vorm');
    summary.textContent = datum || tijd
      ? `${vorm || 'Gesprek'}${datum ? ` op ${datum}` : ''}${tijd ? ` om ${tijd}` : ''}`
      : 'Kies hierboven een dag en tijd';
  };
  booking.addEventListener('change', updateSummary);
  updateSummary();

  const buildMessage = () => {
    const f = new FormData(booking);
    return [
      'Hoi Vizora Digital! Ik wil graag een gratis kennismakingsgesprek plannen.',
      '',
      `Voorkeur: ${val('vorm')} op ${val('datum')} om ${val('tijd')}`,
      `Interesse in: ${f.getAll('dienst').join(', ') || 'nog niet zeker'}`,
      '',
      `Naam: ${f.get('naam')}`,
      f.get('bedrijf') ? `Bedrijf: ${f.get('bedrijf')}` : null,
      `Telefoon: ${f.get('telefoon')}`,
      f.get('bericht') ? `\nToelichting: ${f.get('bericht')}` : null,
    ].filter((l) => l !== null).join('\n');
  };

  const validate = () => {
    const missing = [];
    if (!val('datum')) missing.push('een dag');
    if (!val('tijd')) missing.push('een tijd');
    if (!booking.naam.value.trim()) missing.push('je naam');
    if (!booking.telefoon.value.trim()) missing.push('je telefoonnummer');
    if (missing.length) {
      errorEl.textContent = `Vul nog in: ${missing.join(', ')}.`;
      errorEl.classList.add('is-shown');
      errorEl.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'center' });
      return false;
    }
    errorEl.classList.remove('is-shown');
    return true;
  };

  booking.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!validate()) return;
    window.open(`https://wa.me/${WHATSAPP}?text=${encodeURIComponent(buildMessage())}`, '_blank', 'noopener');
  });
  booking.querySelector('[data-email]').addEventListener('click', () => {
    if (!validate()) return;
    const subject = `Kennismakingsgesprek - ${booking.naam.value.trim()}`;
    window.location.href = `mailto:${EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(buildMessage())}`;
  });
}

/* ---------- Contactformulier vooraf invullen vanuit link ---------- */
if (booking) {
  const params = new URLSearchParams(location.search);
  const bedrijf = params.get('bedrijf');
  const pakket = params.get('pakket');
  const branche = params.get('branche');
  if (bedrijf) booking.bedrijf.value = bedrijf.slice(0, 60);
  if (pakket || branche) {
    const abo = (pakket || '').startsWith('Abonnement');
    const box = booking.querySelector(`[name="dienst"][value="${abo ? 'Website-abonnement' : 'Website'}"]`);
    if (box) box.checked = true;
    const parts = [];
    if (abo) parts.push(`Ik heb interesse in het website-abonnement${pakket.length > 11 ? ` (${pakket.slice(11, 20)})` : ''}.`);
    else if (pakket) parts.push(`Ik heb interesse in het pakket ${pakket.slice(0, 20)}.`);
    if (branche) parts.push(`Mijn zaak: ${branche.slice(0, 30)}.`);
    booking.bericht.value = parts.join(' ');
  }
}

/* ---------- Demo: zie je eigen website ---------- */
const demo = document.querySelector('[data-demo]');
if (demo) {
  const PRESETS = {
    Kapper: { head: 'Fresh cuts, elke dag', cta: 'Maak een afspraak', cards: ['Knippen', 'Baard', 'Styling'], theme: 'barber' },
    Restaurant: { head: 'Proef het verschil', cta: 'Reserveer een tafel', cards: ['Menu', 'Lunch', 'Diner'], theme: 'resto' },
    Salon: { head: 'Jouw moment van rust', cta: 'Boek een behandeling', cards: ['Nagels', 'Gezicht', 'Massage'], theme: 'beauty' },
    Bedrijf: { head: 'Vakwerk waar je op bouwt', cta: 'Vraag een offerte aan', cards: ['Diensten', 'Projecten', 'Reviews'], theme: 'build' },
  };
  const input = demo.querySelector('[data-demo-input]');
  const view = demo.querySelector('[data-demo-view]');
  const nameEls = view.querySelectorAll('[data-demo-name]');
  const initialEl = view.querySelector('[data-demo-initial]');
  const urlEl = view.querySelector('[data-demo-url]');
  const headEl = view.querySelector('[data-demo-head]');
  const ctaEl = view.querySelector('[data-demo-cta]');
  const cardEls = view.querySelectorAll('[data-demo-card]');
  const go = demo.querySelector('[data-demo-go]');

  const slug = (t) => t.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, '') || 'jouwzaak';

  const update = () => {
    const name = input.value.trim() || 'Jouw Zaak';
    const type = demo.querySelector('[name="demo-type"]:checked').value;
    const p = PRESETS[type];
    nameEls.forEach((el) => { el.textContent = name; });
    initialEl.textContent = name.charAt(0).toUpperCase();
    urlEl.textContent = `${slug(name)}.nl`;
    headEl.textContent = p.head;
    ctaEl.textContent = p.cta;
    cardEls.forEach((el, i) => { el.textContent = p.cards[i]; });
    view.dataset.theme = p.theme;
    const q = new URLSearchParams({ branche: type });
    if (input.value.trim()) q.set('bedrijf', input.value.trim());
    go.href = `contact.html?${q}`;
  };
  let pulse;
  const bump = () => {
    view.classList.remove('is-updated');
    void view.offsetWidth;
    view.classList.add('is-updated');
    clearTimeout(pulse);
    pulse = setTimeout(() => view.classList.remove('is-updated'), 600);
  };
  input.addEventListener('input', update);
  demo.addEventListener('change', () => { update(); bump(); });
  update();
}

/* ---------- Verfijning voor muis-gebruikers ---------- */
const finePointer = window.matchMedia('(pointer: fine)').matches;
if (finePointer && !reduceMotion) {
  // cursor-ring die zacht meebeweegt
  const ring = document.createElement('div');
  ring.className = 'cursor';
  ring.setAttribute('aria-hidden', 'true');
  document.body.append(ring);
  let mx = -100, my = -100, rx = -100, ry = -100, raf = null;
  const follow = () => {
    rx += (mx - rx) * 0.2;
    ry += (my - ry) * 0.2;
    ring.style.transform = `translate3d(${rx}px, ${ry}px, 0)`;
    raf = Math.abs(mx - rx) + Math.abs(my - ry) > 0.3 ? requestAnimationFrame(follow) : null;
  };
  window.addEventListener('pointermove', (e) => {
    mx = e.clientX; my = e.clientY;
    ring.classList.add('is-active');
    if (!raf) raf = requestAnimationFrame(follow);
  }, { passive: true });
  document.addEventListener('pointerleave', () => ring.classList.remove('is-active'));
  document.addEventListener('pointerover', (e) => {
    ring.classList.toggle('is-hover', !!e.target.closest('a, button, label, input, textarea, [data-contour]'));
  });

  // magnetische knoppen
  document.querySelectorAll('.btn').forEach((btn) => {
    btn.addEventListener('pointermove', (e) => {
      const r = btn.getBoundingClientRect();
      const x = (e.clientX - r.left - r.width / 2) * 0.18;
      const y = (e.clientY - r.top - r.height / 2) * 0.3;
      btn.style.translate = `${x.toFixed(1)}px ${y.toFixed(1)}px`;
    });
    btn.addEventListener('pointerleave', () => { btn.style.translate = ''; });
  });
}

/* ---------- Zachte overgang tussen pagina's ---------- */
if (!reduceMotion) {
  document.addEventListener('click', (e) => {
    const a = e.target.closest('a[href]');
    if (!a || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    if (a.target === '_blank' || a.hasAttribute('download')) return;
    const url = new URL(a.href, location.href);
    if (url.origin !== location.origin || !/\.html$|\/$/.test(url.pathname)) return;
    if (url.pathname === location.pathname && url.hash) return;
    e.preventDefault();
    document.body.classList.add('is-leaving');
    setTimeout(() => { location.href = url.href; }, 320);
  });
  window.addEventListener('pageshow', (e) => {
    if (e.persisted) document.body.classList.remove('is-leaving');
  });
}

/* ---------- Voor/na-schuif ---------- */
document.querySelectorAll('[data-ba]').forEach((ba) => {
  const range = ba.querySelector('.ba__range');
  const set = (v) => { ba.style.setProperty('--pos', `${v}%`); };
  range.addEventListener('input', () => set(range.value));
  // slepen met muis of vinger over het hele beeld
  let dragging = false;
  const fromPointer = (e) => {
    const r = ba.getBoundingClientRect();
    const v = Math.min(100, Math.max(0, ((e.clientX - r.left) / r.width) * 100));
    range.value = v; set(v.toFixed(1));
  };
  ba.addEventListener('pointerdown', (e) => { dragging = true; ba.dataset.touched = '1'; ba.setPointerCapture(e.pointerId); fromPointer(e); });
  ba.addEventListener('pointermove', (e) => { if (dragging) fromPointer(e); });
  ['pointerup', 'pointercancel'].forEach((t) => ba.addEventListener(t, () => { dragging = false; }));
  // eenmalige hint-beweging zodra de schuif in beeld komt
  if (!reduceMotion) {
    new IntersectionObserver(([e], obs) => {
      if (!e.isIntersecting) return;
      obs.disconnect();
      const start = performance.now();
      const step = (now) => {
        const t = Math.min(1, (now - start) / 1600);
        const v = 50 + Math.sin(t * Math.PI * 2) * 22 * (1 - t);
        if (ba.dataset.touched) return;
        set(v.toFixed(1)); range.value = v;
        if (t < 1 && !ba.dataset.touched) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    }, { threshold: 0.5 }).observe(ba);
  }
});

/* ---------- Groei-calculator ---------- */
const calc = document.querySelector('[data-calc]');
if (calc) {
  const PRESETS = {
    kapper: { spend: 30, extra: 8, freq: 8 },
    restaurant: { spend: 45, extra: 15, freq: 3 },
    salon: { spend: 55, extra: 6, freq: 6 },
    bakkerij: { spend: 12, extra: 20, freq: 25 },
    anders: { spend: 150, extra: 3, freq: 2 },
  };
  const PACKAGE = 350;
  const eur = new Intl.NumberFormat('nl-NL', { style: 'currency', currency: 'EUR', maximumFractionDigits: 0 });
  const inputs = ['spend', 'extra', 'freq'].reduce((o, n) => ({ ...o, [n]: calc.querySelector(`[name="${n}"]`) }), {});
  const out = (n) => calc.querySelector(`[data-out="${n}"]`);
  const res = (n) => calc.querySelector(`[data-res="${n}"]`);
  let shown = 0, anim;

  const countTo = (el, to) => {
    cancelAnimationFrame(anim);
    const from = shown, start = performance.now(), dur = reduceMotion ? 0 : 600;
    const step = (now) => {
      const t = dur ? Math.min(1, (now - start) / dur) : 1;
      shown = from + (to - from) * (1 - Math.pow(1 - t, 3));
      el.textContent = eur.format(Math.round(shown));
      if (t < 1) anim = requestAnimationFrame(step);
    };
    anim = requestAnimationFrame(step);
  };

  const update = () => {
    const spend = +inputs.spend.value, extra = +inputs.extra.value, freq = +inputs.freq.value;
    Object.values(inputs).forEach((i) => i.style.setProperty('--fill', `${((i.value - i.min) / (i.max - i.min)) * 100}%`));
    out('spend').textContent = eur.format(spend);
    out('extra').textContent = extra;
    out('freq').textContent = `${freq}×`;
    // nieuwe klanten komen gelijkmatig binnen; wie in maand m komt, komt de rest van het jaar terug (minstens 1 bezoek)
    let visits1 = 0;
    for (let m = 1; m <= 12; m++) visits1 += extra * Math.max(1, (freq * (13 - m)) / 12);
    countTo(res('year'), Math.round(visits1 * spend));
    res('client').textContent = eur.format(spend * freq);
    const pay = Math.ceil(PACKAGE / spend);
    res('payback').textContent = `${pay} ${pay === 1 ? 'klantbezoek' : 'klantbezoeken'}`;
  };
  const applyPreset = (key) => {
    const p = PRESETS[key];
    Object.entries(p).forEach(([k, v]) => { inputs[k].value = v; });
    update();
  };
  calc.addEventListener('input', (e) => { if (e.target.type === 'range') update(); });
  calc.addEventListener('change', (e) => { if (e.target.name === 'calc-type') applyPreset(e.target.value); });
  applyPreset('kapper');
}

/* ---------- Jaar in footer ---------- */
document.querySelectorAll('[data-year]').forEach((el) => { el.textContent = new Date().getFullYear(); });

/* ---------- Contactknop rechtsonder ---------- */
const dock = document.querySelector('[data-dock]');
if (dock) {
  const fab = dock.querySelector('.dock__fab');
  const panel = dock.querySelector('.dock__panel');
  const setOpen = (open) => {
    panel.hidden = !open;
    dock.classList.toggle('is-open', open);
    fab.setAttribute('aria-expanded', open);
    fab.setAttribute('aria-label', open ? 'Contactopties sluiten' : 'Contactopties openen');
  };
  fab.addEventListener('click', () => setOpen(panel.hidden));
  dock.querySelector('[data-dock-close]').addEventListener('click', () => { setOpen(false); fab.focus(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !panel.hidden) { setOpen(false); fab.focus(); } });

  // bereikbaar: ma t/m za 09:00 - 18:00 (Nederlandse tijd)
  const status = dock.querySelector('[data-dock-status]');
  try {
    const parts = Object.fromEntries(new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/Amsterdam', weekday: 'short', hour: 'numeric', hour12: false })
      .formatToParts(new Date()).map((p) => [p.type, p.value]));
    const hour = parseInt(parts.hour, 10) % 24;
    const open = parts.weekday !== 'Sun' && hour >= 9 && hour < 18;
    if (!open) {
      status.classList.add('is-closed');
      const nextMonday = parts.weekday === 'Sun' || (parts.weekday === 'Sat' && hour >= 18);
      const when = nextMonday ? 'maandag ' : (hour >= 18 ? 'morgen ' : '');
      status.querySelector('span').textContent = `We reageren ${when}vanaf 09:00`;
    }
  } catch (e) { /* laat standaardtekst staan */ }
}

/* ---------- Snel bericht (homepage) ---------- */
const quick = document.querySelector('[data-quick]');
if (quick) {
  const err = quick.querySelector('.reach__error');
  const val = (n) => quick.elements[n].value.trim();
  const message = () => [
    'Hallo Vizora Digital,', '',
    val('bericht') || 'Ik wil graag meer weten over jullie diensten.', '',
    `Naam: ${val('naam')}`,
    val('bedrijf') ? `Bedrijf: ${val('bedrijf')}` : '',
    `Bereikbaar op: ${val('contact')}`,
  ].filter((l, i, a) => l !== '' || a[i - 1] !== '').join('\n');
  const ok = () => {
    const good = val('naam') && val('contact');
    err.hidden = !!good;
    return good;
  };
  quick.querySelector('[data-send="wa"]').addEventListener('click', () => {
    if (ok()) window.open(`https://wa.me/31638705348?text=${encodeURIComponent(message())}`, '_blank', 'noopener');
  });
  quick.querySelector('[data-send="mail"]').addEventListener('click', () => {
    if (ok()) window.location.href = `mailto:halilsahinai@gmail.com?subject=${encodeURIComponent('Vraag via de website - ' + val('naam'))}&body=${encodeURIComponent(message())}`;
  });
}
