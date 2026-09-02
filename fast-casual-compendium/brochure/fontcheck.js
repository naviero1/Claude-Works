const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage();
  await p.goto('file://' + process.cwd() + '/What-Delivery-Costs-You.html', { waitUntil: 'networkidle' });
  await p.waitForTimeout(1500);
  const r = await p.evaluate(async () => {
    await document.fonts.ready;
    const loaded = [...document.fonts].map(f => ({ f: f.family, w: f.weight, status: f.status }));
    const probe = (sel) => { const el = document.querySelector(sel);
      return el ? getComputedStyle(el).fontFamily.split(',')[0] : null; };
    // measure whether the display face is actually applied vs falling back
    const meas = (fam) => { const c = document.createElement('canvas').getContext('2d');
      c.font = '48px ' + fam + ', monospace'; const a = c.measureText('Handgloves').width;
      c.font = '48px monospace'; const b = c.measureText('Handgloves').width;
      return { fam, w: Math.round(a), fallbackW: Math.round(b), differs: Math.abs(a-b) > 1 }; };
    return { loaded, h1: probe('h1'),
             checks: ['Bricolage Grotesque','Newsreader','DM Mono'].map(meas) };
  });
  console.log(JSON.stringify(r, null, 1));
  await b.close();
})();
