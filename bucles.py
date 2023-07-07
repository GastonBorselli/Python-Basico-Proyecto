#permiten hacer una tarea tipic relacionada a una lista de datos

comidas = ['manzana','leche','tomates','queso','uvas']

for comida in comidas:
    if comida == "queso":
    #     print("tienes que comprar esto") puedo colocar validaciones dentro
        #break  se detiene el ciclo
        continue #permite continuar el ciclo sin tener en cuenta el valor asignado
    
    print(comida)

for numero in range(1,8):
    print(numero)
    
for letra in "Hello":   #muestra caracter por caracter
    print(letra)
    
count = 4
#bucle while
while count<=10:
    print(count)
    count+=1
    
