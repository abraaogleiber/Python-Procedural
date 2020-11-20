"""
Programa 041
Área de estudos.
data 20.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Verificando se um número é dicimal ou inteiro.
numero = str(input('Digite um número.: ')).strip().lower()

if '.' in numero:
    print('Decimal')
else:
    print('Inteiro')
