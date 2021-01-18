# Este é o script principal do programa, ele efetua a chamada de módulos e funções.
#
# @Autor: Abraão A. Silva

import Acesso


def main():
    "Corpo principal do programa."
    while True:
        print('-'*30)
        user = str(input('Você já tem Conta(s\\n): ')).strip().upper()[0]
        if user == 'N':
            Acesso.cadastro_de_usuario()
            continue
        elif user == 'S':
            Acesso.validando_acesso()
        else:
            print('Essa opção não existe, digite "sim" ou "não".')
            continue


main()

