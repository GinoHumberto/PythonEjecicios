# datos_a = [78,87,81,89,85]
# datos_b = [94,91,87,90,88]
# datos_c = [73,78,69,83,76]
# datos_d = [79,83,78,69,81]

# media_a = 84
# media_b = 90
# media_c = 75.8
# media_d = 78

# result = []


# for i in datos_a:
#     total_a = (i-media_a)**2
#     result.append(total_a)
# for i in datos_b:
#     total_b = (i-media_b)**2
#     result.append(total_b)
# for i in datos_c:
#     total_c = (i-media_c)**2
#     result.append(total_c)
# for i in datos_d:
#     total_d = (i-media_d)**2
#     result.append(total_d)

# print(sum(result))

##################################
######## Resolucion valen ########
##################################

# 78 87 81 89 85
# 94 91 87 90 88
# 73 78 69 83 76
# 79 83 78 69 81

# tabla = [
#     [78, 87, 81, 89, 85],
#     [94, 91, 87, 90, 88],
#     [73, 78, 69, 83, 76],
#     [79, 83, 78, 69, 81]
# ]

# medias = [84, 90, 75.8, 78]
# i = 0
# total = []

# for datos in tabla:
#     media = medias[i]
#     i += 1
#     resultado = 0
#     for numero in datos:
#         resultado += (numero-media)**2
#     total.append(resultado)

# print(f'Lista de valores:{total}\nSuma:{sum(total)}')


tabla = [
    [78, 87, 81, 89, 85],
    [94, 91, 87, 90, 88],
    [73, 78, 69, 83, 76],
    [79, 83, 78, 69, 81]
]

valor_total = []
gran = 81.95

for datos in tabla:
    for numero in datos:
        valor = (numero-gran)**2
        valor_total.append(valor)
print(sum(valor_total))