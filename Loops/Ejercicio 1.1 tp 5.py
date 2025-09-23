# Se dispone de un conjunto de ​N familias, cada una de las cuales tiene un número ​M diferente de hijos.
# Escriba un algoritmo para averiguar:
# a) el promedio de edad de los hijos de cada familia.
# b) el promedio de edad de los hijos de todas las familias.

# Input: edades de los hijos de cada familia
# Output: Promedio de edad de los hijos de cada familia y promedio de edad de los hijos de todas las familias

##############
# Q familias #
##############

family_quantity = int(input('Ingresa la cantidad de familais del analisis: '))
while family_quantity <= 0:
    print('debe ser un número positivo')
    family_quantity = int(input('Ingresa la cantidad de familais del analisis: '))

set_of_families = {}
total_ages = []
while len(set_of_families) != family_quantity:
    son_quantity = int(input('Ingresa la cantidad de hijos de la familia '))
    sons = 0
    ages = []
    while sons != son_quantity:
        age = int(input('Ingresa la edad del hijo '))
        if age >= 0:
            ages.append(age)
            total_ages.append(age)
            sons += 1
    promedy_family = (sum(ages)/len(ages))
    set_of_families[str(input('Nombre de la familia '))] = promedy_family 
total_promedy = (sum(total_ages)/len(total_ages))

print('\nLos promedios de edad para cada familia son: \n')

for familia in set_of_families:
    print(f'El promedio de edad de los hijos de la familia {familia} es, {set_of_families[familia]} años')

print(f'El promedio total de las edades de las familias es de {total_promedy} años')

#KEY pensar: Sum_of_ages += Ages