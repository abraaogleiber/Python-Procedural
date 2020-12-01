"""
Programa 091
Área de estudos.
data 01.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Lista
valores = [1, 12, 34, 1, 9]

# Iteração por indíce.
for valor in range(1, len(valores)+1):
    print(valores[valor - (2*valor)], end=' ')


    # Opção 2; Utilizando método
valores.reverse()
print(valores)
