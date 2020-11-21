"""
Programa 043
Área de estudos.
data 21.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# conjunto de perguntas.
perg1 = str(input('Você telefonou para a vitíma.: ')).strip().lower()[0]
perg2 = str(input('Você esteve no loca do crime.: ')).strip().lower()[0]
perg3 = str(input('Você morava perto da vitíma.: ')).strip().lower()[0]
perg4 = str(input('Vocẽ devia à vitíma.: ')).strip().lower()[0]
perg5 = str(input('Você já trabalhou com a vitḿa.: ')).strip().lower()[0]

# Criando um string para verificação na condição.
resp_suspeito = (perg1 + perg2 + perg3 + perg4 + perg5)
print('')

# Serie de verificações.
if resp_suspeito.count('s') == 2:
    print('Classificação.: Suspeito')
elif 3 <= resp_suspeito.count('s') <= 4:
    print('Classificação.: Cúmplice')
elif resp_suspeito.count('s') == 5:
    print('Classificação.: Assasino')
else:
    print('Classificação.: Inocente')
