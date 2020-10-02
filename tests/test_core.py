from core import Jogador, Propriedade, Dado


def test_jogador():
    jogador_01 = Jogador()
    assert isinstance(jogador_01, Jogador)
    assert jogador_01.status == 'Ativo'
    assert jogador_01.saldo == 300
    assert jogador_01.propriedades is None
    assert jogador_01.posicao == 1


def test_propriedade():
    propriedade_01 = Propriedade()
    assert isinstance(propriedade_01, Propriedade)
    assert hasattr(propriedade_01, 'custo')
    assert hasattr(propriedade_01, 'aluguel')
    assert hasattr(propriedade_01, 'proprietario')
    assert hasattr(propriedade_01, 'posicao')


def test_dado():
    dice = Dado()
    assert isinstance(dice, Dado)
    assert hasattr(dice, 'numero')


def test_dado_seed():
    dice = Dado(seed=42)
    assert dice.numero == 6
    dice = Dado(seed=0)
    assert dice.numero == 4


def test_jogador_transacao():
    jogador_01 = Jogador()
    jogador_01.transacao(-50)
    assert jogador_01.saldo == 250
    jogador_01.transacao(100)
    assert jogador_01.saldo == 350


def test_jogador_perde():
    jogador_01 = Jogador()
    jogador_01.transacao(-350)
    assert jogador_01.saldo == -50
    assert jogador_01.status == 'Inativo'
