"""
Programa 081
Área de estudos.
data 29.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

cont = int()
while True:
    num = int(input('Digite um número.: '))

    if num >= 0:
        if 0 <= num <= 25:
            cont += 1
        if 26 <= num <= 50:
            cont += 1
        if 51 <= num <= 75:
            cont += 1
        if 76 <= num <= 100:
            cont += 1
    else:
        print('O número digitado é Negativo.')
        break

print(f'{cont} Números digitados estão dentro dos intervalos.')
