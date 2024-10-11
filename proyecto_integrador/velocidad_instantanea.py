import math as m

def magnitud_velocidad_instantanea(funcion, x):
    # funcion para manejar el ingreso de datos
    def input_float(mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                return valor
            except ValueError:
                print('Por favor, ingrese un numero valido')

    # pedir el valor de x al usuario
    x = input_float('Ingrese el valor de x: ')

    # pedir la función de velocidad al usuario
    print("""
    Ingrese la función derivada f(x, y)
    Ejemplos de como escribir expresiones matematicas:
        - Suma y resta = 2 + 3 - 4
        - Multiplicación = 5*x*y
        - División = x / y
        - Potencia = x**2 (esto significa x al cuadrado)
        - Funciones matematicas = Para seno: m.sin(x), para coseno: m.cos(x), para logaritmos: m.log(x). 
        Para mas información sobre como escribir una función matematica, consultar documentación de modulo math

    NOTA: para funciones matematicas, asegurarse de ingresar 'm.' antes de la función   
    """)

    funcion_velocidad = input_float('f(x) = ')

    # crear entorno seguro que solo permite ciertas funciones matematicas para la expresion de la derivada
    entorno_seguro = {
        'x': 0,
        'm': m,
        '__builtins__': None                # desactiva acceso a funciones peligrosas
    }

    # calcular la magnitud de la velocidad instantanea usando eval para la funcion
    try:
        # evaluar la expresion en el entorno seguro
        entorno_seguro['x'] = x
        velocidad = eval(funcion_velocidad, entorno_seguro)
        magnitud_velocidad = abs(velocidad)

        print(f'La magnitud de la velocidad instantanea en x = {x} es: {magnitud_velocidad}')
    except Exception as e:
        print(f'Error al evaluar la funcion de velocidad: {e}')