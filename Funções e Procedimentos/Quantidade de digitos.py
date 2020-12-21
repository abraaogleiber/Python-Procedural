"""
Programa 130
Área de estudos.
data 21.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""


def saída(r_valor):  # Pilha de execução.
    "Gera uma saída com o \"retorno de quant_digits\"."

    print(f'O valor tem {r_valor} digitos.')


def quant_digits(v):
    "Recebe um valor (int) convertemos para (str) e retornamos o len() do valor."
    v_string = str(v)

    return len(v_string)


def coleta_num():   # Não recebe parâmetros.
    "Quando chamada pede um valor ao usuário."
    numero = int(input('Digite um número.: '))

    return numero


def main():
    "Função principal do programa, onde chama-mos as outras funções."

    tamanho = quant_digits(coleta_num())
    saída(tamanho)


main()  # Função principal.
