from conta import Conta
from titular import Titular
from clientes import Clientes
class CaixaEletronico:
    def __init__(self):
        self.notas = [200, 100, 50, 20, 10, 5, 2]
        self.moedas = [1.0, 0.5, 0.25, 0.10, 0.05, 0.01]
        self.quantidadeNotas = [0,0,0,0,0,0,0]
        self.quantidadeMoedas = 0
        self.notasRetornadas = []
        self.contaLogada = None
        
    def calculaMinimoNotas(self, valor):
        print(str(self.notas))
        for i in range(len(self.notas)):
            if(valor >= self.notas[i]):
                self.quantidadeNotas[i] = int(valor/self.notas[i])
                self.notasRetornadas.append({'Tipo':str(self.notas[i]), 'Quantidade':str(self.quantidadeNotas[i])})
                if(valor % self.notas[i] == 0):
                    print("Retire seu dinheiro")
                else:
                    valor = valor % self.notas[i]    
        self.mostraQuantidadeNotas()

    def mostraQuantidadeNotas(self):
        for i in self.notasRetornadas:
            print(i)

    def mostraMenu(self):
        print("---------------------   Menu   --------------------")
        print("---------------------------------------------------")
        print("Para Saldo digite 0")
        print("Para Saque digite 1")
        print("Para Depósito digite 2")
        print("Para Transferência digite 3")
        print("Digite 0 para continuar ou qualquer tecla para sair")
        print("----------------------------------------------------\n")

        opcao = int(input("digite a ação desejada\n"))
        match opcao:
            case 0:
                print("Saldo")
                self.contaLogada.getSaldo()
                self.mostraMenu()
            case 1:
                print("Saque")
                self.contaLogada.sacar(int(input("Digite o valor de saque\n")))
                self.mostraMenu()
            case 2:
                print("Depósito")
                self.contaLogada.depositar(float(input("Digite o valor para depósito\n")))
                self.mostraMenu()
            case 3:
                print("Transferência")
                valor = int(input("Digite o valor para saque\n"))
                destinatario = Titular("Sika", "424123455666")
                self.contaLogada.transferir(valor, destinatario)
                self.mostraMenu()


    def loginConta(self, agencia, digAgencia, conta, digConta, titular):
        self.contaLogada = Conta(agencia, digAgencia, conta, digConta, titular)
        self.mostraMenu()

caixa = CaixaEletronico()
clientes = Clientes()
titular = clientes.getTitular(4)
caixa.loginConta(3423, 3, 43434343, 43, titular)