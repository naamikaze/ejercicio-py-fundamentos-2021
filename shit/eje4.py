cant_palabras = int(input("Dígame cuántas palabras tiene la lista: "))
lista = []
for numero in range(1, cant_palabras+1):
    palabra = input("Digame la palabra " + str(numero) + " :")
    lista.append(palabra)
palabra_a_buscar = input("Ingresar palabra a buscar: ")
contador = 0
for palabra in range(len(lista)):
    if palabra_a_buscar in lista[palabra]:
        contador += 1
print("La palabra " + palabra_a_buscar + " aparece " + str(contador) + " veces en la lista")
