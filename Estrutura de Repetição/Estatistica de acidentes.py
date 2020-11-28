"""
Programa 079
Área de estudos.
data 28.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

maior_indice, menor_indice, total_veiculos, total_acidentes, quant_cidade = 0, 999, 0, 0, 0
for cidade in range(1, 6):
    print(f'{cidade}º Cidade...:::')
    num = int(input('Nº da Cidade.: '))
    quant_veiculos = int(input('Quant.: veículos de passeio.: '))
    num_acidentes = int(input('Nº de Acidentes.: '))

    # Processamento
    if num_acidentes > maior_indice:
        maior_indice = num_acidentes
        num_cidade = num

    if num_acidentes < menor_indice:
        menor_indice = num_acidentes
        num_cidade = num

    # Media de acidentes na cidade com nº de veículos inferior á 2000.
    if quant_veiculos < 2000:
        quant_cidade += 1
        total_acidentes += num_acidentes

    # Média de veículos.
    total_veiculos += quant_veiculos 


media_veiculos = (total_veiculos / 5)
media_acidentes = (total_acidentes / quant_cidade)

print(f'A cidade com maior número de acidentes tem Nº {num_cidade} com {maior_indice} acidentes registrados.')
print(f'A cidade com menor número de acidentes tem Nº {num_cidade} com {menor_indice} acidentes registrados.')
print(f'As cincos cidades juntas somam o total de {media_veiculos:.1f} veículos em circulação.')
print(f'As cidades com nº de veiculos inferior á 2000, possue uma taxa de acidentes igual á {media_acidentes:.2f}.')
