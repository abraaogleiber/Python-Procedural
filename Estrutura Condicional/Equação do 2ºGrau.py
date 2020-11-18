"""
Programa 034
Área de estudos.
data 18.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

"""
Exemplos para teste: (Não possui raizes reais) --> ax²= 1 |bx= -4 |c= 5
                     (Possui apenas uma raiz real) --> ax²= 4 |bx= -4 |c= 1
                     (Possui duas raizes reais) --> ax²= 1 |bx= -5 |c= 6
"""

# Importação do módulo matemático.
import math

# Entrada dos valores da equação.
a = float(input('Valor de [ax²].: '))
b = float(input('Valor de [bx].: '))
c = float(input('Valor de [c].: '))

# Verificação da equação e realização gradativa dos calculos.
# Condição binária com aninhamento.
if a != 0:
    delta = (b**2) - (4*a*c) # Calculo do "Delta"
    if delta < 0: # Não possui raizes reias.
        print('O delta da equação é negativo ou seja não possui raízes reais.')

    elif delta == 0: # Só possui uma raiz real.
        print('A equação possui apenas uma raíz real.')
        x1 = ((-b) + (math.sqrt(delta))) / (2 * a) # Calculo da raiz.
        print(f'A raíz real da equação é {x1}')

    elif delta > 0: # Possui as duas raizes.
        x1 = ((-b) + (math.sqrt(delta))) / (2 * a) # Calculo das duas raizes.
        x2 = ((-b) - (math.sqrt(delta))) / (2 * a)
        print(f'A equação possui as seguintes raízes: ({x1}, {x2}).')
else:
    print('O valor de "ax²" é igual a "0"(zero), o que inválida essa equação.')
