const { chromium } = require('playwright-core');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 1360, height: 1000 } });
  page.on('pageerror', e => console.log('PAGEERROR:', e.message));
  const results = [];
  const check = (l, c, x='') => results.push(`${c?'PASS':'FAIL'}  ${l}${x?' — '+x:''}`);

  await page.goto('file://' + path.join(__dirname, 'dashboard.html'));
  await page.evaluate(() => { window.showOpenFilePicker = undefined; });
  const [chooser] = await Promise.all([page.waitForEvent('filechooser'), page.click('#loadBtn')]);
  await chooser.setFiles(path.join(__dirname, 'comms_assessment_MOCK.xlsx'));
  await page.waitForSelector('#app', { state: 'visible', timeout: 15000 });

  const kpis = await page.$$eval('#kpis .kpi', els => Object.fromEntries(els.map(e =>
    [e.querySelector('.l').textContent.trim(), e.querySelector('.n').textContent.trim()])));
  // was 15 scored/6 defects; +2 required (1 covered FR16, 1 missing FR17) => 17 scored, 7 defects, coverage 10/17=59%
  check('7 open defects (FR17 joins)', kpis['Open defects'] === '7', JSON.stringify(kpis));
  check('coverage 59%', kpis['Coverage'] === '59%');

  const goalRows = await page.$$eval('#goalsTable tr', rs => rs.length - 1);
  check('5 goal rows', goalRows === 5, String(goalRows));
  const classChips = await page.$$eval('#goalsTable .chip', cs => cs.map(c => c.textContent.trim()));
  check('4 core + 1 aspirational badges', classChips.filter(c => c==='core').length === 4 && classChips.filter(c => c==='aspirational').length === 1, classChips.join(','));
  const lastGoal = await page.$eval('#goalsTable tr:last-child', r => r.textContent.replace(/\s+/g,' '));
  check('G5 sorted last (aspirational band), 2 req 1 cov', /G5/.test(lastGoal) && /bench strength/.test(lastGoal), lastGoal.slice(0,140));

  await page.selectOption('#goalFilter', 'G5');
  const g5def = await page.$eval('#defectsTable', t => t.textContent.replace(/\s+/g,' '));
  check('G5 filter: FR17 missing defect, priority 6', /supplier_auditor_training_status/.test(g5def) && /missing/.test(g5def) && /6/.test(g5def), g5def.slice(0,200));
  await page.selectOption('#goalFilter', '');
  await page.screenshot({ path: path.join(__dirname, 'mock_screenshot.png'), fullPage: false });

  await browser.close();
  console.log(results.join('\n'));
  process.exit(results.some(r => r.startsWith('FAIL')) ? 1 : 0);
})().catch(e => { console.error('FATAL', e); process.exit(2); });
