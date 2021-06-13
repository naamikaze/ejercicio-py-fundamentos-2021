
#Declaro todas las listas y variables que voy a usar
cont=-1
contbaz = 1
listnom = []
listcateg = []
listprecio = []
listcant = []
pos= 0

largocateg = len(listcateg)
def punto1(listcateg, largocateg, contbaz):
# //ACA ARRANCA EL PUNTO 1//
#Busco en la lista "listcateg" todos los nro 3
    for i in range(largocateg):
        if listcateg[i] == 3:
            contbaz += 1
    print()
    print(f'Cantidad de productos de bazar: {contbaz}')
pass

def punto2(listnom, pos, cont):
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
pass

def punto3(listprecio, largocateg, listcateg):
# //ACA ARRANCA EL PUNTO 3//
    buscar_categoria = int(input('Ingrese la categoría que desea buscar: '))
    posc = 0
    sumas = 0

    for k in range(largocateg):
        if listcateg[k] == buscar_categoria:
            posc +=1
            sumas += listprecio[k]
        else:
            print(f'ERROR')
    print(f'{posc} {sumas}')
    promedio = sumas/posc
    print(f'El promedio de la categoria {buscar_categoria} es {promedio}')
pass


listnom = ['papa', 'zapallo', 'huevo', 'pancho', 'pantera']
listcateg = [1, 3, 3, 2, 3]
listprecio = [231, 542, 32, 2, 91]
listcant = [32, 52, 12, 325, 21]

print()
#Hago que todo se repita 20 veces
#for x in range(1):
#    print(f'PRODUCTO NRO {x+1}')
#    #Pido toda la información y la pongo en sus respectivas listas
#    nom = input(f'Ingrese el nombre del producto {x+1}: ')
#    listnom.append(nom)
#    categoria = input(f'Ingrese la categoría del producto {x+1} 1-Limpieza // 2-Alimentos // 3-Bazar: ')
#    listcateg.append(categoria)
#    precio = int(input(f'Ingrese el precio del producto {x+1}: '))
#    listprecio.append(precio)
#    cant = int(input(f'Ingrese la cantidad del producto {x+1}: '))
#    listcant.append(cant)
#    print()

elegir = int(input(f'Ingrese que punto desea hacer'))
if elegir == 1:
    punto1(listcateg, largocateg, contbaz)
elif elegir == 2:
    punto2(listnom, pos, cont)
elif elegir == 3:
    punto3(listprecio, largocateg, listcateg)



