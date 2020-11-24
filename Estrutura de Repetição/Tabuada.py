"""
Programa 056
Área de estudos.
data 24.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Entrada da tabuada que o usuário deseja.
tabuada = int(input('Qual tabuada.: '))

# Gerador de tabuada. Utilizando repetição definida.
for t in range(1, 11):
    print(f'{tabuada} + {t:2} = {tabuada + t:3}')

# Utilizando repetição indefinida com teste lógico.
t = 1
while t <= 10:
    print(f'{tabuada} + {t:3} = {tabuada + t:3}')

    t += 1
