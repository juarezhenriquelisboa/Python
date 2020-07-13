
def funcao(arg_a, arg_b):
    return arg_a * arg_b

a = funcao(2, 2)
print(a)

b = lambda arg_a, arg_b: arg_a * arg_b

print(b(2, 2))

"""
##############
"""

lista = [
    ['a', 0],
    ['b', 1],
    ['c', 2],
    ['d', 3],
]

lista.sort(key=lambda item: item[1], reverse=True)
print(lista)