"""
Programa 066
Área de estudos.
data 25.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

iteração, somatoria = 1, 0  # Atribuição multiplas.
while True:
    idade = int(input(f'{iteração}º Idade.: '))     # Entrada das idades.

    # Processamentos dos dados.
    somatoria = (somatoria + idade)
    iteração += 1

    # pergunta se o usuário deseja continuar.
    resposta = str(input('Desejas continuar(S/N).: ')).strip().upper()[0]
    while resposta not in 'NS':
        resposta = str(input('Desejas continuar(S/N).: ')).strip().upper()[0]

    if resposta == 'S':
        continue
    else:
        break

# Calculo da média aritmética.
media = somatoria / (iteração - 1)

# Verifica a média da turma e classifica a mesma como "Jovem", "Adulta", "Idosa".
if 0 <= media < 26:
    print(f'A turma é "Jovem" com média de idade de {media:.1f} anos.')
elif 26 <= media <= 60:
    print(f'A turma é "Adulta" com média de idade de {media:.1f} anos.')
elif media > 60:
    print(f'A turma é "Idosa" com média de idade de {media:.1f} anos.')
else:
    print('Por favor, verifique se as idades estão no padrão correto.[>0 e <150]')
