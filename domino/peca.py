import re


class Peca:
    def _init_(self,a,b):
        self.a = a
        self.b = b
        
    def getA(self):
        return self.a

    def setA(self, a):
        self.a = a

    def getB(self):
        return self.b

    def setB(self, b):
        self.b = b

    def getPeca(self):
        print(f'lado A {self.a} lado B {self.b}')