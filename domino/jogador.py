class Jogador:
    def __init__(self):
        self.name = None
        self.mao = []
        # self.cod = None

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getMao(self):
        retorno = []
        print(f"Mão do jogador {self.name}")
        for i in self.mao:
            retorno.append(i)
            print(f"{i.getA()} - {i.getB()}")
        return retorno