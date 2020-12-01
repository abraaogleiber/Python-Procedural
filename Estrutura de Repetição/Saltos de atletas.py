"""
Programa 086
Área de estudos.
data 01.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

saltos = 0
maior, menor = 0, 1000
while True:
    nome = str(input('Nome do atleta.: '))
    for salto in range(1, 6):
        saltos = float(input(f'{salto}º Salto.: '))

        if saltos > maior:
            maior = saltos
        if saltos < menor:
            menor = saltos
    
        soma_saltos += saltos
    soma_saltos = (soma_saltos - maior - menor)
    media_salto = (soma_saltos / 3)

    print('\n',
         f'Nome.: {nome}'+'\n',
          '\n',
          f'Média dos Saltos -- {media_saltos:.1f}'+'\n', 
         )
