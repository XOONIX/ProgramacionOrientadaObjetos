#El sena quiere automartizar su sistema de Muebles y les solicita la creacion de un S.I
#Que pueda administrar los 7 atributos 

#Se quiere modificar, color, propietario, ubicacion [setter]
#Mostrar informacion antes, durante y despues de la modificacion [getter]

class Mueble:
    def __init__(self, color, propietario, ubicacion, material, tipo, tamaño, estado):
        self.__color = color
        self.__propietario = propietario
        self.__ubicacion = ubicacion
        self.__material = material
        self.__tipo = tipo
        self.__tamaño = tamaño
        self.__estado = estado
        
    # Estos métodos permiten cambiar los atributos privados desde afuera
    def set_color(self, nuevo_color):
        self.__color = nuevo_color

    def set_propietario(self, nuevo_propietario):
        self.__propietario = nuevo_propietario

    def set_ubicacion(self, nueva_ubicacion):
        self.__ubicacion = nueva_ubicacion

    def mostrar_informacion(self):
        print("------------------------------------------")
        print(f"Color: {self.__color}")
        print(f"Propietario: {self.__propietario}")
        print(f"Ubicación: {self.__ubicacion}")
        print(f"Material: {self.__material}")
        print(f"Tipo: {self.__tipo}")
        print(f"Tamaño: {self.__tamaño}")
        print(f"Estado: {self.__estado}")
        print("------------------------------------------")
        
          
    
#Creacion de objeto
mueble1 = Mueble("Cafe", "SENA", "Sala de reuniones", "Madera", "Mesa", "Grande", "Nuevo")
mueble2 = Mueble("Negro", "SENA", "Oficina administrativa", "Metal", "Silla", "Mediano", "Usado")
mueble3 = Mueble("Blanco", "SENA", "Biblioteca", "Plástico", "Estantería", "Pequeño", "Nuevo")  

mueble= int(input("Actualmente existen tres objetos, ¿Cual deseas consultar?(1/2/3): "))
if mueble == 1: 
    mueble1.mostrar_informacion()
    mueble = mueble1
elif mueble == 2:
    mueble2.mostrar_informacion()
    mueble = mueble2
elif mueble == 3:
    mueble3.mostrar_informacion()
    mueble = mueble3
else:
    print("Mueble no reconocido")


#Cambio de atributos utilizando setter

respuesta= input("Quieres modificar el color, propietario y ubicacion del mueble? responde con si/no: ").lower()
if respuesta == "si":
    ncolor = input("Ingrese el nuevo color del mueble: ")
    npropietario = input("Ingrese el nuevo propietario del mueble: ")
    nubicacion = input("Ingrese la nueva ubicación del mueble: ")
    print("Información actualizada del mueble: ")
    
    mueble.set_color(ncolor)
    mueble.set_propietario(npropietario)
    mueble.set_ubicacion(nubicacion)
    
    mueble.mostrar_informacion()
else:
    print("Gracias por participar")

