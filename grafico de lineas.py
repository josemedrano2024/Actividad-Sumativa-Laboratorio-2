import matplotlib.pyplot as plt

# Datos para las dos líneas
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]  # Línea 1 (cuadrados)
y2 = [1, 2, 3, 4, 5]    # Línea 2 (valores originales)

# Crear el gráfico
plt.plot(x, y1, label='Línea 1: DC', color='b', marker='o')
plt.plot(x, y2, label='Línea 2: Marvel', color='r', marker='x')

# Añadir títulos y etiquetas
plt.title('Gráfico de líneas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.show()


#Enlace del dataset
#https://www.kaggle.com/datasets/willianoliveiragibin/marvel-vs-dc