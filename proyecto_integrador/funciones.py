import math as m

def integrales():
    pass

def magnitud_desplazamiento(pix, pfx, piy, pfy):                    # toma punto inicial y punto final de x y y
    desplazamiento_x = pfx - pix                                    # calcula desplazamiento de x
    desplazamiento_y = pfy - piy                                    # calcula desplazamiento de y
    magnitud = m.sqrt(desplazamiento_x**2 + desplazamiento_y**2)    # calcula magnitud con teorema de pitagoras
    return magnitud                                                 # devuelve magnitud


def velocidad_instantanea(funcion, x):
    pass                                                            # calcula con la función???

def aceleración_instantanea(funcion, x):                                  
    pass                                                            # calcula con la función???

# euler

def metodo_euler_intervalo():
    # pedir valores iniciales
    xn = float(input('Ingrese el valor inicial de x (x_0): '))
    yn = float(input('Ingrese el valor inicial de y (y_0): '))
    h = float(input('Ingrese el valor de paso h: '))
    x_final = float(input('Ingrese el valor final del intervalo para x: '))

    # pedir la función derivada 
    print('Por favor, ingrese la función derivada f(x, y). Por ejemplo, para 2x + 3, ingrese "2*x ´3"')
    derivada_input = input('f(x, y) = ')

    # crear la función derivada a partir del input
    def derivada(x, y):
        return eval(derivada_input)
    
    # lista para resultados
    resultados = [(xn, yn)]

    # calcular valores con metodo de euler:
    while xn < x_final:
        pendiente = derivada(xn, yn)
        xn = xn + h
        yn = yn + h * pendiente
        resultados.append((xn, yn))

    print('\nValores calculados con el metodo de Euler:')
    for i, (x_val, y_val) in enumerate(resultados):
        print(f'Paso {i}: x = {x_val}, y = {y_val}')

metodo_euler_intervalo()



