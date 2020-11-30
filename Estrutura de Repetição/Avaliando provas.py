"""
Programa 085
Área de estudos.
data 30.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

aluno = int()   # Variavel contadora; vai contar o número de alunos
while True:
    soma_pontos = int() # Vai contabilizar os acertos de cada aluno. 
    for quest in range(1, 11):
        resp = str(input(f'{quest:2}º Questão.: ')).strip().upper()[0]  # Resposta das questões

        # Série de verificaçes.
        if quest == 1 and resp in 'A':
            soma_pontos += 1
        elif quest == 2 and resp in 'A':
            soma_pontos += 1
        elif quest == 3 and resp in 'D':
            soma_pontos += 1
        elif quest == 4 and resp in 'C':
            soma_pontos += 1
        elif quest == 5 and resp in 'D':
            soma_pontos += 1
        elif quest == 6 and resp in 'D':
            soma_pontos += 1
        elif quest == 7 and resp in 'B':
            soma_pontos += 1
        elif quest == 8 and resp in 'C':
            soma_pontos += 1
        elif quest == 9 and resp in 'A':
            soma_pontos += 1
    aluno += 1
    media_aluno = (soma_pontos / 1) # Calculo da média.
    print(f'A média do {aluno}º aluno é {media_aluno:.1f}') # Saída da média.

    # Verifica se tem mais algum aluno para usar o sistema.
    cont = str(input('Continuar(S/N)? ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Continuar(S/N)? ')).strip().upper()[0]
    if cont == 'N': # Saída do loop.
        break
