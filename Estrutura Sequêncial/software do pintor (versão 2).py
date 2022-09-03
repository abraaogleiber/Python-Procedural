"""
Programa 016 | Área de estudos. | data 17.11.2020 | (Indefinida) Hs
@Autor: Abraão A. Silva
"""

from math import ceil as aredondarCima

capacidadeGalhao = 6
capacidadeLata = 18
areaPintadaPorLitro = 6
valorLata = 80
valorGalhao = 25

area = float(input('Área -> '))

# Sabendo que 1 litro de tinta pinta uma área de 6m².
quantTinta = aredondarCima(area / areaPintadaPorLitro)
quantGalhoes = aredondarCima(quantTinta / capacidadeGalhao)
quantLatas = aredondarCima(quantTinta / capacidadeLata)

# Calculo dos preços.
precoLatas = (quantLatas * valorLata)
precoGalhoes = (quantGalhoes * valorGalhao)

print(
     ' {:=^30}\n'.format(' Opções de Compra '),
      f'Comprar somente Latas ------ {quantLatas}\n',
                f'Valor R${precoLatas}\n',
      f'Comprar somente Galhões ---- {quantGalhoes}\n',
                f'Valor R${precoGalhoes}\n',
     '{}\n'.format('='*30),
      )
