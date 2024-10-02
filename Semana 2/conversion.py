"""
Autor: Santiago Cacho
Fecha: 12/08/24
Función: Convertir metros a pies
"""

metros = 0.0
pies_equivalentes = 0.0
FACTOR_CONVERSION = 3.28084

metros = float(input('Introduce la distancia en metros: '))

pies_equivalentes = metros * FACTOR_CONVERSION

print(f'La distancia en pies es: {pies_equivalentes:.2f} pies')