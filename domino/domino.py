from random import Random, random
import deck
import jogador


class JogoDomino:
    def __init__(self):
        self.deck = deck.Deck().getDeck()
        self.jogadores = []
        self.jogador1 = jogador.Jogador()
        self.jogadorMaquina = jogador.Jogador()

    def start(self):
        self.embaralhaDeck()
        self.leNomesJogadores()
        self.divideDeck()

    def embaralhaDeck(self):
        embaralhado = []
        randon = Random()
        while range(len(self.deck)):
            aleatorio = randon.randint(0, len(self.deck)-1)
            print(aleatorio)
            embaralhado.append(self.deck[aleatorio])
            self.deck.pop(aleatorio)

        self.deck = embaralhado
        self.mostraDeck()

    def leNomesJogadores(self):
        self.jogador1.setName(input("Digite seu nome\n"))
        self.jogadorMaquina.setName("Computador")
        print(f'Bem vindo {self.jogador1.name}')

    def divideDeck(self):
        self.jogadores = [self.jogador1, self.jogadorMaquina]
        for jogador in self.jogadores:
            for i in range(7):
                jogador.mao.append(self.deck[i])
                self.deck.pop(i)
            jogador.getMao()
        self.mostraDeck()

    def mostraDeck(self):
        conjDeck = self.deck
        for i in range(len(conjDeck)):
            print(f"Carta {i} A: {conjDeck[i].getA()} B: {conjDeck[i].getB()}")


jogo = JogoDomino()
jogo.start()
