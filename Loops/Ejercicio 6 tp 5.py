# Escriba un programa que lea un número entero (altura) y a partir de él cree una escalera
# invertida de asteriscos con esa altura. Por ejemplo, si ingresamos una altura de 5 se deberá
# mostrar:
# *****
# ****
# ***
# **
# *

#Input: altura de la escalera invertida de asteriscos
#Output: escalera invertida de asteriscos

ingreso = int(input('Ingresa la altura de tu escalera invertida: '))
while ingreso < 1:
    ingreso = int(input('Ingresa la altura de tu escalera invertida: '))

for alto in range(ingreso, 0, -1):
    for largo in range(alto):
        print('*', end = '')
    print()

#quantity = ingreso
#while quantity != 0:
#    print('*' * quantity)
#    quantity-=1

# palabras = ['Hola', 'Mundo']
# for palabra in (palabras):
#     for letra in (palabra):
#         print(letra)