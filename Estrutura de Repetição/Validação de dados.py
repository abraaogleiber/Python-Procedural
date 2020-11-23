"""
Programa 049
Área de estudos.
data 22.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

import time

while True:

    while True:
        nome = str(input('Nome.: ')).strip().lower()
        if len(nome) > 3:
            break
        else:
            print('Seu nome não pode conter menos que três caracteres.')
            continue

    while True:
        idade = int(input('Idade.: '))
        if 0 <= idade <= 150:
            break
        else:
            print('Sua idade não poder ser menor que 0 ou ser maior que 150 anos.')
            continue

    while True:
        sexo = str(input('Sexo(M/F).: ')).strip().lower()[0]
        if sexo in 'fm':
            break
        else:
            print('Sexo inválido.')
            continue

    while True:
        salario = float(input('Salário(R$).: '))
        if salario > 0:
            break
        else:
            print('Seu salário não poder ser menor que 0 -- "ZERO".')
            continue

    while True:
        est_civil = str(input('Estado Civil.: ')).strip().lower()[0]
        if est_civil in 'scvd':
            break
        else:
            print('Estado Civil inválido.')
            continue
    
    print('Salvando seus dados...Aguarde!')
    time.sleep(3)        
    break
