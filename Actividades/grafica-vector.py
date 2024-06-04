import numpy as np
import matplotlib.pyplot as plt

def gauss_seidel(A, b, x0, tol=1e-10, max_iterations=1000):
    n = len(b)
    x = x0.copy()
    
    for k in range(max_iterations):
        x_old = x.copy()
        
        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i+1:], x_old[i+1:])
            x[i] = (b[i] - sum1 - sum2) / A[i, i]
        
        # Check for convergence
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            break
    
    return x

# Definir el sistema de ecuaciones A*x = b
A = np.array([[4, 1, 2],[3, 5, 1],[1, 1, 3]], dtype=float)
b = np.array([4, 7, 3], dtype=float)
x0 = np.zeros(len(b))

# Aplicar el método de Gauss-Seidel
x = gauss_seidel(A, b, x0)

# Graficar el vector solución x
plt.figure(figsize=(8, 6))
plt.plot(x, 'o-', label='Solución $x$')
plt.xlabel('Índice')
plt.ylabel('Valor de $x_i$')
plt.title('Solución del sistema de ecuaciones usando Gauss-Seidel')
plt.legend()
plt.grid(True)
plt.show()

# Imprimir el vector solución x
print("Vector solución x:", x)

