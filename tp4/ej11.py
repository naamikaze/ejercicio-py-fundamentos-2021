mayor = 0
for x in range(10):
    num = int(input('Ingrese un nro: '))
    if num > mayor:
        mayor = num
print(f'El nro mayor es: {mayor}')
