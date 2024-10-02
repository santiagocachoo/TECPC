"""
Autor: Santiago Cacho
Fecha: 12/08/24
Función: Calcular velocidad promedio
"""

distancia_recorrida = float(input('Introduce la distancia total recorrida: '))
tiempo_utilizado = float(input('Introduce el tiempo total para recorrer la distancia: '))

velocidad_promedio = distancia_recorrida / tiempo_utilizado

print('La velocidad promedio es: ' + str(velocidad_promedio))