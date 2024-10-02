"""
Autor: Santiago Cacho
Fecha: 19/08/24
Función: Calcular area de triangulo con longitudes
"""

import math as m

def area_triangulo(a, b, c):
    s = (a + b + c) / 2
    area = m.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = float(input('Introduzca la longitud del primer lado en cm: '))
b = float(input('Introduzca la longitud del segundo lado en cm: '))
c = float(input('Introduzca la longitud del tercer lado en cm: '))

area = area_triangulo(a, b, c)
print(f'El area de un triangulo cuyos lados son de {a}, {b} y {c} cm es de {area:.2f} cm cuadrados')
