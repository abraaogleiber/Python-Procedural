"""
Programa 103
Área de estudos.
data 05.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Uma lista com as perguntas que serão feitas.
perguntas = ['Telefonou para a vítima', 'Esteve no local do crime', 'Mora perto da vítima', 'Devia para a vítima', 'Já trabalhou com a vítima']

# Declaração e inicalização de variáveis.
respostas = list()
positivo, negativo = 0, 0

# Essa estrutura faz a pergunta, colhe a resposta e armazena na lista. 
for perg in range(5):
    pergunta = str(input(f'{perguntas[perg]} >> ')).strip().upper()[0]

    while pergunta not in 'SN':
        pergunta = str(input(f'{perguntas[perg]} >> ')).strip().upper()[0]

    respostas.insert(perg, pergunta)

# Essa estrutura ela examina a lista usando um método e toma uma decisão.
if respostas.count('S') == 1 or respostas.count('S') == 0: # Eu poderia ter simplificado usando,      
    print('Situação: Inôcente')                   # Operadores de comparação, mas o objetivo é o estudo.
elif respostas.count('S') == 2:
    print('Situação: Suspeito')
elif 3 <= respostas.count('S') <= 4:
    print('Situação: Cúmplice') 
elif respostas.count('S') == 5:
    print('Situação: Culpado')
