#Implementar la clase Punto, que represente un punto en el plano por sus coordenadas x,y. 
# Añadir los getters y setters

class Punto():

    def __init__ (self, puntoX, puntoY):
        self.__puntoX=puntoX
        self.__puntoY=puntoY

    @property
    def puntoX(self):
        return self.__puntoX

    @puntoX.setter
    def puntoX(self, puntoX):
        self.__puntoX=puntoX

    @property
    def puntoY(self):
        return self.__puntoY

    @puntoY.setter
    def puntoY(self, puntoY):
        self.__puntoY=puntoY