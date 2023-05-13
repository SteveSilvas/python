class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo


    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print("-------------")




class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []




    def contratar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)


    def exibir_funcionarios(self):
        print(f"Funcionários da {self.nome}:")
        for funcionario in self.funcionarios:
            funcionario.exibir_informacoes()




funcionario1 = Funcionario("Rian", "Atendente")
funcionario2 = Funcionario("Carla", "Gerente")
funcionario3 = Funcionario("Julia", "Arquiteta")


empresa = Empresa("Arquitetura Familiar")


empresa.contratar_funcionario(funcionario1)
empresa.contratar_funcionario(funcionario2)
empresa.contratar_funcionario(funcionario3)


empresa.exibir_funcionarios()
