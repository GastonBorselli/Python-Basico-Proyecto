listaPrueba = [1, "hola", 1.31, True, [1,2,3]]
colores = ["rojo", "azul", "verde"]

numerosLista = list((1,2,3)) #lista con tupla
print(numerosLista)

r = list(range(1,10))   #rango de la lista
print(r)

print(len(listaPrueba))
print(colores[1])

print("verde" in colores) #para ver si verde esta dentro de la lista colores
print("amarillo" in colores)

print(colores)
colores[1] = "amarillo"   #cambiar el valor 1 de la lista por amarillo
print(colores)

colores.append("violeta")   #agrega un solo elemento
colores.extend(("violeta", "anarajado")) #si le paso una tupla lo agrega a la lista como un elemento individual
colores.extend(("rosado", "negro"))
colores.insert(2,"celeste")     #inserta un elemento en el indice indicado
colores.insert(len(colores),"gris") #inserta un elemento al final de la lista
print(colores)

#colores.pop()   #quita el ultimo elemento de la lista
colores.pop(1) #quita el elemento ubicado en el indice pasado por parametro
#colores.remove("verde") #elimina el elemento indicado en el parametro

#colores.clear() #deja la lista vacia

#ordenar los colores alfabeticamente
colores.sort()

#ordenar los colores inversamente
colores.sort(reverse=True)
print(colores)

print(colores.index("verde")) #obtiene los indices del elemento
print(colores.count("violeta"))





