num = 0
par = []
inpar = []
contpar = 0
continpar = 0

while num != -1:
    num = int(input('Ingrese un nro: '))
    if num % 2 == 0:
        contpar+=1
    elif num % 2 != 0 and num != -1:
        continpar+=1

print(f'Cantidad de nros pares: {contpar}')
print()
print(f'Cantidad de nros inpares: {continpar}')
        

