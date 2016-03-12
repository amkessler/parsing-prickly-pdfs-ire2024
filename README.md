# [bit.ly/parsing-prickly-pdfs](https://bit.ly/parsing-prickly-pdfs)


Resources and worksheet for the NICAR 2016 workshop of the same name. Instructors: [Jacob Fenton](https://github.com/jsfenfen) ([jsfenfen@gmail.com](mailto:jsfenfen@gmail.com)) and [Jeremy Singer-Vine](https://github.com/jsvine) ([jsvine@gmail.com](mailto:jsvine@gmail.com)).

## What We'll Cover

- [The One Weird Thing You Need To Know About PDFs](#the-one-weird-thing-you-need-to-know-about-pdfs)
- [Splitting, Merging, and Rotating PDFs](#splitting-merging-and-rotating-pdfs)
- [Optical Character Recognition](#optical-character-recognition)
- [Extracting Structured Data From PDFs](#extracting-structured-data-from-pdfs) 
- [Additional Resources](#additional-resources)


## The One Weird Thing You Need To Know About PDFs

- It's a print format--the point is to tell a printer what things to print where. There's not much more order than that. But for our purposes we'll talk about three types of PDFs:
	
	- "Text-based PDFs": The document has characters, fonts and font sizes, and information about where to place them stored in the document in a format that (a program) can read. Created by programs that can save to pdf directly. Dragging the mouse will highlight text.
	
	- "Image-based PDFs": The document has images of pages, but not words themselves. Typically the result of scanning. You can't highlight text.
	
	- "Embedded-text PDFs": The document has images of pages, but there's invisible text 'attached' to the document, so you can select text. Typically created by scanners that also run OCR. Sticky wicket: should you assume the attached text is better than what you'd get by running tesseract? Not necessarily (but it probably is...)

## Splitting, Merging, and Rotating PDFs

It's easy enough to split/merge/rotate documents in your favorite PDF viewer. But when you've got a giant batch of PDFs, or want to perform a complex manipulation, command-line tools are handy. A couple of free tools and libraries:

### Coherent PDF / `cpdf`

- [Homepage](http://www.coherentpdf.com/)
- [User guide](http://www.coherentpdf.com/cpdfmanual.pdf)
- Example usage:
    - `cpdf -split original.pdf -o original-split-%%%.pdf -chunk 10`. Splits `original.pdf` into 10-page chunks, titled `original-split-000.pdf`, `original-split-001.pdf`, and so on.
    - `cpdf -merge original-split-*.pdf -o original-merged.pdf`. Rejoins all PDFs matching the pattern `original-split-*.pdf` into a single file.
    - `cpdf -rotateby 90 original.pdf 2-5,12-15 -o original-rotated.pdf`. Rotates pages 2-5 and 12-15 by 90 degrees clockwise.

### PDFtk

- [Homepage](https://www.pdflabs.com/tools/pdftk-server/)
- [User guide](https://www.pdflabs.com/docs/pdftk-man-page/). On Mac OS 10.11 see [here](http://stackoverflow.com/a/33248310).
- Example usage:
    - `pdftk original.pdf burst output original-split-%023.pdf`. Splits `original.pdf` into single-page PDFs, titled `original-split-000.pdf`, `original-split-001.pdf`, and so on.
    - `pdftk original-split-*.pdf cat output original-merged.pdf`. Rejoins all PDFs matching the pattern `original-split-*.pdf` into a single file.
    - `pdftk original.pdf cat 1 2-5right 6-11 12-15right 15-end output original-rotated.pdf`. Rotates pages 2-5 and 12-15 by 90 degrees clockwise.
    - `pdftk infile.pdf cat 1 output output_p1.pdf`. Puts just the first page in output_p1.pdf. Use `cat 2-4` to put pages 2 through 4, for example.

## Optical Character Recognition

Optical Character Recognition (OCR) tools try to extract text from image-based PDFs. Depending on the software, the tool may either (a) convert your image-based PDF into an embedded-text PDF, or (b) simply output the text it has found. Some popular options:

### GUI (Free)

- [DocumentCloud](https://www.documentcloud.org/home) (if you're willing to wait in queue)
- [Overview](https://blog.overviewdocs.com/author/overview/) will now give you searchable pdfs back.
- [CometDocs](https://www.cometdocs.com/user/subscriptions) (web-based, [freemium](https://www.cometdocs.com/user/subscriptions))


### GUI (Paid)

- [ABBYY Fine Reader](http://www.abbyy.com/finereader/) ($120 Mac / $170 Windows). Here's a [scanned doc](examples/klamath_elex/2010NovPrecinct.pdf) released by an Oregon county gov; it's [much better](examples/klamath_elex/2010NovPrecinct_scanned.pdf) with abby. 
- [Adobe Acrobat DC](https://acrobat.adobe.com/us/en/how-to/ocr-software-convert-pdf-to-text.html) (free trial / $15/mo / $450 purchase)
- [Cogniview PDF2XL](https://www.cogniview.com/) Windows only. Free trial. OCR edition: $299; "Enterprise":$399.
- [Datawatch Monarch](http://www.datawatch.com/monarch13/) Specialty tool for structured data extraction; dunno if OCR is included. Free "personal" edition with 'limited imports and exports'; 30-day free trial for enterprise edition. They [claim](http://finance.yahoo.com/news/datawatch-makes-everyone-big-data-131101026.html)  Classic Edition ($895 per user per year) and Complete Edition ($1,595 per user per year).  

- [Abby Flexicapture](http://www.abbyy.com/flexicapture/).  Believe that Abby charges less in other countries, and there's an industry of document conversion services in other countries. Price varies by country. (~ $24K) 


### Command-Line

- [Tesseract](https://github.com/tesseract-ocr/tesseract/wiki)
- Description: Tesseract is free / open source OCR software originally developed by HP, now by Google.  Support for many languages is available. In general the quality is lower than paid OCR, but it's great for processing giant volumes of documents when desktop processing isn't feasible. 
- Installation: See homepage. On Macs, can use `brew install tesseract` ; on Ubuntu try `sudo apt-get install tesseract-ocr tesseract-ocr-eng `.
- Example usage: 
	- 	`tesseract imagefile.png convertedimage` will extract English text from convertedimage.txt. 
	-	`tesseract imagefile.png convertedimage /path/to/configfile` will run the conversion with options specified in the configfile; one useful option (see simple [configfile](/examples/WFLX/configfile) )is making it output in the [hOCR](https://docs.google.com/document/d/1QQnIQtvdAC_8n92-LhwPcjtAUFwBlzE8EWnKAxlgVf0/preview) format, which includes bounding boxes.  
	- `tesseract imagefile.png image_pdf_with_embedded_text pdf` will OCR imagefile.png and create a new pdf file called image_pdf_with_embedded_text.pdf that has text embedded in it (aka it's a searchable pdf). This is only available in v 3.03 and higher. 


## Extracting Structured Data From PDFs

### Tabula

Tabula helps you extract data tables from PDFs. It's free and open-source, and uses an intuitive graphical interface.

- [Homepage](http://tabula.technology/)
- Installation: Follow directions on [homepage](http://tabula.technology/)
- [Usage](https://github.com/tabulapdf/tabula#using-tabula)




### pdftotext

`pdftotext` is the simplest way to convert a PDF to raw text.

- Installation: `brew install poppler` (OSX) / `sudo apt-get install poppler-utils` (Ubuntu) 
- Tips:
	- Can help to use -f [first page] and -l [last page] to split a long document into more readable pieces (which can be parsed in order later.) 
    - It's usually best to use the `-layout` flag to make `pdftotext` use whitespace to approximate the document's physical layout. This does a decent job of approximating linebreaks, though multi-column text can mess things up.
    - In combination with regular expressions, you can parse surprisingly complex documents.
    - Newish versions have a 
 	- The `-bbox` option spits out *word-level* bounding box information, but not fonts. This is a quick-and-dirty way to pull this info for scanned documents (where the fonts probably aren't that reliable anyways) 

### pdftohtml

`pdftohtml` comes from the same [Poppler suite of tools](https://poppler.freedesktop.org/) as `pdftotext`.

- [Homepage](http://linux.die.net/man/1/pdftohtml)
- Installation: `brew install poppler` (OSX) / `sudo apt-get install poppler-utils` (Ubuntu) 
- Tips:
    - Use the `-xml` flag to include location information for text blocks (i.e. the number of pixels to the top of the page and to the left of the page; the width and height of the text box; the font face and size can be figured out from the styling). This can be especially helpful when each cell of a chart is represented as a text block.
    - You can parse the result like you'd parse any other HTML/XML document. ([Example](http://nbviewer.jupyter.org/github/buzzfeednews/2015-02-georgia-cpa-scores/blob/master/notebooks/georgia-cpa-scores.ipynb).)
    - The `-c` option creates .html pages — one for each page — which can come in handy for dead-simple display. It's not quite as useful as the `-xml` output for analysis; it includes the distance to the top and left of the page, but omits the text block width and height.

### tabula-java

`tabula-java` is the Java library underpinning Tabula, and command-line tool that lets you automate table-extraction.

- [Homepage](https://github.com/tabulapdf/tabula-java)
- Requirements: `java` and [`mvn`](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
- [Installation and usage](https://github.com/tabulapdf/tabula-java#build-instructions)

### PDFPlumber

PDFPlumber is a Python library and command-line tool for extracting information from PDFs. Both tools provide granular information about each character, rectangle, and line. The library also has Tabula-style features for extracting tables and text.

- [Homepage](https://github.com/jsvine/pdfplumber)
- Requirements: `python` and [`pip`](https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip)
- Installation: `pip install pdfplumber`



### Structured information from Tesseract
 

#### Preprocessing

This is the simplified version: see full details in the [examples/WFLX](examples/WFLX/README.md) dir.

Tesseract operates on image files, so you'll need to convert pdfs to images first. The simplest way is probably to use imagemagick. For installation see [here](http://www.imagemagick.org/script/binary-releases.php).

For [examples/WFLX/sample_contract.pdf](examples/WFLX/sample_contract.pdf), convert the first page with: `convert -density 300 ./sample_contract.pdf[1] ./sample_contract_p1.png` ; the result is [here](examples/WFLX/sample_contract_p1.png). 

#### Get structured info from that file


Pay attention to tesseract versions. 3.04 is current; 3.01 is needed for bounding box stuff. 

Run tesseract with [this one-line config](examples/WFLX/configfile) file, which tells it to output files in the hOCR format. `tesseract sample_contract_p1.png p1_hocr ./configfile`.


There's a hack [here](https://github.com/jsfenfen/python-hocr) to convert the resulting file [examples/WFLX/p1_hocr.hocr](examples/WFLX/p1_hocr.hocr) to csv.

`$ python convert_hocr.py examples/WFLX/p1_hocr.hocr examples/WFLX/p1_hocr.csv`

The output will be [examples/WFLX/p1_hocr.csv](examples/WFLX/p1_hocr.csv) which has word level bounding boxes. 

### This is starting to look a lot like 'regular' PDF

With a little bit of tooling, we've managed to make image-based PDFs look like regular PDFs: a csv (or json file) of words and their bounding boxes. This is pretty significant because we can use the same strategy to parse image-based pdfs as text-based PDFs, with a few caveats:

1. The font / fontsize information isn't available
2. Lower text quality requires more fuzzy matching
3. Alignment / image quality issues loom larger

### The longer view: making it visual

What do you do with bounding box data. You can stare at it in Excel (I have) but it's easier to understand visually. This is a bit of a larger project I'm working on that just reads the .pdf and .hocr files.

Link to [stripped down viewer](http://jacobfenton.s3.amazonaws.com/demos/pdfs/disembodied_viewer.html). 

### VAPORWARE ALERT

That viewer is just part of a project I'm doing to allow the extraction of structured data from repetitive pdfs.  There are always limits to this stuff, but you can be smart about handling them. 

The viewer just shows a single document, but a web-app backed version of this has a database, so it can show you  every position that the word 'contract' appears on a page, or every page where the word 'contract' appears at the top in the middle. 

If this is something that's of interest to you, sign up here to get [notified](https://docs.google.com/forms/d/1YbZlP8dPZnoUcuIX8-x30BVVxNQxNThUwfN1IgZuCvc/viewform?edit_requested=true) about this project: bit.ly/whatwordwhere -- I'll be beta testing in a month or so. 

 

## Additional Resources


### More REGEXes:

Freefcc includes pdf parsers for about [14 broadcast tv stations](https://github.com/jsfenfen/freefcc/tree/master/scraper/parsers). One way to do it is [lotsa regexes](https://github.com/jsfenfen/freefcc/blob/master/scraper/parsers/KYW-TV/capture_formats.py).


Sunlightlabs' U.S. House [Disbursements parser](https://github.com/sunlightlabs/disbursements); Senate disbursements [parser](https://github.com/sunlightlabs/senate_disbursements/blob/master/114_sdoc7/read_pages.py). 

### PDF liberation hackathon
Yes, there actually was one. 
[github](https://github.com/pdfliberation), [web](https://pdfliberation.wordpress.com/)


### Handwritten forms

Handwriting is a whole different beast. Abby finereader does ok with it--but don't count it for accuracy. 

- [Captricity](https://captricity.com/) Will do document conversions of handwritten stuff for lots of money. Former Code for America folks--ask them for a discount. Gives (or gave?) a break to nonprofits. 

### Academics

You may hear that OCR is a 'solved' problem in the computer science domain (although there are some implementation details that can improved).

There is also work being done in 'layout analysis', and groups like [UMD's language and media processing lab](http://lamp.cfar.umd.edu/media/projects/index.html) do weird research into documents. Papers on the sexy stuff in this field are showcased yearly at the [International Conference on Document Analysis and Recognition](http://lampsrv02.umiacs.umd.edu/projdb/project.php) (in Johannesburg for 2016). UMD's David Doerman now at [DARPA](http://www.darpa.mil/staff/dr-david-doermann) ?

### Tessaract bindings

Check these out; YMMV.  

[https://github.com/jflesch/pyocr](https://github.com/jflesch/pyocr)

[https://github.com/meh/ruby-tesseract-ocr](https://github.com/meh/ruby-tesseract-ocr)

[https://pypi.python.org/pypi/pytesseract](https://pypi.python.org/pypi/pytesseract)

Node:
[https://github.com/creatale/node-dv](https://github.com/creatale/node-dv) which is supposed to work with this form extraction thing: [https://github.com/creatale/node-fv](https://github.com/creatale/node-fv)



 
