"""
Autor: Santiago cacho
Fecha: 15/08/24
Ejercicio: Transformar coordenadas polares a rectangulares y viceversa
"""

# import the math library
import math as m

# iniciando variables float
# forma polar a rectangular
theta_rad = 0.0             # angulo en radianes
theta_deg = 0.0             # angulo en grados
r_polar = 0.0               # coordenada en eje polar

x_trans = 0.0               # transformacion r,0 a x
y_trans = 0.0               # transformacion r,0 a y

cal_interno = 0.0           # variable auxiliar para calculos internos


# forma rectangular a polar
r_trans = 0.0               # (X,Y) transformada a r,0
theta_trans = 0.0           # (X,Y) transformada a r,0
x_usr = 0.0                 # (X,Y) a transformar
y_usr = 0.0                 # (X,Y) a transformar

print('Hola usuario, hora de transformar sistemas coordenados en R2. \n')
print('Primero transformaremos coordenadas polares a rectangulares. \n')

theta_deg = float(input('\tIntroduzca el angulo en grados: '))
theta_rad = m.radians(theta_deg)
r_polar = float(input('\tIntroduzca magnitud de r: '))

x_trans = r_polar * m.cos(theta_rad)
y_trans = r_polar * m.sin(theta_rad)

print(f'Las coordenadas polares ({r_polar}, {theta_deg})')
print(f'\t equivalen a {x_trans:.3f}, {y_trans:.3f} \n')


# coordenadas rectangulares a polares
print('Ahora, transformaremos coordenadas rectangulares a polares. \r')
x_usr = float(input('\t Introduzca la coordenada x: '))
y_usr = float(input('\t Introduzca la coordenada y: '))

# sqrt = raiz cuadrada
# pow(B,E) elevar base B al exponente E
r_trans = m.sqrt(m.pow(x_usr, 2) + m.pow(y_usr, 2))

# atan(y,x) = arcotangente(y/x) = tan a la -1(y/x)
theta_trans = m.atan2(y_usr, x_usr)
theta_trans = m.degrees(theta_trans)
print(f'Las coordenadas equivalen a : ({r_trans:.3f}, {theta_trans:.3f}) en coordenadas polares :)')



