class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.plano = plano
        self.lista_planos = ['basic', 'premium']

cliente = Cliente('claudio', 'claudio@gmail.com', 'basic')
