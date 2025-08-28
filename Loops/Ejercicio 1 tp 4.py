'''
Realice un programa que calcule y visualice el valor máximo, el valor mínimo y el promedio de n
números (n>0). El valor de n se solicitará al principio del programa y los números serán introducidos
por el usuario. Realice dos versiones del programa, una usando el bucle “Mientras” y otra con “Hacer -
Mientras Que”.
'''

# input # 
# numeros > 0 

# output # 
# valor max, min y promedio

###########################
#   Ejercicio con while   #
###########################

value = []

quantity_numbers = int(input('inserta cuantos numeros tiene tu lista: '))

if quantity_numbers > 0:
    i = 0
    end = (quantity_numbers-1)
    while i <= end:
        number = int(input('Inserta un numero: '))
        value.append(number)
        i += 1
    print(f'tu valor minimo es {min(value)}')
    print(f'tu valor maximo es {max(value)}')
    print(f'tu promedio es de {sum(value)/quantity_numbers}')
else:
    print('tu lista debe tener más de un número')


#########################
#   Ejercicio con for   #
#########################

if quantity_numbers > 0:
    for i in range(quantity_numbers):
        number = int(input('Inserta un numero: '))
        value.append(number)
    print(f'tu valor minimo es {min(value)}')
    print(f'tu valor maximo es {max(value)}')
    print(f'tu promedio es de {sum(value)/quantity_numbers}')
else:
    print('tu lista debe tener más de un número')

