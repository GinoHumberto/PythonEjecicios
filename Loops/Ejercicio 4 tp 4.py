#Si​mular la división usando solamente restas. Dados dos números enteros mayores que uno, realizar un
#algoritmo que calcule el cociente y el residuo usando sólo restas.

#input: 2 numeros enteros > 1
#output: cociente y times_of_rest de una division

#############################
#       Toma de datos       #
#############################

first_num=int(input('selecciona un numero entero mayor que 1: '))
while first_num < 1:
    print('Tiene que ser un numero mayor que 1')
    first_num=int(input('selecciona un numero entero mayor que 1: '))
second_num=int(input('selecciona al numero entero mayor que 1 que va a dividir a tu primer número: '))
while second_num < 1:
    print('Tiene que ser un numero mayor que 1')
    second_num=int(input('selecciona al numero entero mayor que 1 que va a dividir a tu primer número: '))

#########################
#       División        #
#########################

quantity_sum = []

times_of_rest = 0
while times_of_rest >= 0:
    first_num = first_num-second_num
    times_of_rest = first_num
    if times_of_rest >= 0:
        quantity_sum.append(first_num)
print(f'El cociente de tu división es {len(quantity_sum)}')

last_index = len(quantity_sum)-1
resto = quantity_sum[last_index]
print(f'El resto es de {resto}')

#Otra forma de ir al ultimo numero de la lista solo en python
#print(f'El resto es de {quantity_sum[-1]}')