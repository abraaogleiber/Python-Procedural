"""
Programa 124
Área de estudos.
data 15.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
""" 


def recolher_valores(lista):        # Função modificadora; efeito colateral.
    "A função executa uma iteração e recolhe três valores."
    for valor in range(1, 4):
        print(f'{valor}º Valor__|')
        v = int(input('>>> '))      # Escopo local.
        lista.append(v)


def somatoria(n1, n2, n3):      # Função frutífera.
    "Essa função recebe três args e retorna a soma. (Docstring)"

    return n1 + n2 + n3


def main():
    "Função principal. Corpo do meu algoritmo."

    valores = list()    # Estrutura que irá armazena os valores recolhidos.

    recolher_valores(valores)
    soma_resultado = somatoria(valores[0], valores[1], valores[2])
    print(f'A soma dos três valores é {soma_resultado}')


main()
