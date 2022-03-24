class Cliente:
    def __init__(self, nome, email, plano): #define as variáveis da classe;
        self.nome = nome #define os atributos recebendo as variáveis;
        self.email = email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            print('Plano Inválido.')
    

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
            print(f'Seu novo plano é: {novo_plano}')
        else:
            print('Plano Inválido.')


    def ver_filme(self, filme, plano_filme):
        if plano_filme not in self.lista_planos:
            print('Plano Inválido.')
        if self.plano == 'plano_filme':
            print(f'Ver filme {filme}')
        elif self.plano == 'premium':
            print(f'Ver filme {filme}')
        elif self.plano != plano_filme:
            print(f'Não é possível ver {filme} com o plano {self.plano}. Faça um upgrade!')



cliente = Cliente('claudio', 'claudio@gmail.com', 'basic')
cliente.mudar_plano('premium')

cliente.ver_filme('Harry Potter', 'premium')