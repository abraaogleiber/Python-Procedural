"""
Programa 004
Área de estudos.
data 14.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Coleta das quatros notas.
n1 = float(input('Primeira Nota.: '))
n2 = float(input('Segunda Nota.: '))
n3 = float(input('Terceira Nota.: '))
n4 = float(input('Quarta Nota.: '))

# Calculo da média, usando os parênteses para força ordem de precedência "0".
media = (n1 + n2 + n3 + n4) / 4

print(f'A média do aluno(a) é igual á {media:.1f}')
