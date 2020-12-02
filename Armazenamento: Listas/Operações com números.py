"""
Programa 097
Área de estudos.
data 02.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Inicialização de variáveis simples e composta.
soma = 0
multiplique = 1
lista_num = []
for rep in range(1, 6): # Iteração realiza coleta.
    n = int(input(f'{rep}º Número.: '))
    lista_num.append(n) # Armazena utilizando método de tratamento de listas.

    # Calculos.
    soma += n
    multiplique *= n

# Saída bem formatada e organizada do programa.
print('{:~^30}'.format(' Relatório '))
print('\n',
      'Soma -- '+f'{soma}'.rjust(18)+'\n',
      'Multiplicação -- '+f'{multiplique}'.rjust(9)+'\n',
      '\n',
      'Valores.: '+f'{tuple(lista_num)}'.rjust(9)+'\n',
      '~'*30+'\n',
     )
