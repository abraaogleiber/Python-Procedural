"""
Programa 064
Área de estudos.
data 25.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Entrada de dados.
n = int(input('Digite o limite da busca.: '))

primos = int()  # Acumuladora (somente primos).

# Iteração encaixada
contar_divisões = 0     # Contabiliza o número de divisões realizadas para encontrar os Primos.
for a in range(1, n+1):
    divisivel = int()   # será zerada a cada iteração.
    for s in range(1, a+1):
        if a % s == 0:
            divisivel += 1  # Conta os divisiveis.
            contar_divisões += 1
        else:
            contar_divisões += 1
    # Conta os primos segundo avaliação.
    if divisivel == 2:
        primos += 1 


# Essa parte do código gera uma saída mostrando os valores Primos do intervalo.
for a in range(1, n+1):
    divisivel = int()
    for s in range(1, a+1):
        if a % s == 0:
            divisivel += 1

    if divisivel == 2:
        print(a, end=' ')

print(f'\nTotal de Primos no intervalo.: {primos}')
print(f'Número de divisões realizadas.: {contar_divisões}')
