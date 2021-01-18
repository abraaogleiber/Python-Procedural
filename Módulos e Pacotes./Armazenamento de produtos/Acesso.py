# Este script contém as funções responsaveis pelo cadastro de inforações de acesso ao sistema
# como também seu armazenamento e validação de informações para acesso ao programa.
#
# @Auto: Abraão A. Silva

import time
import Menu_principal
import os

dicionario_info_usuario = dict()


def dicionario_bd(dicionario, lg, sn):
    "A função será responsavel pelo armazenamento dos dados de acesso."
    dicionario[lg] = sn

    if not os.path.exists('Arquivos_de_dados/Arquivo_loguinhos.txt'):
        arquivo_loguinos = open('Arquivos_de_dados/Arquivo_loguinhos.txt', 'x')
        arquivo_loguinos.close()

    arquivo_loguinos = open('Arquivos_de_dados/Arquivo_loguinhos.txt', 'at')
    arquivo_loguinos.write(f'{lg} {sn}\n')
    arquivo_loguinos.close()


def validando_acesso():
    "A função validará o login e senha permitindo o acesso."
    print('{:-^30}'.format(' Acesse sua conta '))
    login = str(input('Login: ')).strip().upper()
    senha = str(input('Senha: ')).strip()

    dados_txt = [] # lista
    arquivo_loguinhos = open('Arquivos_de_dados/Arquivo_loguinhos.txt', 'rt')
    for linha_txt in arquivo_loguinhos:
        login_txt = linha_txt.split()
        dados_txt += [{"Login": login_txt[0], "Senha": login_txt[1]}]
    arquivo_loguinhos.close()

    while True:
        for log in dados_txt:
            if login == log['Login'] and senha == log['Senha']:
                print('Acessando o sistema... Aguarde!!!')
                time.sleep(3)
                Menu_principal.menu_de_funcionalidade()
                exit()

        print('Login ou Senha inválido...')
        print('{:-^30}'.format(' Acesse sua conta '))
        login = str(input('Login: ')).strip().upper()
        senha = str(input('Senha: ')).strip()
        continue


def cadastro_de_usuario():
    "A função realiza o cadastro de login e senha para o acesso de usuários."
    print('{:-^30}'.format(' Cadastre-se '))
    login = str(input('Login: ')).strip().upper()
    while not(login.isalpha() and len(login) > 3):
        print('Login deve ser totalmente alfabetico e ter mais que três caracteres.')
        login = str(input('Login: ')).strip().upper()

    senha = str(input('Senha: ')).strip()
    while not(senha.isnumeric() and len(senha) > 3):
        print('A senha deve ser numerica e ter mais que três caracteres.')
        senha = str(input('Senha: ')).strip()

    return dicionario_bd(dicionario=dicionario_info_usuario, lg=login, sn=senha)
