# El factorial (!), es una función matemática que consiste en multiplicar un número entero positivo 
# por todos los números enteros positivos hasta llegar a 1. 
# Por ejemplo, el factorial de (5!) se calcula como 5 x 4 x 3 x 2 x 1 = 120.

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# 
# print(factorial(5))

# Crea una función recursiva suma_lista(lista) que calcule la suma de todos los elementos de una lista.
# ej: suma_lista([1, 2, 3, 4]) Resultado esperado: 10

def suma_lista(lista):
    if len(lista) == 1:
        return lista
    else:
        a

print(suma_lista([1 ,2, 3, 4]))
# Escribe una función recursiva invertir(cadena) que devuelva la cadena al revés.
# invertir("hola")  # Resultado esperado: "aloh"