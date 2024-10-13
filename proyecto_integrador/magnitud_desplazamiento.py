import math as m

def magnitud_desplazamiento():
    """
    esta función calcula la magnitud de desplazamiento tomando las coordenadas del punto inicial y punto final
    pide los datos para cada punto y despues calcula el desplazamiento para el eje "x" y "y" 
    finalmente calcula la magnitud usando el teorema de pitagoras con los desplazamientos
    """
    # función para manejar el ingreso de datos 
    def input_float(mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                return valor
            except ValueError:
                print('Por favor, ingrese un número válido.')

    # pedir puntos iniciales y finales
    punto_inicial_x = input_float('Ingrese el punto inicial en x: ')
    punto_inicial_y = input_float('Ingrese el punto inicial en y: ')
    punto_final_x = input_float('Ingrese el punto final en x: ')
    punto_final_y = input_float('Ingrese el punto final en y: ')

    # calcular desplazamientos
    desplazamiento_x = punto_final_x - punto_inicial_x
    desplazamiento_y = punto_final_y - punto_inicial_y

    # calcular magnitud
    magnitud = m.sqrt(desplazamiento_x**2 + desplazamiento_y**2)
    print(f'La magnitud del desplazamiento es: {magnitud}')
