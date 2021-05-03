anno = int(input('Ingrese un año: '))
mes = int(input('Ingrese un mes: '))

if anno >= 1900 and anno <= 2100 and mes >= 1 and mes <= 12:
    print('El par es valido')
else:
    print('El par es invalido')
