#Realizado por Víctor Miranda Y Gonzalo Punta
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

fecha=Fecha(3,3,2218)
fecha2=Fecha(3,3,2018)

print(fecha>=fecha2)



"""
 Heredar de la clase Fecha otra llamada Fecha_mod. Tendrá, además de los
métodos anteriores, otro que imprima por pantalla una fecha en formato
dd/mm/aaaa cuando se ejecute la instrucción:
print objeto_Fecha_mod
Para ello, hay que sobreescribir el método __str__. Se recuerda que la sintaxis
más básica de este método en el ámbito de una clase es:
Pruébelo mediante este código que haga uso de la clase Fecha_mod: 
"""
class Fecha_mod(Fecha):
   def __str__ (self):
       return str(self.dia) + "/" + str(self.mes) + "/" + str(self.anno)
o=Fecha_mod(8, 2, 12)
print (o)


"""
 Implementar la clase Persona, pensando en usarla en un calendario para
felicitaciones, que tendrá como atributos el nombre completo, la fecha de nacimiento, la
fecha de su onomástica (santo), su teléfono y email. Tiene que hacer uso de la clase
Fecha del ejercicio 1. Implementar el constructor y los getter y setter
correspondientes.
Sobreescribir el método __le__ de forma que una persona será menor que otra cuando
su fecha de nacimiento lo sea.
"""
class Persona ():
    def __init__(self, nombreCompleto,fechaNacimiento,fechaSanto,telefono,email):
        self.__nombreCompleto=nombreCompleto
        self.__fechaNacimiento=fechaNacimiento
        self.__fechaSanto=fechaSanto
        self.__telefono=telefono
        self.__email=email

    @property
    def fechaNacimiento(self):
        return self.__fechaNacimiento
    
    @fechaNacimiento.setter
    def dia(self, fechaNacimiento):
        self.__fechaNacimiento=fechaNacimiento
    
    def __le__(self, other):
        return ((self.fechaNacimiento)<=(other.fechaNacimiento))

p=Persona("fdf",'1,2,2020','1,2,2020',3323,'victor@dsfds')
p2=Persona("fdf",'1,2,2018','1,2,2018',3323,'victor@dsfds')

print(p<=p2)
    