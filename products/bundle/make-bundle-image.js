// Bundelfoto (2000x1600): node products/bundle/make-bundle-image.js
const fs = require('fs'); const path = require('path'); const { chromium } = require('playwright');
const root = path.resolve(__dirname, '..');
const d = p => 'data:image/png;base64,' + fs.readFileSync(path.join(root, p)).toString('base64');
const c1 = d('layoff-comeback-interview-kit/preview-images/01-page-1.png');
const c2 = d('gap-proof-resume-kit/preview-images/01-cover.png');
const c3 = d('layoff-answer-cheat-sheet/preview-images/01-page-1.png');
const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><style>
body{margin:0}*{box-sizing:border-box}
.s{width:2000px;height:1600px;position:relative;overflow:hidden;font-family:Inter,sans-serif;color:#14213d;
 background:radial-gradient(circle at 85% 12%,#ffd2bf 0,rgba(255,210,191,0) 40%),radial-gradient(circle at 10% 95%,#bfe8db 0,rgba(191,232,219,0) 40%),linear-gradient(150deg,#fff7f1 0%,#ffe3d3 100%)}
.k{position:absolute;left:120px;top:110px;font-size:32px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#ff6b47;background:rgba(255,107,71,.12);padding:14px 26px;border-radius:40px}
h1{position:absolute;left:120px;top:190px;margin:0;font-family:"Inter Display",Inter,sans-serif;font-size:104px;line-height:1.02;font-weight:800;letter-spacing:-.025em}
h1 em{font-style:normal;color:#ff6b47}
.c{position:absolute;border-radius:12px;box-shadow:0 50px 100px rgba(16,26,51,.30),0 0 0 12px rgba(255,255,255,.6)}
.save{position:absolute;right:120px;top:120px;width:300px;height:300px;border-radius:50%;background:linear-gradient(135deg,#14213d,#24407a);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(8deg);box-shadow:0 30px 60px rgba(16,26,51,.3)}
.save b{font-size:84px;line-height:1} .save span{font-size:30px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#ffb38f;margin-top:8px}
.list{position:absolute;left:0;right:0;bottom:70px;text-align:center;font-size:36px;font-weight:700;color:#3d4658}
.list i{font-style:normal;color:#ff6b47;margin:0 18px}
</style></head><body><div class="s">
<div class="k">3-in-1 bundle · instant download</div>
<h1>Laid off <em>→</em> Hired</h1>
<div class="save"><b>-17%</b><span>vs. separately</span></div>
<img class="c" src="${c3}" style="width:420px;left:200px;top:560px;transform:rotate(-8deg)">
<img class="c" src="${c2}" style="width:440px;left:1360px;top:560px;transform:rotate(7deg)">
<img class="c" src="${c1}" style="width:520px;left:740px;top:440px;transform:rotate(-1deg);z-index:2">
<div class="list">30-day interview e-book<i>+</i>Résumé &amp; cover letter kit<i>+</i>30-second answer cheat sheet</div>
</div></body></html>`;
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2000, height: 1600 } });
  await p.setContent(html, { waitUntil: 'load' });
  await p.screenshot({ path: path.join(__dirname, 'listing-images', '01-bundle.png') }); await b.close(); console.log('bundle image written'); })();
