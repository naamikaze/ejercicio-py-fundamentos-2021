menor = 100000000 
mayor = -1

for x in range(10):
    num = int(input('Ingrese un nro: ')) 
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num
rango = mayor - menor

print()
print(f'El nro mayor es: {mayor}')
print(f'El nro menor es: {menor}')
print(f'El rango de conjunto es: {rango}')
