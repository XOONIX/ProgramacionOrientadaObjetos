#Nombre: Johnny Fabian Cardozo Montenegro 
#Proyecto: Personajes
#Entrada: Eleccion de personaje para atacar y personaje a atacar
#Salida: Muestra la informacion de los personajes, el resultado del ataque y la vida restante del personaje atacado
#Proceso: Crear clases para diferentes tipos de personajes con sus atributos y metodos, crear objetos, mostrar la informacion de los personajes, permitir la eleccion de un personaje para atacar y un personaje a atacar, calcular el daño y mostrar la vida restante del personaje atacado.

#Creacion de las clases 
class ninja: 
    def __init__(self, nombre, vidas, poder ): #Definicion de los atributos de la clase
        self.nombre = nombre
        self.__poder = poder 
        self.__vidas = vidas   
     #Decoradores para poder usar los metodos de ataque desde fuera de la clase
    @property 
    def vidas(self):
        return self.__vidas
    @vidas.setter
    #---------------------------------------------------------------------------   
    def vidas(self, vidas):
        self.__vidas = vidas 
    
    def info(self): #Definicion del metodo para mostrar la informacion del ninja
        return f"El ninja {self.nombre} tiene un poder de {self.__poder} y {self.vidas} de vida" 
    def atacar(self, objetivo):
        daño = self.__poder # El ninja usa su poder
        objetivo.vidas -= daño
        if objetivo.vidas < 0: # Evita que la vida del objetivo sea negativa
            objetivo.vidas = 0
        print("="*30)
        print(f"{self.nombre} ataca a {objetivo.nombre} causando {daño} de daño.")
        print(f"Vida restante de {objetivo.nombre}: {objetivo.vidas}")
        if objetivo.vidas <= 0:
            print(f"{objetivo.nombre} ha sido derrotado por {self.nombre}.")

class dragon:
    def __init__(self, nombre, tamaño, fuerza, vidas):
        self.nombre=nombre  
        self.tamaño=tamaño
        self.__fuerza=fuerza
        self.__vidas= vidas 
     #Decoradores para poder usar los metodos de ataque desde fuera de la clase
    @property
    def vidas(self):
        return self.__vidas
    @vidas.setter
    #---------------------------------------------------------------------------
    def vidas(self, vidas):
        self.__vidas = vidas
    def info(self):
        return f"El dragon {self.nombre} tiene un tamaño {self.tamaño}, una fuerza de {self.__fuerza} y {self.vidas} de vida."
    def atacar(self, objetivo):
        daño = self.__fuerza # El dragon usa su fuerza
        objetivo.vidas -= daño
        if objetivo.vidas < 0: # Evita que la vida del objetivo sea negativa
            objetivo.vidas = 0
        print("="*30)
        print(f"{self.nombre} ataca a {objetivo.nombre} causando {daño} de daño.")
        print(f"Vida restante de {objetivo.nombre}: {objetivo.vidas}")
        if objetivo.vidas <= 0:
            print(f"{objetivo.nombre} ha sido derrotado por {self.nombre}.")

class mago:
    def __init__(self, nombre, nivel_magico, mana, vidas):
        self.nombre=nombre
        self.__nivel_magico=nivel_magico
        self.__mana=mana
        self.__vidas=vidas    
    #Decoradores para poder usar los metodos de ataque desde fuera de la clase
    @property
    def vidas(self):
        return self.__vidas
    @vidas.setter
    #---------------------------------------------------------------------------
    def vidas(self, vidas):
        self.__vidas = vidas
    def info(self):
        return f"El mago {self.nombre} tiene un nivel mágico de {self.__nivel_magico} un mana de {self.__mana} y {self.vidas} de vida."
    def atacar(self, objetivo):
        daño = self.__nivel_magico # El mago usa su nivel mágico
        objetivo.vidas -= daño
        if objetivo.vidas < 0: # Evita que la vida del objetivo sea negativa
            objetivo.vidas = 0
        print("="*30)
        print(f"{self.nombre} ataca a {objetivo.nombre} causando {daño} de daño.")
        print(f"Vida restante de {objetivo.nombre}: {objetivo.vidas}")
        if objetivo.vidas <= 0:
            print(f"{objetivo.nombre} ha sido derrotado por {self.nombre}.")    
            
#__________________________________________________________________________________________________________________________________-
#La IA fue usada para crear una animacion de barra de vida para cada personaje al cargar el programa, mostrando el nombre del personaje, su barra de vida y la cantidad de vida actual. La animacion se realiza con un bucle que incrementa la vida actual del personaje y actualiza la barra visual en la consola.
import time
import sys

def animar_barra(nombre, vida_actual, vida_maxima):
    print(f"{nombre}: ", end="")
    for i in range(vida_actual + 1):
        # Calculamos el porcentaje para la barra visual (ej. 20 bloques max)
        bloques = "█" * (i // 5) 
        # \r vuelve al inicio de la línea, end="" evita el salto de línea
        sys.stdout.write(f"\r{nombre.ljust(10)} [{bloques.ljust(20)}] {i} HP")
        sys.stdout.flush()
        time.sleep(0.02) # Velocidad de la animación
    print() # Salto de línea final
    
    
#_____________________________________________________________________________________________________________________________________

#Creacion de objetos
personaje1 = ninja("Carlos", 30, 60)
#print(personaje1.info())

personaje2 = dragon("Wallas", "Grande", 20, 100)
#print(personaje2.info())    

personaje3 = mago("Merlin", 20, 90, 50)
#print(personaje3.info())    
#_________________________________________Fragmento con la animacion de carga de personajes____________________________________
print("--- CARGANDO PERSONAJES ---")
animar_barra(personaje1.nombre, personaje1.vidas, 60)
animar_barra(personaje2.nombre, personaje2.vidas, 100)
animar_barra(personaje3.nombre, personaje3.vidas, 50)

#Eleccion de personaje para atacar

print("\n Elija un personaje a usar:")
print("1. Ninja Carlos")
print("2. Dragon Wallas")
print("3. Mago Merlin \n")

opcion = int(input("Ingrese el número del personaje que desea usar: "))

if opcion == 1:
    print("Has elegido: ", personaje1.info())
    atacante = personaje1
elif opcion == 2:
    print("Has elegido: ", personaje2.info())
    atacante = personaje2
elif opcion == 3:
    print("Has elegido: ", personaje3.info())
    atacante = personaje3
else:
    print("Opción inválida")
    
#Pregunta de ataque
print("\n" + "+"*30)
print("\n ¿Que personaje desea atacar?")
print("1. Ninja Carlos")
print("2. Dragon Wallas")
print("3. Mago Merlin \n")

opcion_ataque = int(input("Ingrese el número del personaje que desea atacar: "))

if opcion_ataque == 1:
    objetivo = personaje1
    print("\n" + "*"*30)
    print(f"Has elegido atacar a: {objetivo.nombre}")
elif opcion_ataque == 2:
    objetivo = personaje2
    print("\n" + "*"*30)
    print(f"Has elegido atacar a: {objetivo.nombre}")
elif opcion_ataque == 3:
    objetivo = personaje3
    print("\n" + "*"*30)
    print(f"Has elegido atacar a: {objetivo.nombre}")
else:
    print("Opción inválida")
    
#Calculo del daño
       
if 'atacante' in locals() and 'objetivo' in locals():
    print("\n" + "="*30)
    atacante.atacar(objetivo)
    print("/"*objetivo.vidas) # Muestra la vida restante del objetivo con barras
    print("="*30)
    while objetivo.vidas > 0:
        print(f"{objetivo.nombre} aún tiene {objetivo.vidas} de vida.")
        pregunta: str = input("¿Desea atacar nuevamente? (si/no): ")
        if pregunta.lower() == "si":
            atacante.atacar(objetivo)
            print("/"*objetivo.vidas) # Muestra la vida restante del objetivo con barras
        else:
            print("Fin del combate.")
        if pregunta.lower() != "si":
            print("Fin del combate.")
            break
    if objetivo.vidas <= 0:
        print("X.X") # Muestra una cara de derrota
        print("="*30)
else:
    print("No se pudo realizar el ataque debido a una opción inválida.")