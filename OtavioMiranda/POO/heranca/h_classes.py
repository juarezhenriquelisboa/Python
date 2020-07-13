class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'{self.nome} está falando')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} está comprando')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} está estudando')

