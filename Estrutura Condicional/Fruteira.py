"""
Programa 045
Área de estudos.
data 21.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Menu formatado, apresenta a tabela de frutas.
print( 
    'Tabela de Frutas\n'.center(35),
    '\n',
    'até 5kg \t acima de 5kg'.rjust(35)+'\n',
    '{}'.format('-'*36)+'\n',
    'Maçã'+'1.80(kg)'.rjust(17)+'1.50(kg)'.rjust(13)+'\n',
    'Morango'+'2.50(kg)'.rjust(14)+'2.20(kg)'.rjust(13)+'\n',
    '{}'.format('-'*36)+'\n',
    '\n',
     )

quant_maçã = float(input('Maçã[kg].: '))
quant_morango = float(input('Morango[kg].: '))


# Calculando kg da maçã.
if 0 < quant_maçã <= 5:
    valor_maçã = (quant_maçã * 1.80)
else:
    valor_maçã = (quant_maçã * 1.50)

# Calculando kg do morango.
if 0 < quant_morango <= 5:
    valor_morango = (quant_morango * 2.50)
else:
    valor_morango = (quant_morango * 2.20)


# Caso (kg) da compra ultrapasse 8 e o valor 25.
total_kg = (quant_maçã + quant_morango)
valor_total = (valor_maçã + valor_morango)

if total_kg > 8 or valor_total > 25:
    desconto = (valor_total * 10) / 100
    valor_total -= desconto 

# Saída do programa.
print(f'Total de (kg).: {total_kg:.2f}')
print(f'Valor total da compra R${valor_total:.2f}')
