"""
Programa 095
Área de estudos.
data 02.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Recolhe a palavra digitada.
palavra = str(input('Digite uma palavra.: ')).strip().upper()

lista_consuantes = list()   # Armazenará minhas consuantes.
consuantes = 'BCDFGJKLMNPQRSTVWXZ' # String de caracteres.

# Iteração por item
for letra in palavra:
    if letra in consuantes: # Verifica se letra da palavra é pertinênte dentro de consuantes
        lista_consuantes.append(letra)

# Saída
print(f'Número de consunates na palavra.: {len(lista_consuantes)}')
for consu in lista_consuantes:
    print(consu, end=' ')

# ou

print('\n', lista_consuantes)
