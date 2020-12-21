"""
Programa 132
Área de estudos.
data 21.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""


def resultado(valor_dados, rodada):
    "Função responsável por avaliar valores dos dados."

    # Caso Vitoria. 
    if rodada == 1:
        if valor_dados == 7 or valor_dados == 11:
            print('Você ganho!! Parabéns. \nStatus: Natural')
            return 0

        elif valor_dados == 2 or valor_dados == 3 or valor_dados == 12:
            print('Você perdeu!! Que pena. \nStatus: Craps')
            return 0

        else:   # Cobre valore: (4, 5, 6, 8, 9, 10)
            valor_rodada = valor_dados
            print('Você marcou!!! Parabéns. \nStatus: Ponto')
            return 1

    else:
        if valor_dados == 7:
            print('Você perdeu.')
            return 0

        elif valor_dados == valor_rodada:
            print('Você ganhou!! Parabéns. Status: Vitoria')
            return 0
        else:
            print(f'({valor_dados}) Vamos novamente...')
            return 1


def jogar_dados(n_rodada):
    "Função responsavel por gerar valores dos dados."

    import random
    import time

    print('Jogando os dados...')
    time.sleep(3)
    valor_rodada = random.randint(2, 12)   # Representa dois dados sendo lançados.
    rodada = n_rodada

    return resultado(valor_dados=valor_rodada, rodada=rodada)


def main():
    "Função principal, chama as demais funções."
    
    import time

    rodada = 1
    while True:
        print(f'<[{rodada}º Rodada]>')
        time.sleep(3)
        result = jogar_dados(n_rodada=rodada)

        if result == 0:
            break
        else:
            rodada += 1


main()
