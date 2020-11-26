"""
Programa 069
Área de estudos.
data 26.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Entrada do usuário.
quant_cds = int(input('Quantidade de CD`s.: '))

total_gasto = int()
for cd in range(1, quant_cds+1):
    print(f'{cd}º CD...:')
    valor = float(input('Valor do CD.: '))

    # Somatoria dos valores de cada cd.
    total_gasto += valor

# Calculo da media de valor gasto por cd.
media_valor = (total_gasto / quant_cds)

# Relatório do programa.
print(f'O total investido na coleção foi de R${total_gasto:.2f}')
print(f'A valor média gasto em cada CD foi de R${media_valor:.2f}')
