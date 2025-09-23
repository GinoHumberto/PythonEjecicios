# Crea una función que calcule el área de un rectángulo. 
# La función debe aceptar dos parámetros: la base y la altura del rectángulo. 
# Luego, el programa debe pedir al usuario que ingrese la base y la altura, 
# llamar a la función y mostrar el resultado.

# input: base y altura del rectangulo
# output: calculo del área del rectangulo

# base = int(input('Ingresa el número de tu base '))
# altura = int(input('Ingresa el numero de tu altura '))
# while base <= 0 or altura <= 0:
#      base = int(input('Ingresa el número de tu base '))
#      altura = int(input('Ingresa el numero de tu altura '))
# 
# def area (base, altura):
#     funcion = base * altura
#     return funcion
# resultado = area(base,altura)
# print(resultado )

# Write a function called is_prime, which checks if a number is prime. 

# Input: ingresar un numero
# Output: decir si el numero es primo o no 

# numero = int(input('Ingresa un número y te dire si es primo o no '))
# while numero <= 0:
#     numero = int(input('Ingresa un número y te dire si es primo o no '))
# 
# def primo (numero):
#     divisores = 0
#     for n in range(1,numero + 1):
#         if numero % n == 0:
#             divisores +=1
#     if divisores > 2:
#         return False
# 
# resultado = primo(numero)
# if resultado == False:
#     print('Tu numero no es primo')
# else:
#     print('Tu numero es primo')


# Crea una función llamada is_palindrome que verifique si una cadena de texto 
# es un palíndromo. Un palíndromo es una palabra, frase, número o cualquier otra 
# secuencia de caracteres que se lee igual hacia adelante y hacia atrás, ignorando 
# espacios, puntuación y mayúsculas.
#       La función debe aceptar una cadena como entrada.
#       Debe ignorar espacios y caracteres no alfabéticos.
#       Debe devolver True si la cadena es un palíndromo y False en caso contrario.

# Input: palabra
# Output: verdadero si es palindromo y falso si no es palinromo.

palabra = str(input('Ingresa la palabra y te dire si es un palindromo: '))

counter = 0
letras = []
while len(palabra) != counter:
    letra = palabra
    letter_counter = letra[counter]
    letras.append(letter_counter)
    counter += 1
print(letras)
print(counter)

#def is_palindrome (palabra):
#    palabra = palabra.lower()
#    palabra = palabra.replace()
#    counter = -1
#    if palabra == (palabra[::-1]):
#        return True

