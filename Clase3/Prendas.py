class prenda:
    def __init__(self, nombre, precio, stock, color, ubicacion):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__color = color
        self.__ubicacion = ubicacion

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def get_precio(self):
        return self.__precio  
    def set_precio(self, precio):
        self.__precio = precio
    def get_stock(self):
        return self.__stock
    def set_stock(self, stock):
        self.__stock = stock
    def get_color(self):        
        return self.__color
    def set_color(self, color):
        self.__color = color
    def get_ubicacion(self):
        return self.__ubicacion
    def set_ubicacion(self, ubicacion):
        self.__ubicacion = ubicacion
#objetos
prenda1 = prenda("camisa", 20, 10, "rojo", "estante1")
prenda2 = prenda("pantalon", 30, 5, "azul", "estante2")
prenda3 = prenda("falda", 25, 8, "verde", "estante3")
print(f"Prenda: {prenda1.get_nombre()}, Precio: ${prenda1.get_precio()}, Stock: {prenda1.get_stock()} unidades, Color: {prenda1.get_color()}, Ubicación: {prenda1.get_ubicacion()}")
print(f"Prenda: {prenda2.get_nombre()}, Precio: ${prenda2.get_precio()}, Stock: {prenda2.get_stock()} unidades, Color: {prenda2.get_color()}, Ubicación: {prenda2.get_ubicacion()}")
print(f"Prenda: {prenda3.get_nombre()}, Precio: ${prenda3.get_precio()}, Stock: {prenda3.get_stock()} unidades, Color: {prenda3.get_color()}, Ubicación: {prenda3.get_ubicacion()}")

pregunta= input("¿Desea actualizar el stock de alguna prenda? (si/no): ")
if pregunta.lower() == "si":
    prenda_nombre = input("Ingrese el nombre de la prenda a actualizar: ")
    nuevo_stock = int(input("Ingrese el nuevo stock: "))
    if prenda_nombre == prenda1.get_nombre():
        prenda1.set_stock(nuevo_stock)
        print(f"Stock actualizado para {prenda1.get_nombre()}: {prenda1.get_stock()} unidades.")
    elif prenda_nombre == prenda2.get_nombre():
        prenda2.set_stock(nuevo_stock)
        print(f"Stock actualizado para {prenda2.get_nombre()}: {prenda2.get_stock()} unidades.")
    elif prenda_nombre == prenda3.get_nombre():
        prenda3.set_stock(nuevo_stock)
        print(f"Stock actualizado para {prenda3.get_nombre()}: {prenda3.get_stock()} unidades.")
    else:
        print("Prenda no encontrada.")
pregunta_precio = input("¿Desea actualizar el precio de alguna prenda? (si/no): ")
if pregunta_precio.lower() == "si":
    prenda_nombre_precio = input("Ingrese el nombre de la prenda a actualizar el precio: ")
    nuevo_precio = float(input("Ingrese el nuevo precio: "))
    if prenda_nombre_precio == prenda1.get_nombre():
        prenda1.set_precio(nuevo_precio)
        print(f"Precio actualizado para {prenda1.get_nombre()}: ${prenda1.get_precio()}.")
    elif prenda_nombre_precio == prenda2.get_nombre():
        prenda2.set_precio(nuevo_precio)
        print(f"Precio actualizado para {prenda2.get_nombre()}: ${prenda2.get_precio()}.")
    elif prenda_nombre_precio == prenda3.get_nombre():
        prenda3.set_precio(nuevo_precio)
        print(f"Precio actualizado para {prenda3.get_nombre()}: ${prenda3.get_precio()}.")
    else:
        print("Prenda no encontrada.")
