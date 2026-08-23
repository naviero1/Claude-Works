const { chromium } = require('playwright-core');
const path = require('path');
const fs = require('fs');

const DIR = __dirname;
const DASH = 'file://' + path.join(DIR, 'dashboard.html');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
    args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 1360, height: 950 } });
  page.on('pageerror', e => console.log('PAGEERROR:', e.message));
  page.on('console', m => { if (m.type() === 'error') console.log('CONSOLE:', m.text()); });

  const results = [];
  const check = (label, cond, extra='') => { results.push(`${cond ? 'PASS' : 'FAIL'}  ${label}${extra ? ' — ' + extra : ''}`); };

  async function loadAndVerify(xlsxPath, tag) {
    await page.goto(DASH);
    check(`${tag}: page loads, dropzone visible`, await page.locator('#dropzone').isVisible());
    // use the hidden input path (deterministic in headless)
    await page.evaluate(() => { window.showOpenFilePicker = undefined; });
    const [chooser] = await Promise.all([
      page.waitForEvent('filechooser'),
      page.click('#loadBtn'),
    ]);
    await chooser.setFiles(xlsxPath);
    await page.waitForSelector('#app', { state: 'visible', timeout: 15000 });

    const kpis = await page.$$eval('#kpis .kpi', els => els.map(e => ({
      n: e.querySelector('.n').textContent.trim(), l: e.querySelector('.l').textContent.trim() })));
    const kmap = Object.fromEntries(kpis.map(k => [k.l, k.n]));
    check(`${tag}: coverage 60%`, kmap['Coverage'] === '60%', JSON.stringify(kmap));
    check(`${tag}: 6 open defects`, kmap['Open defects'] === '6');
    check(`${tag}: 2 theater`, kmap['Theater claims'] === '2');
    check(`${tag}: 1 unclaimed`, kmap['Unclaimed'] === '1');
    check(`${tag}: 3 decision defects`, kmap['Decision defects'] === '3');
    check(`${tag}: 1 disputed`, kmap['Disputed'] === '1');

    const topDefect = await page.$eval('#defectsTable tr:nth-child(2)', r => r.textContent.replace(/\s+/g, ' ').trim());
    check(`${tag}: top defect is Gandalf→Frodo missing 15`,
      /design_change_notice/.test(topDefect) && /Gandalf/.test(topDefect) && /missing/.test(topDefect) && /15/.test(topDefect), topDefect);

    const goalRows = await page.$$eval('#goalsTable tr', rs => rs.length - 1);
    check(`${tag}: 4 goal rows`, goalRows === 4);

    const meetings = await page.$$eval('#meetingsTable tr', rs => rs.length - 1);
    check(`${tag}: 9 meetings`, meetings === 9, String(meetings));
    const r9row = await page.$$eval('#meetingsTable tr', rs => {
      const row = rs.find(r => /Monthly Ops Status/.test(r.textContent));
      return row ? row.textContent.replace(/\s+/g, ' ') : 'NOT FOUND';
    });
    check(`${tag}: R9 shows theater twice`, (r9row.match(/theater/g) || []).length === 2, r9row.slice(0, 160));

    // goal filter: G3 → zero defects message
    await page.selectOption('#goalFilter', 'G3');
    const g3def = await page.$eval('#defectsTable', t => t.textContent);
    check(`${tag}: G3 filter shows no-defects note`, /No open defects/.test(g3def));
    await page.selectOption('#goalFilter', '');

    // disputed table has one row
    const disp = await page.$$eval('#disputedTable tr', rs => rs.length - 1);
    check(`${tag}: 1 disputed row`, disp === 1, String(disp));
  }

  const ORIGINAL = '/root/.claude/uploads/472c04c7-d930-56cd-b199-fdb48d7ee984/5d4c5d00-comms_assessment_workbook_1.xlsx';
  const LO_REWRITTEN = path.join(DIR, 'full.xlsx'); // LibreOffice-recalculated rewrite (proxy for "saved by a spreadsheet app")

  await loadAndVerify(ORIGINAL, 'original');
  await page.screenshot({ path: path.join(DIR, 'dashboard_screenshot.png'), fullPage: true });

  await loadAndVerify(LO_REWRITTEN, 'lo-rewrite');

  // ---- snapshot export round-trip ----
  const [download] = await Promise.all([
    page.waitForEvent('download'),
    page.click('#exportBtn'),
  ]);
  const snapPath = path.join(DIR, 'snapshot_test.html');
  await download.saveAs(snapPath);
  check('snapshot: downloaded', fs.existsSync(snapPath), `${fs.statSync(snapPath).size} bytes`);

  const page2 = await browser.newPage({ viewport: { width: 1360, height: 950 } });
  page2.on('pageerror', e => console.log('SNAP PAGEERROR:', e.message));
  await page2.goto('file://' + snapPath);
  await page2.waitForSelector('#app', { state: 'visible', timeout: 10000 });
  check('snapshot: renders without load', await page2.locator('#snapshotBanner').isVisible());
  check('snapshot: load button hidden', !(await page2.locator('#loadBtn').isVisible()));
  const snapCov = await page2.$eval('#kpis .kpi .n', e => e.textContent.trim());
  check('snapshot: coverage KPI present', snapCov === '60%', snapCov);
  await page2.selectOption('#goalFilter', 'G1');
  const g1def = await page2.$$eval('#defectsTable tr', rs => rs.length - 1);
  check('snapshot: filter still works (G1 → 2 defects)', g1def === 2, String(g1def));
  await page2.screenshot({ path: path.join(DIR, 'snapshot_screenshot.png'), fullPage: false });

  // dark mode render check
  const page3 = await browser.newPage({ colorScheme: 'dark', viewport: { width: 1360, height: 950 } });
  await page3.goto('file://' + snapPath);
  await page3.waitForSelector('#app', { state: 'visible' });
  const bg = await page3.evaluate(() => getComputedStyle(document.body).backgroundColor);
  check('dark mode: body ground is dark', bg === 'rgb(21, 24, 28)', bg);
  await page3.screenshot({ path: path.join(DIR, 'dashboard_dark.png'), fullPage: false });

  await browser.close();
  console.log('\n' + results.join('\n'));
  const fails = results.filter(r => r.startsWith('FAIL')).length;
  console.log(`\n${results.length - fails}/${results.length} checks passed`);
  process.exit(fails ? 1 : 0);
})().catch(e => { console.error('FATAL', e); process.exit(2); });
