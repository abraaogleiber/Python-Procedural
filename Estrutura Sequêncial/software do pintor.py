"""
Programa 015 | Área de estudos. | data 17.11.2020 | (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# cabeçalho só para melhorar a iteratividade e experiência do usuário.
print('-='*25)
print('~ Orçamento para pinturas ~'.center(49))
print('=-'*25)

area = float(input('Área(m) -> '))

# Sabendo que 1 litro de tinta pinta 3 metros quadrados.
litrosTinta = int(area / 3)
quantLatas = round(litrosTinta / 18)
valorLatas = (quantLatas * 80)

# Resultado do orçamento.
print(f'Para pintar uma área de {area:.1f}(m), será necessário {quantLatas} lata(s) de tinta')
print(f'A(s) {quantLatas} lata(s) de tinta custará(ão) R${valorLatas:.2f}.')
