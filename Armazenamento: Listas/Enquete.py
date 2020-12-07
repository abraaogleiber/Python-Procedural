"""
Programa 106
Área de estudos.
data 06.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Declaração e inicialização de variáveis.
acumulo = list()
jogadores = [x for x in range(1, 24)]

# Trecho responsavel pela coleta do voto.
while True:
    voto = int(input('Número da camisa.: '))

    if voto not in jogadores and voto != 0:
        print('Não existe jogador com esta camisa.')
        continue

    if voto == 0:
        print('Votação encerrada.')
        break
    else: # Caso não seja "0" ou qualquer valor fora do paramêtro.
        acumulo.append(voto)

# Armazenará a maior percentagem.
maior_percentagem = 0

# Saída formatada com iteração de arrays ou processamento de seus dados.
print('\n',
      '^'*42+'\n',
      'Camisa'.rjust(8)+'Nº Votos'.rjust(15)+'Percentual'.rjust(17)+'\n',
      '^'*42+'\n',
      )
for camisa in jogadores:
    if acumulo.count(camisa) != 0:
        percentagem = (acumulo.count(camisa) * 100) / len(acumulo)

        if percentagem > maior_percentagem:
            maior_percentagem = percentagem

        print(f'{camisa}'.rjust(6)+f'{acumulo.count(camisa)}'.rjust(15)+f'{percentagem:.1f}%'.rjust(17))
print()
print(f'Total de votos computados -- {len(acumulo)}')
print(f'O campeão teve {maior_percentagem:.1f}% dos votos.')
print('~'*42)
