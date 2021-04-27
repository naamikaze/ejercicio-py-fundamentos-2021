anno = int(input('Ingrese un año: '))

if anno % 4 == 0 and anno % 100 == 0:
    print('No es biciesto')
elif anno % 4 == 0 and anno % 400 == 0 or anno % 4 == 0 and anno % 100 == 0 and anno % 400 == 0 or anno % 4 == 0:
    print('El año es biciesto')
else:
    print('No es biciesto')
    

