import csv, re
from os import sys, path

line_re = re.compile("\s+(\d+)\s{2,}(.+?)\s{3,}([\d,]+)\s{2,}([\d\.]+)\n")

# write the file data row to the first line of the output file

for thisfile in ['', '-hispanic', '-black', '-asian']:

    
    filename = 'txts/2015-2016-dma-ranks' + thisfile + '.txt'
    print "Reading file %s" % (filename)
    outfile = open('dma_read' + thisfile + '.csv', 'w')

    dw = csv.writer(outfile)
    dw.writerow(['rank','dma', 'households', 'us_percent'])

    infile = open(filename, "r")
    for line in infile:
        result = re.search(line_re, line)
        if result:
            print "%s '%s' %s %s" % (result.group(1), result.group(2), result.group(3), result.group(4))
            dw.writerow([result.group(1), result.group(2), result.group(3), result.group(4)])
        # else:
        #    print "no match in %s" % (line)
    outfile.close()