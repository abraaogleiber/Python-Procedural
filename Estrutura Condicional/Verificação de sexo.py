"""
Programa 020
Área de estudos.
data 18.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Usuario entra com seu sexo.
sexo_usuario = str(input('Seu sexo(M|F).: ')).strip().upper()[0]

# Condição encadeada onde verificamos o sexo correspondente.
if sexo_usuario in 'M':
    print('Sexo definido como "Masculino".')
elif sexo_usuario == 'F':
    print('Sexo definido como "Feminino".')
else:
    print('O sexo informado é inválido.')
