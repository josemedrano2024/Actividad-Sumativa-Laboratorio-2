import matplotlib.pyplot as plt

# Datos para el gráfico de pastel
labels = ['Polarity', 'Subjectivity', 'Target','Other']
sizes = [30, 25, 20, 25]  # Porcentajes de cada segmento
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']  # Colores para los segmentos

# Crear el gráfico de pastel
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Asegurar que el gráfico esté en un círculo
plt.axis('equal')

# Mostrar el gráfico
plt.show()

#Link dataset
#https://www.kaggle.com/datasets/gallo33henrique/twitter-spacex
