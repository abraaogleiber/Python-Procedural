"""
Programa 033
Área de estudos.
data 18.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

l1 = int(input('Lado[1].: '))
l2 = int(input('Lado[2].: '))
l3 = int(input('Lado[3].: '))

# Condição Binária com aninhamento.
# Verificamos a viabilidade de um triângulo pela as médidas dos lados.
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:  
    if l1 == l2 == l3:
        print('Nós temos com os dados um triângulo Equilátero.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Nós temos com os lados um triângulo Isósceles.')
    else:
        print('Nós temos um triângulo Escaleno.')
else:
    print('Os lados informados NÃO PODEM FORMA UM TRIÂNGULO.')
