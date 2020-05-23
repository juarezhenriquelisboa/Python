def soma(*args):
    s=0
    for x in args:
        s+=x
    return s

print(soma(9,10,20,30,40))
