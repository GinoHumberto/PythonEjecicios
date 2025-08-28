'''
Un postulante a un empleo realizó un test de capacitación y se obtuvo la siguiente información: 
cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó
correctamente. Se pide confeccionar un programa al cual se le ingresen los datos e informe el
nivel del postulante según el porcentaje de respuestas correctas que ha obtenido:
Nivel máximo: Porcentaje>=90%
Nivel medio: Porcentaje>=75% y <90%.
Nivel regular: Porcentaje>=50% y <75%
Fuera de nivel: Porcentaje<50%.
'''

#input: cantidad de preguntas, cantidad de respuestas correctas.
#output: mensaje segun: cantidad de respuestas correctas/cantidad de preguntas

print('Resultado del test de capacitación')

cantidad_de_preguntas = int(input('inserta la cantidad de preguntas que se hicieron en el test (inserta el valor en numero entero): '))

if cantidad_de_preguntas > 0:
    
    cantidad_de_respuestas_correctas = int(input('inserta la cantidad de respuestas correctas que se hicieron en el test (inserta el valor en numero entero): '))

    if cantidad_de_respuestas_correctas > 0 and cantidad_de_respuestas_correctas <= cantidad_de_preguntas:
        resultado_del_test = cantidad_de_respuestas_correctas/cantidad_de_preguntas

        if resultado_del_test < 0.5:
            print('El postulante se encuentra fuera de nivel')
        elif resultado_del_test >= 0.5 and resultado_del_test < 0.75:
            print('El postulante se encuentra en un nivel regular')
        elif resultado_del_test >= 0.75 and resultado_del_test < 0.9:
            print('El postulante se encuentra en un nivel medio')
        else:
            print('El postulante se encuentra en el nivel maximo')
    else: 
        print('el valor debe ser un entero positivo y tiene que ser menor o igual a la cantidad de preguntas')
else: 
    print('el valor debe ser un entero positivo')
