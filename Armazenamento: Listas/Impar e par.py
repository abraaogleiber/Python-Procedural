"""
Programa 093
Área de estudos.
data 02.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

pares, impares, todos = list(), list(), list() 

for n in range(1, 21):
    num = int(input(f'{n}º Número.: '))

    todos.append(num)
    if num % 2 == 0:
        pares.append(num) 
    else:
        impares.append(num)

print('---'+'Relatório'.center(20)+'---'+'\n',
     'Pares.:'+f'{len(pares)}'.rjust(15)+'\n',
     'Impares.:'+f'{len(impares)}'.rjust(13)+'\n',
     'Todos.:'+f'{len(todos)}'.rjust(15)+'\n',    
     )
