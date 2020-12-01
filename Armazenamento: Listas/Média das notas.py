"""
Programa 092
Área de estudos.
data 01.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Variável composta; aramzena dados de forma sequêncial, ordenado.
lista_notas = list()


somando_notas = 0
for nota in range(1, 5):  # Iteração para armazenamento.
    lista_notas.append(float(input(f'{nota}º Nota.: ')))

# Iteração por item.
for nota in lista_notas:
    somando_notas += nota

media = (somando_notas / 4) # Calculo da média.
print(f'A média do aluno é {media:.2f}')
