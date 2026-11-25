"""Função 6 — Simulação de parcelamento no cartão (responsável: Carlos, P5).

Regras de negócio:
- RN10: valor da compra maior que zero e parcelas entre 1 e 12 (número inteiro).
- RN11: de 1x a 3x sem juros; o total é o próprio valor da compra
  (os centavos do arredondamento ficam na última parcela).
- RN12: de 4x a 12x com juros de 1,99% ao mês, calculados pela Tabela Price.
"""

TAXA_JUROS_CARTAO = 0.0199
MAX_PARCELAS_SEM_JUROS = 3
MIN_PARCELAS = 1
MAX_PARCELAS = 12


def _parcela_price(valor: float, taxa: float, parcelas: int) -> float:
    """Parcela fixa pela Tabela Price: PMT = V × i / (1 − (1 + i)^(−n))."""
    return round(valor * taxa / (1 - (1 + taxa) ** -parcelas), 2)


def simular_parcelamento(valor: float, parcelas: int) -> dict:
    """Simula uma compra no cartão de 1x a 12x.

    Retorna um dicionário com o número de parcelas, o valor de cada parcela,
    o total pago e se houve juros. Lança ValueError para entradas inválidas.
    """
    if isinstance(parcelas, bool) or not isinstance(parcelas, int):
        raise ValueError("Parcelamento inválido")
    if valor <= 0 or parcelas < MIN_PARCELAS or parcelas > MAX_PARCELAS:
        raise ValueError("Parcelamento inválido")

    if parcelas <= MAX_PARCELAS_SEM_JUROS:
        return {
            "parcelas": parcelas,
            "valor_parcela": round(valor / parcelas, 2),
            "total": round(valor, 2),
            "com_juros": False,
        }

    valor_parcela = _parcela_price(valor, TAXA_JUROS_CARTAO, parcelas)
    return {
        "parcelas": parcelas,
        "valor_parcela": valor_parcela,
        "total": round(valor_parcela * parcelas, 2),
        "com_juros": True,
    }
