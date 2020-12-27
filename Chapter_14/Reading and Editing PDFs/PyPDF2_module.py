import PyPDF2
import os

pdfFile = open('C:\\Emil\\Cursuri\\AF\\Curs 6\\Cautari si Sortari II.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)  # assign a new pdf reader object

print(reader.numPages)

page = reader.getPage(4)
print(page.extractText())
for pagenum in range(reader.numPages):
    print(reader.getPage(pagenum).extractText())

pdfFile1 = open('C:\\Emil\\Cursuri\\AF\\Curs 6\\Cautari si Sortari II.pdf', 'rb')
pdfFile2 = open('C:\\Emil\\Cursuri\\SA\\Curs 1\\Fisa Aplicatie 1_Harti mentale.pdf', 'rb')

reader1 = PyPDF2.PdfFileReader(pdfFile1)
reader2 = PyPDF2.PdfFileReader(pdfFile2)
writer = PyPDF2.PdfFileWriter()  # to be capable of adding pages

for pagenum in range(reader1.numPages):
    page = reader1.getPage(pagenum)  # take every page from pdf1
    writer.addPage(page)  # add the page to a new pdf file

for pagenum in range(reader2.numPages):
    page = reader2.getPage(pagenum)
    writer.addPage(page)

outputFile = open('combinedminutes.pdf', 'wb')  # set the location for output pdf file (default is current working directory)
writer.write(outputFile)  # in output file write the content from writer

outputFile.close()
pdfFile1.close()
pdfFile2.close()

