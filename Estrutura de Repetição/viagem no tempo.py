"""
Programa 082
Área de estudos.
data 29.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

import random
import time


while True: # Enquanto existe espaço-tempo.
    espaço_tempo = random.choice([1, 2, 3])
        
    if espaço_tempo == 1:
        print('Passado')
    elif espaço_tempo == 2:
        print('Presente')
    elif espaço_tempo == 3:
        print('Futuro')
    time.sleep(1)

# Só pra descontrair.