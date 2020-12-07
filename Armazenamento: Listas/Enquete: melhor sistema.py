"""
Programa 107
Área de estudos.
data 07.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

print('\n',
      '{:¨^43}'.format('Opções de Sistemas Operacionais')+'\n',
      '\n',
      'Windows Server'+'-'*25+'[1]'+'\n',
      'Linux'+'-'*34+'[2]'+'\n',
      'Unix'+'-'*35+'[3]'+'\n',
      'Netware'+'-'*32+'[4]'+'\n',
      'Mac Os'+'-'*33+'[5]'+'\n',
      'Outros'+'-'*33+'[6]'+'\n',
      '\n',
      '¨'*43+'\n',
      )


acumulo = list()

# Essa parte, colhe o voto, verifica sua validez e então armazena.
while True:
    voto = int(input('Voto.: '))

    if voto == 0:
        print('Votação Terminada.')
        break

    if not(1 <= voto <= 6):
        print('Opção não é válida...Repita!')
        continue
    else:
        acumulo.append(voto)

# Esse trecho, encontra o sistema mais votado e define o vencedor.
maior_incidencia = 0
for v in acumulo:
    if acumulo.count(v) > maior_incidencia:
        so = v
        maior_incidencia = acumulo.count(v)

if so == 1:
    vencedor = 'Windows Server'
elif so == 2:
    vencedor = 'Linux'
elif so == 3:
    vencedor = 'Unix'
elif so == 4:
    vencedor = 'Netware'
elif so == 5:
    vencedor = 'Mac Os'
elif so == 6:
    vencedor = 'Outros'
else:
    vencedor = 'Empate'

sistemas = ('Windows Server', 'Linux', 'Unix', 'Netware', 'Mac Os', 'Outros')
print(' {:-^54}'.format(' Relatório da enquete '))
print(' Sistema Operacional'+'Votos'.rjust(15)+'Percentagem'.rjust(20)+'\n',
      '-'*54)
for cont, s in enumerate(sistemas):
    percentagem = (acumulo.count(cont+1) * 100) / len(acumulo)
    print(' '+s.ljust(15) +
          f'{acumulo.count(cont+1):.0f}'.rjust(17)+f'{percentagem:.1f}'.rjust(19))
print()
print(f' Sistema Operacional vencedor.: {vencedor}')
print('-'*54)
