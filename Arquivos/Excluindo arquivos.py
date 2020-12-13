"""
Programa 119
Área de estudos.
data 13.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

import os

# os.remove('/home/abraao/Documentos/testando.txt')


# É bom sempre verificar a existencia de um arquivo antes de tenta apaga-lo.
if os.path.exists('/home/abraao/Documentos/testando.txt'):
    os.remove('/home/abraao/Documentos/testando.txt')
    print('Apagado..')
else:
    print('Arquivo inexistente.')
