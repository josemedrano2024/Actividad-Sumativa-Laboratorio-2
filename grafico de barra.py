import matplotlib.pyplot as plt

# Datos para el gráfico
categorias = ['Femenino', 'Masculino',]
valores = [11, 17,]

# Crear el gráfico de barras
plt.bar(categorias, valores, color='blue')

# Agregar títulos y etiquetas
plt.title('Gráfico de Barras ')
plt.xlabel('Genero')
plt.ylabel('Peso')

# Mostrar el gráfico
plt.show()


#link dataset
#https://www.kaggle.com/datasets/valakhorasani/gym-members-exercise-dataset
