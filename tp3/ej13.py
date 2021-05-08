desc=0
civil = 0

sb = int(input('Ingrese su dueldo básico: '))
ant = int(input('Ingrese su antiguedad: '))
print()
print('Ingrese su estado civil')
print()
print('1 - Si es soltero')
print('2 - Si es casado')
print()
ecv = int(input('Ingrese una opcion:'))

neto = sb/ant

if ecv == 1:
    civil = 'Soltero'
    desc = sb*0.05
    desc *= ant
else:
    civil = 'Casado'
    desc = sb*0.07
    desc *= ant
    
jubi = desc*0.11
obs = desc*0.03
sindi = desc*0.03

print()
print(f'INFORME DE TODO')
print()
print(f'Sueldo Básico: {sb}')
print(f'Antiguedad: {ant}')
print(f'Estado Civíl: {civil}')
print()
print('Descuentos')
print()
print(f'Jubilación: {jubi}')
print(f'Obra Social: {obs}')
print(f'Sindicato: {sindi}')
print()
