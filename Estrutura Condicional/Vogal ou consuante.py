"""
Programa 021
Área de estudos.
data 18.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Coleta da letra.
letra = str(input('Digite uma letra.: ')).strip().upper()[0]

# Condição aninhada. Verifica se uma letra é "Vogal" ou "Consoante"
if letra.isalpha():
    if letra in 'AEIOU':
        print(f'Legal! A letra "{letra}" é uma Vogal.')
    else:
        print(f'Hum!! A letra "{letra}" é uma Consoante.')
else:
    print('Por favor, digite somente "LETRAS".')
