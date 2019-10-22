"""
Crear una nueva clase Fecha. Tendrá por atributos el día, mes y anno. Estos
parámetros se podrán inicializar cuando se cree un objeto.
Sobrecargar los métodos especiales __lt__ (menor estricto <), __le__ (menor o
igual <=), __gt__ (mayor estricto >), __ge__ (mayor o igual >=) para que
devuelva True cuando una fecha sea menor que otra, menor o igual que otra,
mayor que otra o mayor o igual que otra, respectivamente.
Un ejemplo de implementación de la función mayor o igual, __ge__, sería:
def __ge__ (self, otra_fecha):
#codigo
"""
class Fecha():
   def __init__(self, dia, mes, anno):
       self.__dia=dia
       self.__mes=mes
       self.__anno=anno
   @property
   def dia(self):
       return self.__dia
   @dia.setter
   def dia(self, dia):
       self.__dia=dia
   @property
   def mes(self):
       return self.__mes
   @mes.setter
   def mes(self, mes):
       self.__mes=mes
   @property
   def anno(self):
       return self.__anno
   @anno.setter
   def anno(self, anno):
       self.__anno=anno
   #Compara el menor estricto
   def __lt__(self, other):
       return (self.anno,self.mes,self.dia)<(other.anno,other.mes,other.dia)
   #Compara el menor o igual estricto
   def __le__(self, other):
       return (self.anno,self.mes,self.dia)<=(other.anno,other.mes,other.dia)
   #Compara el mayor estricto
   def __gt__(self, other):
       return (self.anno,self.mes,self.dia)>(other.anno,other.mes,other.dia)
   #Compara el mayor o igual estricto
   def __ge__(self, other):
       return (self.anno,self.mes,self.dia)>=(other.anno,other.mes,other.dia)


class Fecha_mod(Fecha):

    def __str__ (self):
        return str(self.dia) + "/" + str(self.mes) + "/" + str(self.anno)

o=Fecha_mod(8, 2, 12)
print (o)