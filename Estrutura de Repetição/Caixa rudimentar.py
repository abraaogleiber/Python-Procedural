"""
Programa 074
Área de estudos.
data 27.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

print('---'+'Supermercado Amigo do Povo'+'---')

total_compra = int()
while True:
    valor = float(input('Preços(R$).: '))
    total_compra += valor

    # Fleg (ponto de parada), chama o enceramento da compra.
    if valor == 0:
        print('-----Finalização da compra-----')
        quant_pagamento = float(input('Valor repassado(R$).: \t'))
        troco = (quant_pagamento - total_compra)

        print(f'Valor Total(R$).: \t{total_compra:.2f}')
        print(f'Troco(R$).: \t\t{troco:.2f}')

        total_compra = int()
        print()
        print('---'+'Supermercado Amigo do Povo'+'---')
