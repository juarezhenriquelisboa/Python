class Televisao:
    def __init__(self):
        self.ligada=True
        self.canal=2

    def muda_canal(self):
        self.canal+=1


tv = Televisao()

print(tv.canal)

tv.muda_canal()
tv.muda_canal()

print(tv.canal)

class Netflix(Televisao):
    def __init__(self, ligada=True, canal=2, conectada=False):
        Televisao.__init__(self)
        self.conectada=False

    def conectar(self):
        self.conectada=True

tv_sala = Netflix(Televisao)

print(tv_sala.conectada)
print(tv_sala.ligada)
print(tv_sala.canal)

tv_sala.conectar()

tv_sala.muda_canal()

print(tv_sala.conectada)
print(tv_sala.canal)
