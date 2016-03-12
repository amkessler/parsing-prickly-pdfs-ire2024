## Simplest case: regexes

This is a super-simple example of parsing the output of pdftotext -layout with regular expressions. Because the table is so simple it's not hard to do. There are only a few tables of a few pages each, but this would work equally well with 1,000 pages. This command created the files:

	pdftotext -layout pdfs/2015-2016-dma-ranks.pdf txts/2015-2016-dma-ranks.txt


The python script read_dma_ranks.py does the work, i.e. `python read_dma_ranks.py`

I [once used regexes](https://sunlightfoundation.com/blog/2014/08/05/now-its-easier-to-account-for-how-the-senate-spends-your-money/) to parse the Senate expenditure reports, which are about 2000 pages formatted like it's 1920.


## Tabula

This can also be done by scripting tabula (make sure you've gotten stuff installed right, as described [here](https://github.com/tabulapdf/tabula-java/). It's not clear on that page, but you need [apache maven installed](https://maven.apache.org/install.html) to run `mvn`)
	
We can't use the whole page, instead set the area explicitly using --area(top,left,bottom,right)

	java -jar /path/to/tabula/target/tabula-0.8.0-jar-with-dependencies.jar --pages 1 --area 200,10,720.5,610 2015-2016-dma-ranks-asian.pdf > region.csv
	
This requires us to *know* what the region is; sometimes the best way is just to detect it. 

Because there was just one page to run, we cheated by spitting out the bounding boxes in the doc with: 

`pdftotext -bbox 2015-2016-dma-ranks-asian.pdf` 

and just eyeballing the output. Note that the pages are so consistent we can use the same areas on each page to get a table for all the data (although it contains 4 copies of the header row)

	java -jar /path/to/tabula/target/tabula-0.8.0-jar-with-dependencies.jar --pages 1-4 --area 200,10,720.5,610 2015-2016-dma-ranks-asian.pdf > region.csv
