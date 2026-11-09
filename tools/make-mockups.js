// Maakt productfoto's (mockups) voor Etsy/Payhip: node tools/make-mockups.js products/<map>
const path = require('path'); const fs = require('fs');
const { chromium } = require('playwright');
const dir = path.resolve(process.argv[2]);
const pv = f => 'file://' + path.join(dir, 'preview-images', f);
const files = fs.readdirSync(path.join(dir, 'preview-images')).filter(f => f.endsWith('.png')).sort();
let html = fs.readFileSync(path.join(__dirname, 'mockups.html'), 'utf8')
  .replace(/COVER/g, pv(files[0])).replace('P2', pv(files[2])).replace('P3', pv(files[3]))
  .replace('P4', pv(files[4])).replace('P5', pv(files[5]));
const tmp = path.join(__dirname, '.mockups-tmp.html'); fs.writeFileSync(tmp, html);
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2000, height: 1600 } });
  await p.goto('file://' + tmp, { waitUntil: 'networkidle' });
  for (const id of ['a', 'b']) await (await p.$('#' + id)).screenshot({ path: path.join(dir, 'preview-images', `00-mockup-${id}.png`) });
  await b.close(); fs.unlinkSync(tmp); console.log('mockups written');
})();
