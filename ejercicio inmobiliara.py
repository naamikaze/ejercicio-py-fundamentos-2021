#Ignacio Rodríguez

print('Bienvenido Profesor!')

#Creo un while para así ir pidiendo infinitamente las notas
while True:

    print('Vayamos a ello')
    
    #Ingreso la primera nota
    nota1 = int(input('Ingrese la primera nota: '))
    
    #Acá le digo al programa que si la nota es igual a -1 (Como pide la consigna) el while va a terminar y con ello el programa, utilizando el "break"
    if nota1 == -1: 
        print('Terminando programa...')
        break # <-- Eso hace que termine el while

    #Pido la segunda nota
    nota2 = int(input('Ingrese la segunda nota nota: '))

    #Hago una soma de todas las notas
    final = nota1 + nota2

    # Teniendo en cuenta la suma de las notas hago al programa que decida que decision tomar...
    if final >= 14:
        print(' --Promociona')

    #Si la nota es mayor o igual que 8 y a su vez menor e igual que 13 que de como aprobado, en caso de que sea mayor que 13 ya cuenta como Promocionado con la condición de arriba
    elif final >= 8 and final <= 13:
        print(' --Aprueba la materia')

    #Si no cumple ninguna de las dos condiciones de arriba pasa a quedar desaprobado
    else:
        print(' --Desaprueba')

    #Acá especifico que materia es la que está desaprobada, en caso de que sea ninguna no va a mostrar nada 
    #Para especificar cual es la desaprobada le digo al programa que si x nota es menor o igual que 3, tiene que recuperar esa x nota...
    if nota1 <= 3:
        print('- Debe recuperar primer parcial')

    if nota2 <= 3:
        print('- Debe recuperar segundo parcial ')
