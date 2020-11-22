"""
Programa 048
Área de estudos.
data 22.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

import time # Módulo de controle do tempo.

# Estrutura de repetição indefinido. Só encerra quando chamada uma das funções de parada.
while True:
    login = str(input('Login.: ')).strip().upper()
    senha = str(input('Senha.: ')).strip().upper()

    # Estrutura de condição encadeada.
    if login == senha:
        print('A senha e o login não podem ser iguais.')
        continue
    elif senha in login or login in senha:
        print('A Senha não pode conter partes do login ou vice-versa.')
        continue
    else:
        print('Salvando Login e Senha...Aguarde!')
        time.sleep(3)
        break
