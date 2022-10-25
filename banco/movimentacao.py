import conta

class Movimentacao:
    def __init__(self, tipo):
        self.tipo = tipo
        self.contas = []

    def buscarContas(self):
        print(str(self.contas))
        
    def criarConta(self):
        conta = conta.Conta("Steve", "324.545.765-00")
        self.contas.push(conta)

    def movimentar(self):
        input("digite o 0 para ver seu saldo")

