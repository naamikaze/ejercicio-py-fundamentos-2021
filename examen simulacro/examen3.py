hora = int(input('Ingrese una hora: '))
minutos = int(input('Ingrese unos minutos: '))

if hora >= 0 and hora <= 23 and minutos >= 0 and minutos <= 59:
    print(f'La hora {hora}:{minutos} es valida')
else:
    print(f'La hora {hora}:{minutos} es invalida')

