#!/usr/bin/env python3

from optparse import OptionParser
from glob import glob
from pdfrw import PdfReader, PdfWriter

# Add command line options to parse
parser = OptionParser()
parser.add_option("-o", "--outfile",
        action="store", type="string", dest="outfile")
(options, args) = parser.parse_args()
if not len(args):
    print("No input files")
    exit(1)
input_files = list()
for path in args:
    input_files.extend(glob(path))
out_file_string = options.outfile or 'out.pdf'
writer = PdfWriter()
for path in input_files:
    writer.addpages(PdfReader(path).pages)
writer.write(out_file_string)
