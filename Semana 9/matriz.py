filas = int(input('Introduce el numero de filas: '))
columnas = int(input('Introduce el numero de columnas: '))

matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = input(f'El elemento ({i},{j}) es: ')
        fila.append(valor)
    matriz.append(fila)

print('\nLa matriz es:')
for fila in matriz:
    print(fila)
