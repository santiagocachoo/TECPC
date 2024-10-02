matriz = []
for i in range(2):
    fila = []
    for j in range(2):
        valor = int(input(f'El elemento ({i},{j}) es: '))
        fila.append(valor)
    matriz.append(fila)

print('\nLa matriz es: ')
for fila in matriz:
    print(fila)

a = matriz[0][0]
b = matriz[0][1]
c = matriz[1][0]
d = matriz[1][1]
determinante = (a * d) - (b * c)

print(f'\nEl determinante de la matriz es: {determinante}')