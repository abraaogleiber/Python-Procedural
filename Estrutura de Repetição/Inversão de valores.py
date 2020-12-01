"""
Programa 088
Área de estudos.
data 01.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Coleta do valor.
n = int(input('Digite um valor.: '))
string_num = str(n) # Convertendo um "int" para "str".

# Gerando uma ordem inversa.
for num in range(1, len(string_num)+1):
    print(string_num[num-(2*num)], end=' ')
