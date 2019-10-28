class Carro:
    def __init__(self,consumo,tanque):
        self.__consumo = consumo
        self.tanque = tanque

    def andar(self,kilometragem):
        consumiu = self.__consumo * kilometragem
        self.tanque = self.tanque - consumiu
        print('Ao andar {} você consumiu {}.'.format(kilometragem,consumiu))

    def show_gasolina(self):
        return self.tanque

    def add_gasolina(self,gasolina):
        self.tanque = self.tanque + gasolina


fusca = Carro(10,0)

print('tanque:',fusca.show_gasolina())
fusca.add_gasolina(50)
print('tanque:',fusca.show_gasolina())

fusca.andar(4)
print('tanque:',fusca.show_gasolina())