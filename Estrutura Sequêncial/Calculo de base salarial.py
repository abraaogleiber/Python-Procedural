"""
Programa 008
Área de estudos.
data 15.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Capitação dos dados do usuário.
ganho_hora = float(input('Valor da hora trabalhada.: '))
horas_mes = int(input('Quantas horas trabalhadas(mês).: '))

# Calculo do salário base.
ganho_mensal = (horas_mes * ganho_hora)

# Iteratividade com o usuário
print(f'O seu salário base é de R${ganho_mensal}.')
