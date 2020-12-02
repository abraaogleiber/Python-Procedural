"""
Programa 096
Área de estudos.
data 02.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

notas = list()
for aluno in range(1, 11):
    print(f'{aluno}º Aluno.:')
    nome = str(input('Nome.: ')).strip().title()
    for nota in range(1, 5):
        n = float(input(f'{nota}º Nota.: '))
    
        notas.append(n)

    soma = 0
    for nota in notas:
        soma += nota
    
    media = soma / len(notas)

    print('\n',
          '{:~^30}'.format(' Relatório ')+'\n',
          f'Nome.: {nome}'+'\n',
          '1º Nota --- '+f'{notas[0]:.2f}'.rjust(15)+'\n',
          '2º Nota --- '+f'{notas[1]:.2f}'.rjust(15)+'\n',
          '3º Nota --- '+f'{notas[2]:.2f}'.rjust(15)+'\n',
          '4º Nota --- '+f'{notas[3]:.2f}'.rjust(15)+'\n',
          '\n',
          'Média Final --- '+f'{media:.2f}'.rjust(11)+'\n',
          '~'*30
         )

    notas.clear()
