'''
Escribir un programa que permita ingresar 2 valores racionales de las coordenadas X, Y de un punto
del plano cartesiano. Luego debe mostrar una leyenda que indique a qué cuadrante pertenece
el punto o si está sobre una de las cuatro ramas de los ejes cartesianos.
'''

#input: valor de "x" y valor de "y"
#output: cuadrante del plano cartesiano o sobre que rama del eje cartesiano se encuentra

print('Este programa te va a permitir saber en que cuadrante del plano cartesiano o sobre que rama del eje cartesiano se encuentra tu valor x e y')

x_value = float(input('inserta tu valor del eje x: '))
y_value = float(input('inserta tu valor del eje y: '))

if x_value < 0 and y_value < 0:
    print('tu valor se encuentra en el 3er cuadrante')
elif x_value > 0 and y_value > 0:
    print('tu valor se encuentra en el 1er cuadrante')
elif x_value < 0 and y_value > 0:
    print('tu valor se encuentra en el 2do cuadrante')
elif x_value > 0 and y_value < 0:
    print('tu valor se encuentra en el 4to cuadrante')
elif x_value == 0 and y_value == 0:
    print('tu valor se encuentra en el origen de coordenadas')
elif x_value == 0:
    print('tu valor se encuentra en la rama del eje x')
else:
     print('tu valor se encuentra en la rama del eje y')