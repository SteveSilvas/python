class Animal:
    def __init__(self, nome):
        self.nome = nome

    def som(self):
        pass


class Cachorro(Animal):
    def som(self):
        return "AU AU!"


class Gato(Animal):
    def som(self):
        return "Miau!"


cachorro = Cachorro("Pluto")
print(cachorro.som())  # Saída: "AU AU!"

gato = Gato("Frajola")
print(gato.som())  # Saída: "Miau!"