
lista0 = [1,2,3,4,5,6,7,8,9,0]
lista1 = [variavel for variavel in lista0]
lista2 = [variavel * 2 for variavel in lista0]
lista3 = [(variavel, variavel2) for variavel in lista0 for variavel2 in range(3)]

print(lista1)
print(lista2)
print(lista3)

lista4 = ['Luiz', 'Mauro', 'Maria']
lista5 = [variavel.replace('a', '@').upper() for variavel in lista4]

print(lista4)
print(lista5)

lista6 = list(range(100))
print(lista6)

lista7 = [variavel for variavel in lista6 if variavel % 3 == 0 if variavel % 8 == 0]
print(lista7)

lista8 = [variavel if variavel % 3 == 0 else False for variavel in lista6]
print(lista8)