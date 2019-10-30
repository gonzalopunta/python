"""
Crear un programa con una clase ordenador que permita almacenar características de un ordenador, como
capacidad, procesador, precio base, etc. Crear dos clases hijas, llamadas Tablet y Portátil. Añadir 
atributos que especifiquen su comportamiento respecto a los ordenadores normales. 

La clase madre debe tener un método para calcular el precio de venta al público aplicando un % de 
ganancia del vendedor al precio base. Este método se debe reescribir en las clases hijas con algún 
aspecto concreto de cada una de ellas para calcular el precio de otra forma. Por ejemplo, a la tablet 
se le puede añadir un plus por el seguro de rotura de pantalla y al portátil un descuento. 
Crear un script sencillo para comprobar todo.

"""

class ordenador():
    def __init__(self, precioBase, capacidad, procesador):
        self.__precioBase=precioBase
        self.__capacidad=capacidad
        self.__procesador=procesador
