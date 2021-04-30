l1 = int(input('Ingrese el lado 1: '))
l2 = int(input('Ingrese el lado 2: '))
l3 = int(input('Ingrese el lado 3: '))
triangulo = 0

if l1 > l2 and l1 > l3:
    A = l1
    B = l2
    C = l3

elif l2 > l1 and l2 > l3:
    A = l2
    B = l1
    C = l3

elif l3 > l2 and l3 > l1:
    A = l3
    B = l2
    C = l1

if A >= B + C:
    triangulo = 'No'

elif A**2 == B**2 + C**2:
    triangulo = 'Rectangulo'

elif A**2 > B**2 + C**2:
    triangulo = 'Obtusangulo'

elif A**2 < B**2 + C**2: 
    triangulo = 'Acutangulo'

print(f'Resultado del triangulo: {triangulo}')
