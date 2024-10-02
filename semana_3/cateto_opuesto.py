"""
Autor: Santiago Cacho
Fecha: 19/08/24
Función: Calcular cateto opuesto
"""

import math

hipotenusa = float(input('Introduzca la hipotenusa en cm: '))
angulo_base = float(input('Introduzca el angulo base en grados: '))

#angulo_radianes = math.radians(angulo_base)
cateto_opuesto = hipotenusa * math.sin(math.radians(angulo_base))
print(f'La longitud del cateto opuesto es {cateto_opuesto:.2f} cm.')
