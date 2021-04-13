#EJERCICIO 2
num1 = int(input('Ingrese el primer nro: '))
num2 = int(input('Ingrese el segundo nro: '))
num3 = int(input('Ingrese el tercer nro: '))
num4 = int(input('Ingrese el cuarto nro: '))
num5 = int(input('Ingrese el quinto nro: '))

mayor=num1

if num2 > mayor:
    mayor=num2

if num3 > mayor:
    mayor=num3

if num4 > mayor:
    mayor=num4

if num5 > mayor:
    mayor=num5

print("El número mayor es: ", mayor)
