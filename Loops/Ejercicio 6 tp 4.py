# Desde un dispositivo RS232 un programa lee caracteres enviados por un sensor. Las lecturas se realizan
# de a 5 caracteres (buffer) por vez, los cuales deben llegar con un formato fijo: el primer carácter tiene
# que ser X y el último tiene que ser 0. Las secuencias leídas que respeten el formato se consideran
# correctas, la secuencia especial “&&&&&” marca el final de los envíos (llamémosla FDE), y toda
# secuencia distinta de FDE que no sea correcta se considera inválida. Al finalizar el proceso, se imprime
# un informe indicando los porcentajes de lecturas correctas e inválidas recibidas. Para resolver el
# ejercicio deberá investigar cómo se utilizan las siguientes funciones de PSeInt: ​longitud​ y ​subcadena.

#input: mensaje leidos por el sensor
#output: procentaje de lecturas correctas e invalidas

mensajes=[
    "X1230",
    "Xfce0",
    "kpos0",
    "Xknc0",
    "Xosj0",
    "Xpjmo",
    "jkcil",
    "X1230",
    "Xfce0",
    "kpos0",
    "Xknc0",
    "Xosj0",
    "Xpjmo",
    "jkcil",
    "&&&&&"
]

##########################
#       caso while       #
##########################

input_str = mensajes
i = 0
fail = -1
correct = 0

while input_str != '&&&&&':
    input_str = mensajes[i]
    if input_str[0] == 'X':
        if input_str[4] == '0':
            correct += 1
        else:
            fail += 1
    else:
        fail += 1
    i += 1

print(f'El porcentaje de lecturas correctas es de {correct/(i-1)}')
print(f'El porcentaje de lecturas incorrectas es de {fail/(i-1)}')


#########################
#       caso for        #
#########################

# total = len(mensajes)-1
# correcto = 0
# incorrecto = -1

# for i in mensajes:
#     if i [0] == 'X':
#         if i [4] == '0':
#             correcto += 1
#         else:
#             incorrecto +=1
#     else:
#         incorrecto += 1

# print(f'El porcentaje de lecturas correctas es de {correcto/total}')
# print(f'El porcentaje de lecturas incorrectas es de {incorrecto/total}')