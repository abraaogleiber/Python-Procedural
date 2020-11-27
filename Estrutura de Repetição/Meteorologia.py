"""
Programa 073
Área de estudos.
data 27.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

print('1º Temperatura...:')
temperatura = float(input('Temperatura(°C).: '))

contagem = 2
maior = menor = soma_temperatura = temperatura  # Apelidagem
while True:
    print(f'{contagem}º Temperatura...:')
    temperatura = float(input('Temperatura(°C).: '))    # Coleta das temperaturas.


    if temperatura > maior:     # Verifica a maior temperatura.
        maior = temperatura

    if temperatura < menor:     # Verifica a menor temperatura.
        menor = temperatura

    soma_temperatura += temperatura     # Acumulador (guarda a soma das temperaturas)

    # Analisa a resposta do usuário (quer continuar?)
    res = str(input('Deseja continuar(S/N).: ')).strip().upper()[0]
    while res not in 'NS':
        res = str(input('Deseja continuar(S/N).: ')).strip().upper()[0]
    if res == 'N':
        break
    else:
        contagem += 1
        continue

media = soma_temperatura / contagem
print(f'A maior temperatura é {maior} e a menor {menor}.')
print(f'A média de temperatura é {media:.1f}.')
