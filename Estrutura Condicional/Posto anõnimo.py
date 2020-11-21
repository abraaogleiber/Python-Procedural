"""
Programa 044
Área de estudos.
data 21.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Aplica descontos sobre combustível.
# entrada da litragem e tipo do combustível.
combustivel = str(input('Combustivel Vendido.: ')).strip().upper()[0]
quant_litros = float(input('Litros vendido.: '))

# Condição aninhada.
if combustivel == 'G': # Verifica a gasolina.
    if 0 < quant_litros <= 20:
        valor_integral = (quant_litros * 2.50)
        desconto = (valor_integral * 4) / 100
        valor_pagar = (valor_integral - desconto)
        print(f'Valor integral do abastecimento.: R${valor_integral:.2f}')
        print(f'Desconto de 4%, valor final R${valor_pagar:.2f}')

    elif quant_litros > 20:
        valor_integral = (quant_litros * 2.50)
        desconto = (valor_integral * 6) / 100
        valor_pagar = (valor_integral - desconto)
        print(f'Valor integral do abastecimento.: R${valor_integral:.2f}')
        print(f'Desconto de 6%, valor final R${valor_pagar:.2f}')

    else:
        print('Valores igual á "zero" ou abaixo disso não podem ser calculados.')

elif combustivel == 'A': # Verifica o álcool
    if 0 < quant_litros <= 20:
        valor_integral = (quant_litros * 1.90)
        desconto = (valor_integral * 3) / 100
        valor_pagar = (valor_integral - desconto)
        print(f'Valor integral do abastecimento.: R${valor_integral:.2f}')
        print(f'Desconto de 3%, valor final R${valor_pagar:.2f}')

    elif quant_litros > 20:
        valor_integral = (quant_litros * 1.90)
        desconto = (valor_integral * 5) / 100
        valor_pagar = (valor_integral - desconto)
        print(f'Valor integral do abastecimento>: R${valor_integral:.2f}')
        print(f'Desconto de 5%, valor final R${valor_pagar:.2f}')
    
    else:
        print('Valores igual á "zero" ou abaixo disso não podem ser calculados.')
else: # Caso entrada seja inválida.
    print('Error. Por favor digite "A" para álcool ou "G" para gasolina.')
