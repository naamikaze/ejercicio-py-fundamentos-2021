cantidad = int(input("ingrese cantidad de segundos: "))

dia = cantidad // 86400
restodia = cantidad % 86400

horas = restodia // 3600
restohoras = restodia % 3600

minutos = restohoras // 60
restominutos = restohoras % 60

segundos = restominutos // 1
restosegundos = restominutos % 51

print("cant de dias: ", dia)
print("cant de horas: ", horas)
print("cant de minutos: ", minutos)
print("cant de segundos: ", segundos)
