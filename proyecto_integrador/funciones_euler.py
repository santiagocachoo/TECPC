import math as m

def metodo_euler_intervalo():
    # funcion para manejar ingreso de datos
    def input_float(mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                return valor
            except ValueError:
                print('Por favor, ingrese un numero valido')

    # pedir valores iniciales usando la funcion de input
    xn = input_float('Ingrese el valor inicial de x (x_0): ')
    yn = input_float('Ingrese el valor inicial de y (y_0): ')
    h = input_float('Ingrese el valor de paso h: ')
    x_final = input_float('Ingrese el valor final del intervalo para x: ')

    # pedir la función derivada 
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

    derivada_input = input('f(x, y) = ')

    # crear entorno seguro que solo permite ciertas funciones matematicas para la expresion de la derivada
    entorno_seguro = {
        'x': 0,
        'y':  0,
        'm': m,
        '__builtins__': None                # desactiva acceso a funciones peligrosas
    }

    # convertir la expresion de la funcion a una funcion de python
    def derivada (x, y):
        try:
            # evaluar la expresión en el entorno seguro
            entorno_seguro['x'] = x
            entorno_seguro['y'] = y
            return eval(derivada_input, entorno_seguro)
        except Exception as e:
            print(f'Error al evaluar la función: {e}')
            return None
    
    # lista para resultados
    resultados = [(xn, yn)]

    # calcular valores con metodo de euler:
    while xn < x_final:
        pendiente = derivada(xn, yn)
        if pendiente is None:
            print('El calculo se detuvo debido a un error en la función derivada. Por favor ingresarla correctamente')
            break
        xn = xn + h
        yn = yn + h * pendiente
        resultados.append((xn, yn))

    print('\nValores calculados con el metodo de Euler:')
    for i, (x_val, y_val) in enumerate(resultados):
        print(f'Paso {i}: x = {x_val}, y = {y_val}')


# función que calcula los valores de x tomando la x inicial, la h, y cuantos incrementos se desean
def calcular_siguiente_xn():
    # funciones para manejar ingreso de datos
    def input_float(mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                return valor
            except ValueError:
                print('Por favor, ingrese un numero valido')
    
    def input_int(mensaje):
        while True:
            try:
                valor = int(input(mensaje))
                return valor
            except ValueError:
                print('Por favor, ingrese un numero entero valido')

    # pedir datos iniciales con las funciones adecuadas
    x_inicial = input_float('Ingrese el valor incial de x: ')
    h = input_float('Ingrese el valor de h (tamaño de incrementos): ')
    num_incrementos = input_int('Ingrese el numero de incrementos: ')


    # crear lista para los valores de x
    valores_x = [x_inicial]

    # generar los valores restantes con el incremento que se indico
    for _ in range(num_incrementos):
        x_inicial += h
        valores_x.append(x_inicial)

    print('Los valores de x son:')
    print(valores_x)


def calcular_pendiente_euler():
    """
    función para calcular el valor de la pendiente f(x_n, y_n) en el método de Euler.
    solicita al usuario que ingrese los valores de x_n, y_n y la función de la derivada.
    verifica que las entradas sean válidas y evalúa de manera segura.
    """
    # función para manejar el ingreso de datos 
    def input_float(mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                return valor
            except ValueError:
                print('Por favor, ingrese un número válido.')

    # pedimos al usuario que ingrese los valores de x_n y y_n
    x_n = input_float('Ingrese el valor de x_n: ')
    y_n = input_float('Ingrese el valor de y_n: ')

    print("""
    Ingrese la función de aceleración instantanea
    Ejemplos de como escribir expresiones matematicas:
        - Suma y resta = 2 + 3 - 4
        - Multiplicación = 5*x*y
        - División = x / y
        - Potencia = x**2 (esto significa x al cuadrado)
        - Funciones matematicas = Para seno: m.sin(x), para coseno: m.cos(x), para logaritmos: m.log(x). 
        Para mas información sobre como escribir una función matematica, consultar documentación de modulo math

    NOTA: para funciones matematicas, asegurarse de ingresar 'm.' antes de la función   
    """)

    # pedimos la expresión de la derivada al usuario
    derivada_funcion = input("f(x, y) = ")

    # crear entorno seguro que solo permite ciertas funciones matematicas para la expresion de la derivada
    entorno_seguro = {
        'x': x_n,
        'y': y_n,
        'm': m,
        '__builtins__': None  # desactivamos el acceso a funciones peligrosas
    }

    # calcular el valor de la pendiente f(x_n, y_n) usando eval de forma segura
    try:
        pendiente = eval(derivada_funcion, entorno_seguro)  # evaluamos la expresión de la derivada
        print(f"El valor de la pendiente f({x_n}, {y_n}) es: {pendiente}")
    except Exception as e:
        print(f"Error al evaluar la función de la derivada: {e}")


calcular_pendiente_euler()