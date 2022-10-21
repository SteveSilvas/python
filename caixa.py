class CaixaEletronico:
    def __init__(self):
        self.notas = [200, 100, 50, 20, 10, 5, 2]
        self.moedas = [1.0, 0.5, 0.25, 0.10, 0.05, 0.01]
        self.quantidadeNotas = [0,0,0,0,0,0,0]
        self.quantidadeMoedas = 0
        self.notasRetornadas = []
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
        print("Insira o cartão para entrar no seu banco")
        print("Para Saldo digite 0")
        print("Para Saque digite 1")
        print("Para Depósito digite 2")
        print("Para Transferência digite 3")

        opcao = int(input("digite a ação desejada"))
        match opcao:
            case 0:
                print("Saldo")
            case 1:
                print("Saque")
            case 2:
                print("Depósito")
            case 3:
                print("Transferência")

caixa = CaixaEletronico()
caixa.mostraMenu()
valorDeSaque = 445
caixa.calculaMinimoNotas(valorDeSaque)