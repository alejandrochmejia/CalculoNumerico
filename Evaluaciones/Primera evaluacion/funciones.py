import numpy as np

###### CAMBIOS DE BASE #########

def fromDEC(n,base):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(int(n), base)
        nums.append(str(r))
    return ''.join(reversed(nums))

def toDEC(n,base):
    return str(int(n,base))

##### GAUSS SEIDEL ########
def creacionMatriz(n,lista):
    if len(lista) > n**2:
        pass
    else:
        matriz = np.array(lista[:n**2]).reshape(n,n)
        return matriz

def creacionVector(n,lista = []):
    if len(lista) == 0:
        lista = [0.0 for i in range(n)] 
    return np.array(lista[:n])

def GaussSeidel(a, b, x0=None, tol=0.000001, max_ite=100):
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
    
