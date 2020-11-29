"""
Programa 079
Área de estudos.
data 28.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

maior_indice, menor_indice, total_veiculos, total_acidentes, soma_veiculos = 0, 999, 0, 0, 0
for cidade in range(1, 6):
    print(f'{cidade}º Cidade...:::')
    num = int(input('Nº da Cidade.: '))
    quant_veiculos = int(input('Quant.: veículos de passeio.: '))
    num_acidentes = int(input('Nº de Acidentes.: '))

    # Processamento
    if num_acidentes > maior_indice:
        maior_indice = num_acidentes
        num_maior = num

    if num_acidentes < menor_indice:
        menor_indice = num_acidentes
        num_menor = num

    # Media de acidentes na cidade com nº de veículos inferior á 2000.
    if quant_veiculos < 2000:
        soma_veiculos += quant_veiculos
        total_acidentes += num_acidentes

    # Média de veículos.
    total_veiculos += quant_veiculos 


media_veiculos = (total_veiculos / 5)
media_acidentes = (total_acidentes / soma_veiculos)

print(f'Maior número de acidentes: Nº Cidade - {num_maior} Média - {maior_indice}')
print(f'Menor número de acidentes: Nº Cidade - {num_menor} Média - {menor_indice}')
print(f'As cidades tem em média {media_veiculos:.0f} veículos em circulação.')
print(f'A média de acidentes nas cidades com número com de veículos inferior á 2000 é {media_acidentes:.2f}.')
