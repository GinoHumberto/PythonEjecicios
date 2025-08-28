#Es​cribir un programa que lea un número entero y devuelva el número de dígitos que componen ese
#número. Por ejemplo, si introducimos el número 12334, el programa deberá devolver 5. (Restricción:
#NO utilice las funciones de cadenas provistas de PSeInt para su solución).

#input: numero entero
#output: cantidad de digitos del numero

#####################
#       Numero      #
#####################

number = int(input('Ingresa un numero entero positivo: '))
while number < 0:
    print('tu numero debe ser positivo')
    number = int(input('Ingresa un numero entero positivo: '))

#######################
#       Digitos       #
#######################

times_divided = []

loop = number
while loop >= 10:
    number = number/10
    times_divided.append(number)
    loop = number
print(len(times_divided)+1)
