"""
Programa 011 | Área de estudos. | data 16.11.2020 | (Indefinida) Hs
@Autor: Abraão A. Silva
"""

print('='*5, 'Descubra seu peso ideal'.center(30), '='*5)
alturaUsuario = float(input('Digite sua altura -> '))

# Calculo para descubrir o peso ideal, baseado na altura.
pesoIdeal = (72.7 * alturaUsuario) - 58

print(f'Seu peso ideal baseado na sua altura é de {pesoIdeal:.1f}(kg).')
