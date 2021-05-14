num = 0
mayor = int(input('Ingrese un nro principal: '))
lista = []

while num != -1:
    num = int(input('Ingrese un nro: '))
    if num < mayor and num != -1:
        lista.append(num)
    if num == -1:
        print(lista)
        print()
        print(f'Finalizando programa...')

