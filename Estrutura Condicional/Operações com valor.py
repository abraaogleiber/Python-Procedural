"""
Programa 042
Área de estudos.
data 21.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Entrada do usuário.
num = float(input('Digite um número.: '))

# Menu de apresentação das opções.
print(
    '\n',
    ' Menu de Opções\n'.center(29),
    '\n',
    'Positivo | Negativo ------ [1]\n',
    'Impar | Par ---------------[2]\n',
    'Inteiro | Decimal ---------[3]\n',
    )
op = int(input('>>> ')) # Opção escolhida pelo usuário.

# Verifica se o número é positivo ou negativo.
if op == 1:
    if num < 0:
        print(f'O número {num:.0f} é Negativo.')
    else:
        print(f'O número {num:.0f} é Positivo.')

# Verifica se o número é impar ou par.
elif op == 2:
    if num % 2 != 0:
        print(f'O número {num:.0f} é "Impar".')
    else:
        print(f'O número {num:.0f} é "Par".')

# Verifica se o número é inteiro ou decimal.
elif op == 3:
    replica_num = int(num)
    if num > replica_num:
        print(f'O número {num} é "Decimal".')
    else:
        print(f'O número {num:.0f} é "Inteiro".')
