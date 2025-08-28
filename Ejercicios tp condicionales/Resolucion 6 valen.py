#################################
#           CONSIGNA            #
#################################

# Escribir un programa para calcular el monto de una bonificación especial que se paga a los
# empleados de una empresa del siguiente modo:
# Los porcentajes se aplican sobre el monto básico del sueldo, los varones si son solteros reciben
# un adicional del 3%, si no son solteros reciben el 3% más un 7% por su esposa y un 1,2 % por
# cada hijo, hasta dos hijos inclusive, entre 2 y 4 hijos un 1,6% y más de 4 hijos un 2%, pero todos
# esos porcentajes por esposa e hijos sólo los reciben si su antigüedad es mayor de 15 años, si no
# se ven reducidos en un 0,4% cada uno de los porcentajes.
# Para las mujeres es igual, pero si son madres solteras reciben un 3% adicional a lo anterior, más
# los porcentajes por hijos, aplicándose igual esquema de reducción si su antigüedad no es mayor
# de 15 años.
# El sueldo mensual básico tanto para hombres como mujeres es de $750

#################################
#           ANALYSIS            #
#################################

# Input: 
#   - gender
#   - married
#   - child_quantity
#   - working_age

# Output:
#   - Salary

# Data available
# Basic salary: 750

# Workers:
# single => +3%
# married => +10% (3% + 7%)
# women_single_with_kids => +6% (3% + 3%)

# working age increase:
# [0,15] => -0.04%

# kid salary increase:
# [1,2] => +1.2%
# [3,4] => +1.6%
# [1,2] => +2%


#################################
#           SOLUCION            #
#################################

basic_salary = 750
# Single
salary = basic_salary + (basic_salary*0.03)

working_age = int(input('Tiempo (en años) de trabajo en la empresa: '))
reduction_quanty = 1
if 15 < working_age:
    reduction_quanty = -999999
elif working_age < 0:
    print('[!] Se ha colocado un valor negativo.\n[+] Se ha asignado el valor por defecto: 0 años de antiguedad.')

gender = input('Seleccionar genero Hombre/Mujer [H/m]: ')
if gender == 'M' or gender == 'm':
    print('[!] Seleccionado el genero: Mujer')
    gender = 'm'
    spanish_married = 'casada'
else:
    print('[!] Seleccionado el genero por defecto: Hombre')
    gender = 'h'
    spanish_married = 'casado'

married = input(f'Estas {spanish_married} [s/N]: ')
if married == 'S' or married == 's':
    salary = salary + (basic_salary*0.07)
    reduction_quanty += 1
else:
    married = 'n'

if not(gender == 'h' and married == 'n'): #if not a single man ask about kids
    kid_increase = 0
    kids = int(input('¿Cuántos hijos tiene? (Ingrese un número del 0 en adelante): '))
    if 1 <= kids < 100:
        if kids <= 2:
            kid_increase = 0.012
        elif kids <= 4:
            kid_increase = 0.016
        else:
            kid_increase = 0.02

        reduction_quanty += kids
    else:
        kids = 0
        if kids < 0:
            print('[!] Se ha colocado un valor negativo.\n[+] Se ha asignado el valor por defecto: 0 hijos.')
        elif 100 <= kids:
            print('[!] Se ha colocado un valor imposible.\n[+] Se ha asignado el valor por defecto: 0 hijos.')
    salary = salary + (basic_salary*kids*kid_increase)  

if gender =='m' and married == 'n' and kids != 0:
    # Single mother
    salary = salary + (basic_salary*0.03)
    reduction_quanty += 1

if 0 < reduction_quanty:
    salary = salary - (basic_salary * reduction_quanty * 0.004)
