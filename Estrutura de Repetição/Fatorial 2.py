"""
Programa 072
Área de estudos.
data 27.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""


numero = int(input('Digite um número.: '))
fatorial = 1

print(f'{numero}!= ', end='')
for num in range(numero, 0, -1):
    if num != 1:
        print(num, end='x')
    else:
        print(num, end='= ')
    
    fatorial *= num

print(fatorial)
