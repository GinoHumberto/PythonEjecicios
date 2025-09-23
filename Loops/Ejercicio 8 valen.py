# Transponer una matriz cuadrada de orden n sin usar una matriz 
# intermedia (las operaciones deben realizarse sobre la misma 
# matriz con variables temporales)

# i = fila
# j = columna 

numeros = [[1,2,3],[4,5,6], [7,8,9]]

#Matriz normal
for i in (numeros):
    for j in (i):
        print(j, end = '')
    print()
print()
#Matriz transpuesta 
iterador = 0
while len(numeros) != iterador:
    for i in (numeros):
        print(i[iterador], end = '')
    iterador += 1
    print()