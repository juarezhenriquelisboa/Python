from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('João')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

# print(escritor.nome)
# print(caneta.marca)
# caneta.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()