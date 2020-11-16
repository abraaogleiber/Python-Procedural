"""
Programa 012
Área de estudos.
data 16.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Coleta da altura.
altura_usuario = float(input('Digite sua altura(m).: '))

# Procesamento da altura e calculo do peso ideal.
peso_ideal_homens = (72.7 * altura_usuario) - 58
peso_ideal_mulheres = (62.1 * altura_usuario) - 44.7

# Saída dos pesos calculados.
print(f'O peso ideal para homens com altura de {altura_usuario:.1f} é {peso_ideal_homens:.1f}')
print(f'O peso ideal para mulheres com altura de {altura_usuario:.1f} é {peso_ideal_mulheres:.1f}')
