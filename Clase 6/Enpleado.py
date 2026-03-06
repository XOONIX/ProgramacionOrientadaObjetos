#Vamos a crear una clase padre llamada empleado de la cual se hereden los atributos salariobase horastrabajadas y el metodo calcularsalario, luego se crean dos clases hijas llamada empleadoasalariado y empleadoporhora, cada una con su propio metodo calcularsalario que realiza el calculo correspondiente segun el tipo de empleado. En el main se solicita al usuario ingresar los datos necesarios para cada tipo de empleado, se crean objetos de cada clase y se llama al metodo calcularsalario para mostrar el resultado.
from ast import main


class Empleado:
    def __init__(self, salariobase, horastrabajadas):
        self.salariobase = salariobase
        self.horastrabajadas = horastrabajadas
    def validar(self):
        if not isinstance(self.salariobase, (int, float)) or not isinstance(self.horastrabajadas, (int, float)):
            raise ValueError("El salario base y las horas trabajadas deben ser enteros o flotantes")
    def mostrar_datos(self):
        print(f"Salario base: {self.salariobase}")
        print(f"Horas trabajadas: {self.horastrabajadas}")
    def calcularsalario(self):
        print("Calculo generico de salario")
class EmpleadoAsalariado(Empleado):
    def __init__(self, salariobase, horastrabajadas):
        super().__init__(salariobase, horastrabajadas)
    def calcularsalario(self):
        salario = self.salariobase
        print(f"El salario del empleado asalariado es: {salario:.2f}")
class EmpleadoPorHora(Empleado):
    def __init__(self, salariobase, horastrabajadas):
        super().__init__(salariobase, horastrabajadas)
    def calcularsalario(self):
        salario = self.salariobase * self.horastrabajadas
        print(f"El salario del empleado por hora es: {salario:.2f}")
def empleadoAsalariado():
    print("Empleado Asalariado")
    salariobase = float(input("Ingrese el salario base: "))
    horastrabajadas = float(input("Ingrese las horas trabajadas: "))
    empleado_asalariado = EmpleadoAsalariado(salariobase, horastrabajadas)
    empleado_asalariado.validar()
    empleado_asalariado.mostrar_datos()
    empleado_asalariado.calcularsalario()
def empleadoPorHora():
    print("\nEmpleado por Hora")
    salariobase = float(input("Ingrese el salario por hora: "))
    horastrabajadas = float(input("Ingrese las horas trabajadas: "))
    empleado_por_hora = EmpleadoPorHora(salariobase, horastrabajadas)
    empleado_por_hora.validar()
    empleado_por_hora.mostrar_datos()
    empleado_por_hora.calcularsalario()
    
opcion = input("Cual es su tipo de empleado? (asalariado/porhora): ").lower()
if opcion == "asalariado":    empleadoAsalariado()
elif opcion == "porhora":    empleadoPorHora()
else:    print("Opcion no valida")