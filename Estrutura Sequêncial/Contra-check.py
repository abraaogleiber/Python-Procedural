"""
Programa 014 | Área de estudos. | data 17.11.2020 | (Indefinida) Hs
@Autor: Abraão A. Silva
"""

ValorHora = float(input('Valor da sua hora.: '))
quantHorasTrabalhadas = int(input('Quantidade de horas trabalhadas.: '))

# Cálculos e cobranças.
salarioBruto = ValorHora * quantHorasTrabalhadas
inss = (salarioBruto * 7.5) / 100
sindicato = (salarioBruto * 5) / 100
totalDescontos = (inss + sindicato)
salarioLiquido = (salarioBruto - totalDescontos)


print('{:=^35}\n'.format(' Extrato Salarial '),
      '\n',
      f'Salário Bruto --------- [R${salario_bruto:.2f}]\n',
      f'Imposto de Renda ------ [R${imp_renda:.2f}]\n',
      f'INSS ------------------ [R${inss:.2f}]\n',
      f'Sindcato -------------- [R${sindcato:.2f}]\n',
      f'Salário Líquido ------- [R${salario_liquido:.2f}]\n',
      '\n',
      f'Total de Descontos ---- [R${total_descontos:.2f}]\n',
      '\n',
      '='*35)
