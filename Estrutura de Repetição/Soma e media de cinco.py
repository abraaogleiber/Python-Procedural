"""
Programa 053
Área de estudos.
data 24.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

soma = int()
cont = int()
# Repetição definida com variavel de controle.
for n in range(1, 6):
    numero = int(input(f'{n}º Número.: '))

    # Processamneto dos dados.
    soma += numero
    cont += 1

media = soma / cont
print(f'A soma dos números digitados é {soma} e sua média é {media}.') # Saída
