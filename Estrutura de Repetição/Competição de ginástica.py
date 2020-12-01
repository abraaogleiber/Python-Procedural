"""
Programa 087
Área de estudos.
data 01.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Inicialização das variáveis.
cont_ginasta = 1
soma_notas = 0
maior, menor = 0, 1000

# Iteração do corpo principal.
while True:
    nome = str(input(f'Nome da {cont_ginasta}º ginasta.: ')).strip().title()
    if nome in 'tT': # Condição de parada.
        print('Programa finalizado.')
        break
    
    # Coleta das notas.
    for nota in range(1, 8):
        notas = float(input(f'{nota} Nota.: '))

        # Identificando maior e menor nota.
        if notas > maior:
            maior = notas
        if notas <  menor:
            menor = notas

        # Calculo da soma e subtração dos valores maior e menor; a média se define pelos valores intermédiarios.
        soma_notas += notas
    soma_notas = (soma_notas - maior - menor)
    media_notas = (soma_notas / 5)

    # Realtório das notas.
    print('\n',
           '*'*24+'\n',
           f'Nome Ginasta.: {nome}'.center(20),'\n',
           '\n',
           f'Melhor nota.: {maior:.2f}'+'\n',
           f'Pior nota.: {menor:.2f}'+'\n',
           '\n',
           f'Média.: {media_notas:.2f}'+'\n',
           '*'*24+'\n',
        )

    cont_ginasta += 1   # Contador de ginastas.
