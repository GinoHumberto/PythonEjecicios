# Se desea calcular la cantidad de latas de pintura necesarias del mismo color para pintar las paredes de
# todas las habitaciones de una casa. Se conoce la siguiente información: Las puertas son de 0.75 x 2.00
# mts (ancho x alto) y las ventanas son de 1.20 x 1.50 mts. La pintura tiene las siguientes características:
#
# -------------------------------------------------------------------------------
# | Tipo de Latex    Cada litro rinde (por mano)     Viene en latas de (litros) |
# |      Mate                  14 m​2                        1, 4, 10 y 20       |
# -------------------------------------------------------------------------------
# 
# La información variable consiste de:
# ❖ El ancho, largo y alto de cada habitación.
# ❖ Cantidad de cada tipo de aberturas en cada habitación.
# ❖ Cantidad de manos a pintar (una “mano” representa cubrir la superficie completa con pintura).
# Realice un algoritmo para determinar la cantidad de latas de pintura a utilizar de manera tal que se
# minimice el costo total. El costo de cada lata es el siguiente: la lata de 1 litro cuesta $50, la de 4 cuesta
# $170, la de 10 cuesta $400 y la de 20 litros cuesta $700. Observe que, cuantas menos latas se compren
# menos se paga, ya que por ejemplo, una lata de 4 lts cuesta menos que 4 latas de 1 lts.

# Segun el enunciado me pide que utilice el ancho por largo por alto, lo cual significa que todas las paredes van a tener los mismos valores (aunque esto no seria aplicable a la realidad es lo que pide)
# No especifica si me debo adaptar a la cantidad de paredes, por lo tanto se va a considerar que la habitacion tiene 4 paredes (lo convencional)
# voy a aplicar la formula: superfice de paredes = 2 * (alto * largo) + 2 * (alto * ancho)
# en resumen la formula queda como 2*alto*(largo*ancho)


def sup_total():
    no_error = 0
    while no_error == 0:
        try:
            alto_habitación = float(input('Ingresa la altura de la habitación en mts '))
            largo_habitación = float(input('Ingresa el largo de la habitación en mts '))
            ancho_habitación = float(input('Ingresa el ancho de la habitación en mts '))
            print('Se estima que una ventana es de 1.20 x 1.50 mts y una puerta de 0.75 x 2.00 mts')
            q_puertas = int(input('Cuantas puertas tiene tu habitación '))
            q_ventanas = int(input('Cuantas ventanas tiene tu habitación '))
            if alto_habitación > 0 and largo_habitación > 0 and ancho_habitación > 0 and q_puertas > 0 and q_ventanas > 0:
                no_error = 1
            else:
                print('El valor debe ser positivo')
        except:
            print('El valor dado debe ser un numero que tenga coherencia')
    superficie_a_pintar = 2*alto_habitación*(ancho_habitación*largo_habitación)
    sup_ventana = q_ventanas * 1.20 * 1.50
    sup_puerta = q_puertas * 0.75 * 2
    superficie_total = superficie_a_pintar - sup_puerta - sup_ventana
    if superficie_total > 0:
        return(superficie_total)
    else:
        print('\n Algo salio mal \n')
        return(0)

def rendimiento_pintura():
    a_pintar = sup_total()
    print('Se estima que cada litro rinde 14 metros cuadrados por mano')
    no_error = 0
    while no_error == 0:
        try:
            q_manos = int(input('Cuantas manos vas a querer darle a tus paredes '))
            if q_manos > 0:
                no_error = 1
            else:
                print('No puedes darle menos de 1 capa a tu pared')
        except:
            print('Hubo un error en el ingreso de datos')
    litros_por_mano = a_pintar * 1 /14
    litros_necesarios = litros_por_mano * q_manos
    return(litros_necesarios)

def costos():
    a_pintar = rendimiento_pintura()
    q_litros = a_pintar
    costo_total = 0
    # A comprar
    _1lts = 0
    _4lts = 0
    _10lts = 0
    _20lts = 0
    # Costos
    lata_1lts = 50
    lata_4lts = 170
    lata_10lts = 400
    lata_20lts = 700
    # Costo por litro
    while q_litros > 0:
        if q_litros >= 20:
            costo_total += lata_20lts
            q_litros -= 20
            _20lts += 1
        elif q_litros >= 10:
            costo_total += lata_10lts
            q_litros -= 10
            _10lts += 1
        elif q_litros >= 4:
            costo_total += lata_4lts
            q_litros -= 4
            _4lts += 1
        else:
            costo_total += lata_1lts
            q_litros -= 1
            _1lts += 1
    print(f'El costo total es de {costo_total}, vas a pintar {int(a_pintar)} metros cuadrados, necesitas comprar {_1lts} baldes de 1 lsts,{_4lts} baldes de 4 lts,{_10lts} baldes de 10 lts,{_20lts} baldes de 20 lts')

costos()