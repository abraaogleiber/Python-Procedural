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
while True: # loop inifinito.
    nome = str(input(f'Nome do {cont_atleta}º atleta.: '))  # Coleta do nome.
    # Verifica sequência de ações que encerram o programa.
    if nome.isspace():
        print('Finalizando programa.')
        break

    # Coleta dos saltos.
    for salto in range(1, 6):
        saltos = float(input(f'{salto}º Salto.: '))

        # Identifica o melhor e pior salto.
        if saltos > maior:
            maior = saltos
        if saltos < menor:
            menor = saltos
    
        soma_saltos += saltos   # Armagena todos os saltos.
    soma_saltos = (soma_saltos - maior - menor) # Descrementa o pior e o melhor salto.
    # Calcula a média, sabendo que somente os três saltos intermediários são considerados.
    media_saltos = (soma_saltos / 3) 

    # Saída do programa; com formatação.
    print('\n',
         '-'*20+'\n',
         f'Nome.: {nome}'+'\n',
         '\n',
         f'Média dos Saltos -- {media_saltos:.2f}'+'\n',
         '-'*20+'\n',
         )

    # Variavel que conta os atletas.
    cont_atleta += 1
