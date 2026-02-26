class libro: 
    def __init__(self, titulo, autor, editorial, año_publicacion): 
        self.__titulo = titulo 
        self.__autor = autor 
        self.__editorial = editorial 
        self.__año_publicacion = año_publicacion 
        
    #Creacion de decoradores 
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def editorial(self):
        return self.__editorial
    
    @property
    def año_publicacion(self):
        return self.__año_publicacion
    def mostrar_informacion(self):
        print("------------------------------------------")
        print(f"Titulo: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Editorial: {self.__editorial}")
        print(f"Año de publicación: {self.__año_publicacion}")
        print("------------------------------------------")
#Creacion de objeto
libro1 = libro("Cien años de soledad", "Gabriel García Márquez", "Editorial Sudamericana", 1967)
libro1.mostrar_informacion()