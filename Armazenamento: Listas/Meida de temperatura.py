"""
Programa 102
Área de estudos.
data 04.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

temperaturas = list()
for mes in range(1, 13):
    print(f'{mes:2}.2020')
    temperaturas.append(float(input('Temperatura(°C).: ')))

soma = 0
for temp in temperaturas:
    soma += temp
media = (soma / len(temperaturas))

meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}


for mes, temp in enumerate(temperaturas):
    if temp > media:
        print(f'Em {meses[mes+1]} tivemos {temp:.1f}°C, que está acima da média.')
