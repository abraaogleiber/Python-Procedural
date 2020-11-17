"""
Programa 014
Área de estudos.
data 17.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Entrada dos dados do funcionário.
ganho_hora = float(input('Valor da sua hora.: '))
horas_trabalhadas = int(input('Quantidade de horas trabalhadas.: '))

# Calculos de imp. Renda, inss, sindcato, salario líquido e bruto.
salario_bruto = ganho_hora * horas_trabalhadas
imp_renda = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sindcato = (salario_bruto * 5) / 100
total_descontos = (imp_renda + inss + sindcato)
salario_liquido = (salario_bruto - total_descontos)

# Saída dos valores calculados.
print('{:=^32}'.format(' Extrato Salarial '))
print(f'Salário Bruto -------- [R${salario_bruto:.2f}]')
print(f'Imposto de Renda ----- [R${imp_renda:.2f}]')
print(f'INSS ----------------- [R${inss:.2f}]')
print(f'Sindcato ------------- [R${sindcato:.2f}]')
print(f'Salário Líquido ------ [R${salario_liquido:.2f}]')
print()
print(f'Total de descontos --- [R${total_descontos:.2f}]')
