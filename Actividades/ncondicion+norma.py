import numpy as np
import matplotlib.pyplot as plt

# Creamos una matriz 3x3
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calculamos el número de condición de la matriz
cond_A = np.linalg.cond(A)
# Calcular la normal de la matriz
norm_A = np.linalg.norm(A)

#Prints
print("El número de condición de la matriz es:", cond_A)
print("La norma de la matriz:", norm_A)

# Crear un figura y un eje
fig, ax = plt.subplots()

# Graficar la línea hacia la norma
ax.plot([0, norm_A], [0, norm_A], 'b-', label='Norma')

# Graficar la línea hacia el número de condición
ax.plot([0, cond_A], [0, cond_A], 'r-', label='Número de condición')

# Agregar título y etiquetas
ax.set_title('Norma y número de condición de la matriz')
ax.set_xlabel('Valor')
ax.set_ylabel('')

# Mostrar la leyenda
ax.legend()

# Mostrar la gráfica
plt.show()