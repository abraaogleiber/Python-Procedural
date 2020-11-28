"""
Programa 077
Área de estudos.
data 28.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Entrada de dados.
salario = float(input('Salário do funcionário(R$).: '))
taxa = 1.5

# Estrutura de repetição definida; com uso de condição composta.
for ano in range(1995, 2020):
    if ano == 1995:
        continue
    elif ano == 1996:
        aumento = (salario * taxa) / 100
        novo_salario = (salario + aumento)
    else:
        taxa = (taxa * 2)
        aumento = (salario * taxa) / 100
        novo_salario = (salario + aumento)

# Saída de informações.
print(f'O salário do funcionario em 2020 é {novo_salario:.2f}')
