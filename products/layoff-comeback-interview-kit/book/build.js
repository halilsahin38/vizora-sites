// Builds the e-book PDF: node book/build.js (from the product folder or anywhere)
// Requires pandoc, poppler-utils (pdfunite) and Playwright with Chromium.
const { execFileSync } = require('child_process');
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

const dir = __dirname;
const out = path.join(dir, '..', 'Why-Did-You-Leave.pdf');
const md = ['01-front.md', '02-chapters-1-3.md', '03-chapters-4-6.md', '04-chapters-7-11.md', '05-toolkit.md']
  .map(f => path.join(dir, f));

const bodyHtml = path.join(dir, 'body.html');
execFileSync('pandoc', [...md, '-f', 'markdown+fenced_divs+header_attributes+pipe_tables', '-t', 'html5', '-s',
  '--metadata', 'pagetitle=Why Did You Leave?', '-c', 'book.css', '-o', bodyHtml]);

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  await page.goto('file://' + path.join(dir, 'cover.html'), { waitUntil: 'networkidle' });
  const coverPdf = path.join(dir, 'cover.pdf');
  await page.pdf({ path: coverPdf, width: '6in', height: '9in', printBackground: true });

  await page.goto('file://' + bodyHtml, { waitUntil: 'networkidle' });
  const bodyPdf = path.join(dir, 'body.pdf');
  await page.pdf({
    path: bodyPdf, width: '6in', height: '9in', printBackground: true,
    margin: { top: '0.7in', bottom: '0.75in', left: '0.68in', right: '0.68in' },
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;font-family:Inter,sans-serif;font-size:7px;color:#8a92a3;text-align:center;">&ldquo;Why Did You Leave?&rdquo; &nbsp;·&nbsp; <span class="pageNumber"></span></div>',
  });
  await browser.close();

  execFileSync('pdfunite', [coverPdf, bodyPdf, out]);
  for (const f of [coverPdf, bodyPdf, bodyHtml]) fs.unlinkSync(f);
  console.log('Wrote', out);
})();
