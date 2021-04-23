base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

calculo = 0
superficie = 0

if base < 0:
    print("La base no puede ser negativa")
elif altura < 0:
    print("La altura no puede ser negativa")
else:
    calculo = base*altura
    superficie = calculo/2
    print(f'La superficie del triangulo es: {superficie}')
