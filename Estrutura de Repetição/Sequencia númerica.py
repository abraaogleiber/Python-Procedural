"""
Programa 051
Área de estudos.
data 23.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

    # Opção 1
# Iteração por paraêmetro.
for num in range(1, 21):
    print(num)


    # Opção 2
# Iteração por item, estrutura de repetição com variavel de controle.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in lista:
    print(item, end=' ')


    # Opção 3
# Iteração por index (indíce).
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for idx in range(len(lista)):
    print(lista[idx], end=' ')
