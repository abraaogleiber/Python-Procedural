"""
Programa 012 | Área de estudos. | data 16.11.2020 | (Indefinida) Hs
@Autor: Abraão A. Silva
"""

alturaUsuario = float(input('Digite sua altura(m).: '))

# Procesamento da altura e calculo do peso ideal.
pesoIdealHomens = (72.7 * alturaUsuario) - 58
pesoIdealMulheres = (62.1 * alturaUsuario) - 44.7

print(f'O peso ideal para homens com altura de {alturaUsuario:.1f} é {pesoIdealHomens:.1f}')
print(f'O peso ideal para mulheres com altura de {alturaUsuario:.1f} é {pesoIdealMulheres:.1f}')
