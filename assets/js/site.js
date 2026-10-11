/* Vizora Digital — basisgedrag (werkt ook zonder animatiebibliotheken) */
(() => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Mail- en bellinks ----------
     In een ingebedde weergave (zoals de voorbeeldlink) blokkeert de browser mailto:/tel: in het frame zelf
     ("inhoud geblokkeerd"). Daar openen we ze in een nieuw venster; lukt ook dat niet, dan tonen we het adres. */
  const framed = window.top !== window.self;
  let toastEl = null;
  const showToast = (html) => {
    if (!toastEl) {
      toastEl = document.createElement('div');
      toastEl.className = 'toast'; toastEl.setAttribute('role', 'status');
      document.body.append(toastEl);
    }
    toastEl.innerHTML = html;
    toastEl.classList.add('is-shown');
    clearTimeout(showToast.t);
    showToast.t = setTimeout(() => toastEl.classList.remove('is-shown'), 7000);
  };
  const openExternal = (url) => {
    if (!framed) { window.location.href = url; return; }
    let w = null;
    try { w = window.open(url, '_blank'); } catch (e) { /* geblokkeerd */ }
    if (w) { try { w.opener = null; } catch (e) { /* ander domein */ } return; }
    const [scheme, rest] = url.split(':');
    const value = decodeURIComponent(rest.split('?')[0]);
    showToast(scheme === 'tel'
      ? `Bel ons op <b>${value.replace('+31', '0').replace(/^(06)(\d{2})(\d{2})(\d{2})(\d{2})$/, '$1 $2 $3 $4 $5')}</b>`
      : `Mail ons op <b>${value}</b>`);
    if (navigator.clipboard) navigator.clipboard.writeText(value).catch(() => {});
  };
  if (framed) {
    document.addEventListener('click', (e) => {
      const a = e.target.closest('a[href^="mailto:"], a[href^="tel:"]');
      if (!a || e.defaultPrevented) return;
      e.preventDefault();
      openExternal(a.getAttribute('href'));
    });
  }

  /* ---------- Kop: achtergrond bij scrollen, verbergen bij naar beneden scrollen ---------- */
  const hd = document.querySelector('[data-header]');
  if (hd) {
    let lastY = window.scrollY;
    const onScroll = () => {
      const y = window.scrollY;
      hd.classList.toggle('is-scrolled', y > 10);
      const menuOpen = hd.classList.contains('is-open');
      // alleen bij duidelijk naar beneden verbergen, alleen bij naar boven weer tonen
      // (bij soepel scrollen zijn de laatste stapjes klein; die mogen niets veranderen)
      if (!menuOpen && y > 400 && y > lastY + 4) hd.classList.add('is-hidden');
      else if (menuOpen || y < 400 || y < lastY - 4) hd.classList.remove('is-hidden');
      lastY = y;
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });

    const btn = hd.querySelector('.hd__menu');
    const menu = hd.querySelector('#menu');
    const setMenu = (open) => {
      hd.classList.toggle('is-open', open);
      menu.hidden = !open;
      btn.setAttribute('aria-expanded', open);
      btn.querySelector('span').textContent = open ? 'Sluiten' : 'Menu';
      document.documentElement.style.overflow = open ? 'hidden' : '';
      if (open) hd.classList.add('is-scrolled');
    };
    btn.addEventListener('click', () => setMenu(menu.hidden));
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !menu.hidden) { setMenu(false); btn.focus(); } });
    window.matchMedia('(min-width: 961px)').addEventListener('change', (e) => { if (e.matches) setMenu(false); });
  }

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
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !panel.hidden) { setOpen(false); fab.focus(); } });
    document.addEventListener('click', (e) => { if (!panel.hidden && !dock.contains(e.target)) setOpen(false); });

    // bereikbaar ma t/m za 09:00-18:00 (Nederlandse tijd)
    const status = dock.querySelector('[data-dock-status]');
    try {
      const parts = Object.fromEntries(new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/Amsterdam', weekday: 'short', hour: 'numeric', hour12: false })
        .formatToParts(new Date()).map((p) => [p.type, p.value]));
      const hour = parseInt(parts.hour, 10) % 24;
      const open = parts.weekday !== 'Sun' && hour >= 9 && hour < 18;
      if (!open) {
        const nextMonday = parts.weekday === 'Sun' || (parts.weekday === 'Sat' && hour >= 18);
        const when = nextMonday ? 'maandag ' : (hour >= 18 ? 'morgen ' : '');
        status.classList.add('is-closed');
        status.querySelector('span').textContent = `We reageren ${when}vanaf 09:00`;
      }
    } catch (e) { /* standaardtekst laten staan */ }
  }

  /* ---------- Vragen: één tegelijk open ---------- */
  document.querySelectorAll('.qa__item').forEach((d) => {
    d.addEventListener('toggle', () => {
      if (!d.open) return;
      d.parentElement.querySelectorAll('.qa__item[open]').forEach((o) => { if (o !== d) o.open = false; });
    });
  });

  /* ---------- Gesprek plannen (contactpagina) ---------- */
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

    // volgende 12 werkdagen (ma t/m za), vanaf morgen
    if (datesEl) {
      const d = new Date();
      let added = 0;
      while (added < 12) {
        d.setDate(d.getDate() + 1);
        if (d.getDay() === 0) continue;
        const id = `date-${added}`;
        const wrap = document.createElement('div');
        wrap.className = 'choice';
        wrap.innerHTML =
          `<input type="radio" name="datum" id="${id}" value="${fullFmt.format(d)}">` +
          `<label for="${id}"><small>${dayFmt.format(d).replace('.', '')}</small>` +
          `<b>${d.getDate()}</b><small>${monthFmt.format(d).replace('.', '')}</small></label>`;
        datesEl.append(wrap);
        added++;
      }
    }

    const val = (name) => booking.querySelector(`[name="${name}"]:checked`)?.value;
    const updateSummary = () => {
      if (!summary) return;
      const datum = val('datum'); const tijd = val('tijd'); const vorm = val('vorm');
      summary.textContent = datum || tijd
        ? `${vorm || 'Gesprek'}${datum ? ` op ${datum}` : ''}${tijd ? ` om ${tijd}` : ''}`
        : 'Geen dag gekozen? Dan stellen wij een moment voor.';
    };
    booking.addEventListener('change', updateSummary);
    updateSummary();

    // dag en tijd zijn optioneel: nog een keer klikken op je keuze zet hem weer uit
    ['datum', 'tijd'].forEach((name) => {
      let last = val(name) || null;
      booking.addEventListener('change', (e) => { if (e.target.name === name) last = e.target.value; });
      booking.addEventListener('click', (e) => {
        const input = e.target.closest?.(`input[name="${name}"]`);
        if (!input) return;
        if (last === input.value) { input.checked = false; last = null; updateSummary(); } else last = input.value;
      });
    });

    const preference = () => {
      const datum = val('datum'); const tijd = val('tijd');
      if (datum && tijd) return `${datum} om ${tijd}`;
      if (datum) return `${datum}, tijd maakt niet uit`;
      if (tijd) return `${tijd}, dag maakt niet uit`;
      return 'geen, stel zelf een moment voor';
    };

    const buildMessage = () => {
      const f = new FormData(booking);
      const field = (name) => (f.get(name) || '').toString().trim();
      return [
        'Hoi Vizora Digital! Ik wil graag een gratis kennismakingsgesprek plannen.',
        '',
        `Gesprek: ${val('vorm') || 'maakt niet uit'}`,
        `Voorkeur: ${preference()}`,
        `Interesse in: ${f.getAll('dienst').join(', ') || 'nog niet zeker'}`,
        '',
        `Naam: ${field('naam')}`,
        field('bedrijf') ? `Bedrijf: ${field('bedrijf')}` : null,
        `Telefoon: ${field('telefoon')}`,
        field('website') ? `Huidige website/Instagram: ${field('website')}` : null,
        field('bericht') ? `\nToelichting: ${field('bericht')}` : null,
      ].filter((l) => l !== null).join('\n');
    };

    const validate = () => {
      const missing = [];
      if (!booking.naam.value.trim()) missing.push('je naam');
      if (!booking.telefoon.value.trim()) missing.push('je telefoonnummer');
      if (missing.length) {
        errorEl.textContent = `Vul nog in: ${missing.join(', ')}.`;
        errorEl.classList.add('is-shown');
        errorEl.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'center' });
        return false;
      }
      errorEl.classList.remove('is-shown');
      errorEl.textContent = '';
      return true;
    };

    booking.addEventListener('submit', (e) => {
      e.preventDefault();
      if (!validate()) return;
      window.open(`https://wa.me/${WHATSAPP}?text=${encodeURIComponent(buildMessage())}`, '_blank', 'noopener');
    });
    booking.querySelector('[data-email]')?.addEventListener('click', () => {
      if (!validate()) return;
      const subject = `Kennismakingsgesprek - ${booking.naam.value.trim()}`;
      openExternal(`mailto:${EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(buildMessage())}`);
    });

    // vooraf invullen vanuit een link, bv. contact.html?pakket=Groei
    const params = new URLSearchParams(location.search);
    const bedrijf = params.get('bedrijf');
    const pakket = params.get('pakket');
    if (bedrijf && booking.bedrijf) booking.bedrijf.value = bedrijf.slice(0, 60);
    if (pakket && booking.bericht) {
      const abo = pakket.startsWith('Abonnement');
      const box = booking.querySelector(`[name="dienst"][value="${abo ? 'Website-abonnement' : 'Website'}"]`);
      if (box) box.checked = true;
      booking.bericht.value = abo
        ? `Ik heb interesse in het website-abonnement${pakket.length > 11 ? ` (${pakket.slice(11, 20)})` : ''}.`
        : `Ik heb interesse in het pakket ${pakket.slice(0, 20)}.`;
    }
  }

  /* ---------- Jaar in de voet ---------- */
  document.querySelectorAll('[data-year]').forEach((el) => { el.textContent = new Date().getFullYear(); });
})();
