
class Pou:
    def __init__(self,nome,fome,saude,idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self,nome):
        self.nome = nome

    def alterar_fome(self,fome):
        if fome >= 0 and fome <=100:
            self.fome = fome
        else:
            print('erro')

    def alterar_saude(self,saude):
        if saude >= 0 and saude <= 100:
            self.saude = saude

    def alterar_idade(self,idade):
        if idade >= 0 and idade <= 100:
            self.idade = idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def retornar_humor(self):
        alimentacao = 100 - self.fome
        humor = (alimentacao + self.saude)/2

        if humor > 50 and alimentacao > 10 and self.saude > 10:
            return 'Bom humor'

        else:
            return 'Mau humor'

    def brincar(self,tempo):
        if tempo > 0 and tempo < 180:
            self.saude = self.saude * (1+(tempo/100))
            self.fome = self.fome * (1 -(tempo/100))

        elif tempo >= 180:
            tempo_adicional = tempo - 180
            self.saude = self.saude * (1 -(tempo_adicional/100))
            self.fome = self.fome * (1 + (tempo_adicional/100))
        else:
            print('erro')

    def brincar_fixo(self):
        tempo = 10
        if tempo > 0 and tempo < 180:
            self.saude = self.saude * (1+(tempo/100))
            self.fome = self.fome * (1 -(tempo/100))
            print('Os pous brincaram por 10 min')

        elif tempo >= 180:
            tempo_adicional = tempo - 180
            self.saude = self.saude * (1 -(tempo_adicional/100))
            self.fome = self.fome * (1 + (tempo_adicional/100))
            print('Os pous brincaram por 10 min')
        else:
            print('erro')

    def alimentar(self):
        if self.fome > 10:
            self.fome = self.fome - 10
            fominha = self.fome + 10
            print('A fome do Pou foi de {} para {}.'.format(fominha, self.fome))
        else:
            print('O pou está cheio')

    def dar_remedio(self):

        if self.saude <90:
            self.saude = self.saude + 10
            saude = self.saude - 10
            print('O pou tomou o remédio e sua saude aumentou de {} para {}'.format(saude,self.saude))
        else:
            print('A saude do Pou já está OK')

    def str(self):
        print('nome:',self.retornar_nome())
        print('fome:',self.retornar_fome())
        print('saude:',self.retornar_saude())
        print('idade:',self.retornar_idade())
        print('humor:',self.retornar_humor())



novo_pou =[]
i = 0
while True:
    decisao = input('Quer criar um Pou? digite (sim)')
    if decisao == 'sim':
        nome = input('nome:')
        idade = input('idade:')
        novo_pou.append(i)
        novo_pou[i] = Pou(nome,50,50,idade)
        i = i + 1
    elif decisao != 'sim':
        break


condicao = True
opcao = int(input('Digite 1 para interagir com um Pou específico , digite 2 para interagir com todos ao mesmo tempo'))

if opcao == 1:
    for j in range(i):
        print('Digite {} para interagir com o Pou {}.'.format(j,novo_pou[j].nome))
    bixin = int(input('Digite o numero do Pou:'))
    while condicao:
        acao = int(input('Digite (1) para alimentar {}, Digite (2) para brincar com {}, Digite (3) para remediar {}:'.format(novo_pou[bixin].nome,novo_pou[bixin].nome,novo_pou[bixin].nome)))
        if acao == 1:

            novo_pou[bixin].alimentar()
            novo_pou[bixin].str()
            sair = input('deseja sair?')
            if sair =='sim':
                condicao = False
            elif sair !='sim':
                print('Então vamos continuar!')

        if acao == 2:

            novo_pou[bixin].brincar_fixo()
            novo_pou[bixin].str()
            sair = input('deseja sair?')
            if sair == 'sim':
                condicao = False
            elif sair != 'sim':
                print('Então vamos continuar!')

        if acao == 3:

            novo_pou[bixin].dar_remedio()
            novo_pou[bixin].str()
            sair = input('deseja sair?')
            if sair == 'sim':
                condicao = False
            elif sair != 'sim':
                print('Então vamos continuar!')




if opcao == 2:
    while condicao:
        acao = int(input('Digite (1) para alimentar todos os Pous, Digite (2) para brincar com todos os Pous, Digite (3) para dar remédio para todos os Pous:'))
        if acao == 1:
            for j in range(i):
                novo_pou[j].alimentar()
                novo_pou[j].str()
                sair = input('deseja sair?')
                if sair =='sim':
                    condicao = False
                elif sair !='sim':
                    print('Então vamos continuar!')

        if acao == 2:
            for j in range(i):
                novo_pou[j].brincar_fixo()
                novo_pou[j].str()
                sair = input('deseja sair?')
                if sair == 'sim':
                    condicao = False
                elif sair != 'sim':
                    print('Então vamos continuar!')

        if acao == 3:
            for j in range(i):
                novo_pou[j].dar_remedio()
                novo_pou[j].str()
                sair = input('deseja sair?')
                if sair == 'sim':
                    condicao = False
                elif sair != 'sim':
                    print('Então vamos continuar!')


