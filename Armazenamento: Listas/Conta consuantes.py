"""
Programa 095
Área de estudos.
data 02.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Recolhe a palavra digitada.
palavra = str(input('Digite uma palavra.: ')).strip().upper()

contar_consuantes = 0   # Variável contador
consuantes = 'BCDFGJKLMNPQRSTVWXZ' # String de caracteres.

# Iteração por item
for letra in palavra:
    if letra in consuantes: # Verifica se letra da palavra é pertinênte dentro de consuantes
        contar_consuantes += 1

# Saída
print(f'Número de consunates na palavra.: {contar_consuantes}')
