cont = 7
lista = []
while cont != 3001:
    if cont % 7 == 0:
        lista.append(cont)
    cont+=1
print(f'{lista}')

