"""
Programa 117
Área de estudos.
data 13.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Abrimos um arquivo para leitura no formato de texto.
arquivo = open('/home/abraao/Documentos/testando.txt', 'r') # Ou 'rt' Modo que nos permite ler.
texto = arquivo.read()
print(texto)
arquivo.close()

# Podemos também ler somente fatias desse texto.

arquivo = open('/home/abraao/Documentos/testando.txt', 'rt')
fatia_texto = arquivo.read()    # Ou fatia_texto = arquivo.read(30)
print(fatia_texto[4:31])
arquivo.close()
