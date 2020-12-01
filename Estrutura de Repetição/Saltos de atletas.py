"""
Programa 086
Área de estudos.
data 01.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Área de declaração e inicialização de variaveis.
cont_atleta = 1
soma_saltos = 0
maior, menor = 0, 1000

# corpo do meu programa.
print('Para finalizar aperte "space" e em seguida "enter".')
while True:
    nome = str(input(f'Nome do {cont_atleta}º atleta.: '))
    if nome.isspace():
        print('Finalizando programa.')
        break

    for salto in range(1, 6):
        saltos = float(input(f'{salto}º Salto.: '))

        if saltos > maior:
            maior = saltos
        if saltos < menor:
            menor = saltos
    
        soma_saltos += saltos
    soma_saltos = (soma_saltos - maior - menor)
    media_saltos = (soma_saltos / 3)

    print('\n',
         '-'*20+'\n',
         f'Nome.: {nome}'+'\n',
         '\n',
         f'Média dos Saltos -- {media_saltos:.2f}'+'\n',
         '-'*20+'\n',
         )

    cont_atleta += 1
