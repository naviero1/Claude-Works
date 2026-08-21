const pptxgen = require('pptxgenjs');
const { makeHelpers } = require('./deck_lib');
const path = require('path');

const pres = new pptxgen();
pres.layout = 'LAYOUT_WIDE';
pres.author = 'Training Team';
pres.title = 'From Prompts to Agents — Prompt Engineering for Generative & Agentic AI';

const H = makeHelpers(pres);
require('./deck_pt1')(pres, H); // Part I   — primer: history & core concepts
require('./deck_pt2')(pres, H); // Part II  — models & tools landscape
require('./deck_pt3')(pres, H); // Part III+IV — prompt engineering + applied playbook
require('./deck_pt4')(pres, H); // Part V+VI — agentic prompting + prompt management
require('./deck_close')(pres, H); // wrap-up, exercises, glossary, sources, reading

const out = path.join(__dirname, '..', 'deliverables', 'From_Prompts_to_Agents_Training.pptx');
pres.writeFile({ fileName: out }).then(() => console.log('deck written:', out));
