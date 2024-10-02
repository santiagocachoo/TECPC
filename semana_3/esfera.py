"""
Autor: Santiago Cacho
Fecha: 19/08/24
Función: Calcular area y volumen de esfera
"""

import math as m

radio = float(input('Ingrese radio en cm: '))

area = 4 * (m.pi) * m.pow(radio, 2)

volumen = 4/3 * m.pi * m.pow(radio, 3)


print(f'El area de la esfera es de {area:.2f} cm cuadrados, y su volumen es de {volumen:.2f} cm cubicos')