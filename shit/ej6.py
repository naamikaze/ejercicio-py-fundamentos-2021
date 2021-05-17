listpar = []
listinpar = []

canti = int(input('Cuanto nros desea ingresar: '))

def separar(cantidad):
    cont = 0
    while cont != cantidad:
        cont+=1
        num = int(input('Ingrese un nro: '))
        if num % 2 == 0:
            listpar.append(num)
        elif num % 2 != 0 and num != -1:
            listinpar.append(num)

    return f'Nros pares {listpar} // Nros inpares {listinpar}'

print(separar(canti))


