class Conta:
    def __init__(self, agencia, digAgencia, conta, digConta, titular):
        self.saldo = 0.0
        self.digAgencia = digAgencia
        self.agencia = agencia
        self.conta = conta
        self.digConta = digConta
        self.titular = titular
        self.startConta()

    def startConta(self):
        print("Conta criada com sucesso")
        print("Titular: " + self.titular.getNome())
        print("Cpf/Cnpj: " + self.titular.getCpfCnpj())
        print("-------------------------")

    def getSaldo(self):
        print("Saldo atual = " + str(self.saldo))

    def depositar(self, valor):
        self.saldo = self.saldo+valor
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
        return self.titular

    def setTitular(self, titular):
        self.titular = titular
        print("titular alterado para " + self.titular)
