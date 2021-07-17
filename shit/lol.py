# Simulacro 2do Parcial by PANCHO LA PANTERA
import random
dias = 30
produccion = []
for i in range(0, dias):
	# Carga enteros entre 1 y 1000 al azar en el vector producción
	produccion.append(random.randint(1,1000))

# A partir de acá poné tu código
print(f'{produccion}')

def punto1():
    #Informar el día de menor producción.
    primeravez = True
    cont = 0
    diamenor = 0
    for j in range(0, len(produccion)):
        cont+=1
        if primeravez:
            menor = produccion[j]
            primeravez = False
            diamenor = cont
        elif produccion[j] < menor:
            menor = produccion[j]
            diamenor = cont
    print(f'El día de menor producción fue el día {diamenor} ({menor})')
    pass

def punto2():
    promedio = 0
    for j in range(0, 15):
        promedio += produccion[j]
    promedio /= 15
    print(f'El promedio de los primeros 15 dias es: {promedio}')
    pass

def punto3():
#    3. Solicitar al usuario un día y una cantidad producida y actualizar el vector.
    while True:
        cambiar_dia = int(input('Ingrese un dia: '))
        if cambiar_dia >= 1 and cambiar_dia <= 30:    
            cambiar_vector = int(input('Ingrese un vector: '))
            produccion[cambiar_dia-1] = cambiar_vector
            print(f'El día {cambiar_dia} ha sido modificado a {cambiar_vector}')
            print(f'{produccion}')
            break
        else:
            print(f'Ingrese un día valido.')
    pass

def punto4():
#4. Informar la cantidad de días que la producción fue menor al promedio.
    promedio = 0
    for j in range(0, 30):
        promedio += produccion[j]
    promedio /= 30   
    cont=0
    for j in range(len(produccion)):
        if produccion[j] < promedio:
            cont+=1
    print(f'El promedio de los dias es: {promedio}')
    print(f'La cantidad de días de menor producción es:  {cont}')
    pass

def punto5():
#5. Solicitar al usuario un día del mes e informar las cantidades producidas durante los días previos. (desde inicio del mes hasta el día ingresado por el usuario)
    while True:
        dias = int(input('Ingrese cantidad que desea: '))
        lista=[]
        if dias >= 1 and dias <= 30:
            for j in range(0, dias):
                lista.append(produccion[j])
            print(f'Cantidades producidas previas al dia {dias}: {lista}')
            break
        else:
            print(f'Ingrese un dia, invalido')
    pass

def menu():
    print(f'Bienvenido')
    while True:
        opcion = int(input(f'Ingrese una opción: (1-2-3-4-5-6)'))
        if opcion >= 1 and opcion <= 6:
            if opcion == 1:
                punto1()
            elif opcion == 2:
                punto2()
            elif opcion == 3:
                punto3()
            elif opcion == 4:
                punto4()
            elif opcion == 5:
                punto5()
            elif opcion == 6:
                print(f'SALIENDO DEL PROGRAMA MUCHAS GRACIAS POR USAR PANCHOSOFT')
                break
        else:
            print(f'DOWN')
    pass

menu()


