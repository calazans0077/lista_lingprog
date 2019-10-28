class Funcionario:
    def __init__(self,nome,salario):
        self.nome = str(nome)
        self.salario = float(salario)

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario


jaum = Funcionario('Jaum',100000)

print(jaum.get_nome())
print(jaum.get_salario())