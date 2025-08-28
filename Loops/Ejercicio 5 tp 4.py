#R​ealizar un algoritmo que calcule la suma de las siguientes series para un n dado:
#mostrar al usuario el menu para que elija la serie, luego pedir un n
#a) 1/2 + 2/2 + 3/2...n/2
#b) 2/1 + 2^2/2 + 2^3/3 + ... 2^n/n

#input: n, y la serie que quiera elegir
#Output: solucion de la serie

########################
#         Intro        #
########################

print('''Bienvenido a mi programa para calcular las siguiente series: 
1) 1/2 + 2/2 + 3/2...n/2
2) 2/1 + 2^2/2 + 2^3/3 + ... 2^n/n
''')

choice = int(input('Selecciona si queres hacer la serie 1 o la serie 2: '))
while choice != 1 and choice != 2:
    choice = int(input('Selecciona si queres hacer la serie 1 o la serie 2: '))
end = int(input('Dame el valor de n para que calcule la serie: '))
while end <= 0:
    print('Tu numero debe ser positivo')
    end = int(input('Dame el valor de n para que calcule la serie: '))

###########################
#       Serie 1 o 2       # con lista
###########################

#serie_1 = 1/2 + 2/2 + 3/2...n/2
#serie_2 = 2/1 + 2^2/2 + 2^3/3 + ... 2^n/n

# quantity = []
# n = 1#
# if choice == 1:
#    while n != end+1:
#        number = n/2
#        quantity.append(number)
#        n += 1
# else:
#    while n != end+1:
#        number = (2**n)/n
#        quantity.append(number)
#        n += 1
# #print(quantity)
# print(sum(quantity))

###########################
#       Serie 1 o 2       # sin lista
###########################

n = 1
suma = 0

while n != end + 1:
    if choice == 1:
        suma = suma + n/2
        n += 1
    else:
        suma = suma + (2**n)/n
        n += 1
print(suma)
