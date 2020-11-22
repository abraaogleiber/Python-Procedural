"""
Programa 047
Área de estudos.
data 22.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""


    # Opção 1
# Utilizando repetição com teste lógico.
num = int(input('Digite um número entre 0 e 10.: '))

while not(0 <= num <= 10):
    print('O número que você digitou não está entre 0 e 10.')

    num = int(input('Digite um número entre 0 e 10.: '))
else:
    print('Muito obrigado pela colaboração.')


    # Opção 2
# Utilizando repetição indefinida, mas com funções de parada.
while True:
    num = int(input('Digite um número entre 0 e 10.: '))

    if 0 <= num <= 10:
        print('Muito obrigado pela sua colaboração.')
        break   
    else:
        print('Valor fora do parâmetro.')
