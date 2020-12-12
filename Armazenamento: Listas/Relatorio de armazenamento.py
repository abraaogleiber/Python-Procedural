"""
Programa 111
Área de estudos.
data 11.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

megabytes, percentual = list(), list()
empresa, armazenamento = list(), list()
 
# Abrindo arquivo de texto com os dados.
relatorio = open('/home/abraao/relatorio.txt', 'r')

linha = relatorio.readline()    # Método que retornará uma linha do arquivo.
while linha:
    # Nessa parte quebramos as linhas em palavras dentro de uma lista.
    quebrado = linha.split()

    # Armazenamento do dados desejados.
    empresa.append(quebrado[0])
    armazenamento.append(quebrado[1])

    linha = relatorio.readline()    # Essa sempre vai ser a proxima linha. (ponteiro)

relatorio.close()   # Depois que recolhemos os dados terminamos a manipulação.

# Aqui iteramos os dados armazenando do espaço e convertemos de bytes para megabytes.
for item in armazenamento:
    calculo = (int(item) / 1024**2)
    megabytes.append(calculo)

# Realizamos a soma dos valores para definir o percentual.
soma = 0
for item in megabytes:
    soma += item

# Definimos os percentuias de armazenamento de cada empresa.
for items in megabytes:
    percen = (items * 100) / soma

    percentual.append(percen)


# Formantando uma saída.
print('{:-^58}'.format(' Relatório de armazenamento '))
print('Nº'+'Empresa'.rjust(16)+'Espaço'.rjust(18)+'Percentual'.rjust(20))
print('-'*58)
for c in range(len(empresa)):
    print(f'{c+1}'.ljust(10)+f'{empresa[c]}'.ljust(20) +
          f'{megabytes[c]:.2f}'.rjust(6)+f'{percentual[c]:.2f}%'.rjust(18))
