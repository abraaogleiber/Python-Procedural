"""
Programa 065
Área de estudos.
data 25.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

contador, soma = 1, int()   # Atribuição multiplas.
while True:
    n = int(input(f'{contador}º Nota.: '))  # Entrada de dados.
   
    # Processamentos dos dados.
    soma += n
    contador += 1

    # Pergunta ao usuário, visando saber se ele deseja continuar com o programa.
    pergunta = str(input('Desejas Continuar(S/N).: ')).strip().upper()[0]
    while pergunta not in 'SN':
        pergunta = str(input('Desejas Continuar(S/N).: ')).strip().upper()[0]

    if pergunta in 'S':
        continue
    elif pergunta in 'N':
        break

contador -= 1   # Descrementamos 1 de contador já que na contagem 1 é acrescentado.
media = (soma / contador)
print(f'A média dos valores é {media:.2f}')
