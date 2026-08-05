# Excel Grapher

A single-file HTML app that turns any Excel spreadsheet into charts. Open
`index.html` in a browser, drop in a workbook, and the app asks what should be
graphed — pick the sheet, the X axis, and the data sets (columns), then choose a
chart type.

## Using it

1. Open `index.html` in any modern browser (double-clicking the file works).
2. Drag a spreadsheet onto the drop zone, or click it to browse.
   Supported: `.xlsx`, `.xlsm`, `.xls`, `.csv`, `.tsv`.
3. In **"What should be graphed?"** pick:
   - the **sheet** (when the workbook has more than one),
   - the **X axis** column (dates, categories, numbers, or plain row number),
   - the **data sets** — any numeric columns, up to 8 at once,
   - the **chart type**: line, area, bar, stacked bar, horizontal bar, or scatter.
4. A chart appears immediately and re-draws as you change selections.

`sample-data.xlsx` is included to try it out — a "Monthly Sales" sheet for
line/bar charts and an "Ad Performance" sheet for scatter plots.

## Features

- **Reads real Excel files** in the browser via [SheetJS](https://sheetjs.com);
  nothing is uploaded anywhere — the file never leaves your computer.
- **Header detection** — guesses whether the first row is column names, with a
  toggle to override.
- **Hover & keyboard details** — a crosshair tooltip lists every selected series
  at that point (arrow keys step through values); bars and scatter points have
  generous hit targets, so you never have to land on a 2px mark.
- **Table view** — every chart has a table twin, so all values are readable
  without hovering.
- **Light & dark theme** — follows the OS setting, with a manual toggle.
- **Download SVG** — exports the current chart as a standalone `.svg` file.

## Design notes

Charts follow a colorblind-validated eight-color palette (separately stepped for
light and dark surfaces), with thin marks, hairline gridlines, and surface gaps
between touching bars. Series colors stick to their column while selected, so
unchecking one series never recolors the others. Scatter plots cap at 3 series —
past that, the palette can't keep every pairwise combination distinguishable for
color-blind readers.

The only external dependency is the SheetJS script tag, loaded from
`cdn.sheetjs.com` — the first page load needs an internet connection; the chart
rendering itself is dependency-free inline SVG.
