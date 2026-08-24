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

  // ---- information tree view ----
  await page.click('#tabTree');
  check('tree: view switches', await page.locator('#viewTree').isVisible() && !(await page.locator('#viewOverview').isVisible()));
  const treeHtml = await page.$eval('#treeRoot', e => e.textContent.replace(/\s+/g,' '));
  check('tree: G1 change-control gap visible', /change control/.test(treeHtml) && /design_change_notice/.test(treeHtml) && /missing/.test(treeHtml));
  check('tree: G5 training topic under capability building', /capability building/.test(treeHtml) && /supplier_auditor_training_status/.test(treeHtml));
  check('tree: G5 topic summary 1\/2 covered', /1\/2 covered/.test(treeHtml));
  const goalNodes = await page.$$eval('.goalnode', ns => ns.length);
  check('tree: 5 goal nodes', goalNodes === 5, String(goalNodes));
  await page.selectOption('#goalFilter', 'G5');
  const g5nodes = await page.$$eval('.goalnode', ns => ns.length);
  check('tree: filter narrows to 1 node', g5nodes === 1, String(g5nodes));
  await page.screenshot({ path: path.join(__dirname, 'tree_screenshot.png'), fullPage: false });
  await page.selectOption('#goalFilter', '');
  await page.click('#tabOverview');
  check('tree: switch back to overview', await page.locator('#viewOverview').isVisible());

  // ---- flow map view ----
  await page.click('#tabMap');
  check('map: view visible', await page.locator('#viewMap').isVisible());
  const nodeCount = await page.$$eval('g.mapnode', ns => ns.length);
  check('map: 11 actor nodes', nodeCount === 11, String(nodeCount));
  const missEdges = await page.$$eval('#mapWrap path.edge.missing', ps => ps.length);
  check('map: >=3 missing edges drawn', missEdges >= 3, String(missEdges));
  const svgText = await page.$eval('#mapWrap svg', s => s.textContent);
  check('map: isolated badge present', /isolated/.test(svgText));
  check('map: function column labels', /QUALITY/.test(svgText) && /OPERATIONS/.test(svgText));
  await page.check('#defectsOnly');
  const covAfter = await page.$$eval('#mapWrap path.edge.covered', ps => ps.length);
  check('map: defects-only hides covered', covAfter === 0, String(covAfter));
  await page.uncheck('#defectsOnly');

  // ---- people view ----
  await page.click('#tabPeople');
  check('people: view visible', await page.locator('#viewPeople').isVisible());
  const firstPerson = await page.$eval('#peopleTable tr:nth-child(2)', r => r.textContent.replace(/\s+/g,' '));
  check('people: Frodo ranked first with SPOF', /Frodo/.test(firstPerson) && /SPOF/.test(firstPerson), firstPerson.slice(0,120));
  await page.click('#peopleTable .person-link');
  check('people: person detail opens', await page.locator('#detailModal').isVisible());
  const detail = await page.$eval('#detailCard', e => e.textContent.replace(/\s+/g,' '));
  check('people: detail shows produce/receive/meetings', /Must produce/.test(detail) && /Must receive/.test(detail) && /Meetings/.test(detail));
  await page.keyboard.press('Escape');

  // ---- meeting detail + capacity columns ----
  await page.click('#tabOverview');
  const mhead = await page.$eval('#meetingsTable tr', r => r.textContent);
  check('meetings: capacity columns present', /topics/.test(mhead) && /min\/topic/.test(mhead));
  await page.$$eval('.mtg-link', ls => ls.find(l => /Monthly Ops Status/.test(l.textContent)).click());
  const mdetail = await page.$eval('#detailCard', e => e.textContent.replace(/\s+/g,' '));
  check('meetings: R9 detail shows no-cargo capacity note', /no modeled cargo/.test(mdetail), mdetail.slice(0,180));
  await page.keyboard.press('Escape');

  // ---- help modal + KPI sublines ----
  await page.click('#helpBtn');
  check('help: modal opens with element dictionary', /What am I looking at/.test(await page.$eval('#helpModal', e => e.textContent)) && await page.locator('#helpModal').isVisible());
  await page.keyboard.press('Escape');
  const kpiSub = await page.$eval('#kpis .kpi .s', e => e.textContent);
  check('kpi: n-of-m subline present', /of .* required flows covered/.test(kpiSub), kpiSub);
  const kpiCount = await page.$$eval('#kpis .kpi', els => els.length);
  check('kpi: 7 tiles incl. VA ratio', kpiCount === 7, String(kpiCount));

  // ---- decompose view ----
  await page.click('#tabDecompose');
  check('decompose: view visible', await page.locator('#viewDecompose').isVisible());
  const cards = await page.$$eval('.pickcard', cs => cs.length);
  check('decompose: 5 goal cards', cards === 5, String(cards));
  await page.$$eval('.pickcard', cs => cs.find(c => /G1/.test(c.textContent)).click());
  const hero = await page.$eval('.goalhero', e => e.textContent.replace(/\s+/g,' '));
  check('decompose: G1 hero renders', /Reduce supplier defect rate/.test(hero) && /core/.test(hero), hero.slice(0,120));
  const dec = await page.$eval('#decomposeRoot', e => e.textContent.replace(/\s+/g,' '));
  check('decompose: required spec with rationale', /must hear/.test(dec) && /why:/.test(dec));
  check('decompose: missing gap sentence', /nothing usable delivers this to Frodo Baggins/i.test(dec) || /Gap — nothing usable/.test(dec));
  check('decompose: reality shows carrier chips', /does send it/.test(dec));
  check('decompose: theater meeting listed', /theater/.test(dec) && /Monthly Ops Status/.test(dec));
  check('decompose: decisions stage present', /Decisions & follow-ups/.test(dec));
  const openFolds = await page.$$eval('details.topicfold[open]', ds => ds.length);
  check('decompose: gap topics start open', openFolds >= 1, String(openFolds));
  await page.screenshot({ path: path.join(__dirname, 'decompose_view.png'), fullPage: true });
  await page.click('#decomposeBack');
  const cardsBack = await page.$$eval('.pickcard', cs => cs.length);
  check('decompose: back returns to picker', cardsBack === 5, String(cardsBack));




  await browser.close();
  console.log(results.join('\n'));
  process.exit(results.some(r => r.startsWith('FAIL')) ? 1 : 0);
})().catch(e => { console.error('FATAL', e); process.exit(2); });
