'''
Escribir un programa para calcular el monto de una bonificación especial que se paga a los
empleados de una empresa del siguiente modo:
Los porcentajes se aplican sobre el monto básico del sueldo, los varones si son solteros reciben
un adicional del 3%, si no son solteros reciben el 3% más un 7% por su esposa y un 1,2 % por
cada hijo, hasta dos hijos inclusive, entre 2 y 4 hijos un 1,6% y más de 4 hijos un 2%, pero todos
esos porcentajes por esposa e hijos sólo los reciben si su antigüedad es mayor de 15 años, si no
se ven reducidos en un 0,4% cada uno de los porcentajes.
Para las mujeres es igual, pero si son madres solteras reciben un 3% adicional a lo anterior, más
los porcentajes por hijos, aplicándose igual esquema de reducción si su antigüedad no es mayor
de 15 años.
El sueldo mensual básico tanto para hombres como mujeres es de $750
'''

###########################################################################################################

'''
bonificaciones:
soltero: hombre y mujer 0.03
casado: hombre y mujer (0.03 + 0.07) = 0.1                 |
<= 2 hijos = casado(0.1) + 0.012 por hijo                  |  Solo si tienen mas de 15 años de antiguedad
> 2 hijos y <=4 hijos = casado(0.1) + 0.016                |
> 4 hijos = casado(0.1) + 0.02                             |

casado: hombre y mujer (0.03 + 0.07) = 0.1 - 0.004         |
<= 2 hijos = casado(0.1) + 0.012 por hijo - 0.004          |  Solo si tienen menos de 15 años de antiguedad
> 2 hijos y <=4 hijos = casado(0.1) + 0.016 - 0.004        |
> 4 hijos = casado(0.1) + 0.02 - 0.004                     |

Madres solteras: + 0.03

<= 2 hijos = casado(0.1) + 0.012 por hijo                  |  Solo si tienen mas de 15 años de antiguedad
> 2 hijos y <=4 hijos = casado(0.1) + 0.016                |
> 4 hijos = casado(0.1) + 0.02                             |

<= 2 hijos = casado(0.1) + 0.012 por hijo - 0.004          |  Solo si tienen menos de 15 años de antiguedad
> 2 hijos y <=4 hijos = casado(0.1) + 0.016 - 0.004        |
> 4 hijos = casado(0.1) + 0.02 - 0.004                     |
'''

#input: hombre/mujer soltero/a casado/casada con o sin hijos y años de antiguedad
#output: salario con la bonificacion correspondiente


salary = 750

#bonificaciones
soltero = 0.03
casado = 0.1
dos_hijos_o_menos = 0.012                    #con antiguedad de +15 años
mas_de_dos_hijos_menos_de_cuatro = 0.016     #con antiguedad de +15 años
mas_de_cuatro_hijos = 0.02                   #con antiguedad de +15 años

#otras bonificaciones
madre_soltera = 0.03

#con antiguedad de -15 años (restar 0.004)
sin_antiguedad = 0.004

genero = str(input('¿Es hombre o mujer? '))
if genero == 'hombre':
    estado = str(input('¿Es casado o soltero? '))
    if estado == 'casado':
        antiguedad = str(input('¿Tabajo en la empresa por más de 15 años? (si o no) '))
        if antiguedad == 'si':
            cantidad_de_hijos = int(input('¿Cuantos hijos tiene? '))
            if cantidad_de_hijos > 0 and cantidad_de_hijos <= 2:
                print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*dos_hijos_o_menos * cantidad_de_hijos)}')
            elif cantidad_de_hijos > 2 and cantidad_de_hijos <= 4:
                print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*mas_de_dos_hijos_menos_de_cuatro * cantidad_de_hijos)}')
            elif cantidad_de_hijos > 4:
                print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*mas_de_cuatro_hijos * cantidad_de_hijos)}')
            elif cantidad_de_hijos == 0:
                print(f'El salario más las bonificaciones es de {salary + (casado*salary)}')
            else:
                print('El numero debe ser un entero positivo')
        elif antiguedad == 'no':
            cantidad_de_hijos = int(input('¿Cuantos hijos tiene? '))
            if cantidad_de_hijos > 0 and cantidad_de_hijos <= 2:
                print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*dos_hijos_o_menos * cantidad_de_hijos) - (salary*sin_antiguedad)}')
            elif cantidad_de_hijos > 2 and cantidad_de_hijos <= 4:
                print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*mas_de_dos_hijos_menos_de_cuatro * cantidad_de_hijos) - (salary*sin_antiguedad)}')
            elif cantidad_de_hijos > 4:
                print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*mas_de_cuatro_hijos * cantidad_de_hijos) - (salary*sin_antiguedad)}')
            elif cantidad_de_hijos == 0:
                print(f'El salario más las bonificaciones es de {salary + (casado*salary) - (salary*sin_antiguedad)}')
            else:
                print('El numero debe ser un entero positivo')
        else:
            print('Porfavor solo escriba "si" o "no" todo en minuscula tal como aparece escrito en esta oración')
    elif estado == 'soltero':
            print(f'El salario más la bonificacion es de {salary + (salary*soltero)}')
    else:
        print('Porfavor solo escriba "casado" o "soltero" todo en minuscula tal como aparece escrito en esta oración')
elif genero == 'mujer':
    estado = str(input('¿Es casada o soltera? '))
    if estado == 'casada':
        antiguedad = str(input('¿Tabajo en la empresa por más de 15 años? (si o no) '))
        if antiguedad == 'si':
            cantidad_de_hijos = int(input('¿Cuantos hijos tiene? '))
            if cantidad_de_hijos > 0 and cantidad_de_hijos <= 2:
                print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*dos_hijos_o_menos * cantidad_de_hijos)}')
            elif cantidad_de_hijos > 2 and cantidad_de_hijos <= 4:
                print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*mas_de_dos_hijos_menos_de_cuatro * cantidad_de_hijos)}')
            elif cantidad_de_hijos > 4:
                print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*mas_de_cuatro_hijos * cantidad_de_hijos)}')
            elif cantidad_de_hijos == 0:
                print(f'El salario más las bonificaciones es de {salary + (casado*salary)}')
            else:
                print('El numero debe ser un entero positivo')
        elif antiguedad == 'no':
            cantidad_de_hijos = int(input('¿Cuantos hijos tiene? '))
            if cantidad_de_hijos > 0 and cantidad_de_hijos <= 2:
                print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*dos_hijos_o_menos * cantidad_de_hijos) - (salary*sin_antiguedad)}')
            elif cantidad_de_hijos > 2 and cantidad_de_hijos <= 4:
                print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*mas_de_dos_hijos_menos_de_cuatro * cantidad_de_hijos) - (salary*sin_antiguedad)}')
            elif cantidad_de_hijos > 4:
                print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*mas_de_cuatro_hijos * cantidad_de_hijos) - (salary*sin_antiguedad)}')
            elif cantidad_de_hijos == 0:
                print(f'El salario más las bonificaciones es de {salary + (casado*salary) - (salary*sin_antiguedad)}')
            else:
                print('El numero debe ser un entero positivo')
        else:
            print('Porfavor solo escriba "si" o "no" todo en minuscula tal como aparece escrito en esta oración')
    elif estado == 'soltera':
            madre = str(input('¿Es madre? (si o no) '))
            if madre == 'si':
                antiguedad = str(input('¿Tabajo en la empresa por más de 15 años? (si o no) '))
                if antiguedad == 'si':
                    cantidad_de_hijos = int(input('¿Cuantos hijos tiene? '))
                    if cantidad_de_hijos > 0 and cantidad_de_hijos <= 2:
                        print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*dos_hijos_o_menos * cantidad_de_hijos) + (salary*madre_soltera)}')
                    elif cantidad_de_hijos > 2 and cantidad_de_hijos <= 4:
                        print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*mas_de_dos_hijos_menos_de_cuatro * cantidad_de_hijos) + (salary*madre_soltera)}')
                    elif cantidad_de_hijos > 4:
                        print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*mas_de_cuatro_hijos * cantidad_de_hijos) + (salary*madre_soltera)}')
                    else:
                        print('El numero debe ser un entero positivo')
                elif antiguedad == 'no':
                    cantidad_de_hijos = int(input('¿Cuantos hijos tiene? '))
                    if cantidad_de_hijos > 0 and cantidad_de_hijos <= 2:
                        print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*dos_hijos_o_menos * cantidad_de_hijos) - (salary*sin_antiguedad) + (salary*madre_soltera)}')
                    elif cantidad_de_hijos > 2 and cantidad_de_hijos <= 4:
                        print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*mas_de_dos_hijos_menos_de_cuatro * cantidad_de_hijos) - (salary*sin_antiguedad) + (salary*madre_soltera)}')
                    elif cantidad_de_hijos > 4:
                        print(f'El salario más las bonificaciones es de {salary + (casado*salary) + (salary*mas_de_cuatro_hijos * cantidad_de_hijos) - (salary*sin_antiguedad) + (salary*madre_soltera)}')
                    else:
                        print('El numero debe ser un entero positivo')
                else:
                    print('Porfavor solo escriba "si" o "no" todo en minuscula tal como aparece escrito en esta oración')
            elif madre == 'no':
                print(f'El salario más la bonificacion es de {salary + (salary*soltero)}')
            else:
                print('Porfavor solo escriba "si" o "no" todo en minuscula tal como aparece escrito en esta oración')
    else:
        print('Porfavor solo escriba "casada" o "soltera" todo en minuscula tal como aparece escrito en esta oración')
else:
    print('Porfavor solo escriba "hombre" o "mujer" todo en minuscula tal como aparece escrito en esta oración')
