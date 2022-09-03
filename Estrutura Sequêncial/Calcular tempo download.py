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

tamanho_arquivo = float(input('Tamanho do arquivo(MB).: '))
velocidade_rede = float(input('Velocidade da rede(Mb/s).: '))

# Calculo do tempo estimado de download em segundos e minutos.
taxa_transferencia = (velocidade_rede / 8)
tempo_segundo = tamanho_arquivo / (velocidade_rede / 8)
tempo_minuto = (tempo_segundo / 60)

# Relatório de Download.
print(
    ' {:=^50}\n'.format(' Informações da Transferencia '),
    f'Taxa de Transferência ---- {taxa_transferencia:.3f}(MB)\n',
    f'Tempo de Download(s) ----- {tempo_segundo:.0f} segundo(s)\n',
    f'Tempo de Download(m) ----- {tempo_minuto:.1f} minuto(s)\n',
    '{}\n'.format('='*50),   
     )
