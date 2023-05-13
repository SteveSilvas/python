class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def exibir_saldo(self):
        print(f"Saldo: R${self.saldo}")

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo, taxa_juros):
        super().__init__(titular, saldo)
        self.taxa_juros = taxa_juros

    def aplicar_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros

conta_poupanca = ContaPoupanca("João", 150, 1.3)
conta_poupanca.exibir_saldo()
