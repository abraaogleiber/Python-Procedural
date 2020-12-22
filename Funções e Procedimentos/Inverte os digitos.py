"""
Programa 130
Área de estudos.
data 21.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""


def saida(n_int):
    "Recebe o valor invertido e imprimi na tela."
    print(f'O valor inverso é {n_int}')


def inverter_num(n):
    "A função recebe um inteiro e converte para str() e retorna depois do processo um int(). "
    n_string = str(n)
    i_string = str()
    for dig in range(1, len(n_string)+1):
        i_string += n_string[-dig]
    n_int = i_string
    return saida(n_int)


def colher_num():
    "A função pedi um valor ao usuário e retorna à função inverter_num()."
    n = int(input('Digite um número.: '))

    return inverter_num(n=n)


def main():
    "Função principal."
    
    colher_num()


main()
