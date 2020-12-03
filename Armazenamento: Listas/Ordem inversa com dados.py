"""
Programa 098
Área de estudos.
data 02.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Inicialização dos objetos listas.
lista_idade = []
lista_altura = []

# Iteração para colher os dados.
for repet in range(1, 6):
    print(f'{repet}º Sequência de dados.:')
    lista_idade.append(int(input('Idade.: ')))
    lista_altura.append(float(input('Altura(m).: ')))
    print('~'*30)

# O objetivo é reproduzir as listas da direita para a esquerda.
lista_idade.reverse()
lista_altura.reverse()
print(lista_idade)
print(lista_altura)


