num_paq = 1
importe = 0
km_precio = 0
precio_total = 0
cant_paq = int(input('Ingrese la cantidad de paquetes a enviar: '))
while cant_paq < 1:
    print('Puso un valor incorrecto')
    cant_paq = int(input('Ingrese la cantidad de paquetes a enviar: '))
    print()
while num_paq <= cant_paq:
    #Habia un comentario de validación pero la consigna no pide validación alguna
    print('Para el paquete número', num_paq, 'ingrese')
    peso_paq = int(input('Cuánto pesa el paquete: '))
    vol_paq = int(input('Cuál es el volumen del paquete: '))
    km_paq = int(input('A qué distancia va el paquete: '))
    if km_paq < 60: #En la consigna pide que sea menor a 60
        km_precio = 100 #Había un 0 en vez de 100
    #Estaba haciendo otra vez el if para saber si es menos de 60
    elif km_paq >= 60 and km_paq < 500:
        km_precio = 300
    else:
        km_precio = 500
    importe = 200 + peso_paq * 10 + vol_paq * 2 + km_precio
    print('El precio del paquete número', num_paq, 'es $', importe)
    print()
    precio_total += importe
    num_paq += 1
print('El importe total a pagar es $', precio_total)
print()
print('No hay más paquetes que despachar, hasta mañana!')
