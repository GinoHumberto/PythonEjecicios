# Realizar un programa que permita realizar la división entre dos números y obtenga el cociente y el
# resto utilizando el método de restas sucesivas.

def division_resta(dividendo, divisor):
    numero_optimo = 1
    cociente = 0
    while cociente == 0:
        operacion = divisor * numero_optimo
        if dividendo - operacion > 0:
            numero_optimo += 1
        elif dividendo - operacion == 0:
            cociente = numero_optimo
        else:
            cociente = numero_optimo-1
    resto = dividendo - divisor * cociente
    return(cociente, resto)       

#################
#    Entrada    #
#################

no_error = 0
while no_error != 1:
    try:
        dividendo = int(input('¿Qué número quieres dividir? '))
        divisor = int(input('¿Por qué numero lo quieres dividir? '))
        if dividendo > 0 and divisor > 0:
            if divisor > dividendo:
                print('El divisor debe ser menor que el dividendo')
            else:
                no_error = 1
        else:
            print('El número debe ser positivo')
    except ValueError:
        print('Tiene que ser un número entero')

division = division_resta(dividendo, divisor)
print('El cociente y el resto es: ',division)