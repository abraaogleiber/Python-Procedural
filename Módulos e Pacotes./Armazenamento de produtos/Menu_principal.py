# Este script contém as funções necessarias para cadastro de produtos,
# visualização de estoque e apresentação de menu de opções.
#
# @Autor:  Abraão A. Silva


import os
import time
import random

# Esta é a variável composta para armazenamento dos produtos.
lista_de_produtos = list()


def modelo_cupon_fiscal(*info):
    "Docstring."
    cupon = f'''
    ----------------------------------------------
                    Cupon Fiscal
    ----------------------------------------------
    Nº do Cupon: {info[0]}            Serie: {info[1]}
    CNPJ: {info[2]}      
    -|---------------------|--------------------|-
    
    Produto: {info[3]}        Valor Unit.: R${info[4]} 
    Quantidade: {info[5]}
    
    
    Valor Total: R${info[6]}   
    
    
    
    
    ----------------------------------------------
                    Multiplástico
    ----------------------------------------------
            '''
    print(cupon)


def gerar_cupon_fiscal():
    "Docstring."
    num_cupon = random.randint(1000, 2000)
    serie_cupon = random.randint(10, 12)
    CNPJ = '987.123.0001/12'
    produto = str(input('Nome produto: ')).strip().capitalize()
    valor_unit = float(input('Valor unit.: '))
    quant = int(input('Quantidade: '))
    valor_total = (valor_unit * quant)

    return modelo_cupon_fiscal(num_cupon, serie_cupon, CNPJ, produto, valor_unit, quant, valor_total)


def consulta_de_estoque():
    "A função retorna um relatório dos produtos já cadastrados."

    print(' Salvando informações no arquivo "Produtos_cadastrados.txt"...Aguarde!!')
    cria_e_salva_arquivo_txt()
    time.sleep(3)

    print('-'*70)
    print('Produto'.rjust(14)+'Quantidade'.rjust(32)+'Preço unit.'.rjust(23))
    print('-'*70)
    produtos_cadastrados = open('Arquivos_de_dados/Produtos_cadastrados.txt', 'rt')
    for linha in produtos_cadastrados:
        info_produto = linha.split('|')
        print(f'{info_produto[0]}'.ljust(25)+f'{info_produto[1]}'.rjust(15)+f'R${info_produto[2]}'.rjust(25), end='')
    produtos_cadastrados.close()
    print('-'*70)


def cria_e_salva_arquivo_txt():
    "A funçõa simplismente cria ou abri um arquivo de texto e adiciona as informações dos produtos."

    if not os.path.exists('Arquivos_de_dados/Produtos_cadastrados.txt'):
        produtos_cadastrados = open('Arquivos_de_dados/Produtos_cadastrados.txt', 'xt')
        produtos_cadastrados.close()

    produtos_cadastrados = open('Arquivos_de_dados/Produtos_cadastrados.txt', 'at')
    for prod in lista_de_produtos:
        produtos_cadastrados.write(f'{prod["Produto"]}'+'|'+f'\t{prod["Quantidade"]}'+'|'+f'{prod["Preço"]}'+'\n')
    produtos_cadastrados.close()


def cadastro_de_produtos():
    "A função realizará o cadastro de produtos."

    print(' {:-^30}'.format(' Cadastro de Produto '))
    while True:
        print(' '+'-'*30)
        nome_produto = str(input(' Nome(Produto): ')).strip().capitalize()
        if nome_produto == '0':
            break

        quantidade = int(input(' Quantidade: '))
        valor_unit = float(input(' Valor Unit.: '))
        lista_de_produtos.append({'Produto': nome_produto, 'Quantidade': quantidade, 'Preço': valor_unit})


def menu_de_funcionalidade():
    "A função imprimirá um menu, ira colher uma opção e então avaliar o retorno."

    while True:
        print('\n',
              '{:-^30}'.format(' Menu de opções ')+'\n',
              'Cadastro de produtos ----> '+'[1]'+'\n',
              'Consulta de estoque  ----> '+'[2]'+'\n',
              'Gerar cupon fiscal   ----> '+'[3]'+'\n',
              'Sair                 ----> '+'[0]'+'\n',
              '-'*30, end='')
        print()

        try:
            op = int(input(' >>> '))
            if op == 1:
                cadastro_de_produtos()
            elif op == 2:
                consulta_de_estoque()
            elif op == 3:
                gerar_cupon_fiscal()
            elif op == 0:
                print(' Fechando programa...')
                time.sleep(3)
                break
            else:
                print(' Esta opção não existe. Repita novamente.')
        except ValueError:
            print(' Por gentileza, digite somente um dos valores indicados.')
