"""
Programa 009
Área de estudos.
data 15.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Entrada de dados (input)
temperatura_celsius = float(input('Temperatura(°C).: '))
temperatura_fahrenheit = float(input('Temperatura(F).: '))

# Processamento das informações passadas.
converte_para_celsius = (temperatura_fahrenheit - 32) * 5/9
converte_para_fahrenheit = (temperatura_celsius * 9/5) + 32

# Saída do resultado da conversão.
print(f'{temperatura_fahrenheit:.1f}(F) \t {converte_para_celsius:.1f}(°C) \n'
      f'{temperatura_celsius:.1f}(°C) \t {converte_para_fahrenheit:.1f}(F)')
