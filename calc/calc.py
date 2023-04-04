import basicas
from components.components import Components


class Calc:
    def __init__(self):
        self.basicas = basicas.Basicas()

    def startMenu(self):
        print("Digite 1 para Somar")
        print("Digite 2 para Subtrair")
        print("Digite 3 para Multiplicar")
        print("Digite 4 para Dividir")
        comp =  Components()
        option = comp.inputNumber("Entre com o tipo de cáculo")
        match option:
            case 1:
                self.startSoma()
            case 2:
                self.startSub()
            case 3:
                self.startMult()
            case 4:
                self.startDiv()

    def startSoma(self):
        print("SOMA")
        a = float(input("Digite um número"))
        b = float(input("Digite outro número"))
        print("A Soma de "+ a + " + " + b + " = {:.2f}".format(self.basicas.toSum(a,b)))

    def startSub(self):
        print("SUBTRAÇÃO")
        a = float(input("Digite um número"))
        b = float(input("Digite outro número"))
        print("A Subtração de "+ a + " - " + b + " = {:.2f}".format(self.basicas.toSub(a,b)))

    def startMult(self):
        print("MULTIPLICAÇÃO")
        a = float(input("Digite um número"))
        b = float(input("Digite outro número"))
        print("A Multiplicação de "+ a + " * " + b + " = {:.2f}".format(self.basicas.toMult(a,b)))

    def startDiv(self):
        print("DIVISÃO")
        a = float(input("Digite um número"))
        b = float(input("Digite outro número"))
        print("A divisão de "+ a + " / " + b + " = {:.2f}".format(int(self.basicas.toDiv(a,b))))
    
calc = Calc()
calc.startMenu()