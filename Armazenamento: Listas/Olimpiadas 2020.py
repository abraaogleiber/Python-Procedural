"""
Programa 105
Área de estudos.
data 06.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Declaraçao e inicialização de variavies simples e compostas.
media, saltos = list(), list()
saltos_t, nomes = list(), list()

# Essa parte colhe o nome do atleta e armazana um um vetor.
for atleta in range(1, 4):
    print(f'{atleta}º Atleta____|')
    nome = str(input('Nome >> ')).strip().capitalize()
    nomes.append(nome)

    # Esse pedaço colhe os saltos, calcula a média, armazena em uma lista.
    soma = 0
    for s in range(1, 6):
        salto = float(input(f'{s}º Salto.: '))
        saltos.append(salto)
        soma += salto
    saltos_t += [saltos[:]]
    media.append(soma / len(saltos))
    saltos.clear() # Lista auxiliar, é atualizada a cada laço.

    print('\n'*2)


# Procesamento da saída.
print('Nome'+'\tS1'+'\tS2'+'\tS3'+'\tS4'+'\tS5'+'\t\tMédia') # Formatamos usando o caractere de escape "\t".
print('~'*62)
for ex in range(len(nomes)):
    print(f'{nomes[ex]}', end='')
    for it in range(5):
        print(f'\t{saltos_t[ex][it]}', end='')
    print(f'\t\t{media[ex]:.2f}')
    print('\n') # Acessamos os elementos do array utilizando indíce.
print('~'*62)