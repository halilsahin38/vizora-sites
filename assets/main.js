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

/* ---------- Jaar in footer ---------- */
document.querySelectorAll('[data-year]').forEach((el) => { el.textContent = new Date().getFullYear(); });
