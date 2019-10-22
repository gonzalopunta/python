class Persona():
    def __init__ (self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def __str__ (self):
        return self.nombre + " " + self.apellido + ", " + self.edad + " años"

    def __gt__(self, other):
        return self.apellido > other.apellido


pedro=Persona ("Pedro", "ZLopez", 40)
maria=Persona ("Maria", "ACampos", 26)

print (pedro<maria)