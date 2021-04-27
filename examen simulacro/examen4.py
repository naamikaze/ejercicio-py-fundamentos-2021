multi = 0
for x in range(20):
    num = int(input('Ingrese un número: '))
    if num % 5 == 0:
        multi += num

print(f'La suma de los multiplos de 5 es de: {multi}')
