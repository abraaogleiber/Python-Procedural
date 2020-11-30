"""
Programa 084
Área de estudos.
data 30.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Biblioteca que controla o tempo.
import time

# Cabeçalho da urna.
print('Eleições Presidenciais'.center(35)+'\n',
      '-'*30+'\n',
      'João Pé de Feijão'+'_'*10+'1'.rjust(3)+'\n',
      'Inácio Pelota'+'_'*14+'2'.rjust(3)+'\n',
      'Igor Ferradura'+'_'*13+'3'.rjust(3)+'\n',
      'Jonas Vai e Vem'+'_'*12+'4'.rjust(3)+'\n',
      '-'*30+'\n',
     )

# Inicialização das variaveis.
brancos = nulos = total_votos = 0
votos_1 = votos_2 = votos_3 = votos_4 = 0
while True:
    voto = int(input('Voto.: '))    # Coleta do voto.

    # Ponto de parada do loop.
    if voto == 1545:
        print('Finalizando urna...')
        time.sleep(3)
        break
    
    total_votos += 1
    if voto == 1:
        votos_1 += 1
    elif voto == 2:
        votos_2 += 1
    elif voto == 3:
        votos_3 += 1
    elif voto == 4:
        votos_4 += 1
    elif voto == 5:
        brancos += 1
    elif voto == 6:
        nulos += 1
    else:
        print('Candidato inválido.')
        total_votos -= 1

#  Calculos dos percentuais.
percentagem_nulos = (nulos * 100) / total_votos
percentagem_brancos = (brancos * 100) / total_votos

# Relatório do programa.
print()
print('Candidato'.rjust(13)+'Votos'.rjust(20))
print('\n',
      '-'*32+'\n',
      'João Pé de Feijão'+f'{votos_1}'.rjust(13)+'\n',
      'Inácio Pelota'+f'{votos_2}'.rjust(17)+'\n',
      'Igor Ferradura'+f'{votos_3}'.rjust(16)+'\n',
      'Jonas Vai e Vem'+f'{votos_4}'.rjust(15)+'\n',
      '-'*32+'\n',
     )

print('\n',
      'Brancos'+f'{brancos}'.rjust(13)+'\n',
      'Nulos'+f'{nulos}'.rjust(15)+'\n',
     )

print('\n',
      'Percentual Brancos'+f'{percentagem_brancos:.1f}'.rjust(15)+'\n',
      'Percentual Nulos'+f'{percentagem_nulos:.1f}'.rjust(17)+'\n',
     )
