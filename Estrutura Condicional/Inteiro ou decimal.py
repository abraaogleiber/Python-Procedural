"""
Programa 041
Área de estudos.
data 20.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Verificando se um número é dicimal ou inteiro.
numero = float(input('Digite um número.: '))
replica_numero = int(numero) # Criamos uma versão da parte inteira de "numero".

# Condição composta, verifica se é inteiro ou decimal.
if numero > replica_numero:
    print('Decimal')
else:
    print('Inteiro')
