lista = []
cant = int(input('Ingrese la cantidad de palabras que desea ingresar: '))
for x in range(cant):
    word = input(f'Ingrese la palabra nro {x}: ')
    lista.append(word)
print(f'La lista generada es la siguiente: {lista}')
AAAnomb = input(f'Sustituir la palabra {lista[0]} por: ')
lista[1] = nomb
print(f'La lista es ahora: {lista}')
    
