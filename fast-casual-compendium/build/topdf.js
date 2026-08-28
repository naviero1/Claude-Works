const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ colorScheme: 'light' });
  await p.goto('file://' + process.cwd() + '/preview.html', { waitUntil: 'networkidle' });
  await p.emulateMedia({ media: 'print', colorScheme: 'light' });
  await p.waitForTimeout(2500);
  const foot = `<div style="width:100%;font-family:Archivo,Helvetica,Arial,sans-serif;font-size:6.6pt;
      letter-spacing:.09em;text-transform:uppercase;color:#6E7568;padding:0 13mm;
      display:flex;justify-content:space-between;">
      <span>The Fast-Casual Compendium &middot; Second edition</span>
      <span>Research Triangle, North Carolina</span>
      <span class="pageNumber"></span></div>`;
  await p.pdf({
    path: 'The-Fast-Casual-Compendium.pdf',
    format: 'Letter',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: foot,
    margin: { top: '14mm', bottom: '16mm', left: '13mm', right: '13mm' },
  });
  await b.close();
  console.log('ok');
})();
