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
if inicio < termina:
    for t in range(inicio, termina+1):
        print(f'{tabuada:2} + {t:2} = {tabuada + t:2}')

else:
    print('O inicio não poder igual ao termino e o termino nao pode ser maior que o inicio.')
