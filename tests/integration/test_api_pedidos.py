import pytest
from fastapi.testclient import TestClient

from src.app import PEDIDOS_DB, app

client = TestClient(app)


@pytest.fixture(autouse=True)
def limpar_banco_em_memoria():
    PEDIDOS_DB.clear()
    yield
    PEDIDOS_DB.clear()


def test_health_check_retorna_200():
    resp = client.get("/health")

    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_criar_pedido_com_desconto_e_frete_retorna_201():
    resp = client.post(
        "/pedidos",
        json={"item": "Teclado Mecânico", "valor": 200.0, "distancia_km": 10.0},
    )

    assert resp.status_code == 201
    dados = resp.json()
    assert dados["item"] == "Teclado Mecânico"
    assert dados["total_com_desconto"] == 180.0
    assert dados["frete"] == 25.0
    assert dados["total_final"] == 205.0


def test_criar_pedido_valor_negativo_retorna_400():
    resp = client.post(
        "/pedidos",
        json={"item": "Mouse", "valor": -10.0, "distancia_km": 5.0},
    )

    assert resp.status_code == 400
    assert "negativo" in resp.json()["detail"]


def test_criar_pedido_item_vazio_retorna_400():
    resp = client.post(
        "/pedidos",
        json={"item": "   ", "valor": 100.0, "distancia_km": 5.0},
    )

    assert resp.status_code == 400
    assert "obrigatório" in resp.json()["detail"]


def test_listar_pedidos_retorna_pedidos_cadastrados():
    client.post("/pedidos", json={"item": "Monitor", "valor": 500.0, "distancia_km": 10.0})

    resp = client.get("/pedidos")

    assert resp.status_code == 200
    lista = resp.json()
    assert len(lista) == 1
    assert lista[0]["item"] == "Monitor"
    assert lista[0]["frete"] == 0.0
