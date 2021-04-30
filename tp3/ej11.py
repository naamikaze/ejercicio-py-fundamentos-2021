anno = int(input('Ingresá un año: '))

A = anno % 19
B = anno % 4
C = anno % 7
D = A * 19 + 24
D = D % 30
E = B*2+C*4+D*6+5
E = E % 7
fecha = D + E + 22

if fecha > 31:
    fecha -= 31
    print(f'Las pascuas de {anno} serán el día {fecha} de abril')
else:
    print(f'Las pascuas de {anno} serán el día {fecha} de marzo')
