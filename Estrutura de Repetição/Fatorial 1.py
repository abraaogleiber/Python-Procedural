"""
Programa 061
Área de estudos.
data 25.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

while True:
    # Entrada do valor.
    print('Descubra o fatorial de um número')
    valor = int(input('Número.: '))

    # O processo encontra o fatorial do valor.
    fatorial = 1
    print(f'{valor}!', end='= ')
    while valor > 0:
        if valor != 1:  # Condição como método de formatação.
            print(valor, end='x')
        else:
            print(valor, end=' = ')

        fatorial *= valor  # Calculo do fatorial.
        valor -= 1  # Processo de descremento até que cheguemos ao caso base.

    print(fatorial)

    # Perguntamos ao usuário se ele deseja continuar o programa.
    pergunta = str(input('Desejas continuar(S/N)?.: ')).strip().upper()[0]
    while pergunta not in 'SN':
        print('Resposta inválida..')
        pergunta = str(input('Desejas continuar(S/N)?.: ')).strip().upper()[0]
    if pergunta == 'S':
        continue
    elif pergunta == 'N':
        break
