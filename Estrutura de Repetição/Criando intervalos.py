"""
Programa 055
Área de estudos.
data 24.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Entrada de dados.
n1 = int(input('Digite um número.: '))
n2 = int(input('Digite outro número.: '))

# Geramos os valores do intervalo passado (N1,N2).
if n1 < n2:
    for n in range(n1+1, n2):
        print(n, end=' ')
elif n2 < n1:
    for n in range(n2+1, n1):
        print(n, end=' ')
else:
    print('Não computamos valores iguais.')
