# Solicitar al usuario que digite un número y determine lo siguiente:
# a. Si el número es capicúa (ej. 12321)
# b. Si el número es primo o no. Un número es primo cuando es divisible sólo por 1 y por sí mismo,
# por ejemplo: 2, 3, 5, 7, 11, 13, 17, etc.
# c. Si el número tiene todos sus dígitos impares (ejemplo: 333, 55, etc.)
# Todas las opciones deben ser presentadas al usuario a través de un menú de opciones. Además, las
# operaciones se deben resolver matemáticamente, ​NO es posible convertir el número a cadena para
# resolver el problema.

# Input: Un numero
# Output: si el numero es capicua, primo o si el numero tiene todos los numero impares

##########################
#       Funciones        #
##########################
# Capicua:
def capicua (numero):
    normal = numero
    invertido = 0
    while numero > 0:
        digito = numero % 10
        invertido = invertido * 10 + digito
        numero //= 10
    if normal == invertido:
        print('Tu número es capicua')
    else:
        print('Tu número no es capicua')
# Primo:
def primo (numero):
    divisible = 0
    n = 1
    while n <= numero :
        if numero%n == 0:
            divisible += 1
        n += 1
    if divisible <= 2:
        print ('Tu numero es primo')
    else:
        print ('Tu numero no es primo')
# Digitos impares:
def impar (numero):
    x = numero
    par = 0
    while x != 0:
        if x % 2 == 0:
            par += 1
        x = x//10
    if par > 0:
        print('Tu numero tiene algun digito par')
    else:
        print('Tu numero tiene todos sus digitos impares')


#######################
#        input        #
#######################

numero = int(input('Dame un número '))
if numero < 0:
    numero = numero*-1

#########################
#       Programa        #
#########################

menu=('''\n|-------------------------------------------------------|
|                Selecciona una opcion                  |
|1.  Quieres saber si tu número es capicua              |
|2.  Quieres saber si el número es primo                |
|3.  quieres saber si todos sus digitos impares         |
|4.  Salir                                              |
|-------------------------------------------------------|''')
loop = 0

while loop == 0:
    print(menu)
    choice = int(input('¿Qué opcion seleccionaste? '))
    if choice == 1:
        capicua(numero)
        print(capicua)
    elif choice == 2:
        primo(numero)
        print(primo)
    elif choice == 3:
        impar(numero)
        print(impar)
    elif choice == 4:
        loop = 1
    else:
        print('eligi una opcion del menu')