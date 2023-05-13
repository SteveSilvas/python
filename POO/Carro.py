class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def ligar(self):
        print("Motor ligado.")

    def desligar(self):
        print("Motor desligado.")


class Carro:
    def __init__(self, motor):
        self.motor = motor

    def ligar_carro(self):
        self.motor.ligar()
        print("Carro ligado.")

    def desligar_carro(self):
        self.motor.desligar()
        print("Carro desligado.")


motor = Motor("Gasolina")

carro = Carro(motor)

carro.ligar_carro()
carro.desligar_carro()
