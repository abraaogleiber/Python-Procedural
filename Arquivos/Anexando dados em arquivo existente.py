"""
Programa 115
Área de estudos.
data 13.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Abrimos um arquivo para gravação de dados.
arquivo = open('/home/abraao/Documentos/testando.txt', 'w')     # Modo 'w' sobrescreve o arquivo.
while True:
    nome = str(input('Nome: '))

    if nome.isdigit():
        print('Programa encerrado.')
        break
    else:
        arquivo.write(nome+'\n')
arquivo.close()

# Ou

arquivo = open('/home/abraao/Documentos/testando.txt', 'a')     # Modo 'a' Anexa uma atrás da outra.
for n in range(3):
    nome = str(input('Nome: '))
    arquivo.write(nome+'\n')
arquivo.close()
