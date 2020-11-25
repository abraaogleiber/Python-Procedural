"""
Programa 059
Área de estudos.
data 25.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Entrada da quantidade de termos.
quant_termo = int(input('Quantos termos desejas mostrar.: ')) + 1

# Definimos o primeiro e segundo termo.
t1 = t2 = 1 # Apelidagem de valores. (t1 e t2 são referências ao mesmo objeto.)

# Saída dos dados e geração do termo posterior, somando os dois anteriores.
print(t1, t2, end=' ')
for termo in range(3, quant_termo):
    # Modelo de transição de valores.
    t3 = (t1 + t2)

    t1 = t2
    t2 = t3

    print(t3, end=' ')
