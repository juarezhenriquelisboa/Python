from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def superset(target_field):
    directory = "PDF/"
    file_list =  os.listdir(directory)

    result_supterset = []

    for f in file_list:
        # Opening file
        f = directory+f
        with open(f, 'rb') as input_file:
            reader = PdfFileReader(input_file)
            metadata = reader.getDocumentInfo()
            if target_field in metadata:
                field_value = metadata.get(target_field)
                if field_value not in attr_superset:
                    result_supterset.append(field_value)

    return result_supterset

# PRINTAR ATRIBUTOS ESPECIFICOS

print superset('/Creator')

print superset('/Author')

#PRINTAR TODOS OS ATRIBUTOS

for attr in attr_superset:
    attr = '/'+attr
    print "==========> "+attr
    print superset(attr)


