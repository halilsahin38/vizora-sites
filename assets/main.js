// Navigatie: achtergrond bij scrollen + mobiel menu
const nav = document.querySelector('.nav');
const toggle = document.querySelector('.nav__toggle');

const onScroll = () => nav.classList.toggle('is-scrolled', window.scrollY > 20);
onScroll();
window.addEventListener('scroll', onScroll, { passive: true });

toggle.addEventListener('click', () => {
  const open = nav.classList.toggle('is-open');
  toggle.setAttribute('aria-expanded', open);
});
document.querySelectorAll('.nav__links a').forEach((link) =>
  link.addEventListener('click', () => {
    nav.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
  })
);

// Elementen laten infaden bij scrollen
const io = new IntersectionObserver(
  (entries) => entries.forEach((e) => {
    if (e.isIntersecting) {
      e.target.classList.add('is-visible');
      io.unobserve(e.target);
    }
  }),
  { threshold: 0.12 }
);
document.querySelectorAll('.reveal').forEach((el, i) => {
  el.style.transitionDelay = `${(i % 4) * 80}ms`;
  io.observe(el);
});

// Contactformulier: opent mailprogramma met ingevuld bericht
document.getElementById('contact-form').addEventListener('submit', (e) => {
  e.preventDefault();
  const d = new FormData(e.target);
  const subject = `Aanvraag ${d.get('dienst')} - ${d.get('naam')}`;
  const body =
    `Naam: ${d.get('naam')}\nBedrijf: ${d.get('bedrijf') || '-'}\nE-mail: ${d.get('email')}\n` +
    `Dienst: ${d.get('dienst')}\n\n${d.get('bericht')}`;
  window.location.href =
    `mailto:halilsahinai@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
});

document.getElementById('year').textContent = new Date().getFullYear();
