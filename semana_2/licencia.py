"""
Autor: Santiago Cacho
Fecha: 15/08/24
Función: Determinar si persona puede sacar licencia de conducir
"""

edad = int(input('Introduzca edad:'))
id = str(input('Tiene identificacion oficial?(Si/No)'))

if edad >= 18 and id == 'Si':
    print('Puede sacar licencia de conducir') 
else:
    print('No puede sacar licencia de conducir')  