"""
Programa 118
Área de estudos.
data 13.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Abrimos um arquivo para manipulação.
arquivo = open('/home/abraao/Documentos/testando.txt', 'r')     # Ou 'rt' Modo de leitura de texto.

texto = arquivo.read()      # Utilizamos o método 'splitlines' para transforma todas as linhas
lista = texto.splitlines()      # Em elementos de uma lista.
print(lista)

arquivo.close()


# Ou 

arquivo = open('/home/abraao/Documentos/testando.txt', 'rt')

lista = arquivo.readlines() # Utilizamos o método 'readlines' para gerar uma lista onde cada elemento é uma linha do arquivo.
print(lista)

arquivo.close()
