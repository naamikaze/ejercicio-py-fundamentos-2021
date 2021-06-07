lista = []
cant = int(input('Ingrese la cantidad de palabras que desea ingresar: '))
for x in range(cant):
    word = input(f'Ingrese la palabra nro {x+1}: ')
    lista.append(word)
print(f'La lista generada es la siguiente: {lista}')
    
