"""
Programa 025
Área de estudos.
data 18.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""
# Coleta dos três valores.
prod1 = float(input('[1]Preço(R$).: '))
prod2 = float(input('[2]Preço(R$).: '))
prod3 = float(input('[3]Preço(R$).: '))

# Fazemos a verificação de valores comparando os três produtos.
if prod2 > prod1 < prod3:
    print(f'É melhor comprar o produto [1] com valor R${prod1:.2f}.')
elif prod1 > prod2 < prod3:
    print(f'É melhor comprar o produto [2] com valor R${prod2:.2f}.')
elif prod1 > prod3 < prod2:
    print(f'É melhor comprar o produto [3] com valor R${prod3:.2f}.')
elif prod1 == prod2 == prod3:
    print('Fique a vontade em escolher o produto que quiser.')
else:
    print('Sinto muito; mais nosso sistema não tem suporte para produtos com valores duplicados.')
