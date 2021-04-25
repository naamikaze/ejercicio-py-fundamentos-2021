pags = int(input('Ingrese el nro de páginas: '))

precio = 0
precio = pags * 2.20
precio += 125    

if pags > 300:
    precio += 80

if pags > 600:
    precio += 136

print(f'El precio de libro sería de: ${precio}')


