contador = 1
while contador != 0:
    num = int(input('Ingrese un nro'))
    if num < 0:
        print(f'El nro {num} es negativo')
    elif num == 0:
        contador = 0
