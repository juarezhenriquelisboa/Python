import pefile

#carregando o binario
pe = pefile.PE('notepad.exe')

pe

#mostrando a estrutura do arquivo:
dir(pe)

#o header do arquivo:
import pprint

pprint.pprint(dir(pe.DOS_HEADER))

#printando o magic number

# Decimal
print pe.DOS_HEADER.e_magic

# Hex
print hex(pe.DOS_HEADER.e_magic)

# ASCII Char string
a = hex(pe.DOS_HEADER.e_magic)
a =  a[2:]
print a.decode("hex")

# numero de seções
print pe.FILE_HEADER.NumberOfSections

# seções
print pe.sections

# seções especificas
pprint.pprint(dir(pe.sections[0]))

# nome e tamanho dos dados das seções
for section in pe.sections:
    print section.Name
    print section.SizeOfRawData
    print '\n'


#upx
import pefile

pe = pefile.PE('notepad_upx.exe')

for section in pe.sections:
    print section.Name
    print section.SizeOfRawData
    print '\n'
