'''
Determinar el precio de un pasaje de avión ida y vuelta, conociendo la distancia a recorrer y
sabiendo que si el número de días de estancia es superior a siete y la distancia es superior a
800km, el pasaje tiene un descuento del 30%. El precio por km es de $2.5.
'''

#input: distancia y dias de estancia
#output: precio con o sin descuento

distance = float(input('¿Cuantos km se van a recorrer en avion? '))
days_on = float(input('¿Cuantos dias de estancia? '))
price = 2.5
discount = 0.3
#total = price*discount

if distance > 0 and days_on > 0:
    if distance > 800 and days_on > 7:
        print(f'tu precio de pasaje de ida y vuelta es de {distance*(price - (price * discount))}') #(total-(total*discount))
    else:
        print(f'El precio de tu pasaje de ida y vuelta es de {distance*price}') #(total)
else:
    print('tu numero en km y dias de estancia deben ser positivos y mayor que 0')