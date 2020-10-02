import random


class Jogador:
    def __init__(self):
        self.status = 'Ativo'
        self.saldo = 300
        self.propriedades = None
        self.posicao = 1


class Propriedade:
    def __init__(self, custo=0, aluguel=0, posicao=1):
        self.custo = custo
        self.aluguel = aluguel
        self.posicao = posicao
        self.proprietario = None


class Dado:
    def __init__(self, seed=None):
        self.seed = seed

    @property
    def numero(self):
        random.seed(self.seed)
        return random.randint(1, 6)
