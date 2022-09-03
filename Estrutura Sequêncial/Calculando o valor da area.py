"""
Programa 006
Área de estudos.
data 15.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Calculo da área de uma circunferência.
# Formula A = Pi.r**2

PI = 3.14

raio = float(input('Valor do Raio.: '))
areaCircunferencia = PI * (raio**2)
print(f'A circunferência, cujo raio é {raio:.1f} tem área igual a {areaCircunferencia:.1f}.')
