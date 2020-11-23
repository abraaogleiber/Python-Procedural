"""
Programa 052
Área de estudos.
data 23.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

maior = int()
for perg in range(1, 6):
    numero = int(input(f'Digite o {perg}º número.: '))

    if numero > maior:
        maior = numero

print(f'O maior valor repassado foi {maior}.')
