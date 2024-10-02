def crear_matriz(num_filas, num_columnas):
    matriz = []
    for i in range(num_filas):
        fila = []
        for j in range(num_columnas):
            valor = int(input(f"El elemento ({i},{j}) es: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumar_columnas(matriz):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    suma_columnas = [0] * num_columnas  # Lista inicializada con ceros para las sumas

    for j in range(num_columnas):
        for i in range(num_filas):
            suma_columnas[j] += matriz[i][j]  # Suma los elementos de cada columna

    return suma_columnas

def main():
    # Solicitar dimensiones de la matriz
    num_filas = int(input("Ingrese el número de filas: "))
    num_columnas = int(input("Ingrese el número de columnas: "))

    # Crear la matriz a partir de los valores ingresados por el usuario
    matriz = crear_matriz(num_filas, num_columnas)

    # Mostrar la matriz ingresada
    print("\nMatriz ingresada:")
    for fila in matriz:
        print(fila)

    # Calcular la suma de cada columna
    suma_columnas = sumar_columnas(matriz)

    # Mostrar la lista con la suma de cada columna
    print("\nSuma de cada columna:", suma_columnas)

# Bloque estándar para ejecutar el código cuando se corre directamente
if __name__ == '__main__':
    main()
