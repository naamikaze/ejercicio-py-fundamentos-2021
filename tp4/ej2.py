num = 0
valor = 0
cont = 0

#Creo la lista
lista = []

while num != -1:

    num = int(input('Ingrese un nro: '))
    
    #Le digo a la lista que vaya metiendo las variables que estoy ingresando
    lista.append(num)
    if num == -1:
        #Muestro el nro ingresado en x parte de la lista en este caso al principio (0)
        print(f'Primer nro ingresado: {lista[0]}')
        #Muestro el ultimo nro de la lista, poniendo resultados negativos puedo ir al ultimo nro
        print(f'Ultimo nro ingresado: {lista[-2]}')

