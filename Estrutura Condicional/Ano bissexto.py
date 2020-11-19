"""
Programa 035
Área de estudos.
data 19.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Ano retornado pelo usuário.
ano = int(input('Digite o ano para verificação.: '))

# Verificamos se o ano repassado será, é ou foi bissexto.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    if ano < 2020:
        print(f'O ano de {ano} foi bissexto.')
    elif ano == 2020:
        print(f'O ano de {ano} é bissexto.')
    else:
        print(f'O ano de {ano} será bissexto.')
else:
    if ano < 2020:
        print(f'O ano de {ano} não foi bissexto.')
    elif ano == 2020:
        print(f'O ano de {ano} não é bissexto.')
    else:
        print(f'O ano de {ano} não será bissexto.')
