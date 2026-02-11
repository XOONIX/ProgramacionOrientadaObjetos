#Indexing es cuando retiramos un unico caracter de una cadena de caracteres
cadena = "Hola mundo"
print(cadena[0]) #Necesitamos [] y el valor numerico del caracter que queremos retirar

print(cadena[6])

#slicing es cuando retiramos un rango de caracteres
cadena = "Hola mundoo que tal"
print(cadena[0:5]) #Necesitamos ":" dentro de [] aqui podremos elegir el valor inicial y el valor final
print(cadena[:5])#Si no ponemos nada antes de los puntos python lo interpreta como si fuese 0 
print(cadena[5:])#Si no ponemos nada al final, python interpreta que va hasta el ultimo caracter

#Slicing con caracteres intermedios 
telefono= "2-3-4-6-7-8-10"
print (telefono[0:8:2]) #Si agregamos unos ":" adicionales podemos elegir cada cuando queremos que salten los elementos 
print(telefono[::3])

#Slicing negativo
frase= "Hola esta es una frase de prueba."
print (frase[-6:-1]) #Al agregar un "-" en los numeros, la frase se va tomara en sentido contrario o invertido.

frase= "Hola esta es una frase de prueba."
print (frase[::-2]) #Para hacer saltos inversos invirtiendo la frase solo se le agrega "-"
 