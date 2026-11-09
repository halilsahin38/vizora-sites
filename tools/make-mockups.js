// Maakt productfoto's (mockups) voor Etsy/Payhip: node tools/make-mockups.js products/<map>
const path = require('path'); const fs = require('fs');
const { chromium } = require('playwright');
const dir = path.resolve(process.argv[2]);
const pv = f => 'file://' + path.join(dir, 'preview-images', f);
const files = fs.readdirSync(path.join(dir, 'preview-images')).filter(f => f.endsWith('.png') && !f.startsWith('00-mockup')).sort();
let html = fs.readFileSync(path.join(__dirname, 'mockups.html'), 'utf8')
  .replace(/COVER/g, pv(files[0]));
const mc = fs.existsSync(path.join(dir, 'mockup.json')) ? JSON.parse(fs.readFileSync(path.join(dir, 'mockup.json'), 'utf8')) : { badge: '53-page e-book<br>+ worksheets', list: '<b>30-day plan</b> · 30-second layoff answer<br>Résumé-gap scripts · 14 tough questions<br>Printable worksheets &amp; email templates' };
const pi = mc.pages || [2, 3, 4, 5];
html = html.replace('P2', pv(files[pi[0]])).replace('P3', pv(files[pi[1]])).replace('P4', pv(files[pi[2]])).replace('P5', pv(files[pi[3]]));
html = html.replace('BADGE', mc.badge).replace('LIST', mc.list);
const tmp = path.join(__dirname, '.mockups-tmp.html'); fs.writeFileSync(tmp, html);
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2000, height: 1600 } });
  await p.goto('file://' + tmp, { waitUntil: 'networkidle' });
  for (const id of ['a', 'b']) await (await p.$('#' + id)).screenshot({ path: path.join(dir, 'preview-images', `00-mockup-${id}.png`) });
  await b.close(); fs.unlinkSync(tmp); console.log('mockups written');
})();
