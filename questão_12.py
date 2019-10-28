class Conta:
    def __init__(self,numero,nome,saldo):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self,nome):
        self.nome = nome

    def saque(self,dinheiro):
        if(dinheiro <= self.saldo and dinheiro > 0):
            self.saldo = self.saldo - dinheiro
            return 'Você sacou R${}, seu saldo agora é R${}.'.format(dinheiro,self.saldo)
        else:
            return 'Você não pode sacar esse valor.'
    def deposito(self,dinheiro):
        if(dinheiro > 0):
            self.saldo = self.saldo + dinheiro
            return 'Você depositou R${}, seu saldo agora é R${}.'.format(dinheiro,self.saldo)
        else:
            return 'Você não pode depositar valores negativos ou nada.'

    def adicione_juros(self,taxa):
        self.saldo = self.saldo * taxa


jaum = Conta(40028922,'João',1000)

print(jaum.saldo)

for i in range(5):
    jaum.adicione_juros(1.10)
    print(jaum.saldo)