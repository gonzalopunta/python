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
"""
class Ordenador():
   def __init__(self, precioBase, capacidad, procesador):
      self.__precioBase=precioBase
      self.__capacidad=capacidad
      self.__procesador=procesador

   @property
   def precioBase(self):
      return self.__precioBase
    
   @precioBase.setter
   def precioBase(self, precioBase):
      self.__precioBase=precioBase


   @property
   def capacidad(self):
      return self.__capacidad
   
   @capacidad.setter
   def capacidad(self, capacidad):
      self.__capacidad=capacidad


   @property
   def procesador(self):
      return self.__procesador
   
   @procesador.setter
   def procesador(self, procesador):
      self.__procesador=procesador

   def precioVenta(self, porcentaje):
      return (self.precioBase*porcentaje)/100


class Portatil(Ordenador):
   def __init__(self, precioBase, capacidad, procesador, descuento):
      self.__precioBase=precioBase
      self.__capacidad=capacidad
      self.__procesador=procesador
      self.__descuento=descuento

   @property
   def descuento(self):
      return self.__descuento
    
   @descuento.setter
   def descuento(self, descuento):
      self.__descuento=descuento

   def precioVenta(self, porcentaje, descuento):
      precioSinDescuento = (self.precioBase*porcentaje)/100
      return  precioSinDescuento - (precioSinDescuento*(descuento/100))


class Tablet(Ordenador):
   def __init__(self, precioBase, capacidad, procesador, seguroPantalla):
      self.__precioBase=precioBase
      self.__capacidad=capacidad
      self.__procesador=procesador
      self.__seguroPantalla=seguroPantalla

   @property
   def seguroPantalla(self):
      return self.__seguroPantalla
    
   @seguroPantalla.setter
   def seguroPantalla(self, seguroPantalla):
      self.__seguroPantalla=seguroPantalla

   def precioVenta(self, porcentaje, seguroPantalla):
      precioSinDescuento = (self.precioBase*porcentaje)/100
      return  precioSinDescuento + seguroPantalla


nuevaTablet=Tablet(200, 1024, "i7", 15)

print(nuevaTablet.precioVenta(20, 15))

"""


"""
Escribir un programa que tenga una clase Documento y dos clases derivadas, Tarjeta de visita y Carta. Crear los métodos 
necesarios para que cada tipo de documento se imprima en pantalla de una forma diferente, según sus características 
propias reescribiendo el método mágico str. Crear un script para hacer una prueba con cada método llamado con objetos 
de las distintas clases. Por ejemplo, el documento solo tiene un pequeño encabezado con los datos de la empresa, la 
tarjeta lleva además, el nombre de la persona y la carta, la fecha.

"""
 
"""
class Documento():

   def __init__ (self, encabezado):
      self.__encabezado=encabezado

   @property
   def encabezado(self):
      return self.__encabezado
   
   @encabezado.setter
   def encabezado(self, encabezado):
      self.__encabezado=encabezado

   def __str__(self):
      print("Empresa: ", self.encabezado)


class TarjetaVisita(Documento):

   def __init__ (self, encabezado, persona):
      self.__encabezado=encabezado
      self.__persona=persona

   @property
   def persona(self):
      return self.__persona
   
   @persona.setter
   def persona(self, persona):
      self.__persona=persona


   def __str__(self):
      print("Empresa: ", self.encabezado, ", persona: ", self.persona)

class Carta(Documento):

   def __init__ (self, encabezado, fecha):
      self.__encabezado=encabezado
      self.__fecha=fecha

   @property
   def fecha(self):
      return self.__fecha
   
   @fecha.setter
   def fecha(self, fecha):
      self.__fecha=fecha


   def __str__(self):
      print("Empresa: ", self.encabezado, ", fecha: ", self.fecha)


nuevaCarta=Carta("Abogados fernandez", 23/12/2018)
print(nuevaCarta)
"""



"""
Los vehículos a motor pagan un determinado impuesto de circulación. La cantidad a pagar depende de la cilindrada, caballos 
y tipo de combustible. Crear un programa para calcular la cantidad que debe pagar un vehículo dependiendo de sus 
características. (Los vehículos a motor pueden ser motocicletas, coches y furgonetas). El impuesto se calcula con una 
cantidad fija por el simple hecho de ser un vehículo con motor, más el 60 % de la potencia en el caso de las motocicletas, 
más una cantidad fija a las furgonetas por ser transporte de mercancías y más el 25 % de la cilindrada para los coches.
La jerarquía de clases no tiene mucho sentido en este ejemplo, pero está puesto para reescribir métodos. Probar todo en 
un script 
"""

"""
class Vehículos():

   def __init__(self, cilindradas, caballos, tipoCombustible):
      self.__cilindradas=cilindradas
      self.__caballos=caballos
      self.__tipoCombustible=tipoCombustible

   @property
   def cilindradas(self):
      return self.__cilindradas
   
   @cilindradas.setter
   def cilindradas(self, cilindradas):
      self.__cilindradas=cilindradas


   @property
   def caballos(self):
      return self.__caballos
   
   @caballos.setter
   def caballos(self, caballos):
      self.__caballos=caballos


   @property
   def tipoCombustible(self):
      return self.__tipoCombustible
   
   @tipoCombustible.setter
   def tipoCombustible(self, tipoCombustible):
      self.__tipoCombustible=tipoCombustible

   
   def impuestoCirculacion(self, precioFijo):
      return precioFijo


class Moto(Vehículos):

   def __init__(self, cilindradas, caballos, tipoCombustible):
      self.__cilindradas=cilindradas
      self.__caballos=caballos
      self.__tipoCombustible=tipoCombustible

   def impuestoCirculacion(self, precioFijo):
      return precioFijo + ((self.caballos*60)/100)


class Furgoneta(Vehículos):

   def __init__(self, cilindradas, caballos, tipoCombustible):
      self.__cilindradas=cilindradas
      self.__caballos=caballos
      self.__tipoCombustible=tipoCombustible

   def impuestoCirculacion(self, precioFijo, fijoMercancias):
      return precioFijo + fijoMercancias


class Coche(Vehículos):

   def __init__(self, cilindradas, caballos, tipoCombustible):
      self.__cilindradas=cilindradas
      self.__caballos=caballos
      self.__tipoCombustible=tipoCombustible

   def impuestoCirculacion(self, precioFijo):
      return precioFijo + ((self.cilindradas*25)/100)


nuevaMoto=Moto(500, 250, 'Gasoil')
nuevaFurgoneta=Furgoneta(200, 175, 'Gasolina')
nuevoCoche=Coche(300, 200, 'Diesel')

print(nuevaMoto.impuestoCirculacion(340))
print(nuevaFurgoneta.impuestoCirculacion(340, 120))
print(nuevoCoche.impuestoCirculacion(340))
"""

