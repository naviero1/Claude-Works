const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 430, height: 900 }, colorScheme: 'light' });
  await p.goto('file://' + process.cwd() + '/preview.html', { waitUntil: 'networkidle' });
  await p.waitForTimeout(1200);
  const out = await p.evaluate(() => {
    const de = document.documentElement, res = [];
    document.querySelectorAll('*').forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.width > de.clientWidth + 1 || r.right > de.clientWidth + 1 || r.left < -1)
        res.push({ tag: el.tagName, cls: (el.className || '').toString().slice(0, 34),
                   w: Math.round(r.width), l: Math.round(r.left), r: Math.round(r.right) });
    });
    return { scrollW: de.scrollWidth, clientW: de.clientWidth, offenders: res.slice(0, 12) };
  });
  console.log(JSON.stringify(out, null, 1));
  await b.close();
})();
