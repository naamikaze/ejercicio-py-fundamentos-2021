anno = int(input('Ingrese un año: '))
mes = int(input('Ingrese un mes: '))

def calcular(anio, mees):

    if anio >= 1900 and anio <= 2100 and mees >= 1 and mees <= 12:
        print('El par es valido')
    else:
        print('El par es invalido')

calcular(anno, mes)

