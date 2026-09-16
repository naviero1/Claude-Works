#!/usr/bin/env python3
# Supplier Quality Dashboard — the prepared output for exercise 2 (Round 17).
# Reads the workbook Data tab, embeds the 144 clean detail rows, and emits one
# self-contained offline HTML file with the controls the exercise teaches.
# The page runs a visible SELF-CHECK on load: Berlin x Bravo Plastics,
# 2026-03..2026-08 must equal 8,575 units / 21 returns / 0.245% (verified
# independently with pandas/openpyxl — notes/design/round17_sequence.md).
import os, json, datetime
import openpyxl

HERE = os.path.dirname(__file__)
wb = openpyxl.load_workbook(os.path.join(HERE, '..', 'deliverables', 'exercise-data', 'Course_Workbook.xlsx'))
ws = wb['Data']
rows = []
for r in ws.iter_rows(min_row=2, values_only=True):
    if r[0] == 'TOTAL':
        continue
    rows.append({'m': r[0], 'site': r[1], 'sup': r[2], 'u': r[3], 'ret': r[4],
                 'def': r[5], 'ih': (None if r[6] == 'n/a' else r[6]), 'cost': r[7], 'ot': r[8]})
assert len(rows) == 144
DATA = json.dumps(rows, separators=(',', ':'))
TODAY = datetime.date.today().isoformat()

HTML = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Supplier Quality Dashboard — training snapshot</title>
<style>
  :root { --teal:#0E7C7B; --teal-d:#0A5B5A; --ink:#232A31; --slate:#46545F; --mute:#7A8790;
          --line:#DCE3E6; --panel:#F2F5F6; --amber:#B96A1B; --red:#AF3230; }
  * { box-sizing:border-box; }
  body { margin:0; font:14px/1.45 Calibri, 'Segoe UI', Arial, sans-serif; color:var(--ink); background:#FFFFFF; padding:0 16px; }
  header { padding:18px 4px 8px; border-bottom:2px solid var(--teal); }
  h1 { font-size:22px; margin:0 0 2px; } .sub { color:var(--slate); }
  .bar { display:flex; flex-wrap:wrap; gap:14px; align-items:flex-end; padding:12px 4px; background:var(--panel); margin:12px 0; border-radius:8px; padding:12px; }
  .ctl label { display:block; font-size:11px; font-weight:bold; color:var(--teal-d); letter-spacing:.4px; margin-bottom:2px; }
  select, button { font:inherit; padding:4px 6px; border:1px solid var(--line); border-radius:5px; background:#fff; color:var(--ink); }
  select[multiple] { min-width:150px; height:74px; }
  button { cursor:pointer; } button:focus, select:focus { outline:2px solid var(--teal); outline-offset:1px; }
  #reset { background:var(--teal); color:#fff; border-color:var(--teal); font-weight:bold; }
  #active { font-size:12.5px; color:var(--slate); padding:2px 6px; }
  #active b { color:var(--teal-d); }
  .tiles { display:flex; flex-wrap:wrap; gap:12px; margin:10px 0; }
  .tile { flex:1 1 160px; min-width:150px; background:var(--panel); border-radius:8px; padding:10px 14px; }
  .tile .lab { font-size:11px; font-weight:bold; letter-spacing:.4px; color:var(--teal-d); }
  .tile .val { font-size:26px; font-weight:bold; }
  .tile .note { font-size:11px; color:var(--mute); }
  .grids { display:flex; flex-wrap:wrap; gap:16px; }
  .card { flex:1 1 420px; min-width:320px; border:1px solid var(--line); border-radius:8px; padding:10px 14px; }
  .card h2 { font-size:15px; margin:2px 0 8px; }
  table { border-collapse:collapse; width:100%; font-size:12.5px; }
  th, td { border:1px solid var(--line); padding:3px 7px; text-align:right; }
  th { background:var(--panel); cursor:pointer; user-select:none; }
  th:first-child, td:first-child, th:nth-child(2), td:nth-child(2), th:nth-child(3), td:nth-child(3) { text-align:left; }
  .empty { padding:26px; text-align:center; color:var(--amber); font-weight:bold; }
  footer { margin:18px 0 24px; padding-top:10px; border-top:1px solid var(--line); font-size:12px; color:var(--slate); }
  footer b { color:var(--ink); }
  #selfcheck.ok { color:#1E7B34; } #selfcheck.bad { color:var(--red); }
  .bars rect:hover, .bars rect:focus { opacity:.75; cursor:pointer; }
  @media (max-width:640px){ .bar{flex-direction:column; align-items:stretch;} select[multiple]{width:100%;} }
</style></head><body>
<header>
  <h1>Supplier Quality Dashboard</h1>
  <div class="sub">The case question: <b>which supplier has the highest return rate, and what should we investigate next?</b>
  &nbsp;·&nbsp; Fictional training data · period 2025-09 to 2026-08 · grain: one row = month × site × supplier</div>
</header>

<div class="bar" role="group" aria-label="Filters">
  <div class="ctl"><label for="m1">START MONTH</label><select id="m1"></select></div>
  <div class="ctl"><label for="m2">END MONTH (inclusive)</label><select id="m2"></select></div>
  <div class="ctl"><label for="fsup">SUPPLIERS (multi-select)</label><select id="fsup" multiple></select></div>
  <div class="ctl"><label for="fsite">SITES (multi-select)</label><select id="fsite" multiple></select></div>
  <div class="ctl"><label for="grp">COMPARE BY</label><select id="grp"><option value="sup">Supplier</option><option value="site">Site</option></select></div>
  <div class="ctl"><label for="gran">TREND GRANULARITY</label><select id="gran"><option value="m">Monthly</option><option value="q">Quarterly</option></select></div>
  <div class="ctl"><label for="met">METRIC</label><select id="met">
    <option value="units">Units shipped</option>
    <option value="rr" selected>Return rate</option>
    <option value="dr">Defect rate</option></select></div>
  <div class="ctl"><label>&nbsp;</label><button id="reset">Reset all</button></div>
</div>
<div id="active"></div>

<div class="tiles" id="tiles"></div>
<div class="grids">
  <div class="card"><h2 id="trendTitle"></h2><div id="trend"></div></div>
  <div class="card"><h2 id="rankTitle"></h2><div id="rank"></div>
    <div style="font-size:11.5px;color:var(--mute);margin-top:4px">Bars are ranked highest→lowest on the selected metric. Click a bar to drill down to its records in the table.</div></div>
</div>
<div class="card" style="margin-top:16px"><h2 id="tabTitle">Records in the current selection</h2><div id="tab"></div></div>

<footer>
  <b>Definitions</b> — Return rate = sum(Units_Returned) ÷ sum(Units_Shipped) over the selected records ·
  Defect rate = sum(Defects_Found) ÷ sum(Units_Shipped) · rates shown to three decimals; sums, never averaged row percentages.
  Defects (caught at inspection) and returns (escaped to customers) are separate measures.
  One Inspection_Hours value is missing in the source and is shown blank — missing is not zero.<br>
  <b>Data snapshot</b> — embedded from Course_Workbook.xlsx (Data tab, 144 detail rows; TOTAL row excluded), generated __TODAY__.
  This file is a static snapshot, not a live reporting system — regenerate it when the source changes. Works offline; no network calls.
  Fictional training data: no real company, suppliers, or prices. &nbsp; <span id="selfcheck"></span>
</footer>

<script>
const D = __DATA__;
const MONTHS = [...new Set(D.map(r=>r.m))].sort();
const SUPS = [...new Set(D.map(r=>r.sup))].sort();
const SITES = [...new Set(D.map(r=>r.site))].sort();
const COLORS = ['#0E7C7B','#AF3230','#B96A1B','#46545F'];
const $ = id => document.getElementById(id);
const METRIC = { units:{lab:'Units shipped', unit:'units'}, rr:{lab:'Return rate', unit:'%'}, dr:{lab:'Defect rate', unit:'%'} };
let drill = null;          // {key, val} from clicking a bar
let sortCol = 0, sortAsc = true;

function fill(sel, vals, all){ sel.innerHTML=''; vals.forEach(v=>{const o=document.createElement('option');o.value=v;o.textContent=v;o.selected=all;sel.appendChild(o);}); }
function init(){
  fill($('m1'), MONTHS, false); fill($('m2'), MONTHS, false);
  $('m1').value = MONTHS[0]; $('m2').value = MONTHS[MONTHS.length-1];
  fill($('fsup'), SUPS, true); fill($('fsite'), SITES, true);
  ['m1','m2','fsup','fsite','grp','gran','met'].forEach(id=>$(id).addEventListener('change', ()=>{drill=null; render();}));
  $('reset').addEventListener('click', ()=>{ init0(); drill=null; render(); });
  render();
}
function init0(){ $('m1').value=MONTHS[0]; $('m2').value=MONTHS[MONTHS.length-1];
  [...$('fsup').options].forEach(o=>o.selected=true); [...$('fsite').options].forEach(o=>o.selected=true);
  $('grp').value='sup'; $('gran').value='m'; $('met').value='rr'; sortCol=0; sortAsc=true; }
const picked = sel => [...sel.selectedOptions].map(o=>o.value);
function filtered(){
  const a=$('m1').value, b=$('m2').value, lo=a<b?a:b, hi=a<b?b:a;
  const su=picked($('fsup')), si=picked($('fsite'));
  return D.filter(r=> r.m>=lo && r.m<=hi && su.includes(r.sup) && si.includes(r.site));
}
const q = m => m.slice(0,4)+'-Q'+Math.ceil(+m.slice(5)/3);
function agg(rs){ const u=rs.reduce((s,r)=>s+r.u,0), re=rs.reduce((s,r)=>s+r.ret,0), de=rs.reduce((s,r)=>s+r.def,0);
  return {u, re, de, rr: u? re/u*100 : null, dr: u? de/u*100 : null}; }
const mv = (a,m)=> m==='units'? a.u : m==='rr'? a.rr : a.dr;
const fmt = (v,m)=> v==null? '—' : m==='units'? v.toLocaleString('en-US') : v.toFixed(3)+'%';

function render(){
  const rs0 = filtered();
  const rs = drill ? rs0.filter(r=> (drill.key==='sup'? r.sup : r.site)===drill.val) : rs0;
  const met=$('met').value, grpKey=$('grp').value, grpLab= grpKey==='sup'?'supplier':'site';
  const a=agg(rs0);
  // active-selection line
  const su=picked($('fsup')), si=picked($('fsite'));
  $('active').innerHTML = 'Showing <b>'+rs0.length+'</b> of 144 records · months <b>'+$('m1').value+'</b>–<b>'+$('m2').value+'</b>'
    + ' · suppliers <b>'+(su.length===SUPS.length?'all':su.join(', ')||'none')+'</b>'
    + ' · sites <b>'+(si.length===SITES.length?'all':si.join(', ')||'none')+'</b>'
    + (drill? ' · <b style="color:var(--amber)">drill-down: '+drill.val+'</b> (click Reset or change a filter to clear)':'');
  // tiles (always the FILTERED set, so every view agrees)
  $('tiles').innerHTML = rs0.length===0 ? '' : [
    ['UNITS SHIPPED', a.u.toLocaleString('en-US'), 'sum over selection'],
    ['UNITS RETURNED', a.re.toLocaleString('en-US'), 'escapes to customers'],
    ['RETURN RATE', fmt(a.rr,'rr'), 'returns ÷ shipped'],
    ['DEFECT RATE', fmt(a.dr,'dr'), 'caught at inspection ÷ shipped'],
  ].map(t=>'<div class="tile"><div class="lab">'+t[0]+'</div><div class="val">'+t[1]+'</div><div class="note">'+t[2]+'</div></div>').join('');
  const empty = '<div class="empty">No records match the current selections. This is an empty selection, not a zero — widen the month range or clear a filter (Reset restores everything).</div>';
  // trend
  $('trendTitle').textContent = METRIC[met].lab + ' by ' + ($('gran').value==='m'?'month':'quarter') + ', one line per ' + grpLab;
  $('trend').innerHTML = rs0.length? trendSVG(rs0, met, grpKey) : empty;
  // ranked bars
  $('rankTitle').textContent = METRIC[met].lab + ' by ' + grpLab + ' — ranked';
  $('rank').innerHTML = rs0.length? rankSVG(rs0, met, grpKey) : empty;
  // table
  $('tabTitle').textContent = 'Records in the current selection' + (drill? ' — drill-down: '+drill.val : '') + ' ('+rs.length+' rows)';
  $('tab').innerHTML = rs.length? tableHTML(rs) : empty;
}
function groups(rs, key){ const g={}; rs.forEach(r=>{ (g[key==='sup'?r.sup:r.site] ||= []).push(r); }); return g; }
function trendSVG(rs, met, key){
  const gran=$('gran').value, per = [...new Set(rs.map(r=> gran==='m'? r.m : q(r.m)))].sort();
  const g = groups(rs, key), names=Object.keys(g).sort();
  const series = names.map(n=>{ const by={}; g[n].forEach(r=>{ const p=gran==='m'?r.m:q(r.m); (by[p] ||= []).push(r); });
    return { n, pts: per.map(p=> by[p]? mv(agg(by[p]),met) : null) }; });
  const W=430,H=220,L=52,R=104,T=12,B=34, vals=series.flatMap(s=>s.pts).filter(v=>v!=null);
  if(!vals.length) return '<div class="empty">No computable values in this selection.</div>';
  const vmax=Math.max(...vals)*1.12||1, x=i=> L+(per.length===1?0:(W-L-R)*i/(per.length-1)), y=v=> T+(H-T-B)*(1-v/vmax);
  let s='<svg viewBox="0 0 '+W+' '+H+'" role="img" aria-label="Trend chart" style="width:100%;height:auto">';
  for(let t=0;t<=3;t++){const vy=y(vmax*t/3); s+='<line x1="'+L+'" y1="'+vy+'" x2="'+(W-R)+'" y2="'+vy+'" stroke="#DCE3E6"/>'
    +'<text x="'+(L-5)+'" y="'+(vy+4)+'" font-size="9.5" fill="#7A8790" text-anchor="end">'+(met==='units'? Math.round(vmax*t/3).toLocaleString('en-US') : (vmax*t/3).toFixed(2)+'%')+'</text>';}
  per.forEach((p,i)=>{ if(per.length<=6 || i%2===0) s+='<text x="'+x(i)+'" y="'+(H-B+14)+'" font-size="9" fill="#46545F" text-anchor="middle">'+p+'</text>'; });
  series.forEach((se,si2)=>{ const c=COLORS[si2%COLORS.length];
    const seg=se.pts.map((v,i)=> v==null? null : [x(i),y(v)]).filter(Boolean);
    s+='<polyline fill="none" stroke="'+c+'" stroke-width="2" points="'+seg.map(p=>p.join(',')).join(' ')+'"/>';
    se.pts.forEach((v,i)=>{ if(v!=null) s+='<circle cx="'+x(i)+'" cy="'+y(v)+'" r="3" fill="'+c+'"><title>'+se.n+' · '+per[i]+' · '+fmt(v,met)+'</title></circle>'; });
    const last=seg[seg.length-1]; if(last) s+='<text x="'+(last[0]+6)+'" y="'+(last[1]+3+(si2? (si2%2?9:-7):0))+'" font-size="10" font-weight="bold" fill="'+c+'">'+se.n.split(' ')[0]+'</text>';
  });
  return s+'</svg>';
}
function rankSVG(rs, met, key){
  const g=groups(rs,key);
  const items=Object.entries(g).map(([n,r])=>({n, v:mv(agg(r),met)})).filter(i=>i.v!=null).sort((p,r)=>r.v-p.v);
  const W=430, bh=30, H=items.length*bh+8, vmax=Math.max(...items.map(i=>i.v))||1;
  let s='<svg viewBox="0 0 '+W+' '+H+'" role="img" aria-label="Ranked bars" class="bars" style="width:100%;height:auto">';
  items.forEach((it,i)=>{ const bw=Math.max(2,(W-190)*it.v/vmax), yy=i*bh+4;
    s+='<rect x="120" y="'+yy+'" width="'+bw+'" height="'+(bh-10)+'" rx="4" fill="#0E7C7B" tabindex="0" role="button" aria-label="Drill down to '+it.n+'" onclick="drillTo(\\''+key+'\\',\\''+it.n.replace(/'/g,"\\\\'")+'\\')" onkeydown="if(event.key===\\'Enter\\')drillTo(\\''+key+'\\',\\''+it.n.replace(/'/g,"\\\\'")+'\\')"><title>'+it.n+' · '+fmt(it.v,met)+' — click to drill down</title></rect>'
      +'<text x="114" y="'+(yy+14)+'" font-size="11" fill="#232A31" text-anchor="end">'+it.n+'</text>'
      +'<text x="'+(126+bw)+'" y="'+(yy+14)+'" font-size="11" font-weight="bold" fill="#232A31">'+fmt(it.v,met)+'</text>'; });
  return s+'</svg>';
}
function drillTo(key,val){ drill={key,val}; render(); }
function tableHTML(rs){
  const cols=[['m','Month'],['site','Site'],['sup','Supplier'],['u','Shipped'],['ret','Returned'],['def','Defects'],['ih','Insp. hours'],['cost','Unit cost $'],['ot','On-time %']];
  const sorted=[...rs].sort((a,b)=>{ const k=cols[sortCol][0]; const av=a[k]??-1, bv=b[k]??-1;
    return (av<bv?-1:av>bv?1:0)*(sortAsc?1:-1); });
  let h='<div style="overflow-x:auto"><table><tr>'+cols.map((c,i)=>'<th onclick="setSort('+i+')" title="Click to sort">'+c[1]+(i===sortCol?(sortAsc?' ▲':' ▼'):'')+'</th>').join('')+'</tr>';
  sorted.slice(0,40).forEach(r=>{ h+='<tr>'+cols.map(c=>'<td>'+(r[c[0]]==null?'':(typeof r[c[0]]==='number'&&c[0]==='u'? r[c[0]].toLocaleString('en-US'):r[c[0]]))+'</td>').join('')+'</tr>'; });
  h+='</table></div>';
  if(sorted.length>40) h+='<div style="font-size:11.5px;color:var(--mute)">Showing 40 of '+sorted.length+' rows — narrow the selection or drill down to see the rest.</div>';
  return h;
}
function setSort(i){ if(sortCol===i) sortAsc=!sortAsc; else {sortCol=i; sortAsc=true;} render(); }
// visible self-check: the exercise's verified filtered result
(function(){ const sel=D.filter(r=> r.site==='Berlin' && r.sup==='Bravo Plastics' && r.m>='2026-03' && r.m<='2026-08');
  const a=agg(sel), ok = sel.length===6 && a.u===8575 && a.re===21 && a.rr.toFixed(3)==='0.245';
  const el=$('selfcheck'); el.className= ok?'ok':'bad';
  el.textContent='Self-check '+(ok?'PASSED':'FAILED')+': Berlin × Bravo Plastics, 2026-03..2026-08 → '+sel.length+' rows, '+a.u.toLocaleString('en-US')+' units, '+a.re+' returns, '+fmt(a.rr,'rr')+(ok?' — matches the workbook.':' — INVESTIGATE.');
})();
init();
</script></body></html>
"""

out = os.path.join(HERE, '..', 'deliverables', 'exercise-data', 'Supplier_Quality_Dashboard.html')
open(out, 'w').write(HTML.replace('__DATA__', DATA).replace('__TODAY__', TODAY))
print('dashboard written:', out, f'({os.path.getsize(out)//1024} KB, {len(rows)} rows embedded)')
