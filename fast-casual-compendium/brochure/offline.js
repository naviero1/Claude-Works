const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1280, height: 1000 } });
  // hard-fail any network request: the file must be entirely self-contained
  const external = [];
  await p.route('**', route => {
    const u = route.request().url();
    if (u.startsWith('file://') || u.startsWith('data:')) return route.continue();
    external.push(u); return route.abort();
  });
  await p.goto('file://' + process.cwd() + '/What-Delivery-Costs-You.html', { waitUntil: 'load' });
  await p.waitForTimeout(1800);
  const r = await p.evaluate(async () => {
    await document.fonts.ready;
    const meas = fam => { const c = document.createElement('canvas').getContext('2d');
      c.font = '48px ' + fam + ', monospace'; const a = c.measureText('Handgloves').width;
      c.font = '48px monospace'; return Math.abs(a - c.measureText('Handgloves').width) > 1; };
    return { applied: { bricolage: meas('Bricolage Grotesque'), newsreader: meas('Newsreader'),
                        dmmono: meas('DM Mono') },
             scrollW: document.documentElement.scrollWidth,
             clientW: document.documentElement.clientWidth };
  });
  console.log('blocked external requests:', external.length ? external : 'none — fully self-contained');
  console.log('fonts applied offline:', JSON.stringify(r.applied));
  console.log('no sideways scroll:', r.scrollW === r.clientW);
  await p.screenshot({ path: 'offline-proof.png' });
  await b.close();
})();
