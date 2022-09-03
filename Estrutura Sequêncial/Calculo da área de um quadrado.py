"""
Programa 007 | Área de estudos | data 14.11.2020 | (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Calculo da área de um quadrado.
# Formula [A = l**2] ou [A = b.h]

from math import floor as fr 

lado = float(input("Valor de um lado do quadrado => "))
areaQuadrado = (lado ** 2)

print(f'A área do quadrado é igual a {round(areaQuadrado)}.')
print('O dobro dessa área é {}.'.format(fr(areaQuadrado*2)))
