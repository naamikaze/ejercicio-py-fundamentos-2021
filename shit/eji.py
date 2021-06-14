#Declaro todas las listas y variables que voy a usar
menor = 999999
produ = 0
posi = 0
producto_menor = 0
cont=-1
contbaz = 1
listnom = []
listcateg = []
listprecio = []
listcant = []

print()
#Hago que todo se repita 20 veces
for x in range(3):
    print(f'PRODUCTO NRO {x+1}')
    #Pido toda la información y la pongo en sus respectivas listas
    nom = input(f'Ingrese el nombre del producto {x+1}: ')
    listnom.append(nom)
    categoria = input(f'Ingrese la categoría del producto {x+1} 1-Limpieza // 2-Alimentos // 3-Bazar: ')
    listcateg.append(categoria)
    precio = int(input(f'Ingrese el precio del producto {x+1}: '))
    listprecio.append(precio)
    cant = int(input(f'Ingrese la cantidad del producto {x+1}: '))
    listcant.append(cant)
    print()

# //ACA ARRANCA EL PUNTO 1//
#Busco en la lista "listcateg" todos los nro 3
largocateg = len(listcateg)
for i in range(largocateg):
    if listcateg[i] == 3:
        contbaz += 1
print()
print(f'Cantidad de productos de bazar: {contbaz}')

# //ACA ARRANCA EL PUNTO 2//
#Ingreso el nombre del producto que quiero reemplazar el precio y el mismo a reemplazar
nuevo_nombre = input('Ingrese el nombre del producto a reemplazar: ')
nuevo_precio = input('Ingrese el nuevo precio: ')
print()

#Hago que la cantidad de veces que se repite el for sea el mismo que el largo de la lista
largonom = len(listnom)
for j in range(largonom):
    #Con un contador voy sabiendo que posición va a tomar en caso de encontrar la palabra clave
    cont+=1
    #Si el rango x es igual a lo que busco hago una variable con el valor de la posición donde está el nombre
    if listnom[j] == nuevo_nombre:
        pos = cont

#Teniendo la variable con la posición en el rango de lo que busco ya puedo ubicarlo con solo ese numero
listprecio[pos] = nuevo_precio
print(f'El precio de {listnom[pos]} ha sido cambiado a {listprecio[pos]}')

# //ACA ARRANCA EL PUNTO 3//
largoprecio = len(listprecio)
buscar_categoria = int(input('Ingrese la categoría que desea buscar: '))
posc = 0
sumas = 0

for k in range(largocateg):
    if listcateg[k] == buscar_categoria:
        posc +=1
        sumas += listprecio[k]

promedio = sumas/posc
print(f'El promedio de la categoria {buscar_categoria} es {promedio}')

#ACA ARRANCA EL PUNTO 4

for h in range(largocateg):
    posi += 1
    if listacateg[k] == 2:
        if listcant[k] < menor:
            menor = listcant[k] 
            producto_menor = posi

produ = listnom[producto_menor]
print(f'El precio con menor stock de la categoria alimentos es: {produ} con un stock de {producto_menor}')

#ACA ARRANCA EL PUNTO 5

for b in range(largocateg)
