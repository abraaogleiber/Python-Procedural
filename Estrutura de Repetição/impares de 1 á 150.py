"""
Programa 054
Área de estudos.
data 24.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Gerando valores impares dos parêmetros de "range()".

    # Opção 1
for num in range(1, 151):
    if num % 2 != 0:
        print(num, end=' ')


    # Opção 2
for num in range(1, 151, 2):
    print(num, end=' ')
