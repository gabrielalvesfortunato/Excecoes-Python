from dominio import Cliente, ContaCorrente
from exececoes_negocio import SaldoInsuficienteError
import pytest


@pytest.fixture
def marcos():
    marcos = Cliente("Marcos", "000.000.000-00", "Administrador")
    return marcos

@pytest.fixture
def conta_marcos(marcos):
    conta_marcos = ContaCorrente(marcos, 2135, 123456)
    conta_marcos.depositar(100.00)
    return conta_marcos # Inicializa a conta com 100.00

@pytest.fixture
def emma():
    emma = Cliente("Emma", "123.456.789-00", "Atriz")
    return emma

@pytest.fixture
def conta_emma(emma):
    conta_emma = ContaCorrente(emma, 2136, 654321)
    conta_emma.depositar(100.00)
    return conta_emma # inicializa conta com 100.00


def test_deve_permitir_sacar_um_valor_quando_tiver_saldo_necessario_em_conta(conta_marcos):
    conta_marcos.sacar(100.00)
    assert conta_marcos.saldo == 0.0


def test_nao_deve_permitir_sacar_um_valor_quando_o_valor_for_maior_que_o_valor_em_conta(conta_marcos):
    with pytest.raises(SaldoInsuficienteError):
        conta_marcos.sacar(150.0)
        assert conta_marcos.saldo == 100.00


def test_nao_deve_permitir_sacar_um_valor_negativo(conta_marcos):
    with pytest.raises(ValueError):
        conta_marcos.sacar(-100.00)
        assert conta_marcos.saldo == 100.00


def test_nao_deve_permitir_transferir_um_valor_negativo(conta_marcos, conta_emma):
    with pytest.raises(ValueError):
        conta_marcos.transferir(-200.00, conta_emma)
        assert conta_marcos.saldo == 100.00 and conta_emma.saldo == 100.00


def test_deve_permitir_transferencia_quando_saldo_for_suficiente(conta_marcos, conta_emma):
    conta_marcos.transferir(50.0, conta_emma)
    assert conta_marcos.saldo == 50.0 and conta_emma.saldo == 150.00


def test_nao_deve_permitir_transferencia_quando_saldo_for_insuficiente(conta_marcos, conta_emma):
    with pytest.raises(SaldoInsuficienteError):
        conta_marcos.transferir(200.00, conta_emma)
        assert conta_marcos.saldo == 100.00 and conta_emma.saldo == 100.00


def test_deve_atualizar_saldo_quando_deposito_for_realizado(conta_marcos):
    conta_marcos.depositar(500.00)
    assert conta_marcos.saldo == 600.00
