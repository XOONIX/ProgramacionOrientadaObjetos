#Nombre: Johnny Fabian Cardozo Montenegro 
#Proyecto: Biblioteca de libros
#Entrada: Nombre del libro a buscar
#Salida: Muentra informacion del libro buscado
#Proceso: Crear una clase libro con sus atributos y metodos, crear objetos, almacenarlos en una lista y un diccionario, mostrar la informacion de los libros y permitir la busqueda por nombre.

class Libro:
  def  __init__(self, Editorial, Autor, Edad, NombreLibro, FechaPublicacion, precio, Disponiblidad):
    self.Editorial = Editorial
    self.Autor = Autor
    self.Edad = Edad
    self.NombreLibro = NombreLibro
    self.FechaPublicacion = FechaPublicacion
    self.precio = precio
    self.Disponiblidad = Disponiblidad
  def info(self):
    estado = "disponible" if self.Disponiblidad else "prestado"
    return f"El libro '{self.NombreLibro}' de {self.Autor}, publicado por {self.Editorial} en {self.FechaPublicacion}, cuesta {self.precio} y está {estado}."
    # Creacion de objetos 
libro1 = Libro("Penguin Random House", "Gabriel Garcia Marquez", 36, "Cien Años de Soledad", 1967, 20.5, True)
libro2 = Libro("HarperCollins", "J.K. Rowling", 30, "Harry Potter y la Piedra Filosofal", 1997, 15.0, True)
libro3 = Libro("Simon & Schuster", "Stephen King", 26, "El Resplandor", 1977, 18.0, False)
libro4 = Libro("Macmillan Publishers", "George Orwell", 46, "1984", 1949, 12.0, True)
libro5 = Libro("Hachette Livre", "J.R.R. Tolkien", 45, "El Señor de los Anillos", 1954, 25.0, False)
libro6 = Libro("Scholastic", "Suzanne Collins", 34, "Los Juegos del Hambre", 2008, 14.0, True)

    #Creacion de una lista de libros
libros = [libro1, libro2, libro3, libro4, libro5, libro6]
    #Diccionario de libros
biblioteca = {}
biblioteca[libro1.NombreLibro] = libro1
biblioteca[libro2.NombreLibro] = libro2
biblioteca[libro3.NombreLibro] = libro3
biblioteca[libro4.NombreLibro] = libro4
biblioteca[libro5.NombreLibro] = libro5
biblioteca[libro6.NombreLibro] = libro6

for nombre, libro in biblioteca.items():
    print(libro.info())
    
    #Sistema de busqueda de libros
    
busqueda=input("Ingrese el nombre del libro que desea buscar: ")
if busqueda in biblioteca:
    libro = biblioteca[busqueda]
    print(libro.info())
else:
    print("El libro no se encuentra en la biblioteca.")


    


  