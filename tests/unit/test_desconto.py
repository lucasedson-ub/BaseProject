import pytest

from src.desconto import calcular_desconto, calcular_frete


@pytest.mark.parametrize(
    "valor,esperado",
    [
        (0.0, 0.0),
        (50.0, 50.0),
        (99.99, 99.99),
        (100.0, 90.0),
        (200.0, 180.0),
    ],
)
def test_calcular_desconto_faixas_e_limites(valor, esperado):
    # Arrange / Act
    resultado = calcular_desconto(valor)

    # Assert
    assert resultado == esperado


def test_calcular_desconto_rejeita_valor_negativo():
    with pytest.raises(ValueError, match="negativo"):
        calcular_desconto(-0.01)


@pytest.mark.parametrize(
    "valor_pedido,distancia_km,esperado",
    [
        (200.0, 50.0, 0.0),
        (350.0, 10.0, 0.0),
        (199.99, 0.0, 25.0),
        (50.0, 0.0, 10.0),
    ],
)
def test_calcular_frete_regras(valor_pedido, distancia_km, esperado):
    assert calcular_frete(valor_pedido, distancia_km) == esperado


@pytest.mark.parametrize("valor_pedido,distancia_km", [(-1.0, 10.0), (50.0, -5.0)])
def test_calcular_frete_rejeita_valores_negativos(valor_pedido, distancia_km):
    with pytest.raises(ValueError, match="negativ"):
        calcular_frete(valor_pedido, distancia_km)
