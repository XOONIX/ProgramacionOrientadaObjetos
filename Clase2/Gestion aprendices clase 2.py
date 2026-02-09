#Nombre: Johnny Fabian Cardozo Montenegro
#Proyecto: Gestion aprendices
#Entrada: Documento del aprendiz a buscar
#Salida: Muestra informacion del aprendiz buscado
#Proceso: Crear una clase aprendiz con sus atributos y metodos, crear objetos, almacenarlos en una lista y un diccionario, mostrar la informacion de los aprendices y permitir la busqueda por documento.
class aprendiz:
    def __init__(self, edad, nombres, peso, estatura, genero, documento):
        self.edad = edad
        self.nombres = nombres
        self.peso = peso
        self.estatura = estatura
        self.genero = genero
        self.documento = documento
        
    def info(self):
        print (f"El aprendiz {self.nombres} con documento {self.documento}, de genero {self.genero}, tiene {self.edad} años, pesa {self.peso} kg y mide {self.estatura} m.")
        
    #Creacion de objetos
aprendiz1 = aprendiz(20, "Juan Perez", 70, 1.75, "Masculino", "12345678")
aprendiz2 = aprendiz(22, "Maria Gomez", 60, 1.65, "Femenino", "87654321")
aprendiz3 = aprendiz(19, "Carlos Rodriguez", 80, 1.80, "Masculino", "11223344")
aprendiz4 = aprendiz(21, "Ana Martinez", 55, 1.60, "Femenino", "44332211")
aprendiz5 = aprendiz(23, "Luis Hernandez", 90, 1.85, "Masculino", "55667788")
aprendiz6 = aprendiz(18, "Sofia Lopez", 50, 1.55, "Femenino", "88776655")
    #Creacion de una lista de aprendices
aprendices = [aprendiz1, aprendiz2, aprendiz3, aprendiz4, aprendiz5, aprendiz6]
    #Diccionario de aprendices
gestion_aprendices = {}
gestion_aprendices[aprendiz1.documento] = aprendiz1           
gestion_aprendices[aprendiz2.documento] = aprendiz2
gestion_aprendices[aprendiz3.documento] = aprendiz3
gestion_aprendices[aprendiz4.documento] = aprendiz4
gestion_aprendices[aprendiz5.documento] = aprendiz5
gestion_aprendices[aprendiz6.documento] = aprendiz6

for documento, aprendiz in gestion_aprendices.items():
    aprendiz.info()   
    #Sistema de busqueda de aprendices
busqueda = input("Ingrese el documento del aprendiz que desea buscar: ")
if busqueda in gestion_aprendices:
    aprendiz = gestion_aprendices[busqueda]
    print("Aprendiz encontrado:")
    aprendiz.info()
else:
    print("El aprendiz no se encuentra en la gestión.")