const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ colorScheme: 'light' });
  await p.goto('file://' + process.cwd() + '/What-Delivery-Costs-You.html', { waitUntil: 'networkidle' });
  await p.emulateMedia({ media: 'print', colorScheme: 'light' });
  await p.waitForTimeout(2500);
  const foot = `<div style="width:100%;font-family:Helvetica,Arial,sans-serif;font-size:6.4pt;
      letter-spacing:.12em;text-transform:uppercase;color:#7A7E88;padding:0 14mm;
      display:flex;justify-content:space-between;">
      <span>What Delivery Costs You</span>
      <span>Research Triangle, North Carolina</span>
      <span class="pageNumber"></span></div>`;
  await p.pdf({ path: 'What-Delivery-Costs-You.pdf', format: 'Letter', printBackground: true,
    displayHeaderFooter: true, headerTemplate: '<div></div>', footerTemplate: foot,
    margin: { top: '14mm', bottom: '16mm', left: '14mm', right: '14mm' } });
  await b.close(); console.log('ok');
})();
