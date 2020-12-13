"""
Programa 116
Área de estudos.
data 13.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Abrimos o arquivo para leitura.
arquivo = open('/home/abraao/Documentos/testando.txt', 'rt')    # Ou 'r' modo que nos permite ler.

for linha in arquivo:   # Lendo linha por linha do arquivo.
    print(linha)
arquivo.close()


# Ou

arquivo = open('/home/abraao/Documentos/testando.txt', 'r') # Ou 'rt' modo que nos permite ler.

linha = arquivo.readline()  # utilizando método 'readline' para ler as linhas do arquivo.
while linha:
    print(linha)

    linha = arquivo.readline() # Direcionando o ponteiro de execução para proxima linha.
arquivo.close()
