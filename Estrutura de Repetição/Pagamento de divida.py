"""
Programa 080
Área de estudos.
data 29.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Valor da divida.
valor_divida = float(input('Valor da divida.: '))

# Cabeçalho da tabela e montagem da tabela com "for"
print('Valor da Divida(R$)  Parcelas    Juros(R$)   valor da parcela(R$)')
for parcela in range(0, 13, 3): # Os valores iterados representam as parcelas.

    # Daqui pra baixo é feita uma série de verificações e calculos das parcelas e multas.
    if parcela == 0:
        parcela = 1
        valor_parcela = valor_divida
        juros = 0
        print(f'{valor_divida:.2f}'.rjust(13)+f'{parcela}'.rjust(12)+f'{juros:.1f}'.rjust(13)+f'{valor_parcela:.2f}'.rjust(19)+'\n')

    valor_parcela = float() # A cada laço "valor_parcela" e "valor_divida" é zerada.
    if parcela == 3:
        juros = (valor_divida * 10) / 100
        valor_divida += juros
        valor_parcela = (valor_divida / 3)
        print(f'{valor_divida:.2f}'.rjust(13)+f'{parcela}'.rjust(12)+f'{juros:.1f}'.rjust(15)+f'{valor_parcela:.2f}'.rjust(17)+'\n')
        valor_divida -= juros   # Estou descrementado o valor do juros pra não interferir no próximo calculo.

    valor_parcela = float()
    if parcela == 6:
        juros = (valor_divida * 15) / 100
        valor_divida += juros
        valor_parcela = (valor_divida / 6)
        print(f'{valor_divida:.2f}'.rjust(13)+f'{parcela}'.rjust(12)+f'{juros:.1f}'.rjust(15)+f'{valor_parcela:.2f}'.rjust(17)+'\n')
        valor_divida -= juros

    valor_parcela = float()
    if parcela == 9:
        juros = (valor_divida * 20) / 100
        valor_divida += juros
        valor_parcela = (valor_divida / 9)
        print(f'{valor_divida:.2f}'.rjust(13)+f'{parcela}'.rjust(12)+f'{juros:.1f}'.rjust(15)+f'{valor_parcela:.2f}'.rjust(17)+'\n')
        valor_divida -= juros

    valor_parcela = float()
    if parcela == 12:
        juros = (valor_divida * 25) / 100
        valor_divida += juros
        valor_parcela = (valor_divida / 12)
        print(f'{valor_divida:.2f}'.rjust(13)+f'{parcela}'.rjust(12)+f'{juros:.1f}'.rjust(15)+f'{valor_parcela:.2f}'.rjust(17)+'\n')
        valor_divida -= juros
