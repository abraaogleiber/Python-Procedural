"""
Programa 007
Área de estudos.
data 14.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Calculo da área de um quadrado.
# Formula [A = l**2] ou [A = b.h]

from math import ceil

lado = float(input('Um lado do quadrado.: '))
area = lado ** 2    # Ou area = lado * lado

print(f'A área do quadrado é igual a {round(area)}.')
print('O dobro dessa área é {}'.format(ceil(area*2)))
