"""
Programa 125
Área de estudos.
data 15.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
""" 


# Somente estudo, sei que não precisava dessa função... ela retorna o valor passado.
def somando(v):   # Não sei quantos valores serão repassados, usei *args arbitrários
    "Docstring"

    somador = 0
    somador += v

    return somador


def recolher_valores(lista):     # Função frutífera, padrão modificador, com efeito colateral.
    "Docstring"

    itera = 1
    while True:
        print(f'{itera}º Valor______|')
        v = int(input('>>> '))

        if v == 0:
            print('Coleta encerrada...')
            break
        else: 
            lista.append(v)
        itera += 1
    return lista


def main():     # Chama as demais funções e suas respectivas intruções.
    "Docstring"

    soma = 0
    valores = list()

    print('A qualquer momento digite "0"(zero) para terminar a coleta.')
    lista = recolher_valores(valores)
    
    for idx in range(len(lista)):
        soma += somando(lista[idx])    

    print(f'A soma total é {soma}')


main()
