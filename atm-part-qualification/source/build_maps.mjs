import fs from 'node:fs/promises';
import path from 'node:path';
import { Presentation, PresentationFile } from '@oai/artifact-tool';
import { finalizePresentation } from '/root/.codex/skills/builtins/presentations/container_tools/artifact_tool_utils.mjs';
const ROOT=path.resolve(import.meta.dirname,'..');
const B=path.join(ROOT,'build');
const OUT=path.join(ROOT,'deliverables');
const C={blue:'#318DFF',amber:'#FFD77D',green:'#99D8AA',ink:'#202A34',red:'#B43D36',gray:'#EAF0F5',white:'#FFFFFF'};
const p=Presentation.create({slideSize:{width:1600,height:900}});
let idx=0;
function text(s,t,x,y,w,h,size=26,bold=false,color=C.ink,align='left'){
 const o=s.shapes.add({geometry:'textbox',name:t.slice(0,65),position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 o.text=t;o.text.style={typeface:'Carlito',fontSize:size,bold,color,alignment:align,verticalAlignment:'middle',autoFit:'none',insets:{left:0,right:0,top:0,bottom:0}};return o;
}
function box(s,t,x,y,w,h,fill=C.blue,size=25,geo='rect'){
 const o=s.shapes.add({geometry:geo,name:t.slice(0,65),position:{left:x,top:y,width:w,height:h},fill,line:{fill:fill===C.white?C.ink:fill,width:1.4}});
 o.text=t;o.text.style={typeface:'Carlito',fontSize:size,color:C.ink,alignment:'left',verticalAlignment:'middle',autoFit:'none',insets:{left:16,right:16,top:10,bottom:10}};return o;
}
function link(s,a,b,from='bottom',to='top',dashed=false){return s.shapes.connect(a,b,{kind:from==='bottom'&&to==='top'?'straight':'elbow',fromSide:from,toSide:to,line:{fill:C.ink,width:2.2,style:dashed?'dashed':'solid'},tail:{type:'triangle',width:'med',length:'med'}});}
function route(s,pts,dashed=false){
 const nodes=pts.map(([x,y])=>s.shapes.add({geometry:'rect',position:{left:x-.5,top:y-.5,width:1,height:1},fill:'none',line:{fill:'none',width:0}}));
 for(let i=1;i<nodes.length;i++)s.shapes.connect(nodes[i-1],nodes[i],{kind:'straight',line:{fill:C.ink,width:2.2,style:dashed?'dashed':'solid'},...(i===nodes.length-1?{tail:{type:'triangle',width:'med',length:'med'}}:{})});
}
function slide(title,sub,notes=''){
 const s=p.slides.add();s.background.fill=C.white;idx++;
 text(s,title,55,32,1490,62,43,true);text(s,sub,55,101,1490,54,24);
 text(s,`Review draft  •  17 September 2026     /     ${idx}`,55,864,1490,24,17,false,'#52606C');
 s.speakerNotes.textFrame.setText(notes+'\nSource: original Map A and Map B, working handoff v1 dated 16 September 2026, original supplier training draft dated 4 June 2026, and Oscar decisions dated 17 September 2026. Document identifiers ending XXX remain unassigned.');return s;
}
// 1 Faithful current-state topology, all native editable objects.
{
 const s=slide('As-is process map','Current Advanced Tissue Models supplier controls and informal part qualification', 'This is the current-state map supplied by Oscar. The note describing reduced inspection is source history, not a new authorization. No supplier training step appears in the source map.');
 text(s,'New supplier, new part\nExisting supplier, new part\nNew supplier, existing part',60,197,360,130,25);
 const a=box(s,'668008 SOP, SUPPLIER\nCONTROLS, ATM',505,183,355,98);
 const b=box(s,'668009 DOP,SUPPLIER\nSELECTION,APPROVAL AND\nMONITORING,ATM',355,333,410,123);
 const c=box(s,'668504 WI, SUPPLIER\nAUDITING, ATM',65,505,350,100);
 const d=box(s,'668529 ATM,WI,ASL USE\nAND MAINTENANCE',575,505,370,100);
 const e=box(s,'668007 SOP,PURCHASING\nAND PLANNING,ATM',1125,183,410,98);
 const f=box(s,"Once supplier is on ASL, informal part qualification process is done; 1st article inspection or multiple lots inspected prior to dropping inspection reqt’s.\n\nSame informal process is done for new parts from existing suppliers",520,654,620,175,C.blue,22);
 route(s,[[682,281],[682,309],[560,309],[560,333]]);route(s,[[560,456],[560,480],[240,480],[240,505]]);route(s,[[560,456],[560,480],[760,480],[760,505]]);route(s,[[760,605],[760,630],[830,630],[830,654]]);link(s,d,e,'right','bottom',true);
 text(s,'Original labels retained\n\nATM (Advanced Tissue Models)\nSOP (Standard Operating Procedure)\nDOP (Department Operating Procedure)\nWI (Work Instruction)\nASL (Approved Supplier List)',1180,365,350,250,20);
}
// 2 To-be workflow.
{
 const s=slide('To-be process map','Supplier approval precedes tissue personnel certification and component qualification', '668008 and 668009 remain separate. No document retires or absorbs another. New supplier with an existing tissue part still requires site/supplier-specific qualification. Personnel turnover alone does not automatically requalify an already-qualified part.');
 const a=box(s,'668008\nSupplier Controls',60,187,280,85);
 const b=box(s,'668009\nSupplier Selection, Approval\nand Monitoring',60,325,330,117,C.blue,23);
 const c=box(s,'668504\nSupplier Auditing',60,510,270,85);
 const d=box(s,'668529\nSupplier approval recorded\nin the Approved Supplier List',455,325,380,117);
 const e=box(s,'NEW 668XXX\nTissue Supplier Personnel\nTraining and Certification',930,212,510,105,C.green);
 const f=box(s,'NEW 668XXX\nComponent Qualification\nTissue and non-tissue paths',930,455,510,117);
 const g=box(s,'668529\nQualified part and supplier-site\nscope recorded',455,700,380,104);
 const h=box(s,'668007\nPurchasing and Planning\nLead time and reorder points',1030,700,410,104);
 route(s,[[200,272],[200,299],[225,299],[225,325]]);route(s,[[225,442],[225,477],[195,477],[195,510]]);link(s,b,d,'right','left');route(s,[[835,383],[877,383],[877,264],[930,264]]);route(s,[[1440,264],[1515,264],[1515,512],[1440,512]]);route(s,[[835,383],[900,383],[900,512],[930,512]],true);route(s,[[930,540],[890,540],[890,658],[645,658],[645,700]]);link(s,g,h,'right','left');
 text(s,'Tissue',830,200,120,35,22,true);text(s,'Non-tissue',675,467,210,35,22,true);
 text(s,'Personnel gate\n≥95% first-pass yield\n≥2 consecutive harvest days\n≥30 inspected units per person/task/family',965,333,530,113,23);
 text(s,'Tissue part gate\nEvery qualification lot ≥95% first-pass yield\nLot count requires approval before execution',945,590,575,85,23);
 text(s,'All existing documents remain separate.\nBlue = local document   Green = new training procedure',60,715,365,109,22);
}
// 3 document dependencies.
{
 const s=slide('To-be qualification document map','Corporate references remain amber; local qualification documents remain blue', 'Original corporate labels retained. Applicability is determined for each part. Do not assume tissue exemption from any corporate material requirement. Verify current controlled revisions before release. PPQP means Purchased Part Qualification Process in the source handoff.');
 const a=box(s,'668XXX SOP,COMPONENT\nQUALIFICATION,ATM\n\nREF: DOP,PPQP 1003684\nPilot PPQP quick reference guide\nnon-prime parts',55,180,445,200,C.blue,24);
 const b=box(s,'668XXX FORM,COMPONENT\nQUALIFICATION,CHECKLIST,ATM\n\nREF: FORM,PPQP CHECKLIST\n1004112',55,466,445,156,C.blue,24);
 const c=box(s,'668XXX WI,FAIR,ATM\n\nREF: DOP,FAIR 854197\nFAIR quick reference guide',568,466,400,156,C.blue,24);
 const d=box(s,'668XXX FORM,FAIR,ATM\nREF: FORM,FAIR 800084',568,693,400,87,C.blue,24);
 const e=box(s,'1049262 SOP,REGULATED\nMATERIALS COMPLIANCE',1080,180,465,85,C.amber,24);
 const f=box(s,'854133 SOP,MATERIALS',1080,312,465,72,C.amber,24);
 const g=box(s,'853313 SOP,ENVIRONMENTAL\nCOMPLIANCE SYSTEMS (ROHS)',1080,431,465,91,C.amber,24);
 const h=box(s,'1009008 WI,ROHS\nDOCUMENTATION FOR MATERIALS,\nPARTS, AND SUB-ASSEMBLIES',1080,582,465,113,C.amber,24);
 link(s,a,b);route(s,[[277,380],[277,422],[768,422],[768,466]]);link(s,c,d);link(s,g,h);route(s,[[1080,222],[1020,222],[1020,279],[500,279]],true);route(s,[[1080,348],[1020,348],[1020,279],[500,279]],true);route(s,[[1080,638],[1020,638],[1020,279],[500,279]],true);
 text(s,'Tissue checklist evidence\nPersonnel certification plus approved\nqualification lots inspected at the supplier site',55,677,475,127,25);
 text(s,'FAIR (First Article Inspection Report)   PPQP (Purchased Part Qualification Process)\nSOP (Standard Operating Procedure)   DOP (Department Operating Procedure)   WI (Work Instruction)\nATM (Advanced Tissue Models)   RoHS (Restriction of Hazardous Substances)',55,801,1480,59,17);
}
// 4 main training map, both gates and rework.
{
 const s=slide('Supplier training process map','Harvest and build personnel follow training, monitoring, certification and the qualification handoff', 'Procedure Sections 4–6. Inspector certification follows a separate attribute-agreement route, not the harvest yield gate. Training outputs cannot be counted as unassisted certification evidence. At 30 units, 29 passes meet the threshold and 28 fail.');
 const a=box(s,'1  Prerequisites\nSupplier status verified\nControlled instruction and specification\nQualified trainer and inspector\nPer-unit trainee attribution ready',55,186,440,174,C.blue,22);
 const b=box(s,'2  Training Phase\nTissue expert demonstrates the task\nOperations Supervisor supports\nCoaching and questions permitted',565,186,440,174,C.green,25);
 const c=box(s,'3  Readiness sign-off\nTrainer and inspector agree\nRecord task, revisions and date',1080,186,460,174,C.green,25);
 const d=box(s,'4  Monitoring Phase\nTrainee performs the task\nInspector examines every unit\nRecord first result and attribution',1080,452,460,150,C.green,25);
 const e=box(s,'5  Personnel gate\n≥95% first-pass yield\n≥2 consecutive harvest days\n≥30 units in the evaluation window',565,452,440,150,C.white,25);
 const f=box(s,'6  Certification\nSupplier Engineer evaluates evidence\nRecord on 800082 and training log\nScope: person, site, task and family',55,452,440,150,C.green,23);
 link(s,a,b,'right','left');link(s,b,c,'right','left');link(s,c,d);link(s,d,e,'left','right');link(s,e,f,'left','right');
 text(s,'Ready',1390,388,140,35,22,true);text(s,'Pass',507,495,60,35,22,true);
 const g=box(s,'Gate not met or technique concern\nContinue only under defined monitoring controls\nRecurring <95%: inspector shadows and retrains\nFresh monitoring window after coached retraining',585,686,920,137,C.gray,24);
 link(s,e,g);text(s,'No',835,631,80,35,22,true);
 text(s,'New supplier or tissue part\nSeparate component qualification follows.\nEvery lot ≥95%; approved lot count required.\nExisting part with new personnel: assess whether\npart requalification is needed.',55,680,475,155,23);
 text(s,'Not ready: return to Training Phase',1065,146,480,31,19,false,C.red);
}
// 5 recurring low yield response.
{
 const s=slide('Recurring low yield and recovery','The 95% threshold stays in force; recurring results below it trigger inspector shadow training', 'Every failure receives review. The numeric recurrence count/window is not approved yet and must be set in Appendix A before release. Do not wait for a monthly call to contain an identified issue. A quality-approved deviation is a controlled exception, not certification or product release.');
 const a=box(s,'Yield below 95%\nFlag the result and segregate\nnonconforming output',55,185,400,125,C.white);
 const b=box(s,'Supplier Engineer and Quality review\nUse the approved recurrence rule\nCheck technique, process and\ninspection consistency',570,185,440,125,C.blue,24);
 const c=box(s,'Recurring below 95%\nInspector shadows harvesting technician\nReinforces training and inspects output\nRecords defects and observed causes',1090,185,455,158,C.green,24);
 link(s,a,b,'right','left');link(s,b,c,'right','left');
 const d=box(s,'Technique corrected\nFresh unassisted monitoring window\n≥95% first-pass yield / ≥30 units\n≥2 consecutive harvest days',1090,485,455,137,C.green,24);
 const e=box(s,'Recovery approval\nSupplier Engineer reviews evidence\nQuality authorizes return to routine work\nUpdate status and training records',570,485,440,150,C.blue,22);
 const f=box(s,'Routine work and trend review\nIndependent incoming inspection\ncontinues at Advanced Tissue Models',55,485,400,137,C.blue,24);
 link(s,c,d);link(s,d,e,'left','right');link(s,e,f,'left','right');text(s,'Gate passed',970,645,210,34,22,true);
 text(s,'Gate not met: keep monitoring controls and repeat training or correct the process',610,700,935,57,25,true,C.red);
 text(s,'Process or material cause: correct the process and assess part requalification.\nSupplier-site versus receipt difference: investigate handling, freezing and transport.\nDo not assign a cause to the technician from yield alone.',55,345,965,121,25);
 text(s,'Exception path: Quality approves the scope, duration, added inspection and exit criteria in writing before work.\nExpiration ends the authorization. A deviation does not certify personnel, qualify a part or release nonconforming tissue.',55,786,1490,63,23);
}
// 6 triggers as clean exact comparative rows (native editable text).
{
 const s=slide('Entry paths and qualification boundaries','Each trigger enters the appropriate stage without repeating unrelated approvals');
 const rows=[
 ['Trigger','Personnel route','Component qualification'],
 ['New supplier, new or existing tissue','Full training, monitoring and certification','Required for the supplier/site and part'],
 ['Existing supplier, new tissue','Family-specific training and certification','Required for the new part scope'],
 ['New or reassigned personnel, existing part','Train and certify the individual','Assess impact; no automatic repeat'],
 ['Instruction or specification revision','Training on changes; evaluate monitoring need','Quality and Design Engineer assess impact'],
 ['Technique issue or recurring yield below 95%','Inspector shadow training, then fresh monitoring','Assess process or part impact'],
 ['Approved inactivity limit reached','Reassess competence and repeat monitoring','Assess only if other changes occurred']
 ];
 let y=192;for(let i=0;i<rows.length;i++){const h=i?79:58;const fill=i===0?C.blue:i%2?C.gray:C.white;box(s,rows[i][0],55,y,440,h,fill,i?23:25);box(s,rows[i][1],495,y,535,h,fill,i?23:25);box(s,rows[i][2],1030,y,515,h,fill,i?23:25);y+=h;}
 text(s,'Quality certifies inspection personnel with the Design Engineer using attribute agreement.\nThe harvest yield gate does not establish inspection accuracy.',55,759,1490,78,27,true);
}
// 7 controls, open fields.
{
 const s=slide('Release decisions and remaining fields','The approved decisions are incorporated; incomplete settings prevent controlled release');
 text(s,'Confirmed by Oscar',60,192,620,49,33,true);
 text(s,'30 inspected units per person, task and tissue family\n\nAt least 2 consecutive harvest days\n\n95% minimum first-pass yield for personnel and lots\n\nRecurring low yield triggers inspector shadow training\n\nQuality-approved deviations with explicit controls\n\n668008, 668009 and all other documents stay separate',60,264,675,500,27);
 text(s,'Required before controlled release',840,192,690,49,33,true);
 text(s,'Qualification-lot count and lot/sample definition\n\nRecurrence count and review window below 95%\n\nInspector agreement criteria and reference-set design\n\nConfirmed acceptance specification and revisions\n\nMonitoring attempt limit and inactivity interval\n\nApproved attribution method and record repository',840,264,690,500,27);
 text(s,'These fields require designated stakeholder approval. Blank fields do not authorize qualification or shipment.',60,786,1480,56,26,true,C.red);
}
// 8/9 preserve source references, no reconstruction of cropped content.
for (const [letter,title,file] of [['A','Original current-state map','Original_Map_A_Current_ATM_Supplier_Controls_and_Part_Qualification.png'],['B','Original proposed map','Original_Map_B_Proposed_Qualification_Structure.png']]){
 const s=slide(`${title} reference`,'Unaltered source image for comparison with the editable maps',letter==='B'?'The source screenshot cuts off the green notes along the top. Their missing content is not reconstructed. Its merged 668008/668009 label is superseded by Oscar’s 17 September decision to retain separate documents.':'Source map reproduced without changes.');
 s.images.add({blob:await fs.readFile(path.join(ROOT,'reference',file)),contentType:'image/png',fit:'contain',alt:title,position:{left:55,top:172,width:1490,height:675}});
}
await fs.mkdir(B,{recursive:true});await fs.mkdir(OUT,{recursive:true});
await (await PresentationFile.exportPptx(p)).save(path.join(B,'candidate.pptx'));
await fs.writeFile(path.join(B,'deck.proto.json'),JSON.stringify(p.toProto()));
for(let i=0;i<p.slides.items.length;i++){
 const s=p.slides.items[i];const img=await p.export({slide:s,format:'png',scale:1});await fs.writeFile(path.join(B,`slide-${i+1}.png`),new Uint8Array(await img.arrayBuffer()));
}
const result=await finalizePresentation({workspaceDir:ROOT,candidatePath:path.join(B,'candidate.pptx'),finalPath:path.join(OUT,'ATM_Qualification_Process_Maps_v4.pptx'),pythonExecutable:process.env.CODEX_PRIMARY_RUNTIME_PYTHON,integrityValidatorPath:'/root/.codex/skills/builtins/presentations/container_tools/inspect_presentation_package_integrity.py',layoutValidatorPath:'/root/.codex/skills/builtins/presentations/container_tools/inspect_presentation_layout_geometry.py',layoutArgs:['--expected-slide-size-emu','15240000,8572500','--validate-heading-fit'],fontPolicy:{basis:'design',families:['Carlito']},requiredNativeTableOwnerSlides:[],verifyArtifactToolImport:true,receiptPath:path.join(B,'validation-v4.json')});
console.log(JSON.stringify(result));
// Portrait process figures for the procedure; editable source kept with the deck builder.
const q=Presentation.create({slideSize:{width:700,height:930}});
function figure(title){const s=q.slides.add();s.background.fill=C.white;text(s,title,20,8,660,50,29,true);return s;}
{
 const s=figure('Training and certification flow');
 const a=box(s,'1  Verify prerequisites\nSupplier status, controlled documents,\nqualified trainer/inspector and attribution',25,82,460,105,C.blue,23);
 const b=box(s,'2  Training Phase\nTissue expert demonstrates and coaches\nOperations Supervisor supports',25,224,460,105,C.green,23);
 const c=box(s,'3  Ready for Monitoring?\nTrainer and inspector record sign-off',25,370,460,83,C.white,23);
 const d=box(s,'4  Monitoring Phase\nTrainee works; inspector checks each unit\nRecord first result and named trainee',25,498,460,110,C.green,23);
 const e=box(s,'5  Personnel certification gate\n≥95% first-pass yield; ≥30 units\n≥2 consecutive harvest days',25,651,460,104,C.white,23);
 const f=box(s,'6  Certify and record\nSupplier Engineer signs 800082 and log\nThen assess component qualification',25,804,460,105,C.green,23);
 link(s,a,b);link(s,b,c);link(s,c,d);link(s,d,e);link(s,e,f);
 text(s,'Not ready:\nreturn to\nTraining Phase',510,355,175,114,22,true,C.red);
 text(s,'Yes',300,459,100,30,20);text(s,'Pass',300,765,100,30,20);
 text(s,'Not met:\ncontinue controlled\nmonitoring or\nshadow training\n(see next map)',510,643,175,168,22,true,C.red);
}
{
 const s=figure('Low yield response and recovery');
 const a=box(s,'1  Yield below 95%\nFlag result, contain nonconforming output\nSupplier Engineer and Quality review',25,82,460,105,C.blue,23);
 const b=box(s,'2  Recurrence criterion met?\nApply approved count and review window',25,224,460,90,C.white,23);
 const c=box(s,'3  Inspector shadows harvesting technician\nReinforces training and inspects output\nRecords causes and coached units',25,361,460,115,C.green,23);
 const d=box(s,'4  Fresh monitoring after retraining\nUnassisted task execution; inspect every unit\n≥95% yield / ≥30 units / ≥2 harvest days',25,524,460,115,C.green,23);
 const e=box(s,'5  Recovery evidence acceptable?\nSupplier Engineer reviews all evidence',25,687,460,85,C.white,23);
 const f=box(s,'6  Quality authorizes routine work\nUpdate certification and records\nIndependent inspection continues',25,812,460,103,C.blue,23);
 link(s,a,b);link(s,b,c);link(s,c,d);link(s,d,e);link(s,e,f);
 text(s,'No: review cause\nand keep trend\nunder review',507,209,175,105,22);
 text(s,'Yes',300,321,100,30,20);text(s,'Yes',300,779,100,30,20);
 text(s,'No: maintain\nmonitoring controls\nand repeat training\nor correct process',507,665,175,142,22,true,C.red);
 text(s,'Receipt-only gap:\ncheck handling,\nfreezing and\ntransport.',507,388,175,156,22);
}
for(let i=0;i<q.slides.items.length;i++){const img=await q.export({slide:q.slides.items[i],format:'png',scale:2});await fs.writeFile(path.join(B,`procedure-map-${i+1}.png`),new Uint8Array(await img.arrayBuffer()));}
await fs.writeFile(path.join(B,'procedure-maps.proto.json'),JSON.stringify(q.toProto()));
console.log('Deck and procedure figures built');
