#Creo las variables e importo el modulo random de python
import random
puntosper = 0
puntospc = 0
rondaper = 0
rondapc = 0
ronda = 1

#Hago un for para las 3 rondas
for x in range(3):
    #Al terminar la ronda repito el nro de juegos que hay así vuelve a funcionar el while
    ronda = 1
    while ronda < 6:
    #Mientras el nro de rondas sea menor que 6 se va a seguir usando el while
        ronda += 1
        per = input('Ingrese R/Piedra P/Papel S/Tijera: ')
        #Si el usuario no ingreso R, P o S tiene que volverle a preguntar hasta que ingrese alguno de esos caracteres
        if per != 'R' and per != 'P' and per != 'S':
            #En caso de que no cumpla la condición se reinicia la jugada y vuelve a preguntarle
            ronda -= 1
            print('Caracter incorrecto')
        else:
            #En caso de que haya ingresado todo bien sigue el juego
            #El modulo random elije entre alguno de los caracteres especificados (R, P o S)
            pc = random.choice('R' 'P' 'S')
            #Si el caracter del jugador le gana a cualquier posibildad de la maquina le da un punto al jugador, es una manera mas rápida de poner varios if con todas las posibilidades
            if per == 'R' and pc == 'S' or per == 'S' and pc == 'P' or per == 'P' and pc == 'R':
                #En caso de que gane le da un punto
                puntosper += 1
                print('Ganaste!')
            #Si hay empate se reinicia la ronda
            elif puntosper == puntospc:
                print('Empate')
                ronda -= 1
            #En cambio, si no le gana le da un punto a la maquina
            else: 
                puntospc +=1
                print('Gano la pc')

    #Acá termina el while y compara los puntajes ganados y le da un punto de ronda al ganador
    print('Fin de la ronda')
    if puntosper > puntospc:
        print('Ganaste esta ronda')
        rondaper += 1
    else:
        print('La pc ganó esta ronda')
        rondapc += 1

        #Reinicio los puntajes de las jugadas para volver a compararlos al final de la ronda
        puntosper = 0
        puntospc = 0

#Comparo la cantidad de rondas ganadas y en base a ello se define la partida
if rondaper > rondapc:
    print('Ganaste la partida!')
else: 
    print('La pc ganó la partida')

print('Puntuaciones: ')
print('Tu puntuación es de', rondaper, ' Rondas ganadas')
print('La puntuación de la pc es de', rondapc, ' Rondas ganadas')
