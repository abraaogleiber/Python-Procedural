"""
Programa 015
Área de estudos.
data 17.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# cabeçalho só para melhorar a iteratividade e experiência do usuário.
print('-='*25)
print('~ Orçamento para pinturas ~'.center(49))
print('=-'*25)

area = float(input('Área(m).: '))

# Sabendo que 1 litro de tinta pinta 3 metros quadrados, fizemos os calculos.
litros_tinta = int(area / 3)
quant_latas = round(litros_tinta / 18)
valor_latas = (quant_latas * 80)

# Resultado do orçamento.
print(f'Para pintar uma área de {area:.1f}(m), será necessário {quant_latas} lata(s) de tinta')
print(f'A(s) {quant_latas} lata(s) de tinta custará(ão) R${valor_latas:.2f}.')
