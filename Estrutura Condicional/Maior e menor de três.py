"""
Programa 024
Área de estudos.
data 18.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Entrada dos valores.
n1 = int(input('1º Número.: '))
n2 = int(input('2º Número.: ')) 
n3 = int(input('3º Número.: '))

# Verificação do maior valor. seleção encadeada.
if n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
    print('Por favor, não repita valores.')
    exit()
elif n2 < n1 > n3:
    print(f'O maior é {n1}.')
elif n1 < n2 > n3:
    print(f'O maior é {n2}.')
elif n1 < n3 > n2: 
    print(f'O maior é {n3}.')
elif n1 == n2 == n3:
    print('Os três valores são iguais.')
    exit()

# Verificação do menor valor. seleção encadeada.
if n2 > n1 < n3:
    print(f'O menor é {n1}.')
elif n1 > n2 < n3:
    print(f'O menor é {n2}.')
elif n1 > n3 < n2:
    print(f'O menor é {n3}.')
