# BaseProject — Testes e Qualidade de Software na Prática: Da Automação ao CI (UNIBRA)

Repositório base para as atividades práticas do curso de extensão de 40h.

## 1. Preparação do Ambiente (No seu computador)

```bash
# 1. Criar e ativar ambiente virtual
python -m venv .venv

# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Linux / macOS:
source .venv/bin/activate

# 2. Instalar dependências
pip install -r requirements.txt
```

## 2. Comandos Úteis

```bash
# Rodar apenas testes unitários
pytest tests/unit -v

# Rodar apenas testes de integração/API
pytest tests/integration -v

# Rodar tudo com relatório de cobertura
pytest --cov=src --cov-report=term-missing
```

## 3. Roteiro das Práticas em Sala

- **Prática 1 (Manhã):** Completar `tests/unit/test_desconto.py` aplicando padrão **AAA**, **Valor Limite** (`@pytest.mark.parametrize`) e **`pytest.raises`**.
- **Prática 2 (Tarde):** Completar `tests/integration/test_api_pedidos.py` testando os endpoints `POST /pedidos` e `GET /pedidos` com `TestClient` e verificando a cobertura com `pytest-cov`.
- **Prática 3 (Tarde):** Criar `.github/workflows/ci.yml` com dois jobs (`unit-tests` e `integration-tests` usando `needs: unit-tests`), fazer `git push` e acompanhar o pipeline no **GitHub Actions**.
