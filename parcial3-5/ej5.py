importe = 0
total = 0
paquetes = int(input('Ingrese la cantidad de paquetes a enviar: '))
for x in range(paquetes):
    peso = int(input('Ingrese el peso: '))
    volumen = int(input('Ingrese el volumen: '))
    distancia = int(input('Ingrese el distancia: '))
    if distancia > 60 and distancia < 500:
        importe = 300
    elif distancia >= 500:
        importe  = 500
    elif distancia < 60:
        importe = 100
    importe = 200 + peso * 10 + volumen * 2 + importe
    print(f'El importe del paquete actual es de:  {importe}')
    total += importe
print(f'La suma de todos los importes calculados es de: {total}')
