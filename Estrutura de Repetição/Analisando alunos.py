"""
Programa 078
Área de estudos.
data 28.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Verificando qual aluno tem maior altura.
maior, menor = int(), 999
for aluno in range(1, 11):
    print(f'{aluno}º Aluno..:')
    numero = int(input('Nº Aluno.: '))
    altura = float(input('Altura(cm).: '))
    print()


    # Auto.
    if altura > maior:
        maior = altura
        alto_numero = numero

    # Baixo.
    if altura < menor:
        menor = altura
        baixo_numero = numero

print(f'O aluno mais alto tem Nº {alto_numero} e altura {maior}(cm).')
print(f'O aluno mais baixo tem Nº {baixo_numero} e altura {menor}(cm).')
