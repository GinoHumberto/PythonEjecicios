# Escribir un programa que procese una secuencia de caracteres ingresada por teclado y terminada en
# punto (leídos de a uno por vez), y luego codifique la palabra o frase ingresada de la siguiente manera:
# cada vocal se reemplaza por el carácter que se indica en la tabla y el resto de los caracteres (incluyendo
# a las vocales acentuadas) se mantienen sin cambios.
# -----------------
# | a  e  i  o  u |
# | @  #  $  %  * |
# -----------------
# Realice un subprograma que reciba una vocal y retorne la codificación correspondiente. Utilice la
# estructura “según” para la transformación. Además se debe calcular cuál es la consonante dentro de la
# frase que se repite más veces.
# Por ejemplo, si el usuario ingresa: Ayer, lunes, salimos a las once y 10.
# La salida del programa debería ser:
# @y#r, l*n#s, s@l$m%s @ l@s %nc# y 10.
# La letra s es la más repetida y aparece 4 veces

class Typeshit(Exception):
    msg = 'La cadena debe terminar con punto'

def ingreso():
    ingreso = input('Ingresa tu oracion, tiene que terminar con ".": ')
    ingreso.lower()
    if ingreso[-1] != '.':
        raise Typeshit
    return ingreso

def cambio_caracteres():
    caracteres = {'a': '@', 'e' : '#', 'i' : '$', 'o' : '%', 'u' : '*'}
    a = 0
    try:
        cadena = ingreso()
        cadena_codificada = ''
        for letra in cadena:
            if letra == 'a':
                letra = caracteres['a']
            elif letra == 'e':
                letra = caracteres['e']
            elif letra == 'i':
                letra = caracteres['i']
            elif letra == 'o':
                letra = caracteres['o']  
            elif letra == 'u':
                letra = caracteres['u']
            cadena_codificada += letra
        print(cadena_codificada.capitalize())
    except Typeshit as e:
        print(e.msg)

cambio_caracteres()