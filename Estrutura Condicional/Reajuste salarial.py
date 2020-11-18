"""
Programa 029
Área de estudos.
data 18.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

import time # importamos o módulo ou biblioteca "time" que trabalho com o tempo.

# Salário do colaborador.
salario_atual = float(input('Salário do colaborador(R$).: '))

# Avaliação do salário para ver em qual critério o mesmo se encaixa.
if 0 < salario_atual < 280: 
    reajuste = (salario_atual * 20) / 100
    novo_salario = salario_atual + reajuste
    percentagem = 20

elif 280 <= salario_atual < 700:
    reajuste = (salario_atual * 15) / 100
    novo_salario = salario_atual + reajuste
    percentagem = 15

elif 700 <= salario_atual < 1500:
    reajuste = (salario_atual * 10) / 100
    novo_salario = salario_atual + reajuste
    percentagem = 10

elif salario_atual >= 1500:
    reajuste = (salario_atual * 5) / 100
    novo_salario = salario_atual + reajuste
    percentagem = 5

# Relatório final do reajuste.
print('Gerando o Reajuste...Aguarde um pouco!')
time.sleep(3)
print(
    ' {:-^43}\n'.format(' Dados do Reajuste '),
    f'Salário Atual ----------------- R${salario_atual:.2f}\n', 
    f'Percentagem do Reajuste ------- {percentagem}%\n',
    f'Valor do Reajuste --------------R${reajuste:.2f}\n',
    f'Novo Salário -------------------R${novo_salario:.2f}\n',
    '{}\n'.format('-'*43),
     )
