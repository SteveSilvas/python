# PRIMEIRA FORMA
# nome_contato = "João"
# emails_contato = ["joao@example.com", "joao@gmail.com"]
# numero_contato = 123456789

# print("Nome:", nome_contato)
# print("E-mails:", ', '.join(emails_contato))
# print("Número:", numero_contato)

## SEGUNDA FORMA
# def verContato(nome, emails, numero):
#     print("Nome:", nome)
#     print("E-mails:", ', '.join(emails))
#     print("Número:", numero)


# nome_contato = "João"
# emails_contato = ["joao@example.com", "joao@gmail.com"]
# numero_contato = 123456789

# verContato(nome_contato, emails_contato, numero_contato)

### TERCEIRA FORMA
# def verContato(nome, emails, numero):
#     print("Nome:", nome)
#     print("E-mails:", ', '.join(emails))
#     print("Número:", numero)

# def criaContato(nome, emails, numero):
#     return nome, emails, numero

# nome_contato, emails_contato, numero_contato = criaContato("Steve",['steve.evets00@gmail.com'], '997681306')
# verContato(nome_contato, emails_contato, numero_contato)

##### QUARTA FORMA
# class Contato:
#     def __init__(self):
#         self.name = None
#         self.email = []
#         self.numero = 0

#     def verContato(self):
#         print("-----------------------------------")
#         print("Nome:", self.name)
#         print("E-mails:", ', '.join(self.email))
#         print("Número:", self.numero)
#         print("-----------------------------------")


# QUINTA FORMA
class Contato:
    def __init__(self, nome=None, emails=None, numero=0):
        self.name = nome
        self.email = emails if emails is not None else []
        self.numero = numero

    def verContato(self):
        print("-----------------------------------")
        print("Nome:", self.name)
        print("E-mails:", ', '.join(self.email))
        print("Número:", self.numero)
        print("-----------------------------------")

contato = Contato()
contato.name = "João"
contato.email = ["joao@example.com", "joao@gmail.com"]
contato.numero = 123456789

contato.verContato()

eu = Contato()
eu.name = "steve"
eu.email = ["steve@example.com", "steve@gmail.com"]
eu.numero = 987654321
eu.verContato()

import datetime

class Amigo(Contato):
    def __init__(self, nome=None, emails=None, numero=0, aniversario=None):
        super().__init__(nome, emails, numero)
        self.aniversario = aniversario

    def verificaAniversario(self):
        if self.aniversario is None:
            return False

        hoje = datetime.date.today()
        dia_aniversario = self.aniversario.day
        mes_aniversario = self.aniversario.month
        return hoje.day == dia_aniversario and hoje.month == mes_aniversario

    def verContato(self):
        super().verContato()
        if self.verificaAniversario():
            print("É aniversário desse amigo hoje!")


aniversario_amigo = datetime.date(1990, 8, 22) 
amigo = Amigo("Icaro", ["icaro@icaro.com"], "123456789", aniversario_amigo)
amigo.verContato()
