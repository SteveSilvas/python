class Conta:
    def __init__(self, titular, cpfCnpj):
        self.saldo = 0.0
        self.titular = titular
        self.cpfCnpj = cpfCnpj
        self.startConta()

    def startConta(self):
        print("Conta criada com sucesso")
        print("Titular: "+self.titular)
        print("Cpf/Cnpj: "+self.cpfCnpj)
        print("-------------------------")

    def getSaldo(self):
        print("Saldo atual = "+str(self.saldo))
    
    def depositar(self, quantidade):
        self.saldo = self.saldo+quantidade
        print("deposito realizado com sucesso")
        self.getSaldo()

    def sacar(self, valorDeSaque):
        if(self.saldo > valorDeSaque):
            self.saldo -= valorDeSaque
            print("saque realizado com sucesso")
        else:
            print('Saldo indisponível para este saque')
        self.getSaldo()
        

    def getTitular(self):
        print("Titular: "+ self.titular)

    def setTitular(self, titular):
        self.titular = titular
        print("titular alterado para "+ self.titular)
