"""
Programa 108
Área de estudos.
data 08.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

cont = 0
salarios = list()

# Coleta de salários.
while True:
    salario = float(input(f'{cont+1:2}º Salário.: '))

    # Condição de parada.
    if salario == 0:
        print('Programa encerrado.')
        break
    if 100 <= salario <= 5500:
        salarios.insert(cont, salario)
        cont += 1
    else:
        print('O valor está fora do padrão salarial.')
        continue


# Calcula o valor do abono de cada salário.
abono = list()
for sl in range(len(salarios)):
    percentagem = (salarios[sl]*20) / 100
    if percentagem < 100:
        abono.insert(sl, 100)   # Esse é o piso do abono ou seja valor minimo a se receber.
    else:
        abono.insert(sl, percentagem)


# Processando a saída; com formatação.
# Esse trecho, realizo iteração por indice e somatória de valores.
soma_abono = 0
print('\n'*2)
print(' Salário(R$) '+'-'*10+' Abonos(R$) ')
for fun in range(len(salarios)):
    soma_abono += abono[fun]
    print(f'{salarios[fun]:.2f}'.rjust(10)+f'{abono[fun]:.2f}'.rjust(22))
print('\n')
print(f'Quantidade de salarios computados.: {len(salarios)}')
print(f'Total a ser gasto com abonos(R$).: {soma_abono:.2f}')
print(f'Nº de funcionários que receberam o piso.: {abono.count(100)}')
print(f'O maior valor a ser pago como abono é(R$).: {max(abono):.2f}')
print(f'O menor valor a ser pago como abono é(R$).: {min(abono):.2f}')
