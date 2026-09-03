const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 430, height: 900 }, colorScheme: 'light' });
  await p.goto('file://' + process.cwd() + '/preview.html', { waitUntil: 'networkidle' });
  await p.waitForTimeout(1000);
  const out = await p.evaluate(() => {
    const de = document.documentElement;
    const base = de.scrollWidth;
    const res = [];
    // hide each top-level block in turn and see which one owns the overflow
    document.querySelectorAll('.wrap > *').forEach((el, i) => {
      const prev = el.style.display;
      el.style.display = 'none';
      res.push({ i, cls: (el.className||'').toString().slice(0,20) || el.tagName, sw: de.scrollWidth });
      el.style.display = prev;
    });
    return { base, clientW: de.clientWidth, res };
  });
  console.log(JSON.stringify(out, null, 1));
  await b.close();
})();
