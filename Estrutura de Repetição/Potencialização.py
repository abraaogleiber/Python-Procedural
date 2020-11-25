"""
Programa 057
Área de estudos.
data 25.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Entrada de dados.
base = int(input('Base.: '))
expoente = int(input('Expoênte.: '))


contador = 0
resultado = 1
# Repetição com teste lógico.
while not(contador == expoente): # Operador lógico negando uma expressão booleana.
    resultado *= base # Operador de atribuição; com o padrão acumulador.

    contador += 1 # Variavel contadora.

print(resultado)
