"""
Programa 089
Área de estudos.
data 01.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Coleta da quantidade de termos e inicialização de variáveis.
n = int(input('Termos.: '))
soma = 0
divisor = 1

# Iteramos a quantidade de termos que o usuário desejar.
for operador in range(1, n+1):
    soma += (operador / divisor)    # Dividimos e logo somamos o resultado da divisão.

    divisor += 2 # Incrementamos 1 ao divisor.

print(soma)
