"""
Programa 028
Área de estudos.
data 18.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Cabeçalho e coleta de informações.
print('[Obs: Digite "M" Matutino, "V" Vespertino ou "N" Noturno.]')
turno_user = str(input('Turno.: ')).strip().lower()
nome_user = str(input('Nome.: ')).strip().title()

# Verificamos onde se encaixa o turno do aluno e imprimimos uma saudação.
if turno_user == 'm':
    print('Olá {}, tenha um Bom dia de estudos.'.format(nome_user))
elif turno_user in 'v':
    print(f'Olá {nome_user}, tenha uma Boa tarde de estudos.')
elif turno_user == 'n':
    print(f'Olá {nome_user}, tenha uma Boa noite de estudos.')
else:
    print('Informação inválida.')
