# Es​criba un algoritmo en el cual se solicite un listado de 10 números enteros positivos al usuario. Una
# vez ingresados los valores se deben realizar las siguientes estadísticas:
# a) Cantidad de números que son pares o avisar al usuario que no se ingresó ninguno.
# b) Suma de los múltiplos de 5 (si los hay) o avisar al usuario que no se ingresó ninguno.
# c) El Promedio de los números impares que fueron ingresados.
# Notas:
# - Se debe llamar la atención al usuario cuando ingrese un valor que no es positivo.
# - No se debe mostrar las estadísticas hasta haber recibido del usuario un listado completamente
# “válido” de números solicitados (es decir, que los 10 números recibidos sean positivos).
# - Ayuda: Investigar la opción de PseInt de “predefenir entrada” para simplificar la prueba del
# algoritmo.

#input: 10 numeros enteros positivos
#output: 
# a) Cantidad de números que son pares o avisar al usuario que no se ingresó ninguno.
# b) Suma de los múltiplos de 5 (si los hay) o avisar al usuario que no se ingresó ninguno.
# c) El Promedio de los números impares que fueron ingresados.


##############################
#       toma de datos        #
##############################

numbers = []

while len(numbers) != 10:
    number = int(input('Ingresa un numero entero positivo: '))
    while number < 0:
        number = int(input('Tu numero debe ser un entero positivo: '))
    else: 
        numbers.append(number)
print(numbers)

##########################
#       caso while       #
##########################

end_flag = len(numbers)
i = 0

num_par = 0
mult_5 = 0
num_inp = 0

suma = 0

while end_flag != i:
    value = numbers[i]
    if value%2 == 0:
        num_par += 1
    if value%5 == 0:
        mult_5 = value 
        suma = suma + mult_5
    if value%2 != 0:
        num_inp += 1
    i += 1

if num_par > 0:
    print(f'la cantidad de numeros pares que hay son {num_par}')
else:
    print('No hay ningun número par')
if suma > 0:
    print(f'La sumatoria de tus numeros multiplos de 5 es de {suma}')
else:
    print('No tienes numeros multiplos de 5')
if num_inp > 0:
    print(f'El promedio de numeros impares es de {num_inp/len(numbers)}')    
else:
    print('No tienes numeros impares')    
    

#########################
#       caso for        #
#########################

# num_par = 0
# mult_5 = []
# num_inp = []

# for i in numbers:
#     if i%2 == 0:
#         num_par += 1
#     if i%5 == 0:
#         mult_5.append(i)
#     if i%2 != 0:
#         num_inp.append(i)

# if num_par > 0:
#     print(f'la cantidad de numeros pares que hay son {num_par}')
# else:
#     print('No hay ningun número par')
# if sum(mult_5) > 0:
#     print(f'La sumatoria de tus numeros multiplos de 5 es de{sum(mult_5)}')
# else:
#     print('No tienes numeros multiplos de 5')
# if len(num_inp) > 0:
#     print(f'El promedio de numeros impares es de {len(num_inp)/len(numbers)}')    
# else:
#     print('No tienes numeros impares')    