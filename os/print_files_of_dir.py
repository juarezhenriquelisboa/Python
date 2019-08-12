from PyPDF2 import PdfFileReader, PdfFileWriter
import os

file_list =  os.listdir("PDF")

counter = 1
for f in file_list:
    print str(counter)+"  "+f
    counter = counter + 1
