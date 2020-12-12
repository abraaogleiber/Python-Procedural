"""
Programa 112
Área de estudos.
data 12.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

import time

ips_validos, ips_invalidos = list(), list()

print('Lendo lista de ips...')
time.sleep(4)

# Abrimos o arquivo, iteramos suas linhas.
ips = open('/home/abraao/ips', 'r')


print('Validando ips...')
time.sleep(4)
for linha in ips:
    quebrando = linha.split('.')
    juntando = ''.join(quebrando)

    # Validando ip.
    if len(juntando) < 8:
        ips_invalidos.append(juntando)
    else:
        ips_validos.append(juntando)

ips.close() # Terminamos a leitura do arquivo.

print('Criando um arquivo na memória...')
time.sleep(4)
print('Armazenando os ips válidos...')
time.sleep(4)

# Criamos um arquivo e armazenamos ips válidos.
list_ips_validos = open('/home/abraao/list_ips_validos', 'w')

for ip in ips_validos:
    list_ips_validos.write(ip)

list_ips_validos.close()

print('Criando um arquivo na memória...')
time.sleep(4)
print('Armazenando ips inválidos...')
time.sleep(4)

# Criamos um arquivo e armazenamos ips invalidos.
list_ips_invalidos = open('/home/abraao/list_ips_invalidos', 'w')

for ip in ips_invalidos:
    list_ips_invalidos.write(ip)

list_ips_invalidos.close()

print('Encerrando processo...')
time.sleep(4)
print('Pronto!! foram criados dois arquivos na memória do seu computador!')
