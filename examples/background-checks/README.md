# Example: NICS Firearm Background Checks

The [PDF in this example](background-checks.pdf) is one page of a report from the [FBI's National Instant Criminal Background Check System](https://www.fbi.gov/about-us/cjis/nics).

## Outputs

In rough, decreasing order of novice-friendliness:

### abbyy-finereader-output.xlsx

- Open ABBY FineReader

- Select *New Task*, then *Convert to Excel Spreadsheet*


### tabula-output.csv

- Open Tabula
- Import PDF
- Drag selection box from just above "State / Territory" to the final row of the table.
- Click "Preview & Export Extracted Data"
- Under "Choose Alternate Extraction Method", select "Stream"
- Click "Export"

### pdftotext-output.txt

```sh
pdftotext background-checks.pdf - > pdftotext-output.txt
```

### pdftotext-bbox-output.html

```sh
pdftotext -bbox -layout background-checks.pdf - > pdftotext-bbox-output.html
```

### pdftohtml-xml-output.xml

```sh
pdftohtml background-checks.pdf -xml -stdout > pdftohtml-xml-output.xml
```

### pdfplumber-cli-output.csv

```sh
pdfplumber < background-checks.pdf > pdfplumber-cli-output.csv
```

### pdfplumber-script-output.tsv

```sh
python pdfplumber-script.py background-checks.pdf > pdfplumber-script-output.tsv
```

See also: [A similar example, in Jupyter Notebook form.](https://github.com/jsvine/pdfplumber/blob/master/examples/notebooks/extract-table-nics.ipynb)
