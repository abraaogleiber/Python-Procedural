"""
Programa 121
Área de estudos.
data 13.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

import os

# Criando um arquivo ou verificando se o mesmo existe.
if os.path.exists('/home/abraao/informações.txt'):
    pass
else:
    arquivo = open('/home/abraao/informações.txt', 'x')
    arquivo.close()


# Aqui fazemos a coleta dos dados e depois de verificada armazenamos em .txt
while True:
    print('-'*15)

    nome = str(input('Nome: ')).strip().title()     # Qualque número freia o programa.
    if nome.isdigit():
        print('Programa encerrado.')
        break

    # Verificamos se o nome já não existe dentro do arquivo.
    arquivo = open('/home/abraao/informações.txt', 'rt')
    for linha in arquivo:
        if nome in linha:
            print('Está pessoa já foi cadastrada. Inicie mais uma vez.')
            arquivo.close()
            exit()
    arquivo.close()
   

    idade = int(input('Idade: '))
    if idade > 150 or idade < 0:
        print('Idade inválida. Começe novamente.')
        continue
    
    sexo = str(input('Sexo: ')).strip().upper()[0]
    if sexo not in 'MF':
        print('Sexo inválido. Começe novamente.')
        continue


    # Aqui é onde gravamos ou anexamos os dados no arquivo.
    arquivo = open('/home/abraao/informações.txt', 'at')
    arquivo.write(nome+'\t'+str(idade)+'\t'+sexo+'\n')
    arquivo.close()
