"""
Programa 083
Área de estudos.
data 29.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Cardápio com todos os items a venda.
print(
      '\n',
      '-'*4+'Cardápio'.center(35)+'-'*4+'\n',
      'Item'.rjust(10)+'Código'.rjust(19)+'Preço'.rjust(10)+'\n',
      '-'*43+'\n',
      'Sanduíche Simples'+'100'.rjust(10)+'6.80'.rjust(12)+'\n',
      'Sanduíche Casa'+'101'.rjust(13)+'7.40'.rjust(12)+'\n', 
      'Pão Irlândes'+'102'.rjust(15)+'10.60'.rjust(12)+'\n',
      'Bauru Portugues'+'103'.rjust(12)+'12.50'.rjust(12)+'\n',
      'Gulosão'+'104'.rjust(20)+'13.99'.rjust(12)+'\n',
      '-'*43+'\n',
     )
print('Obs.: Digite 0 Para finalizar o pedido.')

valor_pagar = float()
while True:
    item = int(input('Item(código).: '))
    # Saída do programa, finalização da venda.
    if item == 0:
        break
    quant = int(input('Quantidade.: '))

    # Saída do programa, finalização da venda.
    if item == 0:
        break

    # Verificações dos produtos escolhidos.
    if item == 100:
        valor_pagar += (quant * 6.80)
    elif item == 101:
        valor_pagar += (quant * 7.40)
    elif item == 102:
        valor_pagar += (quant * 10.60)
    elif item == 103:
        valor_pagar += (quant * 12.50)
    elif item == 104:
        valor_pagar += (quant * 13.99)
    else:
        print('Item inválido. Repita por gentileza.')

print(f'Total á pagar(R$).: {valor_pagar:.2f}')
