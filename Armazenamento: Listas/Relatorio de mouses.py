"""
Programa 110
Área de estudos.
data 08.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Declaração e inicialização das variáveis compostas.
codigo_objetos, relatorios = list(), list()

# Imprimi a tabela, recolhe as informações, faz verificações de validez, por fim armazena.
while True:
    print('{:-^46}'.format(' Opções de Relatório '))
    print('\n',
          'Necessita de esfera'+' '*23+'[1]'+'\n',
          'Necessita de limpeza'+' '*22+'[2]'+'\n',
          'Necessita troca de cabo ou conector'+' '*7+'[3]'+'\n',
          'Inutilizavel'+' '*30+'[4]'+'\n',
          '\n',
          '-'*46+'\n',
         )  

    codigo_mouse = int(input('Código identificador.: '))
    if codigo_mouse == 0:
        print('Programa encerrado...')
        print()
        break

    if codigo_mouse in codigo_objetos:
        print('Este objeto já foi cadastrado.')
        print()
        continue

    relatorio = int(input('Situação do Equipamento.: '))
    if relatorio < 0 or relatorio > 4:
        print('Opção inválida.')
        print()
        continue

    codigo_objetos.append(codigo_mouse)
    relatorios.append(relatorio)
    print()


# Definindo o percentual
percentual = list()

for item in range(1, 5):
    percentagem = (relatorios.count(item) * 100) / len(relatorios)
    percentual.append(percentagem)


# Formatando uma saída.
print(f' Quantidade de Mouses: {len(codigo_objetos)}')
print('\n', 
      f'[1]- Necessita da esfera'+f'{relatorios.count(1)}'.rjust(25)+f'{percentual[0]}%'.rjust(20)+'\n',
      f'[2]- Necessita de limpeza'+f'{relatorios.count(2)}'.rjust(24)+f'{percentual[1]}%'.rjust(20)+'\n',
      f'[3]- Necessita troca cabo ou conector'+f'{relatorios.count(3)}'.rjust(12)+f'{percentual[2]}%'.rjust(20)+'\n',
      f'[4]- Inutílizavel'+f'{relatorios.count(4)}'.rjust(32)+f'{percentual[3]}%'.rjust(20)+'\n',
      )
