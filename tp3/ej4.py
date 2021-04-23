num1 = int(input('Ingrse un nro: '))
num2 = int(input('Ingrse un nro: '))

if num1 % num2 == 0:
    print(f'{num1} Es multiplo de {num2}')
else:
    print(f'{num1} No es multiplo de {num2}')

if num2 % num1 == 0:
    print(f'{num2} Es multiplo de {num1}')
else:
    print(f'{num2} No es multiplo de {num1}')

   

