#Ignacio Rodríguez 1136034
#Segundo Parcial FDI
import random
bitcoin = []
for i in range(0, 30):
	bitcoin.append(random.randint(1,1000))
print(f'{bitcoin}')

def punto1():
#1. Solicitar al usuario 2 días e indicar el valor mínimo del Bitcoin entre esos 2 días.
    while True:
        dia1 = int(input('Ingrese el primer dia: ')) 
        dia2 = int(input('Ingrese el segundo dia: ')) 
        if dia2 > dia1 and dia1 >= 1 and dia1 <= 30 and dia2 <= 30:
            primeravez = True
            menorr=0
            cont=dia1
            for j in range(dia1-1, dia2):
                if primeravez:
                    menorr = bitcoin[j]
                    diamenor=cont
                    primeravez = False
                elif bitcoin[j] < menorr:
                    diamenor=cont
                    menorr = bitcoin[j]
                cont+=1
            print(f'El día de menor producción fue el día {diamenor} ({menorr})')
            break
        else:
            print(f'Datos invalidos, intente nevamente')
    pass

def punto2():
    #2. Solicitar al usuario el día de compra, el día de venta y la cantidad comprada. Con esos datos informar la ganancia o la perdida de la operación.
    while True:
        compra = int(input('Ingrese que dia compró: '))
        venta = int(input('Ingrese que dia vendió: '))
        if compra >= 1 and compra <= 30 and venta > compra and venta <=30:
            cant = int(input('Ingrese que cantidad compró: '))
            compra = bitcoin[compra-1]
            compra *=cant
            venta = bitcoin[venta-1]
            venta *=cant
            if compra > venta:
                final = compra-venta
                print(f'Tuviste una perdida de -{final}')
            elif venta > compra:
                final = venta-compra
                print(f'Tuviste una ganancia de {final}')
            elif venta == compra and compra == venta:
                print(f'No tuviste ganancia ni perdida (0)')
            break
        else:
            print(f'Ingrese dias validos')
    pass

def punto3():
    #3. Un proceso de carga que pida al usuario día a día las cotizaciones y las guarde en el vector.
    while True:
        dia = int(input('Que día desea cambiar: '))
        if dia >= 1 and dia <= 30:
            coti = int(input('Que valor desea ingresar: '))
            bitcoin[dia-1]=coti
            print(f'Lista Actualizada:')
            print(f'{bitcoin}')
            break
        else:
            print(f'Ingrese un dia valido')
            print()
    pass

def punto4():
#4. Informar la cotización promedio de los primeros 10 días.
    contador = 0
    for j in range(0, 10):
        contador+=bitcoin[j]
    contador/=10
    print(f'El promedio de los primeros 10 dias es: {contador}')
    pass

def punto5():
    #5. Informar el valor máximo alcanzado por la cotización entre los días 10 y 20 del mes.
    primeravez = True
    mayor = 0
    cont=9
    diamayor = 0
    for j in range(9, 20):
        if primeravez:
            mayor=bitcoin[j]
            diamayor=cont
            primeravez = False
        elif bitcoin[j] > mayor:
            diamayor = cont
            mayor = bitcoin[j]
        cont+=1
    print(f'El dia de mayor producción fue el dia {diamayor+1} ({mayor})')
    pass

def menu():
    while True:
        print()
        opcion = int(input('Ingrese una opcion (1,2,3,4,5) o si quiere salir presione 6: '))
        if opcion >= 1 and opcion <= 6:
            if opcion == 1:
                punto1()
            elif opcion ==2:
                punto2()
            elif opcion ==3:
                punto3()
            elif opcion ==4:
                punto4()
            elif opcion ==5:
                punto5()
            elif opcion ==6:
                print(f'Saliendo del programa...')
                print()
                break
        else:
            print(f'Ingrese una opción valida:')

menu() 


