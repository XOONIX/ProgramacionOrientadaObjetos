#Super
class Operaciomatematica:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        print("Inicizando operacion")

    def calcular(self):
        print("Operacion generica \n")
    
    def validar(self):
        if not isinstance(self.numero1, (int, float)) or not isinstance(self.numero2, (int, float)):
            raise ValueError("Los numeros deben ser enteros o flotantes")

class Suma(Operaciomatematica):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2) #Llamada al constructor de la clase padre
        print("Preparando para sumar")
    def calcular(self):
        super().calcular() #Llamada al metodo calcular de la clase padre
        resultado = self.numero1 + self.numero2
        print(f"El resultado de la suma es: {resultado:.0f}")
#RESTA
class Resta(Operaciomatematica):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2) #Llamada al constructor de la clase padre
        print("Preparando para restar")
    def calcular(self):
        resultado = self.numero1 - self.numero2
        super().calcular() #Llamada al metodo calcular de la clase padre
        resultado = self.numero1 - self.numero2
        print(f"El resultado de la resta es: {resultado:.0f}")
#MULTIPLICACION
class Multiplicacion(Operaciomatematica):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2) #Llamada al constructor de la clase padre
        print("Preparando para multiplicar")
    def calcular(self):
        resultado = self.numero1 * self.numero2
        super().calcular() #Llamada al metodo calcular de la clase padre
        resultado = self.numero1 * self.numero2
        print(f"El resultado de la multiplicacion es: {resultado:.0f}")
#DIVISION
class Division(Operaciomatematica):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2) #Llamada al constructor de la clase padre
        print("Preparando para dividir")
    def calcular(self):
        if self.numero1 == 0 or self.numero2 == 0:
            print("Error: No se puede dividir por cero")
        else:
            resultado = self.numero1 / self.numero2
            super().calcular() #Llamada al metodo calcular de la clase padre
            resultado = self.numero1 / self.numero2
            print(f"El resultado de la division es: {resultado:.0f}")
def main():
    numero1 = float(input("Ingrese el primer numero: "))
    numero2 = float(input("Ingrese el segundo numero: "))
    suma = Suma(numero1, numero2)
    suma.calcular()
    resta = Resta(numero1, numero2)
    resta.calcular()
    multiplicacion = Multiplicacion(numero1, numero2)
    multiplicacion.calcular()
    division = Division(numero1, numero2)
    division.calcular()
if __name__ == "__main__":
    main()