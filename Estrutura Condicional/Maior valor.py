"""
Programa 018
Área de estudos.
data 18.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Pedidos dois valores aleatórios ao usuário.
num1 = int(input('Digite um valor.: '))
num2 = int(input('Agora digite outro.: '))

# Fazemos as verificações. Utilizando condição encadeada.
if num1 > num2:
    print(f'{num1} é maior que {num2}.') 
elif num1 < num2:
    print(f'{num2} é maior que {num1}.')
else:
    print('Os valores são iguais.')
