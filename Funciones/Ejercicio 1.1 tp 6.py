# Solicitar al usuario que digite un número y determine lo siguiente:
# a. Si el número es capicúa (ej. 12321)
# b. Si el número es primo o no. Un número es primo cuando es divisible sólo por 1 y por sí mismo,
# por ejemplo: 2, 3, 5, 7, 11, 13, 17, etc.
# c. Si el número tiene todos sus dígitos impares (ejemplo: 333, 55, etc.)
# Todas las opciones deben ser presentadas al usuario a través de un menú de opciones. Además, las
# operaciones se deben resolver matemáticamente, ​NO es posible convertir el número a cadena para
# resolver el problema.

########################
#       Capicua        #
######################## 

# Input: Un numero
# Output: si el numero es capicua, primo o si el numero tiene todos los numero impares

def capicua(numero):
    original = numero
    invertido = 0
    q_digitos = len(str(numero))
    digito = 10 ** (q_digitos-1)
    iteraciones = 0
    while q_digitos != iteraciones:
        val = numero % 10
        numero = numero // 10
        invertido = digito * val + invertido
        digito //= 10
        iteraciones += 1
    print(f'El numero original es {original} El número invertido es {invertido}')
    return(original == invertido)
'''
if capicua(123454321):
    print('Es capicua')
else:
    print('No es capicua')
'''
######################
#       Primo        #
###################### 

def primo(numero):
    divisible = 0
    iterador = 1
    while iterador - 1 != numero:
        if numero % iterador == 0:
            divisible += 1
        iterador += 1
    if divisible == 2:
        return True
'''
if primo(983):
    print('Tu numero es primo')
else:
    print('Tu numero no es primo')
'''
#----------------------#
#   mejora sugerida    #
#----------------------#

def primo_mejorado(numero):
    divisible = 0
    if numero <= 3:
        return True
    elif numero % 2 == 0:
        return False
    else:
        for n in range(5, numero-1, 2):
            if numero % n == 0:
                divisible += 1
        if divisible == 0:
            return True 
'''
if primo_mejorado(983):
    print('Tu numero es primo')
else:
    print('Tu numero no es primo')
'''
################################
#       Digitos Impares        #
################################

def digitos_impares(numero):
    iteracion = 0
    impar = 0
    while numero > 0:
        digito = numero % 10
        numero //= 10
        iteracion += 1
        for n in range(1, digito+1, 2):
            if n == digito:
                impar += 1
    if iteracion == impar:
        return True
            
if digitos_impares(55753):
    print('Todos tus digitos son impares')