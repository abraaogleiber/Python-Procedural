"""
Programa 135
Área de estudos.
data 22.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""


def soma(*valores):
    "A função receberá dois valores e devolverá a soma deles."
    n = int()
    for valor in valores:
        n += valor

    return n


def multiplica(*valores):
    "A função receberá dois valores e devolverá a multiplicação dos mesmos."
    n = int()
    for valor in valores:
        n *= valor

    return n


def media(*valores):
    "A função retorna a média dos valores repassados."
    total = soma(*valores)
    return total / len(valores)
