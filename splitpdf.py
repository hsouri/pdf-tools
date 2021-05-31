from PyPDF2 import PdfFileWriter, PdfFileReader
import sys


'''
    usage: python splitpdf.py [input-pdf-path] [from-page] [to-page]
    example: python splitpdf.py ./sample.pdf 2 5


'''


inputpdf = PdfFileReader(open(sys.argv[1], 'rb'))
frompage = sys.argv[2]
topage = sys.argv[3]

output = PdfFileWriter()
for page in range(int(frompage) - 1, int(topage)):
    output.addPage(inputpdf.getPage(page))
    
with open(f'newpdf_{frompage}_{topage}.pdf', 'wb') as outputStream:
    output.write(outputStream)
