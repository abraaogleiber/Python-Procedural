"""
Programa 113
Área de estudos.
data 12.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Arquivo aberto para leitura.
arquivo = open('/home/abraao/comparativo', 'r')

# Arquivo criado e aberto para gravação subsequênte.
busca = open('/home/abraao/retorno_busca.txt', 'w')     # Criamos um arquivo para armazenar as linhas
for linha in arquivo:   # com a frase "departamento estadual de trânsito".
    if 'DEPARTAMENTO ESTADUAL DE TRÂNSITO' in linha:
        busca.write(linha)

# Fim da manipulação.
busca.close()
arquivo.close()
