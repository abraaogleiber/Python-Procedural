"""
Programa 101
Área de estudos.
data 04.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

soma_alturas = 0
media_geral, quant_alunos = 0, 0
idades, alturas = list(), list()

for info in range(1, 11):
    print('{:~^30}'.format(str(info) + 'º Aluno:'))
    idades.append(int(input('Idade.: ')))
    alturas.append(float(input('Altura.: ')))
    print('~'*30)

    soma_alturas += alturas[info-1])


media_geral = (soma_alturas / len(alturas))

for idx in range(len(idades)):
    if idades[idx] > 13 and alturas[idx] < media_geral:
        quant_alunos += 1

print(f'A média de altura da turma é {media_geral:.2f}')
print(f'{quant_alunos} aluno(s) tem altura abaixo da média.')
