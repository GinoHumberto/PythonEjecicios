# Crear un algoritmo que dibuje una escalera de números, donde cada línea de números comience en
# uno y termine en el número de la línea. Solicitar la altura de la escalera al usuario al comenzar el
# programa. Ejemplo: Si se ingresa que la altura de la escalera es igual a 3, se debe mostrar por pantalla:
# 1
# 12
# 123

#input: altura de la escalera
#output: escalera de numero

altura = int(input('Ingresa la altura de la escalera de numeros que quieres hacer: '))
while altura <= 0:
    altura = int(input('Ingresa la altura de la escalera de numeros que quieres hacer: '))

#numeros = []
#numero = 0
#while altura != numero:
#    numero += 1
#    numeros.append(numero)
#    for n in numeros:
#        print(n, end = '')
#    print()

for n in range(1, altura + 1):
    for i in range(1, n + 1):
        print(i, end = '')
    print()