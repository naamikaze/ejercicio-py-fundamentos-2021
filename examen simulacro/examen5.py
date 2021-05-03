paquetes = int(input('Ingese la cantidad de paquetes: '))
imp=0
calculo = 0
for x in range(paquetes):
    peso = int(input('Ingrese el peso del  paquete: '))
    volumen = int(input('Ingrese el volumne del  paquete: '))
    km = int(input('Ingrese el kilometraje que va recorrer: '))

    if km >= 60 and km <= 500:
        imp = 300
    elif km > 500:
        imp = 500
    elif km < 60:
        imp = 100

    importe = 200+peso*10+volumen*2+imp
    calculo += importe

    print('Va el siguiente')

print(f'La suma de todos los importes es de: {calculo}')

