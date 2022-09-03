"""
Programa 009  | Área de estudos. | data 15.11.2020 | (Indefinida) Hs
@Autor: Abraão A. Silva
"""

tempCelsius = float(input('Temperatura(°C).: '))
tempFahrenheit = float(input('Temperatura(F).: '))

converteParaCelsius = (tempFahrenheit - 32) * (5 / 9)
converteParaFahrenheit = (tempCelsius * 9/5) + 32

print(f'{tempFahrenheit:.1f}(F) \t {converteParaCelsius:.1f}(°C) \n'
      f'{tempCelsius:.1f}(°C) \t {converteParaFahrenheit:.1f}(F)')
