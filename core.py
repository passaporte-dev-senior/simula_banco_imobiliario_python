import random


class Jogador:
    def __init__(self, saldo_inicial=300):
        self._status = 'Ativo'
        self._saldo = saldo_inicial
        self.propriedades = None
        self.posicao = 1

    @property
    def saldo(self):
        return self._saldo

    def transacao(self, valor):
        self._saldo += valor
        if self.saldo < 0:
            self._status = 'Inativo'

    @property
    def status(self):
        return self._status

    # TODO: comportamento Jogador: impulsivo | exigente | cauteloso | aleatório
    # TODO: o Jogador terá registro de suas propriedades? Delega para Propriedade?
    # TODO: o Jogador precisa saber sua posição? Delega para o Tabuleiro?


class Propriedade:
    def __init__(self, custo=None, aluguel=None, posicao=1):
        self.custo = custo
        self.aluguel = aluguel
        self.posicao = posicao
        self.proprietario = None

    # TODO: a Propriedade precisa saber sua posição? Delega para o Tabuleiro?
    # TODO: a Propriedade terá registro de seu proprietário? Delega para Jogador?


class Dado:
    def __init__(self, seed=None):
        self.seed = seed

    @property
    def numero(self):
        random.seed(self.seed)
        return random.randint(1, 6)


class Tabuleiro:
    def __init__(self, posicoes=20):
        self.num_posicoes = posicoes

    # TODO: controle número de rodadas
    # TODO: controle de Jogador/Propriedade em cada posição (??)
    # TODO: solicita ação do Jogador (compra ou não, pagamento aluguel) (??)
    # TODO: solicita ação da Propriedade (venda ou não, cobrança aluguel) (??)
