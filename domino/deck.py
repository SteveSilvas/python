    
from operator import indexOf
import peca    
class Deck:
    def _init_(self):
        self.lista = []

    def buildDeck(self):
        lista = []
        options = [0,1,2,3,4,5,6]
        for i in options:
            b = options[indexOf(options, i)]
            for j in options:
                if(j in options[0:b]):
                    pass
                else:
                    p = peca.Peca()
                    p.setA(i)
                    p.setB(j)
                    lista.append(p)
                    p.getPeca()
        self.lista = lista

    def getDeck(self):
        self.buildDeck()
        return self.lista

    def getCountDeck(self):
        c = len(self.lista)
        print(f'Count = {c}')
