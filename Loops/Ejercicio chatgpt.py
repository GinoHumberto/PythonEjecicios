'''
Ejercicio 1: Contar hasta un número (for)
Objetivo: Usar un bucle for para contar desde 1 hasta un número ingresado por el usuario.

✅ Instrucciones:

Pide al usuario un número entero positivo.
Usa un bucle for para contar desde 1 hasta ese número.
Muestra cada número en la pantalla.
'''

#number = int(input('inserta un numero y contare hasta ese: '))
#
#if number >= 0: 
#    for i in range(1, number + 1):
#        print (i) 
#else: 
#    print ('tu numero debe ser un entero positivo')


'''
Ejercicio 2: Adivinar un número (while)
Objetivo: Usar un bucle while para repetir una acción hasta que se cumpla una condición.

✅ Instrucciones:

Define un número secreto (puedes elegir cualquier número, por ejemplo, 7).
Pide al usuario que ingrese un número.
Usa un bucle while para seguir pidiendo un número hasta que el usuario adivine el número secreto.
Cuando lo adivine, muestra un mensaje de felicitación.
'''

i = 7

number = int(input('ingresa un numero: '))

while i != number:
    print ('ingresa otro numero')
    number = int(input('ingresa un numero: '))
else:
    print ('adivinaste :) ')