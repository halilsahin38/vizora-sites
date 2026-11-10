// Pin-generator: maakt Pinterest-afbeeldingen (1000x1500) en een bulk-upload CSV.
// Gebruik: node tools/make-pins.js products/<product-map>
// Leest <product-map>/pins.json en schrijft naar <product-map>/pins/.
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const dir = path.resolve(process.argv[2] || '.');
const cfg = JSON.parse(fs.readFileSync(path.join(dir, 'pins.json'), 'utf8'));
const outDir = path.join(dir, 'pins');
fs.mkdirSync(outDir, { recursive: true });
const coverData = 'data:image/png;base64,' + fs.readFileSync(path.join(dir, cfg.cover)).toString('base64');

const themes = {
  dark:   { bg: '#14213d', fg: '#ffffff', sub: '#d5dcea', kicker: '#f0875f', accent: '#e8673c' },
  light:  { bg: '#f6f1ea', fg: '#14213d', sub: '#3d4658', kicker: '#d9542b', accent: '#d9542b' },
  accent: { bg: '#d9542b', fg: '#ffffff', sub: '#fde7dd', kicker: '#14213d', accent: '#14213d' },
};
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/\n/g, '<br>');

const html = (p, t) => `<!DOCTYPE html><html><head><meta charset="utf-8"><style>
  body{margin:0}
  .pin{width:1000px;height:1500px;box-sizing:border-box;background:${t.bg};color:${t.fg};padding:90px 80px 70px;
       font-family:Inter,sans-serif;display:flex;flex-direction:column;position:relative;overflow:hidden}
  .kicker{font-size:34px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:${t.kicker}}
  h1{font-family:"Inter Display",Inter,sans-serif;font-size:92px;line-height:1.04;font-weight:800;letter-spacing:-.02em;margin:34px 0 0}
  .bar{width:120px;height:10px;background:${t.accent};margin:44px 0 36px;border-radius:5px}
  .sub{font-family:"Bitstream Charter",serif;font-size:44px;line-height:1.4;color:${t.sub};max-width:840px}
  .cover{position:absolute;right:-40px;bottom:120px;width:400px;transform:rotate(-6deg);box-shadow:0 30px 60px rgba(0,0,0,.35);border-radius:6px}
  .foot{margin-top:auto;font-size:30px;font-weight:700;letter-spacing:.06em;color:${t.sub}}
</style></head><body><div class="pin">
  <div class="kicker">${esc(p.kicker)}</div>
  <h1>${esc(p.title)}</h1>
  <div class="bar"></div>
  <div class="sub">${esc(p.sub)}</div>
  <img class="cover" src="${coverData}">
  <div class="foot">${esc(cfg.brand)}</div>
</div></body></html>`;

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1000, height: 1500 } });
  const rows = [['Title', 'Media URL', 'Pinterest board', 'Thumbnail', 'Description', 'Link', 'Publish date', 'Keywords']];
  const start = new Date(); start.setUTCDate(start.getUTCDate() + 1);
  for (const [i, p] of cfg.pins.entries()) {
    const file = `pin-${String(i + 1).padStart(2, '0')}.png`;
    await page.setContent(html(p, themes[p.style] || themes.dark), { waitUntil: 'load' });
    await page.screenshot({ path: path.join(outDir, file) });
    const d = new Date(start); d.setUTCDate(start.getUTCDate() + i);
    d.setUTCHours(18, 0, 0, 0); // één pin per dag, 18:00 UTC
    rows.push([p.pin_title, `MEDIA_BASE_URL/${file}`, cfg.board, '', p.description, cfg.link, d.toISOString().slice(0, 19), '']);
  }
  await browser.close();
  const csv = rows.map(r => r.map(v => `"${String(v).replace(/"/g, '""')}"`).join(',')).join('\n');
  fs.writeFileSync(path.join(outDir, 'pinterest-bulk.csv'), csv + '\n');
  console.log(`Made ${cfg.pins.length} pins + pinterest-bulk.csv in ${outDir}`);
})();
