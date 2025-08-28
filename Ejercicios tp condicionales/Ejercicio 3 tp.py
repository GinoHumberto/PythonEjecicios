'''
Ingresar un número entero con dominio [0, 9999]. Validar que el número pertenezca al
dominio, e indicar si el mismo es múltiplo de 2, 3, 5, o si no es múltiplo de ninguno de ellos.
'''

#input: numero del 0 al 9999
#output: si es multiplo de 2, 3, 5 o si no es multiplo de ellos

number = int(input('inserta un numero del 0 al 9999: '))
factor_2 = 2
factor_3 = 3
factor_5 = 5


if number >= 1 and number <= 9999:
    if number == 1:
        print('tu numero es multiplo de todos los numeros')
    elif number % factor_2 == 0 and number % factor_3 == 0 and number % factor_5 == 0:
        print('tu numero es multiplo de 2, 3 y 5')
    elif number % factor_2 == 0 and number % factor_3 == 0:
        print('tu numero es multiplo de 2 y 3')
    elif number % factor_2 == 0 and number % factor_5 == 0:
        print('tu numero es multiplo de 2 y 5') 
    elif number % factor_3 == 0 and number % factor_5 == 0:
        print('tu numero es multiplo de 3 y 5') 
    elif number % factor_2 == 0:
        print('tu numero es multiplo de 2')
    elif number % factor_3 == 0:
        print('tu numero es multiplo de 3')
    elif number % factor_5 == 0:
        print('tu numero es multiplo de 5')
    else:
        print('tu numero no es multiplo ni de 2 ni de 3 ni de 5')
else:
    print('tu valor debe ser un entero positivo y tiene que ser menor a 9999')
