"""
Programa 111
Área de estudos.
data 11.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

empresa, armazenamento = list(), list()

# Abrindo arquivo de texto com os dados.
relatorio = open('/home/abraao/relatorio.txt', 'r')

linha = relatorio.readline()    # Método que retornará uma linha do arquivo.
while linha:
    quebrado = linha.split()    # Nessa parte quebramos as linhas em palavras dentro de uma lista.
    
    # Armazenamento do dados desejados.
    empresa.append(quebrado[0])
    armazenamento.append(quebrado[1])

    linha = relatorio.readline()    # Essa sempre vai ser a proxima linha. (ponteiro)

relatorio.close()   # Depois que recolhemos os dados terminamos a manipulação.
