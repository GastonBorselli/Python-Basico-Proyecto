myStr = "estoy contento"

#dir permite saber lo que podemos hacer con cierto tipo de dato
#print(dir(myStr)) #se obtienen propiedades y metodos que podemos
#usar y alterar esos valores

print(myStr.upper()) #todo el texto a mayusculas
print(myStr.lower()) #todo el texto en minusculas
print(myStr.swapcase()) #intercala mayusculas y minusculas
print(myStr.capitalize()) #la primer letra de la primer palabra en mayuscula
print(myStr.replace("contento","triste").upper()) #reemplaza la palabra contento por triste
print(myStr.count("o"))

print(myStr.startswith('e')) #saber si el texto empieza con el valor indicado

print(myStr.split()) #separa el texto basado en el parametro que le pasamos y lo guarda en una lista
print(myStr.find("o")) #devuelve la posicion de la cadena en la que encuentra el parametro que le pasamos

print(len(myStr)) #cantidad de caracteres de la cadena
print(myStr.index("e")) #indice en el que esta el parametro que le pasamos

print(myStr.isnumeric()) #devuelve si la cadena es numerica
print(myStr.isalpha())    #o si es alfanumerico

print(myStr[4])

print("En el dia de hoy " + myStr)
print(f"Mi nombre es {myStr}")  #la f es para que lo que esta entre llaves sea interpretado de algo creado anteriormente
print("Mi estado de animo hoy es {0}".format(myStr))