"""
Programa 023
Área de estudos.
data 18.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Coleta dos dados necessarios.
n1 = int(input('Primeiro número.: '))
n2 = int(input('Segundo número.: '))
n3 = int(input('Terceiro número.: '))

# Serie de verificações entre os três valores.
if n1 == n2 != n3 or n2 == n3 != n1 or n1 == n3 != n2:
    print('Por favor, não repita números.')
elif n2 < n1 > n3:
    print(f'O número {n1} é o maior.')
elif n1 < n2 > n3:
    print(f'O número {n2} é o maior.')
elif n1 < n3 > n2:
    print(f'O número {n3} é o maior.')
elif n1 == n2 == n3:
    print('Os três valores são iguais.')
elif n1 == n2 != n3 or n2 == n3 != n1 or n1 == n3 != n2:
    print('Por favor, não repita números.')
