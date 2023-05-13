class Computador:
    def __init__(self):
        self.monitor = Monitor()
        self.teclado = Teclado()
        self.mouse = Mouse()

    def ligar(self):
        print("Computador ligado.")
        self.monitor.ligar()
        self.teclado.ligar()
        self.mouse.ligar()

    def desligar(self):
        print("Computador desligado.")
        self.monitor.desligar()
        self.teclado.desligar()
        self.mouse.desligar()


class Monitor:
    def ligar(self):
        print("Monitor ligado.")

    def desligar(self):
        print("Monitor desligado.")


class Teclado:
    def ligar(self):
        print("Teclado ligado.")

    def desligar(self):
        print("Teclado desligado.")


class Mouse:
    def ligar(self):
        print("Mouse ligado.")

    def desligar(self):
        print("Mouse desligado.")


computador = Computador()

computador.ligar()
computador.desligar()