"""
Programa 010 | Área de estudos. | data 16.11.2020 | (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Coleta de valores pelo teclado.
n1 = int(input('Digite um valor inteiro.: '))
n2 = int(input('Digite outro valor inteiro.: '))
n3 = float(input('Digite agora um valor real.: '))

# O produto do dobro do primeiro com a metade do segundo valor.
produto_Dobro = (n1*2) * (n2/2)

# A soma do triplo do primeiro com o terceiro.
soma_com_terceiro = (n1*3) + n3

# Terceiro elevado ao cubo.
elevado_cubo = n3 ** 3

# Saída dos resultados.
print(f'O produto do dobro do primeiro com a metade do segundo é {produto_Dobro:.0f}')
print(f'A soma do triplo do primeiro com o terceiro vale {soma_com_terceiro:.0f}')
print(f'Terceiro elevado ao cubo é {elevado_cubo:.0f}')
