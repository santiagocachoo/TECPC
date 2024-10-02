"""
Autor: Santiago Cacho
Fecha: 22/08/24
Función: Area con if
"""
import math as m

opcion_usr = 0
# 0 = cuadrado, 1 = rectangulo, 2 = triangulo
lado_01 = 0.0
lado_02 = 0.0
lado_03 = 0.0
area_fi = 0.0
perimetro_fig = 0.0

msg = '''Bienvenido usuario :)
En este programa calcularemos area y perimetro de distintas figuras :)
Las opciones son:
    0 = cuadrado
    1 = rectangulo
    2 = triangulo'''
print(msg)
opcion_usr = int(float(input('Seleccione la figura que desea: ')))

if opcion_usr == 0:
    lado_01 = float(input('Ingrese la medida de un lado del cuadrado: '))
    area_fi = lado_01**2
    perimetro_fig = lado_01*4

if opcion_usr == 1:
    lado_01 = float(input('Ingrese la medida de la base del rectangulo: '))
    lado_02 = float(input('Ingrese la medida de la altura del rectangulo: '))
    area_fi = lado_01*lado_02
    perimetro_fig = (lado_01*2)+(lado_02*2)

if opcion_usr == 2:
    lado_01 = float(input('Ingrese la medida de la base del triangulo: '))
    lado_02 = float(input('Ingrese la medida del siguiente lado del triangulo: '))
    lado_03 = float(input('Ingrese la medida del ultimo lado del triangulo: '))
    s = (lado_01 + lado_02 + lado_03) / 2
    area_fi = m.sqrt(s * (s - lado_01) * (s - lado_02) * (s - lado_03))
    perimetro_fig = s * 2

print(f'El area de la figura seleccionada es: {area_fi:.2f} cm cuadrados, y el perimetro es de: {perimetro_fig:.2} cm')