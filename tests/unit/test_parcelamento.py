"""Testes unitários da Função 6 — simular_parcelamento (responsável: Carlos, P5).

Técnicas: padrão AAA, classes de equivalência, análise de valor limite
(@pytest.mark.parametrize) e validação de exceções (pytest.raises).
"""

import pytest

from src.parcelamento import simular_parcelamento


# Classe válida 1 — sem juros (1x a 3x). Limites: 1 (mínimo) e 3 (último sem juros).
@pytest.mark.parametrize(
    "parcelas, valor_parcela_esperado",
    [
        (1, 1200.00),
        (2, 600.00),
        (3, 400.00),
    ],
)
def test_parcelamento_ate_3x_sem_juros(parcelas, valor_parcela_esperado):
    # Arrange
    valor = 1200.00

    # Act
    resultado = simular_parcelamento(valor, parcelas)

    # Assert
    assert resultado["valor_parcela"] == valor_parcela_esperado
    assert resultado["total"] == valor
    assert resultado["com_juros"] is False
    assert resultado["parcelas"] == parcelas


# Classe válida 2 — com juros de 1,99% a.m. (4x a 12x). Limites: 4 (primeiro com juros) e 12 (máximo).
@pytest.mark.parametrize(
    "parcelas, valor_parcela_esperado, total_esperado",
    [
        (4, 315.07, 1260.28),
        (6, 214.16, 1284.96),
        (12, 113.40, 1360.80),
    ],
)
def test_parcelamento_de_4x_a_12x_com_juros(parcelas, valor_parcela_esperado, total_esperado):
    # Arrange
    valor = 1200.00

    # Act
    resultado = simular_parcelamento(valor, parcelas)

    # Assert
    assert resultado["valor_parcela"] == valor_parcela_esperado
    assert resultado["total"] == total_esperado
    assert resultado["com_juros"] is True
    assert resultado["total"] > valor


def test_parcelamento_sem_juros_total_igual_ao_valor_mesmo_com_arredondamento():
    # Arrange: 1000 / 3 = 333,333... (os centavos ficam na última parcela)
    valor = 1000.00

    # Act
    resultado = simular_parcelamento(valor, 3)

    # Assert
    assert resultado["valor_parcela"] == 333.33
    assert resultado["total"] == 1000.00


# Classe inválida — número de parcelas fora de 1 a 12. Limites: 0 e 13.
@pytest.mark.parametrize("parcelas", [0, 13, -1])
def test_parcelas_fora_do_limite_lanca_erro(parcelas):
    # Arrange
    valor = 1200.00

    # Act / Assert
    with pytest.raises(ValueError, match="Parcelamento inválido"):
        simular_parcelamento(valor, parcelas)


# Classe inválida — valor da compra zero ou negativo. Limite: 0.
@pytest.mark.parametrize("valor", [0, -50.00])
def test_valor_zero_ou_negativo_lanca_erro(valor):
    # Act / Assert
    with pytest.raises(ValueError, match="Parcelamento inválido"):
        simular_parcelamento(valor, 3)


# Classe inválida — parcelas que não são número inteiro.
@pytest.mark.parametrize("parcelas", [2.5, "3", True])
def test_parcelas_nao_inteiras_lanca_erro(parcelas):
    # Act / Assert
    with pytest.raises(ValueError, match="Parcelamento inválido"):
        simular_parcelamento(1200.00, parcelas)
