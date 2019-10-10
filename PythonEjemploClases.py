class Persona():
    
    def __init__(self, nombre, apellido):
        self.__nombre=nombre
        self.__apellido=apellido

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre

    #Se utiliza como alternativa a los setter y getter
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido=apellido

    #Equivale a toString en Java
    def __str__(self):
        return self.nombre + " " + self.apellido

p= Persona("Gonzalo","Punta")
print(p)

p.nombre="Pepe"
p.apellido="Ramos"
print(p)