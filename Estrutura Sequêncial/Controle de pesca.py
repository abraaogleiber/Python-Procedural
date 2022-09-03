"""
Programa 013 | Área de estudos. | data 16.11.2020 | (Indefinida) Hs
@Autor: Abraão A. Silva
"""

valorMultaPorQuilo = 4

quantDia = int(input('Dia da pesca -> '))
peso = float(input('Quantidade pescado(kg) -> '))

# O "excesso" tem o valor da quantidade pescada(kg), menos o peso maximo permitido.
pesoExcesso = (peso - 50)

# "Multa" tem o valor do excesso, multiplicado pelo valor da multa por kg excedente.
valorMulta = (pesoExcesso * valorMultaPorQuilo)

print('=-'*10, 'Relatório da Pesca', '-='*10)
print(f'Dia: {quantDia}')
print(f'Quantidade pescada(kg): {peso:.1f}kg')
print(f'peso excedente(kg): {pesoExcesso:.1f}kg')
print(f'Valor da multa: R${valorMulta:.2f}')
print('='*30)
