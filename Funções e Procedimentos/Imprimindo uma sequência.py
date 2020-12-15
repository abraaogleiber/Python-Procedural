"""
Programa 122
Área de estudos.
data 15.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# FUNÇÃO NÃO FRUTÍFERA OU MELHOR DIZENDO UM PROCEDIMENTO.
def gerador_sequencia(n): # Recebe um args que é passado a seu parâmetro. 
    "Essa função receberá um valor 'n', vai gerar um intervalo até o valor 'n'" # Docstring. A documentação da função.

    for vez in range(1, n+1):
        print(f'{vez}'*vez)


termino = int(input('Termino da sequência.: '))
gerador_sequencia(termino)
