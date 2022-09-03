"""
Programa 017
Área de estudos.
data 17.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

"""
1 Byte é igual á 8 bits. Para calcular, temos que dividir a velocidade da conexão em (Megabits) por 8. ex: 10(velocidade) / 8 = 1.25 (MB/s) taxa de transferência.
Depois dividimos o tamanho do arquivo por pela taxa de transferência.

Equação = tamanho do arquivo (megabytes) / (velocidade da trasmissão em megabits / 8(bits)) = tempo segundo.
"""

tamanhoArquivo = float(input('Tamanho do arquivo(MB).: '))
velocidadeRede = float(input('Velocidade da rede(Mb/s).: '))

# Calculo do tempo de download em segundos e minutos.
taxaTransferencia = (velocidadeRede / 8)
tempoEstimadoSegundo = tamanhoArquivo / (velocidadeRede / 8)
tempoEstimadoMinuto = (tempoEstimadoSegundo / 60)

# Relatório de Download.
print(
    ' {:=^50}\n'.format(' Informações da Transferencia '),
    f'Taxa de Transferência ---- {taxaTransferencia:.3f}(MB)\n',
    f'Tempo de Download(s) ----- {tempoEstimadoSegundo:.0f} segundo(s)\n',
    f'Tempo de Download(m) ----- {tempoEstimadoMinuto:.1f} minuto(s)\n',
    '{}\n'.format('='*50),   
     )
