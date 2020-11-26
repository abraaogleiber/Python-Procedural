"""
Programa 068
Área de estudos.
data 26.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""


quant_turmas = int(input('Quantidade de turmas.: '))

total_alunos = int()
for turma in range(1, quant_turmas+1):
    print(f'{turma}º Turma...:')
    alunos = int(input('Quantidade de alunos.: '))

    total_alunos += alunos

media = (total_alunos / quant_turmas)

print(f'A média por turma é {media} alunos.')
