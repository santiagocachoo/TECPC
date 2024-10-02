import matplotlib.pyplot as plt

categorias = ['A', 'B', 'C', 'D', 'E']
valores = [5, 7, 3, 8, 6]

plt.bar(categorias, valores, color='blue', label='Valores')
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Gráfico de Barras')
plt.legend()
plt.show()