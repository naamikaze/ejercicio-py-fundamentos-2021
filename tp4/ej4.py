num = 0 
lista = []

while num != -1:
    num = int(input('Ingrese un nro'))
    lista.append(num)

if len(lista) % 2 == 0:
    print(lista[-3])
else:
    print(lista[-2])
    

    
