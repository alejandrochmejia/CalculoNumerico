class persona:
    def __init__(self):
        pass
    
    #Setters
    def setNombre(self,nombre=""): 
        if isinstance(nombre,str) and nombre.isalpha(): self.nombre = nombre
        else: print("Nombre no permitido")
    def setEdad(self,edad=0): 
        if isinstance(edad,int): self.edad = edad
        else: print("Edad no permitida")
    def setDNI(self,dni=""):
        if isinstance(dni,str) and dni.isnumeric(): self.dni = dni
        else: print("DNI/CI no permitido")
    
    #Getters
    def getNombre(self,nombre): return nombre
    def getEdad(self,edad): return edad
    def getDNI(self,dni):return self.dni

    #Functions
    def mostrar(self):
        print("\nNombre: {0}\nEdad: {1}\nDNI: {2}\n".format(self.nombre,self.edad,self.dni))

    def esMayor(self):
        if self.edad >= 18: return True
        else: return False

alejandro = persona()
alejandro.setNombre("alejandro")
alejandro.setEdad(19)
alejandro.setDNI("32278392")
alejandro.mostrar()
print("Valor logico de mayoria de edad:",alejandro.esMayor(),"\n")