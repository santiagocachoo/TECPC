"""
Autor: Santiago Cacho
Fecha: 12/08/24
Función: Calcular precio a pagar
"""

precio_kilo = 0.0
peso_bolsa = 0.0
precio_pagar = 0.0

precio_kilo = float(input('Introduce el precio por kilo: '))
peso_bolsa = float(input('Introduce el peso de la bolsa: '))

precio_pagar = precio_kilo * peso_bolsa

print('El total a pagar es: ' + str(precio_pagar))