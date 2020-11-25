"""
Programa 060
Área de estudos.
data 25.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

t1 = t2 = 1 # Apelidagem (t1 e t2 são referências ao mesmo valor.)

print(t1,  t2, end='   ')

# Será gerado uma sequência fibonacci com mais de 500 termos.
contador = 1
while contador <= 500:
    # É usado o modelo de transição de valores.
    t3 = (t1 + t2)

    t1 = t2
    t2 = t3

    print(t3, end='   ')
    contador += 1
