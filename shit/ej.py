def area_rectangulo(base, altura):
    area = base*altura
    return area  

base = int(input('Ingrese la base: '))
altura = int(input('Ingrese la altura: '))

print(f'El area del rectangulo es {area_rectangulo(base, altura)}')

