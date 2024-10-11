import math as m
import sympy as sp

def calcular_integral_indefinida():
    """
    función para calcular la integral indefinida de una función dada
    solicita al usuario la funcion y verifica que la entrada sea valida. despues calcula la integral indefinida con sympy
    """

    # funcion para manejar el ingreso de la funcion
    def input_funcion(mensaje):
        while True:
            try:
                # pedimos al usuario que ingrese la funcion en terminos de la variable 'x'
                expr = input(mensaje)
                funcion = sp.sympify(expr)              # convierte la entrada a una expresion simbolica
                return funcion
            except (sp.SympifyError, ValueError):
                print("Por favor, ingrese una función válida en términos de 'x'")

    # definir variable simbolica
    x = sp.symbols('x')

    # se pide la función al usuario
    funcion = input_funcion('Ingrese la función para calcular la integral indefinida (por ejemplo: 2+x + 3): ')

    # calcular integral indefinida
    try:
        integral_indefinida = sp.integrate(funcion, x)
        print(f'La integral indefinida de la función {funcion} es: {integral_indefinida} + C')
    except Exception as e:
        print(f'Error al calcular la integral indefinida: {e}')

calcular_integral_indefinida()