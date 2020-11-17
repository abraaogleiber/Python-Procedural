"""
Programa 016
Área de estudos.
data 17.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

import math

area = float(input('Área.: '))

# Sabendo que 1 litro de tinta pinta uma área de 6 metros quadrados, fizemos os calculos.
quant_tinta = math.ceil(area / 6)
quant_galhoes = math.ceil(quant_tinta / 3.6)
quant_latas = math.ceil(quant_tinta / 18)

# Calculo dos preços.
preço_latas = (quant_latas * 80)
preço_galhoes = (quant_galhoes * 25)

# Saída do relatório dos valores.
print(
     ' {:=^30}\n'.format(' Opções de Compra '),
      f'Comprar somente Latas ------ {quant_latas}\n',
                f'Valor R${preço_latas}\n',
      f'Comprar somente Galhões ---- {quant_galhoes}\n',
                f'Valor R${preço_galhoes}\n',
     '{}\n'.format('='*30),
      )
