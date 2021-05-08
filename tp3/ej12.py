dia = int(input('Ingrese un dia: '))
mes = int(input('Ingrese un mes: '))
anno = int(input('Ingrese un año: '))

if mes >= 1 and mes <= 12:
    if mes == 2 and dia >= 1 and dia <= 28:
        print(f'La fecha es valida')

    elif mes == 4 and dia >= 1 and dia <= 30 or mes == 6 and dia >= 1 and dia <= 30 or mes == 9 and dia >= 1 and dia <= 30 or mes == 11 and dia >= 1 and dia <= 30:
        print(f'La fecha es valida')

    elif mes == 1 and dia >= 1 and dia <= 31 or mes == 3 and dia >= 1 and dia <= 31 or mes == 5 and dia >= 1 and dia <= 31 or mes == 7 and dia >= 1 and dia <= 31 or mes == 8 and dia >= 1 and dia <= 31 or mes == 10 and dia >= 1 and dia <= 31 or mes == 12 and dia >= 1 and dia <= 31:
        print(f'La fecha es valida')

    else:
        print(f'La fecha es invalidad')

else:
    print(f'La feha es invalida')
