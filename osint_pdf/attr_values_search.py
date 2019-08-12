from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def search_pdfs(target_field, target_value):
    directory = "PDF/"
    file_list =  os.listdir(directory)

    files_matched = {}

    for f in file_list:
        # Opening file
        f = directory+f
        with open(f, 'rb') as input_file:
            reader = PdfFileReader(input_file)
            metadata = reader.getDocumentInfo()
            if target_field in metadata:
                field_value = metadata.get(target_field)
                if target_value in field_value:
                    files_matched[f.replace(directory, '')] = field_value
                    
    return files_matched

print search_pdfs('/Author','Disney')
print search_pdfs('/Creator','Adobe')
