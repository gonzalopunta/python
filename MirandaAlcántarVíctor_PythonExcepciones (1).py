print("Ejercicio1")
try:
    resultado = 10/0
except ZeroDivisionError:
    print("No se puede dividir entre 0\n")

#########

print("Ejercicio2")
lista = [1, 2, 3, 4, 5]
try:
    lista[10]
except IndexError as ErrorLista:
    print("No se puede introducir un valor que no está en la lista\n")

#####

print("Ejercicio3")
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
try:
    colores['blanco']
except KeyError as ErrorNombre:
    print("No se puede introducir un valor que no está en la lista\n")

###

print("Ejercicio4")
try:
    resultado = 15 + "20"
except TypeError as ErrorTipo:
    print("No se puede introducir distinto tipos de datos en una misma variable\n")

####

print("Ejercicio5")
elementos = [1, 5, -2]
def agregar_una_vez(lista, el):

    try:
        if el in lista:
            raise ValueError
        else:   
            lista.append(el)
    except ValueError as ErrorValor:
        print("Error: Imposible añadir elementos duplicados =>",el)

agregar_una_vez(elementos, 10)
agregar_una_vez(elementos, -2)
agregar_una_vez(elementos,"Hola")
print(elementos)