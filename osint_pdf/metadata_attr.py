from PyPDF2 import PdfFileReader, PdfFileWriter
import os

directory = "PDF/"
file_list =  os.listdir(directory)

attr_superset = []

for f in file_list:
    # Opening file
    f = directory+f
    with open(f, 'rb') as input_file:
        reader = PdfFileReader(input_file)
        metadata = reader.getDocumentInfo()
        for item, value in metadata.iteritems():
            item = item.replace('/','')
            if item not in attr_superset:
                attr_superset.append(item)
            
print attr_superset
    
