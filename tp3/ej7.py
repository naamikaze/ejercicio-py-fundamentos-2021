productos = int(input('Ingrese la cantidad de productos: '))
precio = int(input('Ingrese el precio de los productos: '))
preciofinal = 0

if productos >= 13 and productos <= 100:
    preciofinal = precio*0.10
    preciofinal *= productos

elif productos > 100:
    preciofinal = precio*0.25
    preciofinal *= productos

elif productos < 13:
    preciofinal = precio 
    preciofinal *= productos

promedio = preciofinal/productos

print(f'El precio final es de: {preciofinal}')
print(f'El promedio final es de: {promedio}')
