"""
Programa 004
Área de estudos.
data 14.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Coleta das quatros notas.
nota1 = float(input('Primeira Nota.: '))
nota2 = float(input('Segunda Nota.: '))
nota3 = float(input('Terceira Nota.: '))
nota4 = float(input('Quarta Nota.: '))

# Calculo da média, usando os parênteses para força ordem de precedência "0".
mediaFinal = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A média do aluno(a) é igual á {mediaFinal:.1f}')
