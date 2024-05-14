import numpy as np

def fromDEC(n,base): #Función que traduce del sistema decimal a cualquier sistema numérico
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(int(n), base)
        nums.append(str(r))
    return ''.join(reversed(nums))

def toDEC(n,base): #Función que traduce de cualquier sistema numérico al sistema decimal
    return str(int(n,base))

def creacionMatriz(n,lista): #Función que crea una matriz de numpy con los elementos de una lista
    if len(lista) > n**2:
        pass
    else:
        matriz = np.array(lista[:n**2]).reshape(n,n)
        return matriz

def creacionVector(n,lista = []): #Función que crea un vector de numpy con los elementos de una lista
    if len(lista) == 0:
        lista = [0.0 for i in range(n)] 
    return np.array(lista[:n])

def GaussSeidel(a, b, x0=None, tol=0.000001, max_ite=100): #Función que realiza la operación del sistema de ecuaciones con el método Gauss Seidel
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
    x = x0.copy()
    for _ in range(max_ite):
        for i in range(n):
            x[i] = (b[i] - np.dot(a[i, :i], x[:i]) - np.dot(a[i, i + 1:], x[i + 1:])) / a[i, i]
        if np.linalg.norm(x - x0) < tol:
            break
        x0 = x.copy()
    return x.tolist()
    
