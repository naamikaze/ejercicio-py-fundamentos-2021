lista = []
num = 0
while num != -1:
     num = int(input('Ingrese un nro: '))
     lista.append(num)

    #Poniendo len(lista) basicamente obtengo la cantidad de elementos que hay en esa lista
if len(lista) % 2 == 0:
    print(f'El conjunto es par ({len(lista)})')
else:
    print(f'El conjunto es impar ({len(lista)})')

