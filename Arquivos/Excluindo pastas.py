"""
Programa 120
Área de estudos.
data 13.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

import os

# Vamos supor que queremos apagar um diretório inteiro.
if os.path.exists('/home/abraao/meus_pornos'):  # Se dentro do meu servidor existe essa pasta.
    os.rmdir('/home/abraao/meus_pornos')
    print('Apagado..')
else:
    print('Esta pasta não existe')
