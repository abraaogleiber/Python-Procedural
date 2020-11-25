"""
Programa 067
Área de estudos.
data 25.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# quantidade de eleitores.
quant_eleitores = int(input('Número de eleitores.: '))

# Acumuladora de votos (padrão contador).
v_pedroso, v_gleiber, v_mayra = int(), int(), int()

# Catálogo de candidatos.
print(
    ' {:-^30}'.format(' Candidatos Elegíveis ')+'\n',
    'Mário Pedroso'+'[20]'.rjust(16)+'\n',
    'Abraão Gleiber'+'[45]'.rjust(15)+'\n',
    'Elena Mayra'+'[15]'.rjust(18)+'\n',
    f'{"-"*30}'+'\n',
     )

# Faz a coleta dos votos e verifica o formato de dois(2) digitos.
for eleitor in range(1, quant_eleitores+1):
    print(f'{eleitor}º Eleitor....:')
    voto = int(input('Digite o número do seu candidato.: '))
    print('-'*40)

    if len(str(voto)) == 2:
        if voto == 20:
            v_pedroso += 1
        elif voto == 45:
            v_gleiber += 1
        elif voto == 15:
            v_mayra += 1
        else:
            while voto != 20 and voto != 45 and voto != 15:
                print('Não existe candidato com esse número!.')
                voto = int(input('Repita o número do seu candidato.: '))
            print('-'*40)

    else:
        while len(str(voto)) != 2:
            print('Você está votando para Presidente com dois(2) digitos.')
            voto = int(input('Repita o número do seu candidato.: '))
        print('-'*40)

# Calculo das médias.
m_pedroso = (v_pedroso * 100) / quant_eleitores
m_gleiber = (v_gleiber * 100) / quant_eleitores
m_mayra = (v_mayra * 100) / quant_eleitores

# Gera o status da eleição; qual candidato foi eleito.
if m_mayra < m_pedroso > m_gleiber:
    status_pedroso = 'Eleito'
else:
    status_pedroso = 'Não Eleito'

if m_mayra < m_gleiber > m_pedroso:
    status_gleiber = 'Eleito'
else:
    status_gleiber = 'Não Eleito'

if m_gleiber < m_mayra > m_pedroso:
    status_mayra = 'Eleita'
else:
    status_mayra = 'Não Eleita'

# Relatório da eleição.
print(
    ' {:-^68}'.format(' Resultado da Eleição ')+'\n',
    'Nome.:'.rjust(5)+'Quant.:'.rjust(20)+'per.:(%)'.rjust(20)+'Status.:'.rjust(20)+'\n',
    '-'*68 + '\n',
    'Mário Pedroso'+f'{v_pedroso}'.rjust(10)+f'{m_pedroso:.1f}'.rjust(22)+f'{status_pedroso}'.rjust(20)+'\n',
    'Abraão Gleiber'+f'{v_gleiber}'.rjust(9)+f'{m_gleiber:.1f}'.rjust(22)+f'{status_gleiber}'.rjust(20)+'\n',
    'Elena Mayra'+f'{v_mayra}'.rjust(12)+f'{m_mayra:.1f}'.rjust(22)+f'{status_mayra}'.rjust(20)+'\n',
    '-'*68 + '\n',
     )
