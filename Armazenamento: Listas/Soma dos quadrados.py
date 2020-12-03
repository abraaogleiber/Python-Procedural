"""
Programa 099
Área de estudos.
data 02.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Declaração e inicialização de variáveis e listas.
potencia = 0
numeros = list()

# Iteração para coleta de dados.
for n in range(10):
    numeros.append(int(input(f'{n+1:2}º Número.: ')))

    potencia += pow(numeros[n], 2)  # Poderia ser usado (x**2)

# Saída do programa.
print(f'A lista contém {len(numeros)} elementos')
print(f'Elementos.: {numeros}')
print(f'Soma das potências de cada elemento.: {potencia}')
