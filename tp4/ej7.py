num = 0
menor = 1000000000000
mayor = -1

while num != -1:
    num = int(input('Ingrese un nro: '))
    if num > mayor and num != -1:
        mayor = num
    elif num < menor and num != -1:
        menor = num
    if num == -1:
        print()
        print(f'Cerrando Programa...')

print(f'El nro mayor es: {mayor}')
print()
print(f'El nro menor es: {menor}')
    
