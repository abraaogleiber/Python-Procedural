"""
Programa 032
Área de estudos.
data 18.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Notas do aluno.
n1 = float(input('1º Nota.: '))
n2 = float(input('2º Nota.: '))

# Calculo da média.
media = (n1 + n2) / 2

# Série de verificações das notas.
if 0 <= media < 4:
    conceito = "E"
    status = "Reprovado"
elif 4 <= media < 6:
    conceito = "D"
    status = "Reprovado"
elif 6 <= media < 7.5:
    conceito = "C"
    status = "Aprovado"
elif 7.5 <= media < 9:
    conceito = "B"
    status = "Aprovado"
elif 9 <= media <= 10:
    conceito = "A"
    status = "Aprovado"
else:
    print('Verifique as notas repassadas, elas estão fora do padrão [0 á 10].')

# Saída formatada usando caracteres de escapes. Estilo relatório.
print(f'{"1ºN"} \t{"2ºN"} \t{" M"} \t{"Conceito"} \t{"Status"}')
print('-='*24)
print(f'{n1:.1f} \t{n2:.1f} \t{media:.1f} \t{conceito.rjust(4)} \t\t{status}')
print('=-'*24)
