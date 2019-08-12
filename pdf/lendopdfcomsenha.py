from PyPDF2 import PdfFileReader, PdfFileWriter

encrypted_file='secret.pdf'
password='bac321'
with open(encrypted_file, 'rb') as input_file:
    reader = PdfFileReader(input_file)
    reader.decrypt(password)
    for i in range(reader.getNumPages()):
            page = reader.getPage(i)
            page_content = page.extractText()
            print page_content.encode('utf-8')
