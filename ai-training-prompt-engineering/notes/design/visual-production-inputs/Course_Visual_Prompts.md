# From Prompts to Agents — visual production prompts

Prepared by Beebop • 18 September 2026

One Gemini illustration and ten source-based or editable visuals for the first four parts of the course. Slide numbers refer to the original 103-slide baseline; match by title after insertions. These prompts produce review candidates. They do not authorize changes beyond the currently approved slide additions and relocations.

## Shared production requirements

- Preserve the owner-approved treatments, including slide 34 version A, and leave slides 37 and 87 as the owner requested. Keep the existing illustrations on the three restored evidence slides.
- For generated artwork, use off-white #F7F8F6, teal #0E7C7B, charcoal #232A31 and a restrained amber accent. For native diagrams, follow the current deck’s font families and visual hierarchy. Do not recolor an actual application screenshot to imitate the illustration palette.
- Produce separate review assets before inserting anything into the deck. Native diagrams and tables stay editable. Charts stay linked to their actual spreadsheet ranges. Screenshot previews are additional assets, not replacements for the source files.
- If a required source is missing, identify it. Do not synthesize a plausible substitute, fabricate an application interface or reconstruct numerical evidence from memory.
- At the intended display size, every field needed for the lesson must be readable. Crop tightly, preserve aspect ratio and never stretch. Keep an uncropped source reference and record the source filename, sheet/range or page, version and relevant filter state.
- Reveal answer-bearing examples after the participant attempt or as explicitly identified prepared demonstrations.
- Preview dimensions below are production targets. Export at that size without distorting content; retain the editable original where required.

## 1. ASK versus DELEGATE — Gemini prompt for Oscar

**Target:** slide 2, “One skill, two ways to work.”

**Purpose:** distinguish requesting an answer from assigning bounded work, while showing human review in both.

**Placement:** lower half, left scene under ASK and right scene under DELEGATE. Keep the existing slide headings editable.

**Output:** 2400 × 600 pixels, 4:1. Save as `S02_Ask_Delegate_v01.png`.

**Copy-ready prompt:**

> Create one wide editorial illustration for a professional workplace training presentation, 2400 by 600 pixels, aspect ratio 4:1. Use a clean flat vector style, soft off-white background #F7F8F6, teal #0E7C7B, charcoal #232A31 and a very small warm amber accent. Show two clearly separated scenes with generous empty space between them and approximately equal visual weight. Left scene: a professional asks a friendly robot assistant a question, receives a single plain response sheet and examines the answer. Right scene: the same professional hands the same robot a bounded work order; the robot prepares a spreadsheet-like document and presentation-like document at a small desk; the professional reviews the completed files. Make receiving an answer versus delegating a piece of work immediately distinguishable. Human review must be visible in both scenes. Use a restrained, adult, professional style with simple expressive figures and few objects. Keep all essential objects inside an eight-percent safe margin. No text, letters, numbers, logos, watermarks, arrows, decorative badges or intricate software interfaces. No autonomous robot running a business, no magical effects and no busy office background. The image must remain understandable when displayed about two inches tall.

**Acceptance:** two distinct scenes; consistent person and robot; human review in both; no lettering; no fake evidence; clear at slide size.

**Return:** upload the original image to the existing AI training Drive folder: https://drive.google.com/drive/folders/1PYsgL1fVmw1CV92xLh10jjhwAhRrxTDC . Beebop reviews the candidate before placement. It does not block the current slide-location corrections.

## 2. How an answer is produced — Rocksteady production prompt

**Target:** slide 7, “How a language model produces an answer.”

**Source:** current slide wording and its notes. **Format:** editable diagram; 2400 × 900 preview. **Placement:** lower middle, above the takeaway.

> Create a compact editable diagram that supports the current slide’s explanation. Show the trained model carrying learned patterns, with the supplied task and source material entering as current inputs. Show the resulting response. Place the human’s source check outside the model and visibly after the response; make it possible to return a correction to the task. Preserve the slide’s terminology and qualifications. Do not imply that training knowledge is a retrieved document, that the model can inspect inaccessible files, or that a response is automatically validated. Use simple shapes and short editable labels. Match the course fonts and restrained teal/charcoal styling. Deliver the editable diagram and a preview named S07_Answer_And_Check_v01.png. Check that input, model output and external verification are distinguishable without narration.

## 3. Preserve the condition — Rocksteady production prompt

**Target:** slide 14, “Verification belongs in the task.”

**Source:** the exact existing example and its supporting message, where supplied. **Format:** editable excerpt/conclusion comparison; 2400 × 1000 preview. **Placement:** within the existing example area.

> Make the verification habit visible using the exact source wording and qualified conclusion already used on this slide. Highlight the approval condition in the source and connect it to the matching qualification in the conclusion. Preserve wording, names, dates and limitations. Use a restrained highlight rather than another decorative illustration or statistical chart. If the underlying message is unavailable, label the existing slide example as illustrative; do not pretend it is a captured email. The restored hallucination examples will precede this slide, so this visual should teach the corrective action. Deliver editable text and annotation objects plus S14_Preserve_The_Condition_v01.png. Confirm the condition has not disappeared or become an unconditional approval.

## 4. See the double-counting trap — Rocksteady production prompt

**Target:** slide 29, “One task through the improvement loop.”

**Source:** `Supplier_Data_Exercise.xlsx`, including its existing TOTAL row. **Format:** authentic crop with editable annotations; 2000 × 1200 preview. **Placement:** beside the observed problem and revision in a proposed layout.

> Open the current participant data workbook. Capture a few relevant detail rows together with the existing TOTAL row and the column headings needed to understand the calculation. If those rows are nonadjacent, use clearly labeled separate crops instead of silently implying adjacency. Add an editable bracket identifying the detail records used for analysis, and a separate callout explaining that the source total is a reconciliation check, not another detail record. Preserve all displayed values. Do not include answer-key sheets or an unreadably small full-workbook screenshot. Deliver S29_Total_Row_Check_v01.png, the annotation source, and the exact sheet/ranges captured. Confirm that the illustrated calculation excludes the total row.

## 5. Show the returned Excel charts — Rocksteady production prompt

**Target:** slide 36, “Add the Charts and Return the Excel File.”

**Source:** `Supplier_Data_Analyzed.xlsx` and the current exercise definitions. **Format:** native Excel charts plus a 2560 × 1440 review capture. **Placement:** prepared full-screen workbook demonstration; a still requires a legible approved layout.

> Open the current analyzed supplier workbook and prepare a clean view of its actual supplier-comparison chart and monthly trend. Keep both charts native and editable, with valid source ranges. Display the reporting period, units and relevant metric definition. Exclude the existing source total from detail calculations; retain the agreed missing-data treatment. Calculate rates from the appropriate sums and denominators, keep defect and return measures separate, and do not label an unweighted mean of monthly on-time percentages as a true overall delivery rate. Show one chart’s source range during the demonstration. Reconcile the displayed values to the source. Deliver the actual workbook view, S36_Excel_Charts_v01.png and a short record of the chart ranges and calculations. Do not shrink two charts into an unreadable corner of the prompt slide.

## 6. Show one consistent dashboard scope — Rocksteady production prompt

**Target:** slide 38, “Build and Test the Dashboard.”

**Source:** the current prepared supplier dashboard and its underlying exercise records. **Format:** actual browser capture, approximately 2400 × 1200. **Placement:** large lower area or full-screen demonstration. Leave slide 37 unchanged.

> Open the actual supplier dashboard. Apply the exercise’s Berlin site, Bravo Plastics supplier and March–August 2026 date selection. Verify the selected period and all displayed calculations against the workbook before capturing. Frame the selected controls, summary values, trend and enough underlying records to show that all views use the same scope. Preserve the snapshot label and metric units. Use the real application, with no generated interface or altered values. Crop browser chrome only when it does not remove relevant context. Deliver S38_Dashboard_Filtered_v01.png with its exact filter state, dashboard version and reconciliation result. If all elements cannot remain readable in one capture, use a full-screen demo and two labeled detail crops.

## 7. Show the management story — Rocksteady production prompt

**Target:** slide 39, “Turn the Findings into a Five-Slide Management Mock-up.”

**Source:** `Supplier_Quality_Mock_Presentation.pptx`. **Format:** five actual slide renders, one contact sheet and one full-size example. **Placement:** prepared presentation demonstration.

> Render the five slides of the current supplier management presentation in their actual order. Create a clean contact sheet that shows the business question, comparison, trend, follow-up and limitations. Label order outside the slide images with editable captions if necessary. Also provide the key comparison slide at full size, because the contact sheet explains the story’s sequence rather than making every chart readable. Preserve all findings, notes, sources and limitations in the original deck. Reconcile its numerical story to the same workbook and dashboard period. Deliver S39_Management_Story_v01.png at 3000 × 1800 and S39_Management_Example_v01.png at the deck’s native aspect ratio, at least 1920 pixels wide. Do not invent improved results or replace observed findings with recommendations.

## 8. Turn the email thread into action — Rocksteady production prompt

**Target:** slide 41, “Outlook Exercise: Decisions, Actions, and Open Questions.”

**Source:** the supplied fictional thread and verified answer key. **Format:** editable excerpt and table; 2400 × 1200 preview. **Placement:** lower available space, revealed after the attempt. Retain slide 40’s prompt choices.

> Select a short passage from the supplied fictional email thread that includes the changed deadline or approval condition. Place it beside an editable output showing one confirmed decision and two action rows. Include task, owner, current due date, status, dependency and supporting message. Use “Not stated” where the thread does not supply a value. Preserve the difference between proposals, conditional approval and commitments; flag the inaccessible attachment if relevant to the selected actions. Keep original and revised deadlines distinguishable. Do not fabricate an Outlook interface. Deliver S41_Email_To_Actions_v01.png and the editable source. Verify every row against the supporting sender/date or message identifier.

## 9. Extract a quotation faithfully — Rocksteady production prompt

**Target:** slide 42, “Extract Supplier Quotes into Excel.”

**Source:** one of the supplied quotation documents and its corresponding prepared extraction row. **Format:** real document crop plus native spreadsheet row; 2400 × 1200 preview. **Placement:** lower blank area after participant work.

> Choose one supplied supplier quotation with a useful combination of stated and missing commercial terms. Capture only the relevant passage, retaining its page identity. Place the actual matching extraction row beside it. Include a small readable selection of fields such as item, quantity basis, price, currency, lead time and source page. Preserve original units and literal terms; mark missing information explicitly. Keep extraction distinct from normalization. Do not add a fabricated supplier logo or guessed term. Deliver S42_Quote_To_Row_v01.png, the native spreadsheet row and the exact source filename/page. Confirm each populated field is supported by the displayed source or an explicitly identified continuation passage.

## 10. Make quotes comparable — Rocksteady production prompt

**Target:** slide 43, “Normalize and Compare the Supplier Quotes.”

**Source:** the current extracted quotation workbook, original quotation files and exercise comparison rules. **Format:** native comparison table; 2400 × 1200 preview. **Placement:** lower blank area after the extraction example.

> Create a focused native comparison table using the same quoted fields shown in the preceding extraction example. Keep original quantity and price bases separate from normalized comparison fields. Show conversion rules and cost components only when supported by the source and agreed comparison basis. Make missing freight, tooling, minimum quantities or other material terms visible where they actually occur; do not assume all quotes contain these terms. Use “Not stated” or a clearly qualified scenario when necessary. Avoid a winner ranking or cost bar chart if scope is not comparable. Deliver S43_Quote_Normalization_v01.png and the formula-bearing workbook range. Verify conversions, currencies and assumptions against each source page.

## 11. Trace research back to its source — Rocksteady production prompt

**Target:** slide 44, “Turn Reference Files into a Research Spreadsheet.”

**Source:** the supplied research/reference pack and its prepared workbook. **Format:** authentic source crop linked to an editable evidence row; 2400 × 1350 preview. **Placement:** prepared demonstration; embedded still only after a legible layout is agreed.

> Choose one short claim or instruction from a supplied research source. Show the actual passage beside the corresponding Evidence row, including source identifier, exact page or section, claim/instruction, supporting evidence and caveat. Show how that row is referenced from Synthesis and retained in Sources. For procedural material, preserve the source’s sequence and distinguish an instruction from a research finding. Keep quotation separate from paraphrase. Do not invent citations, silently remove qualifications or imply that an inaccessible page was reviewed. Deliver S44_Source_To_Evidence_v01.png, the editable workbook range and exact source location. Verify a reviewer can trace the displayed synthesis statement back to the supplied passage.

## Delivery responsibilities

- Oscar: generate the single Gemini candidate and upload it to the standing image folder. The other visuals require no image-generation work from Oscar.
- Beebop: select and review candidates at their intended slide size, check source fidelity and assess whether they teach the stated idea.
- Rocksteady: use the ten production prompts to prepare authentic or editable visual candidates when that visual work is authorized; keep the current insertion/relocation task separate. Report actual created files and missing sources, not merely intended filenames.

Existing illustrations on the restored hallucination, public-failure and flattery-bias slides are reused. No replacement-image prompts are needed for them or the two new model-selection tables.
