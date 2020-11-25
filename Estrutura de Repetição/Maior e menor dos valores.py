"""
Programa 062
Área de estudos.
data 25.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

n = int(input('1º Número.: '))

contar = 2
maior = menor = soma = n   # Apelidagem
while 0 <= n <= 1000:
    n = int(input(f'{contar}º Número.: '))
    soma += n   # Somatória dos valores.

    # Condição que avalia quem é maior e menor.
    if n > maior:
        maior = n
    if n < menor:
        menor = n

    continuar = str(input('Continuar(S/N)?.: ')).strip().upper()[0] 
    # Repetição seguido de condição para avaliar a resposta do usuário.
    while continuar not in 'SN':
        print('Opção inválida.')
        continuar = str(input('Continuar(S/N).: ')).strip().upper()[0]
    if continuar == 'S':
        contar += 1
        continue    # Volta ao topo do "while" mais externo.
    elif continuar == 'N':
        break   # Para o programa.

print(f'O maior valor é {maior} e o menor {menor}')
print(f'A soma dos valores é {soma}.')
