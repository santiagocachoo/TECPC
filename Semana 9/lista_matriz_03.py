from pprint import pprint

def MatricesEjemplo(NumFilas, NumCol):
    Matriz = []
    for Fila in range(NumFilas):
        Lista = []
        for Columna in range(NumCol):
            # Uso de f-string para formatear la solicitud del dato
            dato = int(input(f"El elemento ({Fila},{Columna}) es: "))
            Lista.append(dato)
        Matriz.append(Lista)
    return Matriz

def MostrarMatriz(Matriz):
    # Utilizamos pprint para imprimir la matriz de manera legible
    pprint(Matriz)
    return None

def main():
    filas = int(input('Ingrese el número de filas:'))
    columnas = int(input('Ingrese el número de columnas:'))
    Matriz = MatricesEjemplo(filas, columnas)
    print("\nMatriz ingresada:")
    MostrarMatriz(Matriz)
    return None

 
# Bloque estándar para ejecutar el código cuando se corre directamente
if __name__ == '__main__':
    main()
