import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.scatter(x, y, color='red', label='Puntos (X, Y)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de Dispersión')
plt.legend()
plt.show()