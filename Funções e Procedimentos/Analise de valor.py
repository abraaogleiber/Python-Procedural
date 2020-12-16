"""
Programa 126
Área de estudos.
data 16.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
""" 


def analisa_valor(l_num):   # Função não frutífera.
    "Recebe um valor e analisa o mesmo."

    if l_num <= 0:
        print('O número é Negativo.')
    else:
        print('O número é Positivo.')


def main():
    "Função principal."

    num = int(input('Digite um número.: '))
    analisa_valor(num) 


main()    # Primeira a ser chamada.
