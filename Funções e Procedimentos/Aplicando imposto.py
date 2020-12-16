"""
Programa 127
Área de estudos.
data 16.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
""" 


def aplica_imposto(valor, tx):
    "Processa o valor do imposto, calcula o imposto e retorna o imposto aplicado."

    imposto = (valor * tx) / 100
    aplicando = (valor + imposto)

    return aplicando


def main():
    "A Função principal"

    v = float(input('Valor do produto(R$).: '))
    t = int(input('Taxa(%).: '))

    valor_final = aplica_imposto(valor=v, tx=t)

    print(f'O valor final do produto é R${valor_final:.2f}')


main()
