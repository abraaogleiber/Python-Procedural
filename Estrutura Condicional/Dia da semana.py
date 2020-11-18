"""
Programa 031
Área de estudos.
data 18.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Valor de entrada
numero = int(input('Digite um valor para ver seu dia correspondente.: '))

# Série de verificações. Processamento de dados.
if numero == 1:
    print('[1]-- Domingo')
elif numero == 2:
    print('[2]-- Segunda-Feira')
elif numero == 3:
    print('[3]-- Terça-Feira')
elif numero == 4:
    print('[4]-- Quarta-Feira')
elif numero == 5:
    print('[5]-- Quinta-Feira')
elif numero == 6:
    print('[6]-- Sexta-Feira')
elif numero == 7:
    print('[7]-- Sábado')
else:
    print('Valor inválido.') # Saída de dados; Assim como todos os "prints".
