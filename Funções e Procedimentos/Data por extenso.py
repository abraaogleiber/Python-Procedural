"""
Programa 133
Área de estudos.
data 22.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""


def imprime(func_coleta):
    "Docstring"
    meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

    mes = int(func_coleta[2:4])

    return print(f'{func_coleta[0:2]} de {meses[mes]} de {func_coleta[4:]}') 


def coleta():
    "Docstring"

    while True:
        data_user = int(input('Data[ddmmaaaa].:'))
        data_string = str(data_user)

        if len(data_string) < 8 or data_user < 111900 or data_user > 31122020:
            print('Null. Verifique o formato da data ou seus dados.')
            continue
        else:
            return imprime(func_coleta=data_string)


def main():
    "Função que chama as demais."
    coleta()


main()
