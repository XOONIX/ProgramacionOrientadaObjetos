#Nombre: Johnny Fabian Cardozo Montenegro   
#Proyecto: Personajes con IA
#Entrada: Animación de barras de vida y ataques
#Salida: Información de personajes, animación de ataques y barras de vida descendiendo.
#Proceso: Definición de clases para ninja, dragon y mago con métodos de ataque e información. Animación de barras de vida y ataques.



import time
import sys

# --- FUNCIONES DE ANIMACIÓN ---
def animar_barra(nombre, vida_actual, vida_maxima):
    print(f"{nombre}: ", end="")
    for i in range(vida_actual + 1):
        bloques = "█" * (i // 5) 
        sys.stdout.write(f"\r{nombre.ljust(10)} [{bloques.ljust(20)}] {i} HP")
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def animar_descenso(nombre, vida_origen, vida_destino):
    for i in range(vida_origen, vida_destino - 1, -1):
        bloques = "█" * (i // 5)
        sys.stdout.write(f"\r{nombre.ljust(10)} [{bloques.ljust(20)}] {i} HP")
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# --- CLASES ---
class ninja: 
    def __init__(self, nombre, vidas, poder):
        self.nombre = nombre
        self.__poder = poder 
        self.__vidas = vidas   

    @property 
    def vidas(self): return self.__vidas

    @vidas.setter
    def vidas(self, valor): self.__vidas = max(0, valor)

    def info(self):
        return f"El ninja {self.nombre} tiene un poder de {self.__poder} y {self.vidas} de vida" 

    def atacar(self, objetivo):
        vida_previa = objetivo.vidas
        daño = self.__poder
        objetivo.vidas -= daño
        print("\n" + "⚔️ " * 15)
        animar_descenso(objetivo.nombre, vida_previa, objetivo.vidas)
        print(f"{self.nombre} ataca a {objetivo.nombre} causando {daño} de daño.")
        if objetivo.vidas <= 0: print(f"💀 {objetivo.nombre} derrotado por {self.nombre}.")

class dragon:
    def __init__(self, nombre, tamaño, fuerza, vidas):
        self.nombre = nombre; self.tamaño = tamaño
        self.__fuerza = fuerza; self.__vidas = vidas 

    @property
    def vidas(self): return self.__vidas

    @vidas.setter
    def vidas(self, valor): self.__vidas = max(0, valor)

    def info(self):
        return f"El dragon {self.nombre} tiene tamaño {self.tamaño}, fuerza de {self.__fuerza} y {self.vidas} HP."

    def atacar(self, objetivo):
        vida_previa = objetivo.vidas
        daño = self.__fuerza
        objetivo.vidas -= daño
        print("\n" + "🔥 " * 15)
        animar_descenso(objetivo.nombre, vida_previa, objetivo.vidas)
        print(f"{self.nombre} ataca a {objetivo.nombre} causando {daño} de daño.")
        if objetivo.vidas <= 0: print(f"💀 {objetivo.nombre} derrotado por {self.nombre}.")

class mago:
    def __init__(self, nombre, nivel_magico, mana, vidas):
        self.nombre = nombre; self.__nivel_magico = nivel_magico
        self.__mana = mana; self.__vidas = vidas    

    @property
    def vidas(self): return self.__vidas

    @vidas.setter
    def vidas(self, valor): self.__vidas = max(0, valor)

    def info(self):
        return f"El mago {self.nombre} nivel {self.__nivel_magico} con {self.__mana} de mana y {self.vidas} HP."

    def atacar(self, objetivo):
        vida_previa = objetivo.vidas
        daño = self.__nivel_magico
        objetivo.vidas -= daño
        print("\n" + "⚡ " * 15)
        animar_descenso(objetivo.nombre, vida_previa, objetivo.vidas)
        print(f"{self.nombre} ataca a {objetivo.nombre} causando {daño} de daño.")
        if objetivo.vidas <= 0: print(f"💀 {objetivo.nombre} derrotado por {self.nombre}.")

# --- LÓGICA PRINCIPAL ---
personaje1 = ninja("Carlos", 60, 30)
personaje2 = dragon("Wallas", "Grande", 20, 100)
personaje3 = mago("Merlin", 20, 90, 50)

print("--- CARGANDO PERSONAJES ---")
animar_barra(personaje1.nombre, personaje1.vidas, 60)
animar_barra(personaje2.nombre, personaje2.vidas, 100)
animar_barra(personaje3.nombre, personaje3.vidas, 50)

print("\nElija un personaje a usar (1. Ninja, 2. Dragon, 3. Mago): ")
op = int(input())
atacante = [personaje1, personaje2, personaje3][op-1] if op in [1,2,3] else None

print("\n¿A quién desea atacar? (1. Ninja, 2. Dragon, 3. Mago): ")
op_a = int(input())
objetivo = [personaje1, personaje2, personaje3][op_a-1] if op_a in [1,2,3] else None

if atacante and objetivo:
    while objetivo.vidas > 0:
        atacante.atacar(objetivo)
        if objetivo.vidas <= 0: break
        if input("\n¿Atacar de nuevo? (si/no): ").lower() != "si": break
    
    if objetivo.vidas <= 0:
        print("\n" + "☠️ " * 10 + "\n      G A M E  O V E R\n" + "☠️ " * 10)
else:
    print("Opciones inválidas.")
