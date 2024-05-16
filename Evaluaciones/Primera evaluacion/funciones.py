import numpy as np

""" Traducción de sistemas numéricos """

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

def ejecucionSn(strEntrada,strSalida,n): #Funcion de conversión de sistemas numéricos
       if strEntrada == "DEC":
             baseEntrada = 10
       elif strEntrada == "BIN":
             baseEntrada = 2
       elif strEntrada   == "TER":
            baseEntrada = 3
       elif strEntrada == "CUA":
            baseEntrada = 4
       elif strEntrada == "OCT":
            baseEntrada = 8
       elif strEntrada == "HEX":
           baseEntrada = 16

       if strSalida == "DEC":
             baseSalida = 10
       elif strSalida == "BIN":
             baseSalida = 2
       elif strSalida   == "TER":
            baseSalida = 3
       elif strSalida == "CUA":
            baseSalida = 4
       elif strSalida == "OCT":
            baseSalida = 8
       elif strSalida == "HEX":
           baseSalida = 16
        
       if baseEntrada == 10:
            if baseSalida == 10: #Si es la misma base decimal, se imprime el mismo valor
                resultado = str(n)
            elif baseSalida == 16: #La base hexadecimal es todo un caso aparte ya que contiene letras
                cadena = hex(int(n))
                cadena = cadena[2:]
                cadena = cadena.upper()
                resultado = cadena
            else: #Para las demás base
                resultado = fromDEC(n,baseSalida)
       else: #Cuando la base de entrada no es la decimal se ejecuta este 'else'
            n = toDEC(n,baseEntrada)
            if baseSalida == 10: #Si la base de salida es decimal
                resultado = str(n)
            elif baseSalida == 16: #Si la base de salida es hexadecimal
                cadena = hex(int(n))
                cadena = cadena[2:]
                cadena = cadena.upper()
                resultado = cadena
            else: #Si la base de salida es cualquiera otra base
                resultado = fromDEC(n,baseSalida)
        
       return resultado

""" Gauss Seidel """

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
    
def GaussSeidel(A, b, x0=None, tolerancia=1e-6, maxIteraciones=100): #Función que resuelve un sistema de ecuaciones lineales utilizando el método de Gauss-Seidel
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
    x = x0.copy()
    for iteration in range(maxIteraciones):
        for i in range(n):
            # Calculamos la suma de los términos conocidos
            suma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
            # Calculamos el nuevo valor de x[i]
            x[i] = (b[i] - suma) / A[i, i]

        # Calculamos el error absoluto manualmente
        error = np.max(np.abs(A @ x - b)) #Se calcula la diferencia del producto de la matriz A y el vector X con el vector B
        if error < tolerancia:
            break

    return x.tolist()
