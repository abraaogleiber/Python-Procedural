"""
Programa 104
Área de estudos.
data 05.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Usamos o modulo matemático, para truncar valores flutuantes.
import math     # utilizando o método "trunc".

# Minha variável de armazenamento de dados.
notas = list()
soma = 0
while True: # Corpo principal, usado para realizar as computações necessarias.
    nota = float(input('Nota.: '))

    # Esse trecho encerra o programa ou continua o mesmo.
    if nota == -1:
        print('Programa encerrado...')
        break
    else:
        soma += nota
        notas.append(nota) # Armazenamento dos valores validos.
media = (soma / len(notas))

# Essa parte, mostra os valoresna ordem armazenada.    
for n in notas:
    print(round(n), end=' ') # Utilizamos "round" para aredondar, mas poderia ser: "ceil", "floor", "trunc".
print()                                             # do módulo "math".

# Esse pedaço dispôe os elementos da minha lista em ordem reversa. Poderia ter sido usado "reverse".
for cont, n in enumerate(notas): # Na parte inferior somamos +1 ao cont(enumerate) e logo depois
    print(math.trunc(notas[(cont+1) - (cont+1)*2])) # Multiplicamos por 2, por último subtraimos um pelo outro
                                                    # O que os torna negativo. (indíce negativo)

# Esse trecho nos diz quantas notas estão acima da média. e quantos estão abaixo de 7(sete)
acima, abaixo= 0, 0
for n in notas:
    if n > media:
        acima += 1
    if n < 7:
        abaixo += 1




print(f'Quantidade valores lidos: {len(notas)}')
print(f'A soma dos valores é {soma:.2f}')
print(f'A média das notas é {media:.2f}')
print(f'{acima} Valores estão acima da média.')
print(f'{abaixo} Valores estão abaixo de 7(sete).')
