cont = 0
menor = 999999999999
for x in range(10):
    cont +=1
    num = int(input('Ingrese un nro: '))
    if num < menor:
        menor = num
        pos = cont
    
print(f'El nro menor es {menor} en la posición {pos}')
