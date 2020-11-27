"""
Programa 076
Área de estudos.
data 27.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Cabeçalho.
print()
print('{:¨^31}'.format(' Academia O brutus '))
print('-'*31)

# Coleta de informações e inicialização de variaveis.
quant_clientes = int(input('Nº de Clientes.: '))

alto, baixo = int(), 999
gordo, magro = int(), 999
soma_pesos = soma_alturas = int()

# Coleta de informações e processamento das informações.
contador = 1
for cliente in range(1, quant_clientes+1):
    print('='*31)
    print(f'{cliente}º Cliente..:')
    codigo = int(input('Código.: '))
    altura = float(input('Altura(m).: '))
    peso = float(input('Peso(kg).: '))

    soma_pesos += peso
    soma_alturas += altura

    # Mais alto, mais baixo.
    if altura > alto:
        alto = altura
        codigo_alto = codigo
        peso_alto = peso
    
    if altura < baixo:
        baixo = altura
        codigo_baixo = codigo
        peso_baixo = peso

    # Mais magro, mais gordo.
    if peso > gordo:
        gordo = peso
        codigo_gordo = codigo
        altura_gordo = altura

    if peso < magro:
        magro = peso
        codigo_magro = codigo
        altura_magro = altura

    contador += 1

# Calculo das médias (peso e altura).
media_peso = (soma_pesos / contador)
media_altura = (soma_alturas / contador)

# Relatório dos resultados.
print(
    '-'*31+'\n',
    'Cliente Alto..: \n',
    f'Código.: {codigo_alto}\n',
    f'Altura(m).: {alto:.2f}\n',
    f'Peso(kg).: {peso_alto:.1f}\n',
     )

print( 
     '-'*31+'\n',
     'Cliente Baixo..: \n',
     f'Código.: {codigo_baixo}\n',
     f'Altura(m).: {baixo:.2f}\n',
     f'Peso(kg).: {peso_baixo:.1f}\n',        
     )

print(
     '-'*31+'\n',
     'Cliente Gordo..:\n',
     f'Código.: {codigo_gordo}\n',
     f'Altura(m).: {altura_gordo:.2f}\n',
     f'Peso(kg).: {gordo:.1f}\n',
     )

print(
     '-'*31+'\n',
     'Cliente Magro..:\n',
     f'Código.: {codigo_magro}\n',
     f'Altura.: {altura_magro:.2f}\n',
     f'Peso.: {magro:.1f}\n',
     )
