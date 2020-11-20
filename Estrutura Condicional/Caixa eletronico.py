"""
Programa 039
Área de estudos.
data 20.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Entrada do valor.
valor_saque = float(input('Valor do Saque.: '))

# Condição Binária, realizando os calculos e fazendo verificaçõe.
if 10 <= valor_saque <= 600:
    cedulas_cem = int(valor_saque / 100)
    cedulas_cinquenta = int(((valor_saque % 100) / 50))
    cedulas_dez = int(((valor_saque % 100) % 10) / 10)
    cedulas_cinco = int(((valor_saque % 100) % 10) / 5)
    cedulas_um = int((((valor_saque % 100) % 10) % 5) / 1)

    # Saída do relatório para o usuário.
    print(
        ' {:-^34}\n'.format(' Relatório de Saque '),
        f'Cédulas de Cem(100) ----------> {cedulas_cem}\n',
        f'Cédulas de Cinquenta(50) -----> {cedulas_cinquenta}\n',
        f'Cédulas de Dez(10) -----------> {cedulas_dez}\n',
        f'Cédulas de Cinco(5) ----------> {cedulas_cinco}\n',
        f'Cédulas de Um(1) -------------> {cedulas_um}\n',
        f'{"-"*34}\n',
         )
# Caso condição de cima não seja atendida.
else:
    print('Valor indisponível no momento.')
