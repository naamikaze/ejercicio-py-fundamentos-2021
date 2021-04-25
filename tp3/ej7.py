productos = int(input('Ingrese la cantidad de productos'))
precio = int(input('Ingrese el precio de los productos'))

contador = 0

preciofinal = 0
while contador == productos:
    contador += 1
    if contador > 12  and contador < 100:
        descdiez = precio*0.10
        preciofinal += descdiez 
    elif contador > 100:
        descvei = precio*0.25
        preciofinal += descvei
    else:
        preciofinal += precio

print(f'El precio final es de: {preciofinal}')
