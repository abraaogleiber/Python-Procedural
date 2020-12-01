"""
Programa 089
Área de estudos.
data 01.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Programa inacabado.
n = int(input('Termos.: '))
soma = 0
for operador in range(1, n+1):
    for divisor in range(1, n+n, 2):
            soma += (operador / divisor)
