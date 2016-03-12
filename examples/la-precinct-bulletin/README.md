# Example: Los Angeles Precinct Bulletin

The [PDF in this example](2014-bulletin-first-10-pages.pdf) represents the first 10 pages of the Los Angeles County's [precinct-by-precinct results for the 2014 general election](http://lavote.net/home/voting-elections/election-resources/past-elections/past-election-results#Nov42014). The data is not quite tabular. You could use a number of strategies to extract the data — e.g., `pdftotext -xml`. The [Jupyter notebook in this directory](la-precinct-bulletin.ipynb) uses `pdfplumber` and `pandas`.
