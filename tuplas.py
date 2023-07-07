#las tuplas permiten definir datos iguales a las listas pero que
#no se pueden cambiar. son mas rapidas que las listas
#son usadas en aplicaciones que se quiere tener mas seguro el codigo

#definir una tupla
x = (1,2,3)  #si colocamos un solo elemento no lo considera como tupla, se debe colocar una ,
print(x)

y = tuple((4,5,6))
print(y)

#print(dir(x)) para ver las funciones que se pueden hacer con tuplas

#diccionario que contiene una tupla de latitud y frecuencia
localizaciones = {
    (35.1234,39.0000):"Tokyo",
    (35.1244, 40.0000): "New York"
}
