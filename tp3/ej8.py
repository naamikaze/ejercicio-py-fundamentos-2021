cliente = int(input('Ingrese el nro de cliente: '))
pagar= int(input('Ingrese el importe su factura: '))

final = 0
calculo = 0
porc = 0


#
def veinte(importe): 
    final = importe
    return final


#
def diez(importe): 
    final = importe-importe*0.02
    if final > 120:
        final = importe
        final += 120
    return final
#

#
def treinta(importe): 
    porc = importe*0.10
    final = importe+porc
    if final < 150:
        final = importe 
        final += 500
    return final
#

print(f'El cliente nro: {cliente} debera abonar lo siguiente:')
print(f'Si el cliente paga antes de los primeros 10 días deberá abonar: {diez(pagar)}')
print(f'Si el cliente paga despues de los primeros 10 días deberá abonar: {veinte(pagar)}')
print(f'Si el cliente paga despues de los 20 días deberá abonar: {treinta(pagar)}')

