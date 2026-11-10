// Maakt extra Etsy/Payhip-productfoto's (2000x1600) uit <productmap>/listing-images.json.
// Gebruik: node tools/make-listing-images.js products/<map>
// Slide-types:
//   feature: kicker, title, bullets[], image (pad binnen productmap), side ("left"|"right")
//   list:    kicker, title, items[] (twee kolommen met vinkjes)
//   steps:   kicker, title, steps[{t, d}]
//   compare: kicker, title, before{label,text}, after{label,text}
const fs = require('fs'); const path = require('path');
const { chromium } = require('playwright');
const dir = path.resolve(process.argv[2]);
const cfg = JSON.parse(fs.readFileSync(path.join(dir, 'listing-images.json'), 'utf8'));
const img = p => 'data:image/png;base64,' + fs.readFileSync(path.join(dir, p)).toString('base64');
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');

const css = `
body{margin:0} *{box-sizing:border-box}
.s{width:2000px;height:1600px;position:relative;overflow:hidden;font-family:Inter,sans-serif;padding:120px 130px;display:flex;flex-direction:column}
.dark{background:#14213d;color:#fff} .light{background:#f6f1ea;color:#14213d}
.kicker{font-size:38px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#e8673c}
h1{font-family:"Inter Display",Inter,sans-serif;font-size:100px;line-height:1.05;font-weight:800;letter-spacing:-.02em;margin:26px 0 0}
.bar{width:140px;height:12px;border-radius:6px;background:#e8673c;margin:50px 0}
.row{display:flex;gap:90px;flex:1;align-items:center}
.row.rev{flex-direction:row-reverse}
.txt{flex:1}
.pic{flex:0 0 720px;display:flex;justify-content:center}
.pic img{width:640px;border-radius:10px;box-shadow:0 50px 100px rgba(0,0,0,.35);transform:rotate(-3deg)}
ul.b{list-style:none;padding:0;margin:0;font-size:52px;line-height:1.45}
ul.b li{padding-left:70px;position:relative;margin-bottom:26px}
ul.b li:before{content:"✓";position:absolute;left:0;color:#e8673c;font-weight:800}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:36px 80px;font-size:50px;line-height:1.35;margin-top:30px}
.grid div{padding-left:70px;position:relative} .grid div:before{content:"✓";position:absolute;left:0;color:#e8673c;font-weight:800}
.steps{display:flex;gap:50px;margin-top:40px}
.step{flex:1;border-radius:28px;padding:56px 50px}
.dark .step{background:rgba(255,255,255,.07)} .light .step{background:#fff;box-shadow:0 20px 50px rgba(20,33,61,.08)}
.step .n{width:110px;height:110px;border-radius:55px;background:#e8673c;color:#fff;font-size:60px;font-weight:800;display:flex;align-items:center;justify-content:center}
.step .t{font-size:56px;font-weight:800;margin:40px 0 18px} .step .d{font-size:42px;line-height:1.4;opacity:.85}
.cmp{display:flex;gap:50px;margin-top:40px;flex:1}
.box{flex:1;border-radius:28px;padding:60px 64px;font-family:"Bitstream Charter",serif;font-size:62px;line-height:1.45;font-style:italic}
.box .l{font-family:Inter,sans-serif;font-style:normal;font-size:36px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;margin-bottom:26px}
.bad{background:#fbe9e7;color:#5b2620} .bad .l{color:#c0392b}
.good{background:#e3f4f1;color:#173f39} .good .l{color:#1f7a6f}
.brand{position:absolute;right:130px;bottom:70px;font-size:34px;font-weight:700;letter-spacing:.08em;opacity:.6}
`;

function slide(s) {
  const head = `<div class="kicker">${esc(s.kicker)}</div><h1>${esc(s.title)}</h1>`;
  let body = '';
  if (s.type === 'feature') {
    body = `<div class="row ${s.side === 'left' ? 'rev' : ''}"><div class="txt">${head}<div class="bar"></div>
      <ul class="b">${s.bullets.map(b => `<li>${esc(b)}</li>`).join('')}</ul></div>
      <div class="pic"><img src="${img(s.image)}"></div></div>`;
    return body;
  }
  if (s.type === 'list') body = `<div class="grid">${s.items.map(i => `<div>${esc(i)}</div>`).join('')}</div>`;
  if (s.type === 'steps') body = `<div class="steps">${s.steps.map((x, i) => `<div class="step"><div class="n">${i + 1}</div><div class="t">${esc(x.t)}</div><div class="d">${esc(x.d)}</div></div>`).join('')}</div>`;
  if (s.type === 'compare') body = `<div class="cmp"><div class="box bad"><div class="l">${esc(s.before.label)}</div>${esc(s.before.text)}</div><div class="box good"><div class="l">${esc(s.after.label)}</div>${esc(s.after.text)}</div></div>`;
  return head + `<div class="bar"></div>` + body;
}

(async () => {
  const out = path.join(dir, 'listing-images'); fs.mkdirSync(out, { recursive: true });
  for (const f of fs.readdirSync(out)) fs.unlinkSync(path.join(out, f));
  fs.copyFileSync(path.join(dir, 'preview-images', '00-mockup-a.png'), path.join(out, '01-cover-mockup.png'));
  fs.copyFileSync(path.join(dir, 'preview-images', '00-mockup-b.png'), path.join(out, '02-whats-inside.png'));
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 2000, height: 1600 } });
  for (const [i, s] of cfg.slides.entries()) {
    const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><style>${css}</style></head><body>
      <div class="s ${s.theme || (i % 2 ? 'light' : 'dark')}">${slide(s)}<div class="brand">${esc(cfg.brand)}</div></div></body></html>`;
    await p.setContent(html, { waitUntil: 'load' });
    await p.screenshot({ path: path.join(out, `${String(i + 3).padStart(2, '0')}-${s.name}.png`) });
  }
  await b.close();
  console.log(`Made ${cfg.slides.length + 2} listing images in ${out}`);
})();
