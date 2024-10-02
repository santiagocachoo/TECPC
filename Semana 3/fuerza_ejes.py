"""
Autor: Santiago Cacho
Fecha: 19/08/24
Función: Calcular fuerza total 
"""

import math as m

f1_magnitud = float(input('Introduzca la magnitud de la fuerza 1: '))
angulo1 = float(input('Introduzca el angulo de la fuerza 1 (en grados): '))

f2_magnitud = float(input('Introduzca la magnitud de la fuerza 2: '))
angulo2 = float(input('Introduzca el angulo de la fuerza 2 (en grados): '))

f3_magnitud = float(input('Introduzca la magnitud de la fuerza 3: '))
angulo3 = float(input('Introduzca el angulo de la fuerza 3 (en grados): '))

angulo1 = m.radians(angulo1)
angulo2 = m.radians(angulo2)
angulo3 = m.radians(angulo3)

f_x_total = f1_magnitud * m.cos(angulo1) + f2_magnitud * m.cos(angulo2) + f3_magnitud * m.cos(angulo3)
f_y_total = f1_magnitud * m.sin(angulo1) + f2_magnitud * m.sin(angulo2) + f3_magnitud * m.sin(angulo3)

print(f_x_total, f_y_total)

fuerza_total = m.sqrt(m.pow(f_x_total, 2) + m.pow(f_y_total, 2))
angulo_total = m.degrees(m.atan2(f_y_total, f_x_total))

print(f'Fuerza total en el eje x: {f_x_total:.2f} N')
print(f'Fuerza total en el eje y: {f_y_total:.2f} N')
print(f'Fuerza total: {fuerza_total:.2f} N')
print(f'Angulo de la fuerza total: {angulo_total:.2f}°')


