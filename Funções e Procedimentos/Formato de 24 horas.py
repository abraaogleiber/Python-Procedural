"""
Programa 128
Área de estudos.
data 16.12.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
""" 


def define_formato(hr, tr):
    "Docstring"   

    f_pm = {13:1, 14:2, 15:3, 16:4, 17:5, 18:6, 19:7, 20:8, 21:9, 22:10, 23:11, 00:1}

    if tr in 'AM':
        f_hora = 'AM'
        h_convertida = hr 

    elif tr in 'PM':
        f_hora = 'PM'
        h_convertida =  f_pm[hr]
    
    return (f_hora, h_convertida)


def saida_formato(hr, tr):
    "Docstring"
    
    print(f'{hr} {tr}')


def main():
    "A função principal, corpo."

    hora = int(input('Hora.: '))
    turno = str(input('Turno(AM/PM).: ')).strip().upper()[:1]

    hora_formatada = define_formato(hr=hora, tr=turno)
    saida_formato(hr=hora_formatada[1], tr=hora_formatada[0])

main()
