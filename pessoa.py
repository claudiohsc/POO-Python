class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = str(nome)
        self.idade = int(idade)
        self.peso = float(peso)
        self.altura = float(altura)

        print(f'Pessoa criada: {self.nome} com {self.idade} anos de idade.')
        print(f'Pesando {self.peso} kilos e medindo {self.altura} cm de altura.')
        print('')

    def envelhecer(self, anos):
        self.anos = int(anos)
        self.idade += self.anos

        print(f'{self.nome} envelheceu {self.anos} anos, está agora com {self.idade} anos.')
        if self.idade <= 21:
            self.altura += 0.5
            print(f'{self.nome} cresceu mais 0.5 cm, está com {self.altura} cm de altura.')

        print('')

    def engordar(self, kilos):
        self.peso += float(kilos)
        print(f'{self.nome} engordou {kilos} kilos. Peso atual: {self.peso} Kg.')
        print('')

    def emagrecer(self, kilos):
        self.peso -= float(kilos)
        print(f'{self.nome} emagreceu {float(kilos)} kilos. Peso atual: {self.peso} Kg.')
        print('')

    def crescer(self, cm):
        self.altura += float(cm)
        print(f'{self.nome} cresceu mais {float(cm)} cm, está com {self.altura} cm de altura.')
        print('')


humano = Pessoa('Claudio', 18, 70, 177)
humano.envelhecer(2)
humano.engordar(2)
humano.emagrecer(3)
humano.crescer(3)