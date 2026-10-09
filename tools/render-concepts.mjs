// Maakt screenshots van de conceptwebsites in /concepts voor gebruik op de site.
// Gebruik: npm i playwright && node tools/render-concepts.mjs
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const out = path.join(root, 'assets', 'concepts');
const statusbar = fs.readFileSync(path.join(root, 'concepts', '_statusbar.html'), 'utf8');
const names = process.argv.slice(2).length ? process.argv.slice(2) : ['merk', 'noir', 'olivo', 'serene', 'goudkorst'];
fs.mkdirSync(out, { recursive: true });

const browser = await chromium.launch(process.env.CHROMIUM ? { executablePath: process.env.CHROMIUM } : {});
for (const name of names) {
  const url = 'file://' + path.join(root, 'concepts', `${name}.html`);
  const shot = async (viewport, scale, file, clip, fullPage = false) => {
    const page = await browser.newPage({ viewport, deviceScaleFactor: scale });
    await page.goto(url);
    await page.evaluate((html) => document.body.insertAdjacentHTML('afterbegin', html), statusbar);
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(400);
    await page.screenshot({ path: path.join(out, file), type: 'jpeg', quality: 84, clip, fullPage });
    await page.close();
  };
  await shot({ width: 1600, height: 800 }, 1.25, `${name}-desktop.jpg`);
  await shot({ width: 390, height: 844 }, 2, `${name}-mobile.jpg`);
  await shot({ width: 390, height: 844 }, 2.4, `${name}-mobile-45.jpg`, { x: 0, y: 0, width: 390, height: 488 });
  // kleine versies voor de schuivende strook
  await shot({ width: 1600, height: 800 }, 0.5, `${name}-thumb.jpg`);
  await shot({ width: 1600, height: 800 }, 0.5, `${name}-thumb-2.jpg`, { x: 0, y: 800, width: 1600, height: 800 }, true);
  await shot({ width: 390, height: 844 }, 0.8, `${name}-mobile-thumb.jpg`);
  console.log('✓', name);
}
// verouderde versie voor de voor/na-schuif
{
  const url = 'file://' + path.join(root, 'concepts', 'oud.html');
  for (const [vp, scale, file, clip] of [
    [{ width: 1600, height: 800 }, 1.25, 'oud-desktop.jpg'],
    [{ width: 390, height: 844 }, 2.4, 'oud-mobile-45.jpg', { x: 0, y: 0, width: 390, height: 488 }],
  ]) {
    const page = await browser.newPage({ viewport: vp, deviceScaleFactor: scale });
    await page.goto(url);
    await page.waitForTimeout(300);
    await page.screenshot({ path: path.join(out, file), type: 'jpeg', quality: 84, clip });
    await page.close();
  }
  console.log('✓ oud');
}
await browser.close();
