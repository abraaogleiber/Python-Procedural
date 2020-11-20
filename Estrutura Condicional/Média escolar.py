"""
Programa 038
Área de estudos.
data 20.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Conjunto de notas.
n1 = float(input('1º Nota.: '))
n2 = float(input('2º Nota.: '))
n3 = float(input('3º Nota.: '))

# Média calculada.
media = (n1 + n2 + n3) / 3

# Série de verificação.
if 0 <= media < 7:
    print('Aluno: Reprovado')
elif 7 <= media < 10:
    print('Aluno: Aprovado')
elif media == 10:
    print('Aluno: Aprovado com distinção')
else:
    print('Verifique as notas repassadas, elas devem está fora do padrão.')
