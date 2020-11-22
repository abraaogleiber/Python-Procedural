"""
Programa 046
Área de estudos.
data 22.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

import time # Módulo para controle do tempo de execução.

# Tabelo de opções e valores.
print(
    '\n',
    'Tabela de Preços'.rjust(30)+'\n',
    '\n',
    'Até 5(kg)'.rjust(30)+'Acima 5(kg)'.rjust(15)+'\n',
    '{}'.format('-'*45)+'\n',
    '[1]Filé Duplo'+'R$ 4.90'.rjust(16)+'R$ 5.80'.rjust(14)+'\n',
    '[2]Alcatra'+'R$ 5.90'.rjust(19)+'R$ 6.80'.rjust(14)+'\n',
    '[3]Picanha'+'R$ 6.90'.rjust(19)+'R$ 7.80'.rjust(14)+'\n',
    '{}'.format('-'*45),
     )
tipo_carne = int(input('Tipo da carne.: '))
quant_kg = float(input('Quantidade(kg).: '))


# Tabela de formas de pagamentos.
print(
    '\n',
    '{}'.format('-'*30)+'\n',
    'Forma de Pagamento'.center(30)+'\n',
    'Cartão ------------------ [C]\n',
    'Dinheiro ---------------- [D]\n',
    '{}'.format('-'*30)+'\n',
     )
forma_pagamento = str(input('Pagar com.: ')).strip().upper()[0]


# Verificação das entradas. Ver se a opção de carne e encaixa o valor correto segundo os critérios.
desconto = 0
if tipo_carne == 1:
    if 0 < quant_kg <= 5: # Verifica a quantidade de carne.
        valor_kg = 4.90
        valor_compra = (quant_kg * 4.90)
        if forma_pagamento == 'C':
            desconto = (valor_compra * 5) / 100
            valor_compra -= desconto
            
    elif quant_kg > 5:
        valor_kg = 5.80
        valor_compra = (quant_kg * 5.80)
        if forma_pagamento == 'C':
            desconto = (valor_compra * 5) / 100
            valor_compra -= desconto

elif tipo_carne == 2:
    if 0 < quant_kg <= 5:
        valor_kg = 5.90
        valor_compra = (quant_kg * 5.90)
        if forma_pagamento == 'C':
            desconto = (valor_compra * 5) / 100
            valor_compra -= desconto

    elif quant_kg > 5:
        valor_kg = 6.80
        valor_compra = (quant_kg * 6.80)
        if forma_pagamento == 'C':
            desconto = (valor_compra * 5) / 100
            valor_compra -= desconto
        
elif tipo_carne == 3:
    if 0 < quant_kg <= 5:
        valor_kg = 6.90
        valor_compra = (quant_kg * 6.90)
        if forma_pagamento == 'C':
            desconto = (valor_compra * 5) / 100
            valor_compra -= desconto

    elif quant_kg > 5:
        valor_kg = 7.80
        valor_compra = (quant_kg * 7.80)
        if forma_pagamento == 'C':
            desconto = (valor_compra * 5) / 100
            valor_compra -= desconto

else:
    print('Esse tipo de carne não foi tabelado.')


# Cupom fiscal.
print('Emitindo Cupom Fiscal...Aguarde!')
time.sleep(5)
print(
    '\n',
    '{}'.format('-'*30)+'\n',
    'Cupom Fiscal'.center(30)+'\n',
    '{}'.format('-'*30)+'\n',
    '\n',
    'Tipo da Carne:'+f'{tipo_carne}'.rjust(14)+'\n', 
    'Quantidade:'+f'{quant_kg:.0f}'.rjust(17)+'\n',
    'Preço(kg):'+f'{valor_kg:.2f}'.rjust(18)+'\n',
    'Desconto Apli.(R$):'+f'{desconto:.2f}'.rjust(9)+'\n',
    '\n',
    'Valor pago(R$):'+f'{valor_compra:.2f}'.rjust(13)+'\n',
    '{}'.format('-'*30)+'\n',
     )
