"""
Programa 058
Área de estudos.
data 25.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Atribuição multipla.
soma, pares, impares = int(), int(), int()

# Coleta de dados com repetição.
for numero in range(1, 11):
    n = int(input(f'{numero:2}º Número.: '))
   
    soma += n
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

# Saída de dados.
print(f'A soma de todos valores é {soma}')
print(f'Ao todo temos {pares} pare(s) e {impares} impare(s).')