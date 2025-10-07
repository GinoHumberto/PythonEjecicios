# Escriba un programa que imprima 10 triángulos, alternando triángulos que tienen 6 renglones de
# asteriscos con otros que tienen 7 renglones de x. Ejemplo:
# *
# **
# ***
# ****
# *****
# ******
# x
# xx
# xxx
# xxxx
# xxxxx
# xxxxxx
# xxxxxxx
def triangulo(imp, n = 0):
    for filas in range(1, 7 + n):
        for columnas in range(filas):
            print(imp , end = '')
        print()

def triangulos():
    iteracion = 0
    while iteracion < 5:
        triangulo('*')
        triangulo('x',1)
        iteracion += 1

triangulos()