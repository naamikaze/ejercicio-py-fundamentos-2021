cont = 0
pares = 0
for x in range(5):
    num = int(input('Ingrese un nro: '))
    if num % 2 == 0:
        cont+=1
        pares+=num
promedio = pares/cont
print(f'El promedio de los numeros pares es: {promedio}')
