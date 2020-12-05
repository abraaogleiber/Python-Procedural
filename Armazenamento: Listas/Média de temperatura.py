"""
Programa 102
Área de estudos.
data 04.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Objeto do tipo lista.
temperaturas = list()
for mes in range(1, 13):    # Faz a coleta de 12 temperaturas.
    print(f'Período: {mes:2}.2020')
    temperaturas.append(float(input('Temperatura(°C).: '))) # Uso de método para alocar valor dentro da lista.

# Iteração que executa os calculos das temperaturas e define a média.
soma = 0
for temp in temperaturas:
    soma += temp
media = (soma / len(temperaturas))

# Estrutura dicionario para criar um mapa de meses do ano.
meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}

# Iteração que cuida da saída.
for mes, temp in enumerate(temperaturas):
    if temp > media:
        print(f'Em {meses[mes+1]} tivemos {temp:.1f}°C, que está acima da média.')
