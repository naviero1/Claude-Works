const {chromium} = require('playwright');
(async () => {
  const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
  const p = await b.newPage();
  const blocked = [];
  await p.route('**/*', r => {
    const u = r.request().url();
    if (!/^(file|data):/.test(u)) { blocked.push(u); return r.abort(); }
    r.continue();
  });
  await p.goto('file://' + __dirname + '/What-Delivery-Costs-You-87.html', {waitUntil:'networkidle'});
  await p.emulateMedia({media:'print'});
  await p.evaluate(() => document.fonts.ready);
  const fonts = await p.evaluate(() => {
    const el = document.querySelector('h1');
    return {h1: getComputedStyle(el).fontFamily,
            loaded: [...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family)};
  });
  console.log('fonts', JSON.stringify(fonts.h1), 'loaded:', [...new Set(fonts.loaded)].join(', '));
  if (blocked.length) console.log('BLOCKED EXTERNAL:', blocked.slice(0,5));
  await p.pdf({path:'What-Delivery-Costs-You-87.pdf', format:'Letter',
    printBackground:true, displayHeaderFooter:true,
    headerTemplate:'<div></div>',
    footerTemplate:`<div style="width:100%;font:8px 'Helvetica';color:#8A8F86;padding:0 14mm;display:flex;justify-content:space-between">
      <span>What Delivery Costs You &#183; 87 dishes, Research Triangle</span>
      <span class="pageNumber"></span></div>`,
    margin:{top:'15mm',bottom:'16mm',left:'14mm',right:'14mm'}});
  await b.close();
})();
