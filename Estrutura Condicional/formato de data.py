"""
Programa 036
Área de estudos.
data 19.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Entrada da data.
data = int(input('Data(dd/mm/aaaa).: '))
data_analise = str(data)

# Analise da data repassada, o formato cobre os anos de 1900 á 2020.
# Condição aninhada. Pouco recomendada no desenvolvimento de software.
if len(data_analise) == 8:
    if 0 < int(data_analise[:2]) <= 30:
        if 0 < int(data_analise[2:4]) <= 12:
            if 1900 <= int(data_analise[4:]) <= 2020:
                print(f'A data {data_analise[:2]}/{data_analise[2:4]}/{data_analise[4:]} é valida.')
            else:
                print('Data fora do padrão.')
        else:
            print('Data fora do padrão.')
    else:
        print('Data fora do padrão.')
else:
    print('Data fora do padrão.')
