"""
Programa 123
Área de estudos.
data 15.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""


def gerando_lista(num):     # Função Frutífera.
    "Docstring"
    minha_lista = [x for x in range(1, num+1)]
    return minha_lista


def sequencia(lista):       # Função Não Frutífera.
    "Docstring"
    for item in lista:
        print(lista[0:item-1])    # Estamos utilizando slice para retorna pedaços da lista.
        # Realizando um "Casting"

def main():     # Função "Principal". ou Procedimento.
    termino = int(input('Termino da sequência.: '))
    lista_retorno = gerando_lista(termino)
    sequencia(lista_retorno)


main()      # Padrão composição, uma função chama outra.
