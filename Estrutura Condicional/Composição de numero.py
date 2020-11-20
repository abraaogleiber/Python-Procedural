"""
Programa 037
Área de estudos.
data 20.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Entrada do valor.
numero = int(input('Digite um número (menor que mil).: '))

# Condição simpls ou unária com aninhamento.
# Os calculos são efetuados e verificados.
if numero < 1000:
    centena = int((numero % 1000) / 100)
    dezena = int((numero % 100) / 10)
    unidade = numero % 10

    if unidade == 0 and dezena != 0 and centena != 0:
        print(f'O valor é composto por {centena} Centena(s) e {dezena} Dezena(s).')
    elif unidade == 0 and dezena == 0 and centena != 0:
        print(f'O valor é composto por {centena} Centena(s).')
    elif unidade != 0 and dezena == 0 and centena != 0:
        print(f'O valor é composto por {centena} Centena(s) e {unidade} Unidade(s).')
    elif unidade != 0 and dezena != 0 and centena != 0:
        print(f'O valor é composto por {centena} Centena(s), {dezena} Dezena(s) e {unidade} Unidade(s).')
    elif unidade != 0 and dezena != 0 and centena == 0:
        print(f'O valor é composto por {dezena} Dezena(s) e {unidade} Unidade(s).')
    elif unidade != 0 and dezena == 0 and centena == 0:
        print(f'O valor é composto por {unidade} Unidade(s).')
