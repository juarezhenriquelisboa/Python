def barra(n=10, c="*"):
    print(c*n)

L = [ [5, "-"], [10, "*"], [5] ]

for e in L:
    barra(*e)


# barra(5, "-") barra(10, "*")


