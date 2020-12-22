"""
Programa 131
Área de estudos.
data 21.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""


def saida(tamanho):
    "A função retorna um print() da quantidade de dígitos."
    return print(f'O número tem {tamanho} dígitos.')


def conta(string):
    "A função recebe uma string e retorna a quantidade de digitos."
    return saida(tamanho=len(string))


def converte_str(n):
    "A função recebe um inteiro e converte (casting) para str()."
    string = str(n) 

    return conta(string=string)


def colher_num():
    "A função pede um número ao usuário."
    n = int(input('Digite um número.: '))

    return converte_str(n=n)


def main():
    "Função principal."

    colher_num()


main()
