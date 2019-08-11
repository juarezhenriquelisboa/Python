import zipfile

sucesso = False

i = 0

z = zipfile.ZipFile("protegido.zip")

with open("dicionario.txt") as f:
    linhas = f.readlines()

for senha in linhas:
    senha = senha.replace('\n', '')
    try:
        z.extractall(pwd=senha)
        senha_correta = 'Senha correta: %s' % senha
        sucesso = True
        break
    except:
        pass
        print "tentativa", i
        i = i+1

if sucesso: 
    print senha_correta
else:
    print "Senha nao encontrada"
