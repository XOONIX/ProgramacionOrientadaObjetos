#Calculadorea basica 
class operacion:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def calcular(self):
        print("Operaciones Genericas")
#Suma y resta heredan de operacion, cada una tiene su propio metodo calcular que realiza la operacion correspondiente y muestra el resultado. En el main se solicita al usuario ingresar dos numeros, se crean objetos de suma y resta con esos numeros y se llama al metodo calcular para mostrar los resultados.
class suma(operacion):
    def calcular(self):
        resultado = self.num1 + self.num2
        print(f"La suma es: {resultado:.0f}")
        print("-----------Fin de la suma-----------")
#Resta hereda de operacion, cada una tiene su propio metodo calcular que realiza la operacion correspondiente y muestra el resultado. En el main se solicita al usuario ingresar dos numeros, se crean objetos de suma y resta con esos numeros y se llama al metodo calcular para mostrar los resultados.
class resta(operacion):
    def calcular(self):
        resultado = self.num1 - self.num2
        print(f"La resta es: {resultado:.0f}\n")
        print("-----------Fin de la resta-----------\n")
class multiplicacion(operacion):
    def calcular (self):
        if self.num1 == 0 or self.num2 == 0:
            print("La multiplicacion es: 0\n")
        else:
            resultado = self.num1 * self.num2
            print(f"La multiplicacion es: {resultado:.0f}\n")
            print("-----------Fin de la multiplicacion-----------\n")
class division(operacion):
    def calcular (self):
        if self.num2 == 0:
            print("Error: No se puede dividir por cero.\n")
        else:
            resultado = self.num1 / self.num2
            print(f"La division es: {resultado}\n")
        print("-----------Fin de la division-----------\n")
class divisionEntera(operacion):
    def calcular (self):
        if self.num2 == 0:
            print("Error: No se puede dividir por cero.\n")
        else:
            resultado = self.num1 // self.num2
            print(f"La division entera  es: {resultado}\n")
        print("-----------Fin de la division entera-----------\n")
class potencia(operacion):
    def calcular(self):
        if self.num2 >= 4:
            print("Valor extremadamente elevado, elija un valor menor\n")
        else:
            resultado= self.num1 ** self.num2
            print(f"La potencia  es: {resultado}\n")
            print("-----------Fin de la potencia -----------\n")
def main():
    numero1 =float(input("- Ingrese el primer número: "))
    numero2 =float(input("- Ingrese el segundo número: "))
    objeto1=suma(numero1, numero2)
    objeto1.calcular()
    objeto2 =resta(numero1, numero2)
    objeto2.calcular()
    objeto3=multiplicacion(numero1, numero2)
    objeto3.calcular()
    objeto4=division(numero1, numero2)
    objeto4.calcular()
    objeto5=divisionEntera(numero1, numero2)
    objeto5.calcular()
    objeto6=potencia(numero1,numero2)
    objeto6.calcular()
if __name__ == "__main__":
    main()