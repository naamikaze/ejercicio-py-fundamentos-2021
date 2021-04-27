paquetes= int(input("Cuantos paquetes quiere enviar : "))
pesoskm=0
importe=0

for x in range(paquetes):
    peso= int(input("cuanto pesa cada paquete: "))
    volumen = int(input("ingrese el volumen de cada paquete: "))
    km = int(input("Cuantos kilometros tiene que viajar el paquete:"))
 
    if km < 60:
        pesoskm = pesoskm+ 100
    if km > 60 and km < 500:
        pesoskm = pesoskm+ 300
    if km > 500:
        pesoskm = pesoskm+ 500

    importe =200+peso*10+volumen*2+pesoskm
    
print("Por favor ingrese los datos de su proximo paquete")
