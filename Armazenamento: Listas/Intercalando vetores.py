"""
Programa 100
Área de estudos.
data 02.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Declaração e inicilização de listas.
lista_um, lista_dois, lista_tudo = list(), list(), list()

print('Digite os 10(dez) primeiro dados.')
for dado in range(1, 21):
    dados = str(input(f'{dado}º Dado.: ')).strip().capitalize()
    if dado <= 10:
        lista_um.append(dados)  # Somente os 10 primeiro dados.
    else:
        lista_dois.append(dados)    # Somente 10 ultimos dados.

# Conjuto de todos os valores.
lista_tudo = (lista_um + lista_dois)

print(lista_tudo)
