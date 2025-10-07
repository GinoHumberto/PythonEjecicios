# Dos números son amigos si cada uno de ellos es igual a la suma de los divisores del otro. Por
# ejemplo 220 y 284 son amigos ya que:
# Suma de divisores de 284= 1 + 2 + 4 + 71 + 142 = 220
# Suma de divisores de 220 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
# Escriba un programa que a través del uso de una función determine si dos números ingresados
# por el usuario son amigos o no.

#########################
#       Metodo 1        #
#########################
def divisores(numero):
    divisor = []
    for divisores in range(1, numero):
        if numero%divisores == 0:
            divisor.append(divisores)
    return(divisor)

num_a = 220
num_b = 284
divisores_a = divisores(num_a)
divisores_b = divisores(num_b)

if sum(divisores_b) == num_a and sum(divisores_a) == num_b:
    print(f'La suma de divisores de {num_b} es igual a {num_a}')
    print(f'La suma de divisores de {num_a} es igual a {num_b}')
    print('Tus numeros son amigos')
else:
    print('Tus numeros no son amigos :(')

#########################
#       Metodo 2        #
#########################
def divisores(numero):
    divisor = 0
    for divisores in range(1, numero):
        if numero%divisores == 0:
            divisor += divisores
    return(divisor)

num_a = 220
num_b = 284
divisores_a = divisores(num_a)
divisores_b = divisores(num_b)

if divisores_b == num_a and divisores_a == num_b:
    print(f'La suma de divisores de {num_b} es igual a {num_a}')
    print(f'La suma de divisores de {num_a} es igual a {num_b}')
    print('Tus numeros son amigos')
else:
    print('Tus numeros no son amigos :(')