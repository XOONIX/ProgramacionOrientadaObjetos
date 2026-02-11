#Johnny Fabian Cardozo Montenegro
#Encapsulamiento con property 
class prenda:
    def __init__(self, color, talla, stock, precio):
        self.color = color
        self._talla = talla
        self.__stock = stock
        self.__precio= precio
    #Encapsulamiento con property
    @property
    def talla(self):
        return self._talla
    
    @property
    def stock(self):
        return self.__stock

    @property
    def precio(self):
        return self.__precio

    @talla.setter
    def talla(self, nueva_talla):
        self._talla = nueva_talla

    @stock.setter
    def stock (self, nuevo_stock):
        self.__stock = nuevo_stock

    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio
        
prenda1 = prenda("rojo", "M", 10, 50)
print(prenda1.talla) #Accedemos a la propiedad talla utilizando el método getter
print(prenda1.stock) #Accedemos a la propiedad stock utilizando el método getter
print(prenda1.precio) #Accedemos a la propiedad precio utilizando el método getter

print (f"La tienda cuenta con {prenda1.stock} unidades de la prenda") #Accedemos a la propiedad stock utilizando el método getter

tipoUsu = str(input("Eres un usuario o un administrador? responde escribiendo usu/admin: "))
tipoUsu = tipoUsu.lower()
if tipoUsu == "admin":
    nueva_talla = str(input("Ingrese la nueva talla de la prenda: "))
    prenda1.talla = nueva_talla #Modificamos la propiedad talla utilizando el método setter
    nuevo_stock = int(input("Ingrese el nuevo stock de la prenda: "))
    prenda1.stock = nuevo_stock #Modificamos la propiedad stock utilizando el método setter
    nuevo_precio = float(input("Ingrese el nuevo precio de la prenda: "))
    prenda1.precio = nuevo_precio #Modificamos la propiedad precio utilizando el método setter
    print(f"Los datos de la prenda han sido actualizados: Talla: {prenda1.talla}, Stock: {prenda1.stock}, Precio: {prenda1.precio}")
else:
    print("Gracias por su visita señor usuario, la tienda te ofrece:")
    print(f"Talla: {prenda1.talla}, Stock: {prenda1.stock}, Precio: {prenda1.precio}")