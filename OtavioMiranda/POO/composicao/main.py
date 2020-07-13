from cls import Cliente

cliente1 = Cliente('Luiz', 21)
cliente1.inserir_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_endereco()
del cliente1
cliente2 = Cliente('Maria', 18)
cliente2.inserir_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_endereco()
del cliente2

print("#################")