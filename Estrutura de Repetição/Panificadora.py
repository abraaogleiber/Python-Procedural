"""
Programa 071
Área de estudos.
data 26.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Cabeçalho da tabela e o valor do pão na unidade.
print('{:-^40}'.format(' Panificadora um Pão e Meio '))
pão = 0.18

# Gerador da tabelo de preços.
for p in range(1, 51):
    print(f'{p:2} - R${pão*p:.2f}')
