"""
Programa 134
Área de estudos.
data 22.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

import random


def embaralha_string(string, imprime=False):
    "A função receberá uma string, irá itera-la e por fim despo de forma embaralhada"
    
    string_emb = random.sample(string, len(string))
    if imprime:
        for letra in string_emb:
            print(f'{letra}', end='')
        print()


def coleta_string():
    "Função será responsavel pela coleta das  informações."
    palavra = str(input('Digite sua palavra.: ')).strip().lower()

    return embaralha_string(string=palavra, imprime=True) 


def main():
    "Função principal."

    coleta_string()


main()
