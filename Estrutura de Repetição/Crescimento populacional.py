"""
Programa 050
Área de estudos.
data 23.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

pais_A = 80000
pais_B = 200000

# Itera até que o país A alcance o nivel populacional do país B.
anos = 0
while True:
    pais_A += (pais_A * 3) / 100
    pais_B += (pais_B * 1.5) / 100

    if pais_A >= pais_B:
        print(f'Serão preciso {anos} anos para que a população do Pais A alcance a do pais B.')
        break
    else:
        anos += 1
        continue
