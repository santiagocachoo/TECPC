import numpy as np
import matplotlib.pyplot as plt
import math as m

# funcion para calcular trayectoria
def calcular_trayectoria(velocidad_inicial, angulo):
    # convertir angulo a radianes
    angulo_radianes = m.radians(angulo)

    # definir constante gravedad
    g = 9.81

    # tiempo de vuelo
    tiempo_vuelo = (2 * velocidad_inicial * m.sin(angulo_radianes)) / g

    # crear matriz para coordenadas
    puntos_tiempo = np.linspace(0, tiempo_vuelo, num=100) 
    coordenadas = np.zeros((100, 2))

    # calcular coordenadas en cada instante
    for i, t in enumerate(puntos_tiempo):
        x = velocidad_inicial * m.cos(angulo_radianes) * t
        y = (velocidad_inicial * m.sin(angulo_radianes) * t) - (0.5 * g * t**2)
        coordenadas[i] = [x, y]
    return coordenadas

# funcion para graficar
def grafica_trayectoria(coordenadas):
    x = coordenadas[:, 0]
    y = coordenadas[:, 1]

    plt.scatter(x, y, label='Trayectoria de objeto')
    plt.title('Trayectoria del objeto en un plano 2D')
    plt.xlabel('Eje X (Distancia horizontal)')
    plt.ylabel('Eje Y (Altura)')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    try:
        velocidad_inicial = float(input('Ingresa la velocidad inicial (m/s): '))
        angulo = float(input('Ingresa el angulo de lanzamiento (grados): '))

        # validar entradas
        if velocidad_inicial <= 0 or angulo <= 0:
            raise ValueError('La velocidad y el angulo deben ser mayores que 0')
        
        # calcular y graficar trayectoria
        coordenadas = calcular_trayectoria(velocidad_inicial, angulo)
        grafica_trayectoria(coordenadas)
    
    except ValueError as e:
        print(f'Error: {e}. Por favor ingrese datos validos.')

main()