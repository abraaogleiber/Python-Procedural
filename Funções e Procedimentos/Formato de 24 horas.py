"""
Programa 128
Área de estudos.
data 16.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
""" 


def define_formato(hr, mn):
    "Docstring"   

    f_pm = {13: 1, 14: 2, 15: 3, 16: 4, 17: 5, 18: 6, 19: 7, 20: 8, 21: 9, 22: 10, 23: 11, 00: 1}

    if hr in f_pm:
        formato_hora = 'PM'
        hora = f_pm[hr]
        minuto = mn

    else:
        formato_hora = 'AM'
        hora = hr
        minuto = mn    
    return (hora, minuto, formato_hora)


def saida_formato(hr, mn, tr):
    "Docstring"
    if hr < 10:
        if mn == 60:
            print(f'{hr+1}:00 ({tr})')
        else:
            print(f'0{hr}:{mn} ({tr})')
    else:
        if mn == 60:
            print(f'{hr+1}:00 ({tr})')
        else: 
            print(f'{hr}:{mn} ({tr})')


def main():
    "A função principal, corpo."

    hora = int(input('Hora.: '))
    minuto = int(input('Minuto.: '))

    if hora > 24 or minuto > 60:
        print('Formato de hora inválida.')
        exit()

    hora_formatada = define_formato(hr=hora, mn=minuto)
    saida_formato(hr=hora_formatada[0], mn=hora_formatada[1], tr=hora_formatada[2])


main()
