# Realizar un programa que lea un número entero (tamaño del lado) y a partir de él cree un
# cuadrado de asteriscos de ese tamaño. Los asteriscos sólo se verán en el borde del cuadrado,
# no en el interior. Por ejemplo, si se ingresa el número 4 se debe mostrar:
# ****
# *  *
# *  *
# ****

ingreso = int(input('Ingresa un numero y te hare un cuadrado de asteriscos: '))
while ingreso <= 1:
    ingreso = int(input('Ingresa un numero y te hare un cuadrado de asteriscos: '))

for filas in range(ingreso):
    for columnas in range(ingreso):
        if filas == 0 or filas == ingreso-1:
            print('*', end = '')
        elif columnas == 0 or columnas == ingreso-1:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()