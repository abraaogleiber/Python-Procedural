"""
Programa 022
Área de estudos.
data 18.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Notas do aluno.
n1 = float(input('1º Nota.: '))
n2 = float(input('2º Nota.: '))

# Calculo da média aritmética
media = (n1 + n2) / 2

# Verificação encadeada. Avalia o desempenho do aluno.
if 0 <= media < 7:
    print('Reprovado: média {:.1f}'.format(media))
elif 7 <= media < 10:
    print('Aprovado: média {:.1f}'.format(media))
elif media == 10:
    print('Aprovado com Distinção: média {:.1f}'.format(media))
else:
    print(' Por favor, verifique as notas repassadas, pois a média calculada \n',
          'não se encontra no parâmetro permitido -- [0 á 10].')
