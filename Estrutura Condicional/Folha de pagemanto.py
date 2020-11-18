"""
Programa 030
Área de estudos.
data 18.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Coleta de dados do colaborador.
valor_hora = float(input('Valor da hora(R$).: '))
quant_hora = int(input('Quantidade de horas.: '))
salario_bruto = (quant_hora * valor_hora)

# Seleção encadeada.
if 0 < salario_bruto <= 900: # Se estiver entre 0 e 900. é isento.
    print('Colaboradores com esta faixa de ganho estão isentos de taxações.')
    exit()
    
elif 900 < salario_bruto <= 1500: # Se estiver entre 900 e 1500.
    imp_renda = (salario_bruto * 5) / 100 # É aplicado 5% de imposto de renda.
    inss = (salario_bruto * 10) / 100
    fgts = (salario_bruto * 11) / 100

    descontos = (imp_renda + inss)
    salario_liquido = (salario_bruto - descontos)

elif 1500 < salario_bruto <= 2500: # Se estiver entre 1500 e 2500.
    imp_renda = (salario_bruto * 10) / 100 # É aplicado 10% de imposto de renda.
    inss = (salario_bruto * 10) / 100
    fgts = (salario_bruto * 11) / 100

    descontos = (imp_renda + inss)
    salario_liquido = (salario_bruto - descontos)

elif salario_bruto > 2500: # Se estiver entre 2500 e maior.
    imp_renda = (salario_bruto * 20) / 100 # É aplicado 20% de imposto de renda.
    inss = (salario_bruto * 10) / 100
    fgts = (salario_bruto * 11) / 100

    descontos = (imp_renda + inss)
    salario_liquido = (salario_bruto - descontos)

# Relatório final da folha de pagamento.
print(
    '\n',
    f'Salário Bruto            : R${salario_bruto:.2f}\n',
    f'Imposto de Renda(-)      : R${imp_renda:.2f}\n',
    f'INSS(-)                  : R${inss:.2f}\n',
    f'FGTS                     : R${fgts:.2f}\n',
    f'Descontos                : R${descontos:.2f}\n',
    '\n',
    f'Salário Líquido          : R${salario_liquido:.2f}\n',
     )
