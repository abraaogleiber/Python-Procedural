"""
Programa 131
Área de estudos.
data 21.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""


def saida(n_int):
    "Recebe o retono de inverte_num() e cria uma representação ao usuário."
    print(f'O valor inverso é {n_int}')


def inverte_num(n):
    """Recebe um valor faz casting para str(), itera o resultado do casting, converte o resultado
    em int() e faz um retorno chamando a função saida()."""

    n_string = str(n)       # Casting
    i_string = str()

    for idx in range(1, len(n_string)+1):
        i_string += n_string[-idx]
    n_int = int(i_string)   # Casting

    return saida(n_int)


def coleta():
    "Recolhe um número do usuário."
    n = int(input('Digite um número.: '))

    return inverte_num(n)


def main():
    "Função principal."

    coleta()


main()
