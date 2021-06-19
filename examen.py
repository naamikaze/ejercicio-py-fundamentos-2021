# Simulacro 2do Parcial
import random
dias = 30
produccion = []
for i in range(0, dias):
	# Carga enteros entre 1 y 1000 al azar en el vector producción
	produccion.append(random.randint(1,1000))
# A partir de acá poné tu código

#Voy a poner la lista acá y en el punto 3 como para saber bien que está funcionando todo
print(f'Produccion Actual: {produccion}')
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
    #Calcular el promedio de producción de los primeros 15 días.
    promedio = 0
    for j in range(0, 15):
        promedio += produccion[j]
    promedio /= 15
    print(f'El promedio de los primeros 15 días es {promedio}')
    pass

def punto3():
    #Solicitar al usuario un día y una cantidad producida y actualizar el vector.
    while True:
        dia = int(input('Ingrese el dia que desea ingresar: ')) 
        if dia < 31:
            dia-=1
            producido = int(input('Ingrese la cantidad producida: '))
            produccion[dia] = producido 
            print(f'El día {dia} hubo una produccion de {produccion[dia]}')
            print(f'Nueva lista:')
            print(f'{produccion}')
            break
        else:
            print('Ese dia es incorrecto...')
    pass

def punto4():
    #Informar la cantidad de días que la producción fue menor al promedio.
    promedio = 0
    for j in range(len(produccion)):
        promedio += produccion[j]
    promedio /= len(produccion)
    conta = 0
    for j in range(len(produccion)):
        if produccion[j] < promedio:
            conta+=1
    print(f'La cantidad de dias con menor produccion al promedio es {conta}')
    pass

def punto5():
    #Solicitar al usuario un día del mes e informar las cantidades producidas durante los días previos. (desde inicio del mes hasta el día ingresado por el usuario)
    while True:
        dia = int(input('Ingrese el día objetivo: '))
        if dia <31:
            lista = []
            for j in range(0, dia):
                lista.append(produccion[j])
            print(f'Producciones del dia 1 al dia {dia}')
            print(f'{lista}')
            break
        else:
            print(f'Dia no valido...')
    pass

def menu():

    print('BIENVENIDO')
    print()
    print('INGRESE QUE OPCION DESEA ELEGIR (1, 2, 3, 4, 5 o 6)')
    print()
    while True:
        opcion = int(input('Eliga su opcion por favor: '))
        if opcion <7:
            if opcion == 1:
                punto1()
            elif opcion == 2:
                punto2()
            elif opcion == 3:
                punto3()
            elif opcion == 4:
                punto4()
            elif opcion ==5:
                punto5()
            elif opcion == 6:
                print(f'SALIENDO DEL PROGRAMA...')
                break
        else:
            print('Opcion incorrecta, intente otra vez por favor...')
    pass

menu()

