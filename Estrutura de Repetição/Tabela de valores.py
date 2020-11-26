"""
Programa 070
Área de estudos.
data 26.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Cabeçalho da tabela.
print('{:-^40}'.format(' Loja na Beira do Ponto '))

# Gerador de preços.
valor_base = 1.99
for item in range(1, 51):
    print(f'{item:2} - R${valor_base*item:.2f}')
