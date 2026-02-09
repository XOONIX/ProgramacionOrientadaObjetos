class aprendiz:
    def __init__(self, nombre, edad, peso, estatura):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
        self.__estatura = estatura
    # Métodos get y set para acceder a los atributos privados
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_peso(self):
        return self.__peso

    def get_estatura(self):
        return self.__estatura
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        if not nombre:
            print("El nombre no puede estar vacío.")
        raise ValueError("El nombre no puede ser un numero")

    def set_edad(self, edad):
        self.__edad = edad
        if edad < 0:
            print("La edad no puede ser negativa o cero.")
        raise ValueError("La edad no puede ser un numero negativo")
    def set_peso(self, peso):
        self.__peso = peso  
        if peso < 0:
            print("El peso no puede ser negativo o cero.")
        raise ValueError("El peso no puede ser un numero negativo")

    def set_estatura(self, estatura):
        self.__estatura = estatura
        if estatura < 0:
            print("La estatura no puede ser negativa o cero.")
        raise ValueError("La estatura no puede ser un numero negativo")
        
    def info(self):
        return f"Aprendiz: {self.__nombre}, Edad: {self.__edad} años, Peso: {self.__peso} kg, Estatura: {self.__estatura} cm."
    # Creación de un objeto aprendiz
aprendiz1 = input("Ingrese el nombre del aprendiz: ")
edad1 = input("Ingrese la edad del aprendiz: ")   
peso1 = input("Ingrese el peso del aprendiz en kg: ")
estatura1 = input("Ingrese la estatura del aprendiz en cm: ")
aprendiz_objeto = aprendiz(aprendiz1, edad1, peso1, estatura1)
print(aprendiz_objeto.info())
