#permite definir un dato a partir de claves y valores

producto = {
    "nombre":"libro",
    "cantidad": 3,
    "precio": 200
}

persona = {
    "primerNombre":"Gaston",
    "apellido":"Borselli"
}

print(type(producto))
#print(dir(producto)) para ver las propiedades del diccionario

print(persona.keys()) #para obtener las claves del diccionario
print(persona.items()) #para obtener los elementos que tiene dentro el diccionario

print(persona)
