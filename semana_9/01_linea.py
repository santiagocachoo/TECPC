import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, label='Cuadrado de X')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de Línea')
plt.legend()
plt.show()
