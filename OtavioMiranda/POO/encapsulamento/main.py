"""
teste
"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self._dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_clientes(1, 'A')
bd.inserir_clientes(2, 'B')
bd.inserir_clientes(3, 'C')
# bd.__dados = not possible
# bd._BaseDeDados__dados = possible