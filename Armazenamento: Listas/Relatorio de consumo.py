"""
Programa 109
Área de estudos.
data 08.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Criação das variáveis compostas; estruturas de armazenamento.
carros, kms = list(), list()

# Entrada das informações e armazenamento.
for cars in range(1, 5):
    print('{}'.format(str(cars)+'º Carro__|'))
    carro = str(input('Veículo: ')).strip().title()
    carros.append(carro) 

    km = float(input('Km por Litro: '))
    kms.append(km)
    print('\n')


# Modelo mais econômico.
maior_km = 0
for k in range(len(kms)):
    if kms[k] > maior_km:
        maior_km = kms[k]
        veiculo = carros[k]

# Relatório das informações processadas.
print('\n')
print('RELATÓRIO DE CONSUMO DE COMBUSTÍVEL'.center(87))
print('-'*87)
print('Veículo'+'Km p/ lts'.rjust(20)+'Consumo p/ 1000(km)'.rjust(30)+'Valor p/ 1000(km)'.rjust(30))
print('-'*87)
for idx in range(len(carros)):
    quant_litros = (1000 / kms[idx])
    print(f'{carros[idx]}'.ljust(12)+f'{kms[idx]:.1f}(km)'.rjust(15)+f'{quant_litros:.1f}(Lts)'.rjust(26)+f'(R$){quant_litros*4.690:.2f}'.rjust(31))
print('\n')
print(f'Veículo mais econômico: {veiculo} --- > 1 Litro faz: {maior_km:.1f}(km)')
print('-'*87)
