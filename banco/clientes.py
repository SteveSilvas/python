from titular import Titular


class Clientes:
    def __init__(self):
        self.clientes = self.buildClientsList()

    def buildClientsList(self):
        clientes = []
        titular = Titular("Steve", '112.765.432-00')
        clientes.append(titular)

        titular2 = Titular("Ana", '443.265.654-50')
        clientes.append(titular2)

        titular3 = Titular("Carla", '123.434.543-50')
        clientes.append(titular3)

        titular4 = Titular("Daiane", '654.265.545-12')
        clientes.append(titular4)

        titular2 = Titular("Julia", '543.545.230-00')
        clientes.append(titular2)

        return clientes

    def getFirstTitular(self):
        return self.clientes[0]

    def getAllTitular(self):
        return self.clientes

    def getTitular(self, index):
        if len(self.clientes) < index :  return
        else : return self.clientes[index] 