temp = int(input('Ingrese una temperatura:  '))
if temp >= 15 and temp <= 25:
    dia = 'templado'
elif temp > 25:
    dia = 'caluroso'
elif temp < 15:
    dia = 'frio'

print(f'El día de hoy está: {dia}')
