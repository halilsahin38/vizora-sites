// Maakt een hoofdfoto (2000x1600): grote belofte links, sfeerfoto rechts.
// Gebruik: node tools/make-hero.js products/<map>   (leest hero.json in die map)
const fs = require('fs'); const path = require('path');
const { chromium } = require('playwright');
const dir = path.resolve(process.argv[2]);
const cfg = JSON.parse(fs.readFileSync(path.join(dir, 'hero.json'), 'utf8'));
const img = 'data:image/png;base64,' + fs.readFileSync(path.join(dir, cfg.photo)).toString('base64');
const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><style>
body{margin:0}*{box-sizing:border-box}
.s{width:2000px;height:1600px;display:flex;font-family:Inter,sans-serif;overflow:hidden;
   background:radial-gradient(circle at 10% 90%,#ffd2bf 0,rgba(255,210,191,0) 45%),linear-gradient(150deg,#fff7f1 0%,#ffe3d3 100%);color:#14213d}
.l{flex:0 0 820px;padding:130px 70px 110px 120px;display:flex;flex-direction:column}
.k{align-self:flex-start;font-size:30px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#ff6b47;background:rgba(255,107,71,.12);padding:14px 26px;border-radius:40px}
h1{font-family:"Inter Display",Inter,sans-serif;font-size:94px;line-height:1.04;font-weight:800;letter-spacing:-.025em;margin:44px 0 0}
h1 em{font-style:normal;color:#ff6b47}
.bar{width:140px;height:12px;border-radius:6px;background:linear-gradient(90deg,#ff6b47,#ffb347);margin:52px 0 44px}
.sub{font-size:42px;line-height:1.4;color:#3d4658}
.chips{margin-top:auto;display:flex;flex-wrap:wrap;gap:18px}
.chips span{font-size:32px;font-weight:700;background:#14213d;color:#fff;padding:18px 30px;border-radius:44px}
.r{flex:1;position:relative}
.r img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;border-top-left-radius:80px;border-bottom-left-radius:80px;box-shadow:-30px 0 80px rgba(20,33,61,.12)}
</style></head><body><div class="s"><div class="l">
<div class="k">${cfg.kicker}</div><h1>${cfg.title}</h1><div class="bar"></div><div class="sub">${cfg.sub}</div>
<div class="chips">${cfg.chips.map(c => `<span>${c}</span>`).join('')}</div></div>
<div class="r"><img src="${img}"></div></div></body></html>`;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2000, height: 1600 } });
  await p.setContent(html, { waitUntil: 'load' });
  await p.screenshot({ path: path.join(dir, 'listing-images', '01-cover-mockup.png') });
  await b.close(); console.log('hero written');
})();
