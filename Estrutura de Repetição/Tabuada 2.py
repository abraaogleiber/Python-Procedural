"""
Programa 075
Área de estudos.
data 27.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Entrada da tabuada, inicio e termino dela.
tabuada = int(input('Montar Tabuada de.: '))
inicio = int(input('Comerça em.: '))
termina = int(input('Termina em.: '))

# Gerador de tabuada.
for t in range(inicio, termina+1):
    print(f'{tabuada:2} + {t:2} = {tabuada + t:2}')
