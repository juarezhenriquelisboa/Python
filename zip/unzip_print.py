import zipfile
import sys

for arg in sys.argv[1:]:
    senha = str(arg)

z = zipfile.ZipFile("protegido.zip")

files = z.namelist()

z.setpassword(senha)

z.extractall()

z.close()

for extracted_file in files:
    print "Nome do arquivo: "+extracted_file+"\n\nConteudo: "
    
    with open(extracted_file) as f:
        content = f.readlines()
        print ''.join(content)
        print '\n\n'
