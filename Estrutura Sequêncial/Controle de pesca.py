"""
Programa 013
Área de estudos.
data 16.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Coleta do dia e peso pescado.
dia = int(input('Dia da pesca.: '))
peso = float(input('Quantidade de pescados(kg).: '))

# O "excesso" tem o valor da quantidade pescada, menos o peso maximo permitido.
excesso = (peso - 50)

# "Multa" tem o valor do excesso, multiplicado pelo valor da multa por kg excedente.
multa = excesso * 4

# Relatório da pesca.
print('=-'*10, 'Dados da Pesca', '-='*10)
print(f'Dia: {dia}')
print(f'Quantidade pescada(kg): {peso:.1f}kg')
print(f'peso excedente(kg): {excesso:.1f}kg')
print(f'Valor da multa: R${multa:.2f}')
print('='*30)
