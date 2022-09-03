"""
Programa 008 | Área de estudos. | data 15.11.2020 | (Indefinida) Hs
@Autor: Abraão A. Silva
"""

valorHora = float(input("Valor da hora trabalhada.: "))
quantHorasMes = int(input("Quantas horas trabalhadas(mês).: "))

salario = (quantHorasMes * valorHora)

print(f'O seu salário base é de R${salario:.2f}')
