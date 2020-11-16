"""
Programa 011
Área de estudos.
data 16.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Entrada de dados do usuário.
print('='*5, 'Descubra seu peso ideal'.center(30), '='*5)
altura_usuario = float(input('Digite sua altura.: '))

# Calculo para descubrir o peso ideal, baseado na altura.
peso_ideal = (72.7 * altura_usuario) - 58

# saída de dados para o usuário.
print(f'Seu peso ideal baseado na sua altura é de {peso_ideal:.1f}(kg).')
