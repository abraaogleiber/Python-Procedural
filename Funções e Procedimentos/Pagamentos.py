"""
Programa 129
Área de estudos.
data 19.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

import time, random


def relatorio_final(ts_t):
    "Docstring"

    print('¨'*40)
    print('Relatório de transações diária'.center(40))
    print('¨'*40)
    for t in ts_t:
        print('Transação Efetuada --> '+f'{t:.2f}'.rjust(10))
    print('_'*40)


def relatorio(dados_pag):
    """Recebe a tupla de retorno da função \"pagamento\", itera seus elementos 
    e retona uma saída elegânte."""

    if len(dados_pag) == 1:
        print('-'*30)
        print(' Relatorio '.center(30))
        print('-'*30)

        print('\n',
              'Valor Parc.: '+f'{dados_pag[0]:.2f}'+'\n',
              'Multa: '+f'{dados_pag[1]:.2f}'+'\n',
              'taxa \\ atraso: '+f'{dados_pag[2]:.2f}'+'\n',
              '\n',
              'Valor final: '+f'{dados_pag[3]:.2f}'+'\n',
              )
        print('-'*30)

    else:
        print('-'*30)
        print(' Relatorio '.center(30))
        print('-'*30)

        print('\n',
              'Valor Parc.: '+f'{dados_pag[0]:.2f}'+'\n',
              'Multa: '+f'R${dados_pag[1]:.2f}'+'\n',
              'taxa \\ atraso: '+f'R${dados_pag[2]:.2f}'+'\n',
              '\n',
              'Valor final: '+f'{dados_pag[3]}'+'\n',
              )
        print('-'*30)


def pagamento(vp, at):
    """Recebe as informações da função \"informações\", realiza os calculos de pagamento
    e retorna uma tupla contendo armazenandos todos os dados."""

    if at == 0:
        multa = atraso = 0
        valor_final = vp

        return (vp, multa, atraso, valor_final)
 
    else:
        multa = (vp * 3) / 100
        atraso = ((vp * 0.1) / 100) * at
        valor_final = (vp + multa + atraso)

        return (vp, multa, atraso, valor_final)


def informações():
    "Recebe e retorna duas informações, que serão utilizadas no decorrer do programa."

    # Optei por utilizar o modulo "Random" para facilitar meu entendimento.
    valor_parcela = random.randint(100, 10000)
    dia_atraso = random.randrange(1, 30)

    return (valor_parcela, dia_atraso)


def main():
    "Corpo principal do meu programa."

    quant_transações = list() 
    while True:
        retorno_inf = informações()
        retorno_pag = pagamento(vp=retorno_inf[0], at=retorno_inf[1])
        relatorio(dados_pag=retorno_pag)
        
        quant_transações.append(retorno_pag[3])
        
        ms = str(input('Deseja efetuar mais algum pagamento(s|n).: ')).strip().lower()[0]
        print('\n')
        while ms not in 'sn':
            print('Opção inexistente.')
            ms = str(input('Deseja efetuar mais algum pagamento(s|n).: ')).strip().lower()[0]
        if ms in 's':
            continue
        elif ms in 'n':
            print('Encerrando...')
            time.sleep(3)
            break

    relatorio_final(quant_transações)

main()  # Chamada ou invocação, modo composição.
