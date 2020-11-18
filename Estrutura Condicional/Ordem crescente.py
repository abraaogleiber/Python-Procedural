"""
Programa 026
Área de estudos.
data 18.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Coleta dos valores.
num1 = int(input('1º Número.: '))
num2 = int(input('2º Número.: '))
num3 = int(input('3º Número.: '))

# Verificação dos valores com comparação.
if num1 == num2 != num3 or num1 == num3 != num2 or num2 == num3 != num1:
    print('Por favor, somente valores diferetes.')

elif num2 > num1 < num3 and num2 < num3:
    print(f'[{num1}][{num2}][{num3}]')
elif num2 > num1 < num3 and num3 < num2:
    print(f'[{num1}][{num3}][{num2}]')

elif num1 > num2 < num3 and num1 < num3:
    print(f'[{num2}][{num1}][{num3}]')
elif num1 > num2 < num3 and num3 < num1:
    print(f'[{num2}][{num3}][{num1}]')

elif num1 > num3 < num2 and num1 < num2:
    print(f'[{num3}][{num1}][{num2}]')
elif num1 > num3 < num2 and num2 < num1:
    print(f'[{num3}][{num2}][{num1}]')

elif num1 == num2 == num3:
    print('Os valores são iguais.')
